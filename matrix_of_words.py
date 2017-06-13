import time
import re
from oxford import get_synonyms
from extractor import create_ontology_data as software_domain_ontology
from bib_extractor_oaei import create_ontology_data as energy_domain_ontology
from preprocessing import preProcessing
from collections import defaultdict


def matrix(label_ontology_list):
    start_time = time.time()
    matrix = []
    if 'algpedia' in label_ontology_list:
        ontologies = software_domain_ontology()
    elif 'ical' in label_ontology_list:
        ontologies = energy_domain_ontology()
    for key in label_ontology_list:
        for onto_class in ontologies[key].classes:
            if onto_class.comment == '':
                if any(char.isdigit() for char in onto_class.name):
                    continue
                else:
                    splited = re.findall('[A-Z][^A-Z]*', onto_class.name)
                    if len(splited) > 1:
                        line = preProcessing(splited)
                    else:
                        print(onto_class.name)
                        #line = get_synonyms(onto_class.name)
            else:
                line = preProcessing(onto_class.comment)
            matrix.append((key, onto_class.name, line))
    print("--- %s seconds ---" % (time.time() - start_time))
    return retina(matrix)


def sum_dictionaries(dicts):
    ret = defaultdict(int)
    outro_dict = {}
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    for k in ret.keys():
        if 1 < ret[k]:
            outro_dict[k] = ret[k]
    return outro_dict


def retina(matrix):
    print(matrix)
    bags_of_words = [line[2] for line in matrix]
    words = sum_dictionaries(bags_of_words)
    print(words)
