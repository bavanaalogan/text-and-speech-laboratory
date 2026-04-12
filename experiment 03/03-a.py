import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, twitter_samples

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('twitter_samples')

# get text
text = ' '.join(twitter_samples.strings()[:5000]).lower()

# tokenize
words = word_tokenize(text)

# remove stopwords and non-words
stop_words = set(stopwords.words('english'))
cleaned = [w for w in words if w.isalpha() and w not in stop_words]

# output
print("Original:", words[:10])
print("Cleaned :", cleaned[:10])