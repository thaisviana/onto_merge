import re
from onto_class import OntologyClass


class CSOOntology:
    def __init__(self, owl, algpedia=False):
        self.classes = []
        if not algpedia:
            lines = owl.iter_lines()
            class_pattern = ""
            number_open_children = 0
            for line in lines:
                if re.search("<owl:Class ", str(line)) and not re.search("/>", str(line)):
                    number_open_children += 1
                elif re.search(b'<owl:Class', line) and not re.search("/>", str(line)):
                    number_open_children += 1
                if number_open_children > 0:
                    class_pattern += line.decode("utf-8")
                if re.search(b'</owl:Class>', line):
                    number_open_children -= 1
                if number_open_children == 0 and class_pattern is not "":
                    self.refine_classes(str(class_pattern))
                    class_pattern = ""

    def refine_classes(self, ontology_class):
        name = self.get_name(ontology_class)
        comment = self.get_comment(ontology_class)
        if (name, comment) is not ('', ''):
            onto_class = OntologyClass()
            onto_class.properties = [self.get_properties(ontology_class)]
            onto_class.name, onto_class.comment = self.get_name(ontology_class), self.get_comment(ontology_class)
            self.classes.append(onto_class)

    def get_name(self, ontology_class):
        pattern = re.compile('<owl:Class rdf:ID="\S+">', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        if match is "":
            pattern = re.compile('<owl:Class rdf:about="\S+">', re.IGNORECASE)
            match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<owl:Class rdf:ID="', '').replace('">', '')
        match = match.replace('<owl:Class rdf:about="#', '').replace('">', '')
        return match

    def get_properties(self, ontology_class):
        pattern = re.compile('<owl:ObjectProperty rdf:ID="\S+"\/>', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<owl:ObjectProperty rdf:ID="', '').replace('"/>', '')
        return match

    def get_comment(self, ontology_class):
        pattern = re.compile('<rdfs:comment rdf:datatype=.* >(.)*<\/rdfs:comment>', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string"', '')
        match = match.replace('</rdfs:comment>', '').replace('    ', '')
        match = match.replace('>', '')
        return match

    def find_pattern(self, pattern, ontology_class):
        match = re.search(pattern, ontology_class)
        if match:
            return match.group(0)
        return ""