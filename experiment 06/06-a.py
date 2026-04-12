import nltk, torch
from nltk.corpus import twitter_samples
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

nltk.download('twitter_samples')

# ── LOAD DATA ──
pos = twitter_samples.strings('positive_tweets.json')
neg = twitter_samples.strings('negative_tweets.json')

texts = pos[:500] + neg[:500]   # small subset for speed
labels = torch.tensor([1]*500 + [0]*500)

# ── SPLIT ──
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2)

# ── TOKENIZER ──
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

def run(batch_size, epochs, max_len, name):

    train_enc = tokenizer(X_train, padding=True, truncation=True, max_length=max_len, return_tensors='pt')
    test_enc  = tokenizer(X_test,  padding=True, truncation=True, max_length=max_len, return_tensors='pt')

    model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
    opt = torch.optim.AdamW(model.parameters(), lr=3e-5)

    # ── TRAIN ──
    model.train()
    for e in range(epochs):
        loss_total = 0
        for i in range(0, len(X_train), batch_size):
            batch = {k: v[i:i+batch_size] for k, v in train_enc.items()}
            y = y_train[i:i+batch_size]

            opt.zero_grad()
            out = model(**batch, labels=y)
            out.loss.backward()
            opt.step()

            loss_total += out.loss.item()

        print(f"{name} Epoch {e+1} Loss:", round(loss_total,3))

    # ── TEST ──
    model.eval()
    with torch.no_grad():
        out = model(**test_enc)
        preds = torch.argmax(out.logits, dim=1)

    print(f"\n{name} Report:")
    print(classification_report(y_test, preds))
    print("="*40)


# ── CONFIGS ──
run(2, 2, 32, "Config 1")
run(4, 4, 64, "Config 2")