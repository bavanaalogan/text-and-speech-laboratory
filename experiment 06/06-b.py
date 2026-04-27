learning_rates = [5e-5, 3e-5]

for lr in learning_rates:
    print("\nLearning Rate:", lr)

    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")

    args = TrainingArguments(
        output_dir="./lr",
        learning_rate=lr,
        num_train_epochs=1,
        per_device_train_batch_size=16
    )

    trainer = Trainer(model=model, args=args, train_dataset=train1)
    trainer.train()

    pred = trainer.predict(test1)
    acc = accuracy_score(pred.label_ids, np.argmax(pred.predictions, axis=1))
    print("Accuracy:", acc)
