from ical import ICALOntology
from ifc import IFCOntology


def create_ontology_data():
    print('create_data')
    f = open('/home/thais/mestrado/onto_merge/oaei/ical.rdf', encoding="utf8")
    ical = ICALOntology(owl=f)
    print('ical', len(ical.classes), [(o_class.name) for o_class in ical.classes if o_class.comment is not ''])

    f = open('/home/thais/mestrado/onto_merge/oaei/index.rdf', encoding="utf8")
    index = IFCOntology(file_path=f)
    print('index', len(index.classes), [(o_class.name) for o_class in index.classes if o_class.comment is not ''])

    f = open('/home/thais/mestrado/onto_merge/oaei/EnergyResourceOntology.owl', encoding="utf8")
    energy = IFCOntology(file_path=f)
    print('ifc', len(energy.classes), [(o_class.name) for o_class in energy.classes if o_class.comment is not ''])

    ontology = {}
    ontology['ical'] = ical
    ontology['index'] = index
    ontology['ifc'] = energy

    return ontology
