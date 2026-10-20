def add(a,b):
    return a + b

def subtrackt(a,b):
    return a - b

def multiply(a,b):

    return a * b

def divide(a,b):
    if b == 0:
        return "Erorr : Divisio by zero"
    return a / b

while True:
    print("\n---Calculator---")
    print("1. add (+)")
    print("2. subtrackt (-)")
    print("3. multiply (*)")
    print("4. divide (/)")
    print("5. Exit")

    choice = input("Choice an option (1-5)")
    if choice == "5":
        print("GoodBye !")
        break

    if choice in ["1","2","3","4"]:
        try:
            num1 = float(input("Enter first number"))
            num2 = float(input("Enter second number"))
            if choice == "1":
                print("Result :",add(num1,num2))
            elif choice == "2":
                print("Result :",subtrackt(num1,num2))
            elif choice == "3":
                print("Result :",multiply(num1,num2))
            elif choice == "4":
                print("Result :",divide(num1,num2))
        except ValueError:
            print("Invalid input !Enter number")




#niazi b class nist vaghti moteghayrr motefavet nadarim va vorodi nfarim

