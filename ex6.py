student = {"name" : "roozbeh","score":19}
if student["score"] >= 18:
    print("Passed")
else:
    print("Failed")



inventory = {"apple": 5, "banana": 2, "orange": 10, "kiwi": 0}
for fruit, count in inventory.items():
    if count > 0:
       print(f"{fruit} : Availble")
    else:
       print(f"{fruit} Not Availble")



scores = [12,13,14,15,16]
result = {}
total = 0
for i in scores:
    total += i
avg = total / len(scores)
result["Average"] = avg
print(result)



phonebook = { "ali" : "0912","sara" : "0917"}
while True:
    name = input("Enter Name or 'exit' To quit")

    if name == "exit":
       break
    if name in phonebook:
       print(f"Phone Number : {phonebook[name]}")
    else:
       print("Not Availble")


