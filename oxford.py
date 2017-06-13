from oxforddict.oxfordwrapper import OxfordDictionary
import time


def get_synonyms(word):
    d = OxfordDictionary()
    time.sleep(2)
    oxford = d.thesaurus(word)
    if oxford != {}:
        lexicalentries = [result['lexicalEntries'] for result in oxford['results']][0]
        entries = [lexicalentry['entries'] for lexicalentry in lexicalentries][0]
        senses = [entry['senses'] for entry in entries][0]
        try:
            subsenses = [i['subsenses'] for i in [sense for sense in senses][0]]
        except TypeError:
            subsenses = senses
        synonyms = [subsense['synonyms'] for subsense in subsenses][0]
        syn_dict = dict()
        for synonym in synonyms:
            syn_dict[synonym['text']] = 1
    return {}
