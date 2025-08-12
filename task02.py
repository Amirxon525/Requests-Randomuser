import requests
import json

r = requests.get("https://randomuser.me/api/?results=10").json()
d = []

for i in r["results"]:
    d.append({
        "name": i["name"]["first"] + " " + i["name"]["last"],
        "email": i["email"],
        "image_url": i["picture"]["large"]
    })

with open("users_with_images.json", "w") as f:
    json.dump(d, f)
