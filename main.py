from datetime import datetime

import requests

# Constants
name = input("Enter Your username for the first")
USERNAME = name
TOKEN_KEY = "gsdkdndndsfkdnksdfnsdfkdsn"
GRAPH_ID = "graph1"
DATE = datetime.now()
TODAY = DATE.strftime("%Y%m%d")

# Endpoints
USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
GRAPH_DEF_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs/graph1/graph-def"

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
        "name": "Coding graph",
        "unit": "hours",
        "type": "float",
        "color": "sora",
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameter, headers=GRAPH_HEADER)
    return response.text


def create_pixel():
    quantity = input("How many hours did you code today? ")
    pixel_creation_parameter = {
        "date": datetime.now().strftime("%Y%m%d"),
        "quantity": quantity,
    }
    response = requests.post(url=GRAPH_ENDPOINT, json=pixel_creation_parameter, headers=GRAPH_HEADER)
    return response.text


def update_pixel():
    quantity = "45.78"  # Replace with the actual quantity
    pixel_update_parameter = {
        "quantity": quantity,
        "optionalData": TODAY,  # Optional date
    }
    response = requests.put(url=f"{GRAPH_ENDPOINT}/{datetime.now().strftime('%Y%m%d')}", json=pixel_update_parameter,
                            headers=GRAPH_HEADER)
    return response.text


def delete_pixel():
    response = requests.delete(url=f"{GRAPH_ENDPOINT}/{datetime.now().strftime('%Y%m%d')}", headers=GRAPH_HEADER)
    return response.text


# Main
if __name__ == "__main__":
    # Uncomment to create a new user
    # print(create_user())

    # Uncomment to create a new graph
    # print(create_graph())

    # Uncomment to create a new pixel
    # print(create_pixel())

    # Uncomment to update a pixel
    print(update_pixel())

    # Uncomment to delete a pixel
    # print(delete_pixel())
