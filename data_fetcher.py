import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.api-ninjas.com/v1/animals'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    url = f"{BASE_URL}?name={animal_name}"
    headers = {
        'X-Api-Key': API_KEY,
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if not data:
                return []
            return data
        except requests.exceptions.JSONDecodeError:
            return None
    else:
        return None