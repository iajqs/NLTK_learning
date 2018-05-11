import nltk
from nltk.book import *

# print(text1)

# print(text1.concordance("monstrous"))

# print(text1.similar("monstrous"))

# print(text2.common_contexts(["monstrous", "very"]))

# print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))
## in the nltk3, this function is unuseful
# print(text3.generate())

# print(len(text1))

# print(sorted(set(text3)))

# print(len(set(text3)))

# print(len(text3)/len(set(text3)))

# print(text3.count("smote"))

# print(100 * text4.count('a')/len(text4))

# print(sent2)

# print(sent4 + sent1)

# str = ['a', 'b', 'c']
# print(str.count('a'))

# print(text4.index('awaken'))

# print(sent1[0:3])
# print(sent1[0])
# print(sent1[1])
# print(sent1[2])

# name = 'Monty'
# print(name[0])
# print(name[0:4])

# name = 'Monty'
# print(name*2)
# print(name+'!')

# print(' '.join(['Monty', 'Python']))
# print('Monty Python'.split())

# fdist1 = FreqDist(text1)
# print(fdist1)
# vocabulary1 = fdist1.most_common(50)
# print(vocabulary1)
# print(fdist1['whale'])

# fdist1 = FreqDist(text1)
# fdist1.plot(50, cumulative=True)

# fdist1 = FreqDist(text1)
# print(fdist1.hapaxes())

# V = set(text1)
# long_words = [w for w in V if len(w) > 15]
# print(sorted(long_words))

## important
# print("text4 : ")
# print(text4.collocations())

fdist = FreqDist([len(w) for w in text1])
print(fdist.keys())
print(fdist.items())
fdist.plot()
fdist.plot(cumulative=True)