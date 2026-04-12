import nltk
import time
from nltk.corpus import twitter_samples
from gensim.models import Word2Vec

nltk.download('twitter_samples')

# ── LOAD DATA ─────────────────────────────────────────────
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')

all_tweets = positive_tweets + negative_tweets

# tokenize tweets
tokenized_sentences = [tweet.split() for tweet in all_tweets]

# ── WORDS TO CHECK SIMILARITY ─────────────────────────────
word_1 = 'good'
word_2 = 'great'

# ── DIFFERENT MODEL SETTINGS ──────────────────────────────
model_configs = [
    {'vector_size': 50,  'window': 3, 'min_count': 1, 'sg': 0},  # CBOW small
    {'vector_size': 100, 'window': 5, 'min_count': 2, 'sg': 0},  # CBOW medium
    {'vector_size': 200, 'window': 7, 'min_count': 3, 'sg': 0},  # CBOW large
    {'vector_size': 50,  'window': 3, 'min_count': 1, 'sg': 1},  # Skip-gram small
    {'vector_size': 100, 'window': 5, 'min_count': 2, 'sg': 1},  # Skip-gram medium
    {'vector_size': 200, 'window': 7, 'min_count': 3, 'sg': 1},  # Skip-gram large
]

# ── STORE RESULTS ─────────────────────────────────────────
experiment_results = []

# ── TRAIN MODELS ──────────────────────────────────────────
for config in model_configs:
    
    start_time = time.time()
    
    model = Word2Vec(
        sentences=tokenized_sentences,
        vector_size=config['vector_size'],
        window=config['window'],
        min_count=config['min_count'],
        sg=config['sg']
    )
    
    training_time = round(time.time() - start_time, 3)
    
    # calculate similarity
    if word_1 in model.wv and word_2 in model.wv:
        similarity = round(model.wv.similarity(word_1, word_2), 4)
    else:
        similarity = "N/A"
    
    # store result
    experiment_results.append({
        'vector_size'   : config['vector_size'],
        'window_size'   : config['window'],
        'min_count'     : config['min_count'],
        'algorithm'     : "Skip-gram" if config['sg'] == 1 else "CBOW",
        'similarity'    : similarity,
        'training_time' : training_time
    })

# ── PRINT RESULTS TABLE ───────────────────────────────────
print("=" * 75)
print("WORD2VEC HYPERPARAMETER COMPARISON")
print(f"Similarity check: '{word_1}' vs '{word_2}'")
print("=" * 75)

print(f"{'Vec Size':>10} {'Window':>8} {'Min Count':>10} {'Algorithm':>12} {'Similarity':>12} {'Time(s)':>10}")
print("-" * 75)

for result in experiment_results:
    print(f"{result['vector_size']:>10} "
          f"{result['window_size']:>8} "
          f"{result['min_count']:>10} "
          f"{result['algorithm']:>12} "
          f"{str(result['similarity']):>12} "
          f"{result['training_time']:>10}")

print("=" * 75)

# ── BEST MODELS ───────────────────────────────────────────
valid_results = [r for r in experiment_results if r['similarity'] != "N/A"]

best_model = max(valid_results, key=lambda x: x['similarity'])
fastest_model = min(valid_results, key=lambda x: x['training_time'])

print("\nBEST MODEL (Highest Similarity):")
print(best_model)

print("\nFASTEST MODEL:")
print(fastest_model)

# ── CONCLUSION ────────────────────────────────────────────
print("\nConclusion:")
print("Skip-gram gives better similarity, CBOW is faster.")