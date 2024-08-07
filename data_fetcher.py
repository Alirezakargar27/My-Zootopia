import requests

API_KEY = '8REHXrpS0bS+aJxyG9BlPQ==ddtNcRZXuVqHHxvk'
BASE_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    url = f"{BASE_URL}?name={animal_name}"
    headers = {
        'X-Api-Key': API_KEY,
    }
    response = requests.get(url, headers=headers)

    # Print the response content for debugging
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not in JSON format")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None
