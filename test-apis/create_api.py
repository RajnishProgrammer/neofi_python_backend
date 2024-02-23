import requests


url = 'http://localhost:8000/notes/create/'

auth_token = '83d84a7fc735d94410d3ae68a52bbe115f65adef'

data = {
    "content": "This is note created by naruto....."
}

headers = {
    'Authorization': f'Token {auth_token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())