import nltk
from nltk.corpus import twitter_samples
from gensim.models import Word2Vec

nltk.download('twitter_samples')

# ── TRAIN MODEL ───────────────────────────
tweets = twitter_samples.strings()
sentences = [t.split() for t in tweets]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=2)

# ── SELECT WORDS ─────────────────────────
words_to_check = ['happy', 'sad', 'angry', 'love', 'hate']

# ── FIND SIMILAR WORDS ───────────────────
for word in words_to_check:
    print("\nWord:", word)
    
    if word in model.wv:
        similar = model.wv.most_similar(word, topn=10)
        for w, score in similar:
            print(f"  {w} ({round(score,3)})")
    else:
        print("  Not found in vocabulary")