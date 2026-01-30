import requests

# Asteroid url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-10-07&end_date=2025-10-07&api_key="
# APOD url = "https://api.nasa.gov/planetary/apod?api_key="

def api_generator(url, unique_key):
    final_url = url + unique_key
    response = requests.get(final_url).json()
    return response