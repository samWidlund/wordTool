
import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('API_KEY')
if not apiKey:
    print("API key not found. Please set the API_KEY environment variable.")
    exit(1)

process = True

while process:
    word = input("inputWord: ")
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)

    response = requests.get(api_url, headers={'X-Api-Key': apiKey})
    if response.status_code == requests.codes.ok:
        data = response.json()
        

        synonyms = data.get('synonyms', [])
        antonyms = data.get('antonyms', [])

        print("word:\n", word)
        print("\n")
        print("synonyms:\n", synonyms)
        print("\n")
        print("antonyms:\n", antonyms)
        print("\n")
    else:
        print("Error:", response.status_code, response.text)
    
    contiue = input("anotherWord? (y/n) ")

    if contiue.lower() == 'n':
        process = False
    elif contiue.lower() == 'y':
        process = True