import requests

payload = {
    "name": "Prashant",
    "age": 22
}

res = requests.get('https://f8279845.ngrok.io/', params = payload)

print(res.headers)