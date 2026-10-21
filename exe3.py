import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

while True:
    print("\n1. Generate | 2. Exit")
    choice = input("Choose: ")
    
    if choice == "2":
        print("Goodbye!")
        break
        
    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Error: Please enter bigger length")
                continue
            print(f"Your password: {generate_password(length)}")
        except ValueError:
            print("Please enter valid value")
    else:
        print("Invalid value")
