import requests

# id=2
url = 'http://localhost:8000/notes/2/'

auth_token = '2171d4f3561e126b007a5d59f614822f0fd956c8'

headers = {
    'Authorization': f'Token {auth_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.json())

#lets share this note id = 1