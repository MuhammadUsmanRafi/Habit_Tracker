from datetime import datetime

import requests

# Constants
# name = input("Enter Your username for the first")
name = input("write a user_name")
USERNAME = name
TOKEN_KEY = "gsdkdndndsfkdnksdfnsdfkdsn"
GRAPH_ID = "graph1"
DATE = datetime.now()
TODAY = DATE.strftime("%Y%m%d")

# Endpoints
USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
UPDATE_DELETE_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime('%Y%m%d')}"

# Headers
GRAPH_HEADER = {
    "X-USER-TOKEN": TOKEN_KEY
}


# Functions
def create_user():
    user_parameter = {
        "token": TOKEN_KEY,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=USER_ENDPOINT, json=user_parameter)
    return response.text


def create_graph():
    graph_parameter = {
        "id": GRAPH_ID,
        "name": "Coding hours",
        "unit": "hours",
        "type": "float",
        "color": "ajisai",
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameter, headers=GRAPH_HEADER)
    return response.text


def update_pixel():
    quantity = input("Enter how many hours did you coding today?")  # Replace with the actual quantity
    pixel_update_parameter = {
        "quantity": quantity,
        "optionalData": TODAY,  # Optional date
    }
    response = requests.put(url=UPDATE_DELETE_ENDPOINT, json=pixel_update_parameter, headers=GRAPH_HEADER)
    return response.text


def delete_pixel():
    response = requests.delete(url=UPDATE_DELETE_ENDPOINT, headers=GRAPH_HEADER)
    return response.text


# Main
if __name__ == "__main__":
    # Uncomment to create a new user
    # print(create_user())

    # Uncomment to create a new graph
    # print(create_graph())

    # Uncomment to update a pixel
    print(update_pixel())

    # Uncomment to delete a pixel
    # print(delete_pixel())
