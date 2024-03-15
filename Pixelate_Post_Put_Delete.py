import requests
from datetime import datetime

USERNAME = "yaseenj"
TOKEN = "hjk123hjk983123hjk"
GRAPH_ID = "graph1"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Miles",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Adding a Pixel to Habit Tracker

today = datetime.now()
day = datetime(year=2024, month=3, day=14)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}
response = requests.post(url=graph_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_params={
    "quantity": "3"
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)

delete_response = requests.delete(url=update_endpoint, headers = headers)
