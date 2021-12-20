import requests
from msvcrt import getch

url = 'https://cataas.com/cat'
filename = 'cat.jpg'

r = requests.get(url)

with open(filename, 'wb') as f:
    f.write(r.content)
    
print("SUCESS!")

print("Press any key to exit...")
junk = getch()
