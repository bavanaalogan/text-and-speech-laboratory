import re
text = "Loving the #Python workshop today! #NLP and #TextAnalysis are so cool. Not a hashtag: #123, just text."
word_tokens    = re.findall(r'\b[a-zA-Z]+\b', text)
hashtag_tokens = re.findall(r'#[a-zA-Z]+\b', text)
print("Word Tokens:   ", word_tokens)
print("Hashtag Tokens:", hashtag_tokens)