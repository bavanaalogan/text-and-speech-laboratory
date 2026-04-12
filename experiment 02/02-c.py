import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

text = """
Natural Language Processing is a branch of Artificial Intelligence.
Natural Language Processing helps machines understand human language.
Language processing is widely used in speech and text analysis applications.
"""

# tokenize and remove stopwords
words = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
words = [w for w in words if w.isalpha() and w not in stop_words]

# frequency
freq = FreqDist(words)
print("Top Words:",freq.most_common(5))

# collocations
finder = BigramCollocationFinder.from_words(words)
pairs = finder.nbest(BigramAssocMeasures().pmi, 5)
print("\nTop Collocations:",pairs)
