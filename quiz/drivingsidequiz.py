import requests
import json
import random


url = "https://api.jonas-jud.com/api/drivingside"

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
        side = country["side"]

        print(f"Do you drive Left or Right in {name}? ")
        userGuess = input("Enter left or right:  ").lower()

        if userGuess in ["help", "quit", "score"]:

            return userGuess
        
        elif userGuess == side:

            answer = True
            
            return answer, name, side

        elif userGuess != side:
            
            answer = False

            return answer, name, side
        else:
            break
