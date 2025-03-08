import requests

session = requests.Session()
session.headers.update({'Authorization': 'Bearer YOUR_API_KEY'})
response = session.get('https://www.instagram.com/accounts/login/')
print(response.status_code)
