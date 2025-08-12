import requests
import json

a = requests.get("https://randomuser.me/api/")
b = a.json()

user = b['results'] [0]

user_p =  { "first_name": user['name']['first'],
    "last_name": user['name']['last'],
    "gender": user['gender'],
    "email": user['email'],
    "phone": user['phone'],
    "address": {
        "street": user['location']['street']['name'],
        "city": user['location']['city'],
        "country": user['location']['country']
    }
}

with open('user.json', 'w') as f:
    json.dump(user_p, f)
    