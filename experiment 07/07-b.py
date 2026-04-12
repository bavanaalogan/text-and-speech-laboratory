import requests
word = input("Enter a word: ")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
response = requests.get(url)
data = response.json()
synonyms = []
if isinstance(data, list):
    for meaning in data[0]["meanings"]:
        for s in meaning.get("synonyms", []):
            synonyms.append(s)
        for d in meaning["definitions"]:
            for s in d.get("synonyms", []):
                synonyms.append(s)
    if len(synonyms) >= 2:
        print("Synonyms:")
        print(synonyms[0])
        print(synonyms[1])
    else:
        print("No synonyms found.")
else:
    print("No synonyms found.")