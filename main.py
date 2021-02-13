import requests
from keys import TOKEN

from datetime import *

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "xsist14"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Quran Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = date.today()
today = today.strftime('%Y%m%d')

pixel_config = {
    "quantity": "10",
    "date": today
}


# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)
update_config = {
    "quantity": "0",
}
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"
# response = requests.put(update_endpoint, json=update_config, headers=headers)
# response.raise_for_status()
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"
response = requests.delete(delete_endpoint, headers=headers)
response.raise_for_status()
print(response.text)
