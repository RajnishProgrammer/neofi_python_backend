import requests


url = 'http://localhost:8000/notes/update/3/'

auth_token = '83d84a7fc735d94410d3ae68a52bbe115f65adef'

updated_content = 'Arigato !!!.'

data = {
    'content': updated_content
}

headers = {
    'Authorization': f'Token {auth_token}',
    'Content-Type': 'application/json'
}

response = requests.put(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())