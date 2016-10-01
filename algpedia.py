from onto_class import OntologyClass
from cso import CSOOntology


def build_ontology():
    classes = []
    #ALGORITHM
    onto_class = OntologyClass()
    onto_class.properties = ['belongs', 'implementation', 'developer']
    onto_class.name = 'ALGORITHM'.lower()
    onto_class.comment = 'formed by the names of algorithms extracted from Wikipedia page. This class has the ' \
                         'attributes description, wikipediaLink and dbpediaLink.A process or set of rules to be ' \
                         'followed in calculations or other problem-solving operations, especially by a computer.'
    classes.append(onto_class)

    #CLASSIFICATION
    onto_class = OntologyClass()
    onto_class.properties = ['belongs']
    onto_class.name = 'CLASSIFICATION'.lower()
    onto_class.comment = 'formed by the algorithm categories extracted in DBPedia crawling process. This class has the' \
                         ' attributes  wikipediaLink and dbpediaLink.  The action or process of classifying something.' \
                         'A category into which something is put.'
    classes.append(onto_class)

    #AUTHOR
    onto_class = OntologyClass()
    onto_class.properties = ['developer']
    onto_class.name = 'AUTHOR'.lower()
    onto_class.comment = 'formed by the individuals who had developed an algorithm.In the sense ‘be the author of’' \
                         ' the verb author is objected to by some traditionalists. It is well established, though, ' \
                         'especially in North America, and has been in use since the end of the 16th century'
    classes.append(onto_class)

    #PROGRAMMING LANGUAGES
    onto_class = OntologyClass()
    onto_class.properties = ['implementation']
    onto_class.name = 'PROGRAMMING LANGUAGES'.lower()
    onto_class.comment = 'formed by the programming language names in which the extracted algorithms are implemented.' \
                         'A system of precisely defined symbols and rules devised for writing computer programs.'
    classes.append(onto_class)
    cso = CSOOntology("algpedia", True)
    cso.classes = classes
    return cso
