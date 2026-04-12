import nltk
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures

nltk.download('punkt')

text = """
Natural Language Processing is a branch of Artificial Intelligence.
Natural Language Processing helps machines understand human language.
Language processing is widely used in speech and text analysis applications.
"""

# tokenize
words = word_tokenize(text.lower())

# print all bigrams
print("ALL BIGRAMS:")
for pair in nltk.bigrams(words):
    print(pair)

# find top 5 collocations
finder = BigramCollocationFinder.from_words(words)
top = finder.nbest(BigramAssocMeasures().pmi, 5)

print("\nTOP 5 COLLOCATIONS:")
for pair in top:
    print(pair)