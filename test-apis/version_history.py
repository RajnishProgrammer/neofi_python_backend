import requests


url = 'http://localhost:8000/notes/version-history/3/'

auth_token = '83d84a7fc735d94410d3ae68a52bbe115f65adef'

headers = {
    'Authorization': f'Token {auth_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())