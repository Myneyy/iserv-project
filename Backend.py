import json

def Save(User, Password):
  data = {
    "User": User,
    "Password": Password
  }
  with open(str(User) + ".json", "w") as f:
    json.dump(data, f)


def Load(User):
  with open(User + ".json", "r") as f:
    return json.load(f)
