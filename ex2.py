a = int(input("How Old Are You?"))

if a >= 18 :
   print("You Can Drive")
else :
   print("You Are Under Age")



user_number = int(input("Put Your Number"))

if user_number >= 50 :
   print("Passed")
else:
   print("Failed")


age = int(input("Put Your Age"))

if age < 13:
   print("Child")
elif age < 20:
   print("Young")
elif age < 60:
   print("Mature")
else:
   print("Old")

number = int(input("Number"))

if number % 2 == 0:
   print("Even")
else:
   print("Odd")

user_name = input("Enter Username")
password = input("Enter Password")
if user_name == "Admin" and password == "1234":
   print("Wellcom")
else:
   print("Wrong Data")

