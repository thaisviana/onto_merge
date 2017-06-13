import rdflib
from onto_class import OntologyClass


class IFCOntology:
    def __init__(self, file_path):
        graph = rdflib.Graph()
        graph.load(file_path)
        self.classes = []
        # print out all the triples in the graph
        for subject, predicate, object in graph:
            onto_class = OntologyClass()
            onto_class.name = subject.replace('http://xmlns.com/foaf/0.1/', '').replace('https://www.auto.tuwien.ac.at/downloads/thinkhome/ontology/EnergyResourceOntology.owl#', '')
            onto_class.comment = ''
            if '#comment' in predicate:
                onto_class.comment = object
            else:
                onto_class.comment = ''
            #print(onto_class.name, onto_class.comment)
            self.classes.append(onto_class)
