import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('API_KEY')
process = True
header = {'X-Api-Key': apiKey}

if not apiKey:
    print("API key not found. Please set the API_KEY environment variable.")
    exit(1)


while process:
    word = input("inputWord:")
    print("\n") #blankspace

    thesaurusUrl = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    dictionaryUrl = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response1 = requests.get(thesaurusUrl, headers=header)
    response2 = requests.get(dictionaryUrl, headers=header)
    
    if response1.status_code == requests.codes.ok and response2.status_code == requests.codes.ok:
        data1 = response1.json()
        data2 = response2.json()

        definition = data2[0]['meanings'][0]['definitions'][0]['definition'] # definition example
        synonyms = data1.get('synonyms', [])
        antonyms = data1.get('antonyms', [])

        if not definition:
            print("definition:\n", "no definition found")
            continue #unsure?
        else:
            print("definition:\n", definition)
        print("\n")
        if not synonyms:
            print("synonyms:\n", "no synonyms found")
        else:
            print("synonyms:\n", synonyms) 
        print("\n")
        if not antonyms:
            print("antonyms:\n", "no antonyms found")   
        else:
            print("antonyms:\n", antonyms)
        print("\n")
    else:
        print("error:", response1.status_code, response1.text, "\nplease enter a valid english word\n")
    
    # end or continue
    contiue = input("anotherWord? (y/n) ")
    print("\n")
    if contiue.lower() == 'n':
        process = False
    elif contiue.lower() == 'y':
        process = True