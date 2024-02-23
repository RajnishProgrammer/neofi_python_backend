import requests

url = 'http://localhost:8000/signup/'
data = {
    'username': 'KingZach',
    'email': 'King@Zach.com',
    'password': 'King1234'
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())