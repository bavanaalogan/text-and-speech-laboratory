import re
from collections import Counter

text = """
Natural Language Processing is a branch of Artificial Intelligence.
natural Language Processing helps machines understand human language.
Language processing is widely used in speech and text analysis applications.
"""

word_tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())
freq_dist = Counter(word_tokens)

print("TOKENS:", word_tokens)
print("TOP 10 MOST FREQUENT WORDS:",freq_dist.most_common(10))
