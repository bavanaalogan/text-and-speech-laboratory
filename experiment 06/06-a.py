from transformers import *
from datasets import load_dataset
from sklearn.metrics import accuracy_score
import numpy as np

# Small dataset
data = load_dataset("imdb")
train = data["train"].select(range(200))
test = data["test"].select(range(50))

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

def tokenize(x, max_len):
    return tokenizer(x["text"], padding="max_length", truncation=True, max_length=max_len)

# -------- CONFIG 1 --------
train1 = train.map(lambda x: tokenize(x, 128), batched=True)
test1 = test.map(lambda x: tokenize(x, 128), batched=True)

train1.set_format("torch", columns=["input_ids","attention_mask","label"])
test1.set_format("torch", columns=["input_ids","attention_mask","label"])

model1 = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")

args1 = TrainingArguments(output_dir="./c1", num_train_epochs=1, per_device_train_batch_size=16)

trainer1 = Trainer(model=model1, args=args1, train_dataset=train1)
trainer1.train()

pred1 = trainer1.predict(test1)
acc1 = accuracy_score(pred1.label_ids, np.argmax(pred1.predictions, axis=1))
print("Config1 Accuracy:", acc1)


# -------- CONFIG 2 --------
train2 = train.map(lambda x: tokenize(x, 64), batched=True)
test2 = test.map(lambda x: tokenize(x, 64), batched=True)

train2.set_format("torch", columns=["input_ids","attention_mask","label"])
test2.set_format("torch", columns=["input_ids","attention_mask","label"])

model2 = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")

args2 = TrainingArguments(output_dir="./c2", num_train_epochs=2, per_device_train_batch_size=32)

trainer2 = Trainer(model=model2, args=args2, train_dataset=train2)
trainer2.train()

pred2 = trainer2.predict(test2)
acc2 = accuracy_score(pred2.label_ids, np.argmax(pred2.predictions, axis=1))
print("Config2 Accuracy:", acc2)
