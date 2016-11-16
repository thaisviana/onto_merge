from ical import ICALOntology


def create_ontology_data():
    f = open('oaei/ical.rdf', encoding="utf8")
    ical = ICALOntology(owl=f)
    print('ical', len(ical.classes), [(o_class.name) for o_class in ical.classes if o_class.comment is not ''])

    f = open('oaei/index.rdf', encoding="utf8")
    index = ICALOntology(owl=f)
    print('index', len(ical.classes), [(o_class.name) for o_class in index.classes if o_class.comment is not ''])

    f = open('oaei/IFC4.ttl', encoding="utf8")
    ifc = ICALOntology(owl=f)
    print('ifc', len(ical.classes), [(o_class.name) for o_class in ifc.classes if o_class.comment is not ''])

    ontology = {}
    ontology['ical'] = ical
    ontology['index'] = index
    ontology['ifc'] = ifc

    return ontology
