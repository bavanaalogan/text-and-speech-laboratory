import requests
word = input("Enter a word: ")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
response = requests.get(url)
data = response.json()
count = 0
for meaning in data[0]['meanings']:
    for d in meaning['definitions']:
        print("-", d['definition'])
        count += 1
        if count == 3:
            break
    if count == 3:
        break