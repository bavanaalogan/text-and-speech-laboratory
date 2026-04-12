"""
pip install wordcloud
"""

import nltk
from nltk.corpus import gutenberg
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('gutenberg')

words = gutenberg.words('austen-emma.txt')

# bigrams
bigrams = list(nltk.bigrams(words))
top_bigrams = Counter(bigrams).most_common(10)
print("Top 10 bigrams:", top_bigrams)

# word cloud
text = ' '.join(str(word) for word in words)
wc = WordCloud().generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()