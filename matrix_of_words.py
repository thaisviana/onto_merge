from extractor import create_ontology_data
from preprocessing import preProcessing
from collections import defaultdict


def matrix():
    words = []
    ontologies = create_ontology_data()
    for key in ['cosc', 'cso', 'algpedia', 'cops']:
        print(key)
        for onto_class in ontologies[key].classes:
            line = preProcessing(onto_class.comment)
            words.append(line)
    return retina(words)

def sum_dictionaries(dicts):
    ret = defaultdict(int)
    outro_dict = {}
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    for k in ret.keys():
        if 1 < ret[k]:
            outro_dict[k] = ret[k]
    print(outro_dict)
    return outro_dict


def retina(lines):
    retina = []
    words = sum_dictionaries(lines)
    l = list(words.keys())
    l_set = set(l)
    path = "C:/Users/viana/Documents/GitHub/onto_merge/retina.py"
    retinafile = open(path, 'w')
    retinafile.write("retina = [")
    for line in lines:
        retina_line = []
        line = set(line.keys())
        if l_set.intersection(line):
            retinafile.write("[")
            for word in l_set:
                appears = 1 if word in line else 0
                retinafile.write(str(appears)) if word == l[-1] else retinafile.write(str(appears) + ", ")
                retina_line.append(appears)
            retinafile.write("],")
            retinafile.write("\n")
            retina.append(retina_line)
    retinafile.write("]")
    return retina
