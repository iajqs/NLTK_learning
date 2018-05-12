from nltk.corpus import brown
import nltk

# get the tagged sentences of brown
brown_tagged_sents = brown.tagged_sents(categories='news')
# get the sentences of brown
brown_sents = brown.sents(categories='news')
# get the unigram_tagger tool
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)

size = int(len(brown_tagged_sents)*0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print(t2.tag(["I","am","a","good","guy"]))
value = t2.evaluate(test_sents)
print(value)

# test_tags = [tag for sent in brown.sents(categories='editorial')
#              for (word, tag) in t2.tag(sent)]
# gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
# print(nltk.ConfusionMatrix(gold_tags, test_tags))
