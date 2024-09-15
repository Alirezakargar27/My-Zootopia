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

    # Log the URL being used for debugging purposes
    print(f"Fetching data from URL: {url}")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")

    if response.status_code == 200:
        try:
            data = response.json()
            if not data:  # Check if the response is an empty list
                print(f"No data found for animal: {animal_name}")
                return []
            return data
        except requests.exceptions.JSONDecodeError:
            print(f"Error: Could not parse response as JSON for {animal_name}")
            return None
    else:
        print(f"Error: Received status code {response.status_code}")
        return None