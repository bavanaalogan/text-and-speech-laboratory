import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import twitter_samples

nltk.download('punkt')
nltk.download('twitter_samples')

# use strings() instead of words()
text = ' '.join(twitter_samples.strings()[:5000])

# clean text
text = re.sub(r'[^a-zA-Z ]', ' ', text)   # remove symbols & numbers
text = re.sub(r' +', ' ', text).lower()   # remove extra spaces

# tokenize
tokens = word_tokenize(text)

print("Cleaned Text:", text[:100])
print("Tokens:", tokens[:10])