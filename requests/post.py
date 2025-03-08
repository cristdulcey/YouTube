import requests

datos = {'titulo': 'Mi primer post', 'body': 'Hola Mundo!'}
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    data=datos
)
print(response.status_code)  # 201 created
