import re
from onto_class import OntologyClass
import requests
from bs4 import BeautifulSoup


class COPSOntology:
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
        comment = self.get_comment(name)
        if (name, comment) is not ('', ''):
            onto_class = OntologyClass()
            onto_class.properties = [self.get_properties(ontology_class)]
            onto_class.name, onto_class.comment = name, comment
            self.classes.append(onto_class)

    def get_name(self, ontology_class):
        pattern = re.compile('<owl:Class rdf:about="http:\/\/www\.semanticweb\.org\/marlem\/ontologies\/2015\/10\/'
                             'untitled-ontology-2#(\S+)[">]', re.IGNORECASE)
        match = self.find_pattern(pattern, ontology_class)
        match = match.replace('<owl:Class rdf:about="http://www.semanticweb.org/marlem/ontologies/2015/10/untitled-'
                              'ontology-2#', '').replace('">', '')
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

    def get_comment(self, class_name):
        name = class_name.lower().replace('_', '').replace('-', '')
        html_page = requests.get('http://pc.net/glossary/definition/' + name)
        soup = self.soup_wrapper(html_page)
        comment = soup.findAll("div", {"id": "definition"})
        if comment:
            result = ''
            for tag in comment:
                result += tag.get_text()
            return result
        else:
            class_name = class_name.lower().replace('-', '_')
            html_page = requests.get('https://en.wikipedia.org/wiki/' + class_name)
            soup = self.soup_wrapper(html_page)
            comment = soup.find(id="mw-content-text")
            about = comment.find('p')
            if about is not None and 'reasons this message may be displayed' not in about.text:
                if 'can refer to:' not in about.text and 'may refer to:' not in about.text:
                    return about.text
        return ''

    def find_pattern(self, pattern, ontology_class):
        match = re.search(pattern, ontology_class)
        if match:
            return match.group(0)
        return ""
