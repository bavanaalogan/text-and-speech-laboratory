import random
words = ["happy","science","computer","nature","music","energy","river","future","planet","language"]
user = input("Type 'suggest' to get a random word: ")
if user == "suggest":
    w = random.choice(words)
    print("Suggested word:", w)