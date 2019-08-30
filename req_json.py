import requests
response = requests.get("https://geo-info.co/43.65,-79.40")
datajson = response.json()
print(datajson)
