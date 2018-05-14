import nltk
from nltk.corpus import conll2000
class ConsecutiveNPChunkTagger(nltk.TaggerI):

    # train the tagger
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            ## just get the <word, tag> list
            untagged_sent = nltk.tag.untag(tagged_sent)
            ## save the all pre word:<word, tag>
            history = []
            ## ok, this word mean <word, tag>, tag mean chunktag
            for i, (word, tag) in enumerate(tagged_sent):
                ### get the featureset by npchunk_features
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        ## train a classifier
        self.classifier = nltk.MaxentClassifier.train(
            train_set)

    # tag function
    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        ## get the <<word, tag>, chunktag> list from train_sents by nltk.chunk.tree2conlltags()
        tagged_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        ## use the ConsecutiveNPChunkTagger to get the tagger
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        ## tag the sentence by tagger, tag <word, tag> to <<word, tag>, chunktag>
        tagged_sents = self.tagger.tag(sentence)
        ## get the tagged list
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        ## return the chunktagged data use conlltagstree struction
        return nltk.chunk.conlltags2tree(conlltags)

# def npchunk_features(sentence, i, history):
#     word, pos = sentence[i]
#     return {"pos": pos}

def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    if i == 0:
        prevword, prevpos = "<START>", "<START>"
    else:
        prevword, prevpos = sentence[i-1]
    if i == len(sentence)-1:
        nextword, nextpos = "<END>", "<END>"
    else:
        nextword, nextpos = sentence[i+1]
    return {"pos": pos,
            "word": word,
            "prevpos": prevpos,
            "nextpos": nextpos,
            "prevpos+pos": "%s+%s" % (prevpos, pos),
            "pos+nextpos": "%s+%s" % (pos, nextpos),
            "tags-since-dt": tags_since_dt(sentence, i)}

def tags_since_dt(sentence, i):
    tags = set()
    for word, pos in sentence[:i]:
        if pos == 'DT':
            tags = set()
        else:
            tags.add(pos)
    return '+'.join(sorted(tags))

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))