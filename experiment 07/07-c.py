history = []
while True:
    word = input("Enter a word (type history / exit): ")
    if word == "exit":
        break
    if word == "history":
        print("Search History:")
        for w in history:
            print(w)
        continue
    history.append(word)
    print("Word stored.")