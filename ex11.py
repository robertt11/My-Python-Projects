try:
   number = int(input("Enter your number"))
   add_number = int(input("Enter your second number"))
   result= number / add_number 
   print("Result : ",result)

except ValueError:
   print(" Please enter digits only")
except ZeroDivisionError:
   print("0 Zero is not allowed")



while True:
    try:
       age = int(input("Enter your age"))
       break
    except ValueError:
       print("Enetr your age correctly")
print("Your age is : ",age)



try:
    with open("test_data.txt","r")as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found ")



def safe_divide(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division is not possible"

print(safe_divide(10,2))
print(safe_divide(5,0))

