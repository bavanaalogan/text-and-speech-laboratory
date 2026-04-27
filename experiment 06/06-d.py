from transformers import pipeline

pipe = pipeline("sentiment-analysis")

tweets = [
    "I love this product!",
    "Worst experience ever",
    "It's okay",
    "Amazing service",
    "I hate it"
]

for t in tweets:
    print(t, "->", pipe(t)[0]["label"])
