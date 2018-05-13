from nltk.corpus import movie_reviews
import nltk
import random

# # 1
# # set the word's feature is the last character of this word
# def gender_features(word):
#     return {'last_letter': word[-1],}
# #
# # print(gender_features('Shrek'))
# #
# #
# # 2
# from nltk.corpus import names
# import random
# names = ([(name, 'male') for name in names.words('male.txt')] +
#          [(name, 'female') for name in names.words('female.txt')])
# # random sort all elements
# random.shuffle(names)
# ## make features list save all feature like {'last_letter', word[-1]}
# featuresets = [(gender_features(n), g) for (n, g) in names]
# train_set, test_set = featuresets[500:], featuresets[:500]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(classifier.classify(gender_features('Neo')))
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(5))
#
# # 3
# # use the apply_features return a likedlist but it will not save in the memory
# from nltk.classify import apply_features
# train_set = apply_features(gender_features, names[500:])
# test_set = apply_features(gender_features, names[:500])
#
# # 4
# train_names = names[1500:]
# devtest_names = names[500:1500]
# test_names = names[:500]
#
# train_set = [(gender_features(n), g) for (n, g) in train_names]
# devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
# test_set = [(gender_features(n), g) for (n, g) in test_names]
#
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, devtest_set))
#
# # 5
# get the error list
# errors = []
# for (name, tag) in devtest_names:
#     guess = classifier.classify(gender_features(name))
#     if guess != tag:
#         errors.append((tag, guess, name))
#
# for (tag, guess, name) in sorted(errors):
#     print('correct=%-8s guess=%-8s name=%-30s' %(tag, guess, name))
#
# # 6
# def gender_features2(word):
#     return {'suffix1': word[-1:],
#             'suffix2': word[-2:]}
# train_set = [(gender_features2(n), g) for (n, g) in train_names]
# devtest_set = [(gender_features2(n), g) for (n, g) in devtest_names]
# test_set = [(gender_features2(n), g) for (n, g) in test_names]
#
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, devtest_set))
#
# # 7
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)
#
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words)[:2000]
# def document_features(document):
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains(%s)' % word] = (word in document_words)
#     return features
#
# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))
#
# # 8
# featuresets = [(document_features(d), c) for (d, c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(5))

# # 9
# from nltk.corpus import brown
# # init a frequence list
# suffix_fdist = nltk.FreqDist()
# # caculate the frequence of foot of the word
# for word in brown.words():
#     word = word.lower()
#     suffix_fdist[word[-1:]] += 1
#     suffix_fdist[word[-2:]] += 1
#     suffix_fdist[word[-3:]] += 1
# # the most common foot of the word -- top100
# common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
# print(common_suffixes)
#
# # print the word's feature -- foot of the word
# def pos_features(word):
#     features = {}
#     for suffix in common_suffixes:
#         features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
#     return features
#
# # get the tagged words of the brown about news
# tagged_words = brown.tagged_words(categories='news')
# # init the set of the features like(foot of the word, tag)
# featuresets = [(pos_features(n), g) for (n, g) in tagged_words]
# # divide the set of features to 1(test_set):9(train_set)
# size = int(len(featuresets) * 0.1)
# # get the train_set, test_set from featuresets
# train_set, test_set = featuresets[size:], featuresets[:size]
# # train by DecisionTree
# classifier = nltk.DecisionTreeClassifier.train(train_set)
# # caculate the accuracy
# accuracy = nltk.classify.accuracy(classifier, test_set)
# print(accuracy)



# # 10
# from nltk.corpus import brown
# ## use the pre word as the features
# def pos_features(sentence, i):
#     features = {"suffix(1)": sentence[i][-1:],
#                 "suffix(2)": sentence[i][-2:],
#                 "suffix(3)": sentence[i][-3:]}
#     if i == 0:
#         features["prev-word"] = "<START>"
#     else:
#         features["prev-word"] = sentence[i-1]
#     return features
#
# print(pos_features(brown.sents()[0], 8))
# ## get the tagged sents from brown about news
# tagged_sents = brown.tagged_sents(categories='news')
# featuresets = []
#
# for tagged_sent in tagged_sents:
#     ### remove the word's tag, and get the untagged sent
#     untagged_sent = nltk.tag.untag(tagged_sent)
#     for i, (word, tag) in enumerate(tagged_sent):
#         featuresets.append((pos_features(untagged_sent, i), tag))
# # divide the set of features to 1(test_set):9(train_set)
# size = int(len(featuresets) * 0.1)
# # get the train_set, test_set from featuresets
# train_set, test_set = featuresets[size:], featuresets[:size]
# # train
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# # test
# accuracy = nltk.classify.accuracy(classifier, test_set)
# print(accuracy)


# 11
## add the pre word and it's tag as the feature
def pos_features(sentence, i, history):
    features = {"suffix(1)": sentence[i][-1:],
             "suffix(2)": sentence[i][-2:],
             "suffix(3)": sentence[i][-3:]}
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):

    # the Entrance
    def __init__(self, train_sents):
        train_set = []
        ## ergodic the sentences' list
        for tagged_sent in train_sents:
            ### get the untagged the sentence
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            ### enumerate the tagged_sent
            for i, (word, tag) in enumerate(tagged_sent):
                #### get the featureset by pos_features function
                featureset = pos_features(untagged_sent, i, history)
                #### add the featureset to the train_set
                train_set.append( (featureset, tag) )
                #### add the history tag to the history list
                history.append(tag)
        ## train
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

from nltk.corpus import brown
tagged_sents = brown.tagged_sents(categories='news')
size = int(len(tagged_sents) * 0.1)
train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
tagger = ConsecutivePosTagger(train_sents)
# this operation will use the tag function , but i don't know why
print(tagger.evaluate(test_sents))