for i in range(1,11):
   print(i)


for i in range(2,21,2):
   print(i)


total = 0
for i in range(1,101):
   total = total + i
print(total)


number = int(input("Please Put Your Number"))
for i in range(1,11):
   result = number * i
   print(f"{number} * {i} = {result}")


i = 10
while i >= 1:
    print(i)
    i = i - 1
print("End")


password = input("Enter Your Password")
while password != "1234":
    password = input("Wrong ! Enter Password")
print("Access Granted")


secret = 5
guess = int(input("Guess The Number"))
while guess != secret:
    if guess > secret:
        print("Too High ! Get Lower")
    else:
        print("Too Low! Get Higher")
    guess = int(input("Guess Again !"))
print(" Well Done")
