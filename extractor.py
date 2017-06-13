import requests
from cso import CSOOntology
from cops import COPSOntology
from algpedia import build_ontology


def create_ontology_data():

    r = requests.get('https://km.aifb.kit.edu/sites/cos/cosc.owl')
    cosc = CSOOntology(owl=r)
    print('cosc', len(cosc.classes), [(o_class.name) for o_class in cosc.classes if o_class.comment is not ''])

    #r = requests.get('http://dontpad.com/thaisviana/cso.owl')
    r = requests.get('https://km.aifb.kit.edu/sites/cos/cso.owl')
    cso = CSOOntology(owl=r)
    print('cso', len(cso.classes), [(o_class.name) for o_class in cso.classes if o_class.comment is not ''])

    algpedia = build_ontology()
    print('algpedia', len(algpedia.classes), [(o_class.name) for o_class in algpedia.classes if o_class.comment is not ''])

    f = open('/home/thais/mestrado/onto_merge/software_domain/cops2.owl', encoding="utf8")
    cops = COPSOntology(owl=f)

    print('cops', len(cops.classes), [(o_class.name) for o_class in cops.classes if o_class.comment is not ''])

    ontology = {}
    ontology['cosc'] = cosc
    ontology['cso'] = cso
    ontology['algpedia'] = algpedia
    ontology['cops'] = cops

    return ontology
