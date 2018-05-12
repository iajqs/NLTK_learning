from nltk.corpus import brown
import nltk
# get the tagged sentences of brown
brown_tagged_sents = brown.tagged_sents(categories='news')
# get the sentences of brown
brown_sents = brown.sents(categories='news')
# get the unigram_tagger tool
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# tag
unigram_tagger.tag(brown_sents[2007])
# test the value
value = unigram_tagger.evaluate(brown_tagged_sents)
print(value)




