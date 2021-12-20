import requests

url = 'https://cataas.com/cat'
filename = 'cat.jpg'

r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)