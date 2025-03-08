import requests

headers = {
    'Authorization': 'Bearer YOUR_API_KEY'
}

response = requests.get(
    'https://api.github.com/users/github',
    headers=headers
)
data = response.json()
