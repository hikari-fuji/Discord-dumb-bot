import requests
#from googletrans import Translator - uncomment for translate

def get_joke(blacklist_genres):
    # Make a request to the Random Jokes API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()

    # Check if the joke genre is in the blacklist
    while data['type'] in blacklist_genres:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()

    # Translate the joke to Vietnamese
    # translator = Translator()
    # setup = translator.translate(setup, dest='vi').text
    # punchline = translator.translate(punchline, dest='vi').text
        
    # Extract the setup and punchline from the API response
    setup = data["setup"]
    punchline = data["punchline"]
    return setup, punchline