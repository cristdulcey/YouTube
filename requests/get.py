import requests

response = requests.get('https://api.github.com/users/github')
data = response.json()
print('followers:', data['followers'])
