from nltk.corpus import wordnet as wn

# print(wn.synsets('motorcar'))
# print(wn.synset('car.n.01').lemma_names())
#
#
# for synset in wn.synsets('car'):
#     print(synset.lemma_names)
#

# find the hypo
# motorcar = wn.synset('car.n.01')
# types_of_motorcar = motorcar.hyponyms()
# print(sorted(lemma.name()
#               for synset in types_of_motorcar
#               for lemma in synset.lemmas()))

# find the hyper
# motorcar = wn.synset('car.n.01')
# paths = motorcar.hypernym_paths()
# print(len(paths))
# print([synset.name() for synset in paths[0]])
# print([synset.name() for synset in paths[1]])

# motorcar = wn.synset('car.n.01')
# print(motorcar.root_hypernyms())
import nltk
nltk.app.wordnet()
