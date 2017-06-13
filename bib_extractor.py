from ical import ICALOntology
from cops import COPSOntology
from cso import CSOOntology
from algpedia import build_ontology

def create_ontology_data():

    print('cops create_data')
    f = open('/home/thais/mestrado/onto_merge/cops.owl', encoding="utf8")
    cops = COPSOntology(owl=f)
    print('cops', len(cops.classes), [(o_class.name) for o_class in cops.classes if o_class.comment is not ''])

    print('cso create_data')
    f = open('/home/thais/mestrado/onto_merge/cso.owl', encoding="utf8")
    cso = CSOOntology(owl=f)
    print('cso', len(cso.classes), [(o_class.name) for o_class in cso.classes if o_class.comment is not ''])


    print('cosc create_data')
    f = open('/home/thais/mestrado/onto_merge/cosc.owl', encoding="utf8")
    cosc = CSOOntology(owl=f)
    print('cosc', len(cosc.classes), [(o_class.name) for o_class in cosc.classes if o_class.comment is not ''])

    ontology = {}
    ontology['COPS'] = cops
    ontology['CSO'] = cso
    ontology['COSC'] = cosc
    ontology['algpedia'] = build_ontology()

    return ontology
