import nltk
# # a sample sentence
# sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
# ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
#
# # the regex rule
# grammar = "NP: {<DT>?<JJ>*<NN>}"
#
# # init the regex tool
# cp = nltk.RegexpParser(grammar)
# # parse the sentence by regex about grammar
# result = cp.parse(sentence)
# print(result)
#
# result.draw()
#
# cp = nltk.RegexpParser('CHUNK: {<V.*><TO><V.*>}')
# brown = nltk.corpus.brown
# for sent in brown.tagged_sents():
#     tree = cp.parse(sent)
#     for subtree in tree.subtrees():
#         if subtree.label() == 'CHUNK': print(subtree)


# # Crevice
# grammar = r"""
#     NP:
#     {<.*>+}
#     }<VBD|IN>+{
#     """
# cp = nltk.RegexpParser(grammar)
# print(cp.parse(sentence))


from nltk.corpus import conll2000
print(conll2000.chunked_sents('train.txt')[99])
print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])

# none regex
cp = nltk.RegexpParser("")
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
print(cp.evaluate(test_sents))

# a easy regex
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
print(cp.evaluate(test_sents))