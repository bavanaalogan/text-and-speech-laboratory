import nltk
from nltk.corpus import gutenberg
nltk.download('gutenberg')
print(gutenberg.fileids())
words = gutenberg.words('austen-emma.txt')
print(words[:20])