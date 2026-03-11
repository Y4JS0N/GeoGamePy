import requests
import json
import random


url = "https://api.jonas-jud.com/api/countrydomain"

def apiCall():

    try:
        response = requests.get(url)
        data = response.json()
        return random.choice(data)
    except json.JSONDecodeError as e:
        print(f"Still failing locally: {e}")


def ask():

    while True:

        country = apiCall()
        name = country["name"]
        domain = country["domain"]

        print(f"What is the ccTLD for {name}? ")
        userGuess = input("Enter it like .ch:  ")
        print(userGuess)

        if userGuess in ["help", "quit", "score"]:

            return userGuess
        
        elif userGuess == domain:

            answer = True
            
            return answer, name, domain
        elif userGuess != domain:
            
            answer = False

            return answer, name, domain
        else:
            break

