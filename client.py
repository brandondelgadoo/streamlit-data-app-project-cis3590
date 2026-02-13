# How do we mke a request to our API?

import requests

URL = "http://127.0.0.1:6767/api/items"
response = requests.get(URL).json()

print(response)