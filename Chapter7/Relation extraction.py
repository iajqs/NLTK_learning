# ok, this also is a very simple example about RE
import re
import nltk
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                                     corpus='ieer', pattern=IN):
        print(nltk.sem.rtuple(rel))



from nltk.corpus import conll2002
vnv = """
(
is/V|    
was/V|   
werd/V|  
wordt/V  
)
.*      
van/Prep 
"""
VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc,
                                   corpus='conll2002', pattern=VAN):
        print(nltk.sem.clause(r, relsym="VAN"))
