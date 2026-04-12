import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples
from collections import Counter

nltk.download('punkt')
nltk.download('twitter_samples')

# use strings() instead of words()
text = ' '.join(twitter_samples.strings()[:5000]).lower()

# tokenize and count words
words = word_tokenize(text)
freq = Counter(w for w in words if w.isalpha())

# print top 20
print("Top Words:")
for w, c in freq.most_common(20):
    print(w, "->", c)