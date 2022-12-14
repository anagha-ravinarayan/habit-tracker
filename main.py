import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    # POST
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_pixel_data():
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now()

    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many kilometers did you cycle today? "),
    }

    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def update_todays_pixel_data():
    today = datetime.now()
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    new_pixel_data = {
        "quantity": "4.5"
    }

    # PUT
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)


def delete_todays_pixel_data():
    today = datetime.now()
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    # DELETE
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)
