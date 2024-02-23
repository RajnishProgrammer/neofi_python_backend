import requests

url = 'http://localhost:8000/login/'

data = {
    'username_or_email': 'King@Zach.com',
    'password': 'L1234'
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

# got this sasuke_auth_token = '2171d4f3561e126b007a5d59f614822f0fd956c8'
# got this naruto_auth_token = '83d84a7fc735d94410d3ae68a52bbe115f65adef'
# got this KingZach_auth_token = '4747da05d4fe0aed767a96ffd1d6d4795067b5a7'
