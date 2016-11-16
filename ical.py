import re
from onto_class import OntologyClass
import requests
from bs4 import BeautifulSoup


class ICALOntology:
    def __init__(self, owl):
        self.classes = []
        class_pattern = ""
        number_open_children = 0
        for line in owl:
            if re.search("<owl:Class ", str(line)) and not re.search("/>", str(line)):
                number_open_children += 1
            elif re.search('<owl:Class', line) and not re.search("/>", str(line)):
                number_open_children += 1
            if number_open_children > 0:
                class_pattern += line
            if re.search('</owl:Class>', line):
                number_open_children -= 1
            if number_open_children == 0 and class_pattern is not "":
                self.refine_classes(str(class_pattern))
                class_pattern = ""

    def refine_classes(self, ontology_class):
        name = self.get_name(ontology_class)
        comment = self.get_comment(ontology_class)
        if comment is not '':
            onto_class = OntologyClass()
            onto_class.properties = [self.get_properties(ontology_class)]
            onto_class.name, onto_class.comment = name, comment
            self.classes.append(onto_class)

    def get_name(self, ontology_class):
        pattern = re.compile('<owl:Class rdf:ID="(\S+)[">]', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<owl:Class rdf:ID="', '').replace('">', '')
        return match

    def get_properties(self, ontology_class):
        pattern = re.compile('<owl:onProperty rdf:resource="http:\/\/www\.semanticweb\.org\/marlem\/ontologies\/2015'
                             '\/10\/untitled-ontology-2#(\S+)["\/>]', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<owl:onProperty rdf:resource="http://www.semanticweb.org/marlem/ontologies/2015/10/'
                              'untitled-ontology-2#', '').replace('"/>', '')
        return match

    def soup_wrapper(self, url):
        content = str(url.content, "ascii", errors="ignore")
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def get_comment(self, ontology_class):
        texts = ontology_class.split('<rdfs:comment>')
        if len(texts) > 1:
            match = texts[1]
            """pattern = re.compile('<rdfs:comment>(.)*<\/rdfs:comment>', re.IGNORECASE)
            match = self.find_pattern(pattern, ontology_class)"""
            match = match.replace('<rdfs:comment>', '')
            match = match.split('</rdfs:comment>')
            match = match[0]
            match = match.replace('>', '')
            match = match.replace('\n', '')
            return match
        return ''

    def find_pattern(self, pattern, ontology_class):
        match = re.search(pattern, ontology_class)
        if match:
            return match.group(0)
        return ""
