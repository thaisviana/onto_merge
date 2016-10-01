import requests
from cso import CSOOntology
from cops import COPSOntology
from owlready import *
from algpedia import build_ontology


def create_ontology_data():
    r = requests.get('https://km.aifb.kit.edu/sites/cos/cosc.owl')
    cosc = CSOOntology(owl=r)
    print('cosc', len([o_class.name for o_class in cosc.classes]))

    r = requests.get('https://km.aifb.kit.edu/sites/cos/cso.owl')
    cso = CSOOntology(owl=r)
    print('cso', len([o_class.name for o_class in cso.classes]))

    #algpedia_ontology = get_ontology('http://algpedia.dcc.ufrj.br/algorithm/static/ontology/algorithm.owl').load()
    algpedia = build_ontology()
    print('algpedia', len([o_class.name for o_class in algpedia.classes]))
    #print(algpedia_ontology.instances)

    f = open('cops.owl', 'r')
    cops = COPSOntology(owl=f)

    print('cops', len([o_class.name for o_class in cops.classes]))

    ontology = {}
    ontology['cosc'] = cosc
    ontology['cso'] = cso
    ontology['algpedia'] = algpedia
    ontology['cops'] = cops

    return ontology
