import requests

BASE = "http://127.0.0.1:5000/"
# response = requests.put(BASE + "videos/2", {"name": "bahubali2 movie", "views":100000, "likes": 250})
response = requests.get(BASE + "videos/6")
print(response.json())