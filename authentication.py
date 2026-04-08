import hashlib
import json

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        
# put json into list of users
with open('database.json', "r") as file:
    data = json.load(file)
    users = [User(**item) for item in data]

# getattr(data, category, failure action)

for user in users:
    text = getattr(user, "password", "Not Found")
    print(text)
    
    # utf-8 is standard for encoding, requried to encode string for hash to work
    hashes = hashlib.sha256(text.encode('utf-8'))

    print(hashes.hexdigest())