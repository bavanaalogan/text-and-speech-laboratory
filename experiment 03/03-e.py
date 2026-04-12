import nltk, re
from nltk.corpus import twitter_samples, movie_reviews, stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('twitter_samples')
nltk.download('movie_reviews')

english_stop_words = set(stopwords.words('english'))

# function to get top words
def top_words(raw_text):
    cleaned_text  = re.sub(r'[^a-zA-Z ]', ' ', raw_text).lower()
    word_tokens   = word_tokenize(cleaned_text)
    filtered_words = [word for word in word_tokens if word not in english_stop_words]
    return Counter(filtered_words).most_common(10)

# use strings() for twitter
twitter_text = ' '.join(twitter_samples.strings()[:5000])
imdb_text    = ' '.join(movie_reviews.words()[:5000])

twitter_top_words = top_words(twitter_text)
imdb_top_words    = top_words(imdb_text)

# plot
twitter_words, twitter_counts = zip(*twitter_top_words)
imdb_words,    imdb_counts    = zip(*imdb_top_words)

plt.subplot(1, 2, 1)
plt.bar(twitter_words, twitter_counts)
plt.xticks(rotation=45)
plt.title("Twitter")

plt.subplot(1, 2, 2)
plt.bar(imdb_words, imdb_counts)
plt.xticks(rotation=45)
plt.title("IMDB")

plt.tight_layout()
plt.show()