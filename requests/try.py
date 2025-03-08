import requests

try:
    response = requests.get('https://api.github.com/users/github')
    response.raise_for_status()
    data = response.json()
    print('followers:', data['followers'])
except Exception as error:
    print('Error:', error)
