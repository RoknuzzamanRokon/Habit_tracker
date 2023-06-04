import requests

TOKEN = "abcdefg"
USER_NAME = "Rokon"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

pixela_response = requests.post(url=pixela_endpoint, params=user_params)


grap_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

grap_params = {
    "id": "roko01",
    "name": "Using pycharm",
    "unit": "HH",
    "type": "float",
    "color": "kuro"
}


grap_response = requests.post(url=grap_endpoint, params=grap_params)

