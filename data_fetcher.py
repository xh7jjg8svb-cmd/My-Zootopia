import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API key not found. Please make sure .env contains API_KEY=your_key")
        return []

    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return []


# Optional test to check if loading works
if __name__ == "__main__":
    test_key = os.getenv("API_KEY")
    print("Loaded API Key:", "Found" if test_key else "Missing")
    print(fetch_data("Fox"))
