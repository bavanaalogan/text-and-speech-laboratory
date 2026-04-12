import nltk
from nltk.corpus import brown
from collections import Counter

nltk.download('brown')
nltk.download('averaged_perceptron_tagger_eng')

# get words
words = brown.words(categories='news')

# POS tagging
tagged = nltk.pos_tag(words)

# filter nouns (NN, NNS, NNP, NNPS)
nouns = [w for w, t in tagged if t.startswith('NN')]

# top 10 nouns
top_nouns = Counter(nouns).most_common(10)
print("Top 10 nouns:", top_nouns)