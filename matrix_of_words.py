from extractor import create_ontology_data
from preprocessing import preProcessing
from collections import defaultdict


def matrix():
    words = []
    ontologies = create_ontology_data()
    for key in ontologies:
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
        if 2 < ret[k] < 32:
            outro_dict[k] = ret[k]
    print(outro_dict)
    return outro_dict


def retina(lines):
    retina = []
    words = sum_dictionaries(lines)
    l = list(words.items())
    path = "C:/Users/viana/Documents/GitHub/ontology_merge/retina.py"
    retinafile = open(path, 'w')
    retinafile.write("retina = [")
    for line in lines:
        retina_line = []
        retinafile.write("[")
        for word in l:
            appears = 1 if word[0] in line else 0
            retinafile.write(str(appears)) if word == l[-1] else retinafile.write(str(appears) + ", ")
            retina_line.append(appears)
        retinafile.write("],")
        retinafile.write("\n")
        retina.append(retina_line)
    retinafile.write("]")
    return retina
