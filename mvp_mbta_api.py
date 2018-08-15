import requests
import json



URL = "https://api-v3.mbta.com/"
headers = {"api-key" : "api_key"}

VEHICLES = "vehicles/" # "{*}/data/attributes/current_status"

r = requests.get(URL+VEHICLES, headers=headers)
r_load = r.json()
print(r_load)
