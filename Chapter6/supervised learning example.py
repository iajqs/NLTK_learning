import nltk

# # 1
# # get the sentences of the treebank_raw
# sents = nltk.corpus.treebank_raw.sents()
# tokens = []
# boundaries = set()
# offset = 0
# # get the all punctuation of the sentences' end
# for sent in nltk.corpus.treebank_raw.sents():
#     tokens.extend(sent)
#     offset += len(sent)
#     boundaries.add(offset-1)
#
# # get the features of the punctuation like [.?!]
# def punct_features(tokens, i):
#     return {'next-word-apitalized': tokens[i+1][0].isupper(),
#             'prevword': tokens[i-1].lower(),
#             'punct': tokens[i],
#             'prev-word-is-one-char': len(tokens[i-1]) == 1}
#
# # get the featuresets of the tokens
# featuresets = [(punct_features(tokens, i), (i in boundaries))
#                for i in range(1, len(tokens)-1)
#                if tokens[i] in '.?!']
#
# # divide the train_set and test_set as 9:1
# size = int(len(featuresets) * 0.1)
# # get the train_set and the test_set
# train_set, test_set = featuresets[size:], featuresets[:size]
# # train
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# # caculate the accuracy-----test
# accuracy = nltk.classify.accuracy(classifier, test_set)
# print(accuracy)

# 2
def rte_features(rtepair):
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

rtepairs = nltk.corpus.rte.pairs(['rte3_dev.xml'])