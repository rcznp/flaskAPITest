import requests

BASE = "http://127.0.0.1:8080/"

# Data to populate
videos = [
    {"likes": 10, "name": "Tim", "views": 10000},
    {"likes": 20, "name": "Tom", "views": 20000},
    {"likes": 30, "name": "Tina", "views": 30000}
]

# Populate the database
for i, video in enumerate(videos, start=1):
    response = requests.put(BASE + f"video/{i}", json=video)
    print(response.json())

#response = requests.get(BASE + "videos")
#response = requests.put(BASE + f"video/6", json={"likes": 6969, "name": "ryan", "views": 104950},)
#print(response.json())


