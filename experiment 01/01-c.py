import re
from collections import Counter
text = "the cat sat on the mat the cat is on the mat"
word_tokens    = re.findall(r'\b[a-zA-Z]+\b', text.lower())
word_frequency = Counter(word_tokens)
print("Word Tokens:", word_tokens)
print("Word Frequency:", word_frequency.most_common())
