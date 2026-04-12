import nltk, torch
from nltk.corpus import twitter_samples
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

nltk.download('twitter_samples')

# ── LOAD BUILT-IN DATA ──
pos = twitter_samples.strings('positive_tweets.json')
neg = twitter_samples.strings('negative_tweets.json')

texts = pos[:500] + neg[:500]   # small subset for speed
labels = torch.tensor([1]*500 + [0]*500)

# tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
inputs = tokenizer(texts, padding=True, truncation=True, max_length=64, return_tensors='pt')

# learning rates
learning_rates = [5e-5, 3e-5, 1e-5]

for lr in learning_rates:
    print(f"\nTraining with LR = {lr}")

    model = DistilBertForSequenceClassification.from_pretrained(
        'distilbert-base-uncased', num_labels=2
    )
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    # ── TRAIN ──
    model.train()
    for epoch in range(2):
        optimizer.zero_grad()
        out = model(**inputs, labels=labels)
        loss = out.loss
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch+1} Loss:", round(loss.item(),4))

    # ── TEST ──
    model.eval()
    with torch.no_grad():
        out = model(**inputs)
        preds = torch.argmax(out.logits, dim=1)

    acc = (preds == labels).sum().item() / len(labels)
    print(f"Accuracy: {acc*100:.2f}%")
    print("="*40)