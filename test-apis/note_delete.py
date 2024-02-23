import requests

url = 'http://localhost:8000/notes/3/delete/'
auth_token = '83d84a7fc735d94410d3ae68a52bbe115f65adef'

headers = {
    'Authorization': f'Token {auth_token}'
}

response = requests.delete(url, headers=headers)

print("Status code:", response.status_code)
print("Message: ", response.json().get('message'))
