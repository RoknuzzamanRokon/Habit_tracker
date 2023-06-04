import requests

TOKEN = "abcdefg43klm4l"
USER_NAME = "rokon"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

pixela_response = requests.post(url=pixela_endpoint, json=user_params)


grap_endpoint = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

grap_params = {
    "id": "roko01",
    "name": "Using pycharm",
    "unit": "HH",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN}

grap_response = requests.post(url=grap_endpoint, json=grap_params, headers=headers)

print(pixela_response.text)
print(grap_response.text)

