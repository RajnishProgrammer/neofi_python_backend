import requests


url = 'http://localhost:8000/notes/share/'

auth_token = 'e8563dc2f61bdd1087411dc10720f1828319b8b8' # sasuke's authentication

data = {
    'note_id': 2, # shared note id
    'users': ['hanu']
}

headers = {
    'Authorization': f'Token {auth_token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())

# lets again login with hanu and check the shared note.