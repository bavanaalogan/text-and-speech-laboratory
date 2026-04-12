import nltk
import matplotlib.pyplot as plt
from nltk.corpus import twitter_samples
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

nltk.download('twitter_samples')

# ── LOAD DATA ───────────────────────────────
tweets = twitter_samples.strings()
sentences = [t.split() for t in tweets]

# ── TRAIN WORD2VEC ─────────────────────────
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2)

# ── SELECT 50 WORDS ────────────────────────
words = list(model.wv.index_to_key)[:50]
vectors = [model.wv[w] for w in words]

# ── APPLY PCA (100D → 2D) ──────────────────
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

# ── PLOT ───────────────────────────────────
plt.figure(figsize=(10,6))
plt.scatter(reduced_vectors[:,0], reduced_vectors[:,1])

for i, word in enumerate(words):
    plt.text(reduced_vectors[i,0], reduced_vectors[i,1], word)

plt.title("Word Embedding Visualization (PCA)")
plt.show()