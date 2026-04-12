import nltk, numpy as np
from nltk.corpus import twitter_samples
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('twitter_samples')

# load data
pos = twitter_samples.strings('positive_tweets.json')
neg = twitter_samples.strings('negative_tweets.json')

tweets = pos + neg
labels = [1]*len(pos) + [0]*len(neg)

# ── WORD2VEC ──
sentences = [t.split() for t in tweets]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2)

def sent_vec(t):
    words = [model.wv[w] for w in t.split() if w in model.wv]
    return np.mean(words, axis=0) if words else np.zeros(100)

X_w2v = np.array([sent_vec(t) for t in tweets])
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X_w2v, y, test_size=0.2)

clf1 = LogisticRegression(max_iter=1000)
clf1.fit(X_train, y_train)

print("Word2Vec Accuracy:", clf1.score(X_test, y_test))


# ── TF-IDF ──
tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(tweets)

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2)

clf2 = LogisticRegression(max_iter=1000)
clf2.fit(X_train, y_train)

print("TF-IDF Accuracy:", clf2.score(X_test, y_test))


# ── PREDICTION ──
sample = input("Enter a tweet to analyze sentiment: ")
vec = sent_vec(sample).reshape(1, -1)

pred = clf1.predict(vec)[0]
print("Prediction:", "Positive 😊" if pred==1 else "Negative 😞")