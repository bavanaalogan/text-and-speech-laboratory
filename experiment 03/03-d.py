import nltk, re
from nltk.corpus import twitter_samples, stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('twitter_samples')

# get text
text = ' '.join(twitter_samples.strings()[:5000]).lower()

# clean text
text = re.sub(r'[^a-zA-Z ]', ' ', text)

# tokenize and remove stopwords
words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
words = [w for w in words if w not in stop_words and w.isalpha()]

# get top 30 words
common = Counter(words).most_common(30)
w, c = zip(*common)

# plot
plt.bar(w, c)
plt.xticks(rotation=45)
plt.title("Top 30 Words")
plt.tight_layout()
plt.show()