import requests
import json

def getQuotes():
    category = 'happiness'
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    api_key ="As3XyZ3Xl3IEUqpyUHpa6A==phjO5S4DqLxtFeqk"
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        data = response.json()
        quote = data[0]["quote"]
        author = data[0]["author"]
        content = f"{quote}\n\n{author}"
        print(content)
        return content
    else:
        print("Error:", response.status_code, response.text)
#getQuotes()