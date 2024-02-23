# import requests

# url = 'http://localhost:8000/signup/'
# data = {
#     'username': 'naruto',
#     'email': 'naruto@hanu.com',
#     'password': 'naruto1234'
# }
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# import requests

# url = 'http://localhost:8000/login/'
# data = {
#     'username_or_email': 'hanu',
#     'password': 'hanu1234'
# }
# response = requests.post(url, json=data)

# print("Status code:", response.status_code)
# if response.status_code == 200:
#     print("Authentication token:", response.json()['token'])
# else:
#     print("Error message:", response.json()['error'])


# import requests

# # Set the URL of your API endpoint
# url = 'http://localhost:8000/notes/create/'

# # Set the authentication token of an authenticated user
# auth_token = 'e8563dc2f61bdd1087411dc10720f1828319b8b8'

# # Set the data for the note content
# data = {
#     "content": "mai sasuke hu....."
# }

# # Set the headers including the authentication token
# headers = {
#     'Authorization': f'Token {auth_token}',
#     'Content-Type': 'application/json'
# }

# # Send the POST request
# response = requests.post(url, json=data, headers=headers)

# # Print the response status code and content
# print("Status code:", response.status_code)
# print("Response:", response.json())