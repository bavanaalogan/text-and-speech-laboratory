import requests
word = input("Enter a word: ")
if not word.isalpha():
    print("Please enter a valid English word.")
else:
    try:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Word found:", data[0]['word'])
        else:
            print("Word not found.")
    except:
        print("Unable to connect to dictionary service. Please try again later.")