import requests

url="http://192.168.99.100:8050/render.html?url=https://www.jd.com&width=1000&height=700"

response = requests.get(url)
print(response.text)
