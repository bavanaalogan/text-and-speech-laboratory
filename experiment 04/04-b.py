import nltk
from nltk.corpus import gutenberg
from nltk import FreqDist
nltk.download('gutenberg')
words = gutenberg.words('austen-emma.txt')

# total words
print("Total words:", len(words))

# vocabulary size
print("Unique words:", len(set(words)))

# top 10 words
fd = FreqDist(words)
print("Top 10 words:", fd.most_common(10))