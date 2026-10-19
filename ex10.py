with open("wite.txt","w")as file:
    file.write("im learning python")
with open("wite.txt","r")as file:
    content = file.read()
    print(content)

#read khoroji set mide k taghiiresh sakhte
#load khoroji dictionery mide 


import json

book = {"title": "Python 101", "author": "Ali", "pages": 200}

with open("book.json","w") as file:
    json.dump(book,file)
print("Saved")

with open("book.json","r") as file:
    content = json.load(file)
content["year"] = 2024

with open("book.json","w")as file:
    json.dump(content,file)
print(content)



users = [
    {"name": "Roozbeh", "age": 34},
    {"name": "Sara", "age": 25},
    {"name": "Ali", "age": 28}
]

with open ("users.json","w") as file:
    json.dunp(users,file)

with open ("users.json","r")as file:
    content = json.load(file)
for i in content:
    print(" User name : " ,i["name"])

