import nltk
from nltk.corpus import conll2000
class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
                      for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        ## get the word's tag
        pos_tags = [pos for (word,pos) in sentence]
        ## tag the chunk
        tagged_pos_tags = self.tagger.tag(pos_tags)
        ## get the chunktagged list
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        ## get the <word, pos, chunktag> list
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        ## return the chunktagged data use conlltagstree struction
        return nltk.chunk.conlltags2tree(conlltags)

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))


