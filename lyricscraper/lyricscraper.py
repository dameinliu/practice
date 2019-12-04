import requests

response = requests.get('https://music.163.com/#/artist/album?id=12046230')
print(response.status_code)