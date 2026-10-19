def show_message():
    print("im learning functions")

show_message()


def add_numbers(a,b):
    print (a +b)

add_numbers(20,3)



def multiplay(a,b):
    return (a * b)

print(multiplay(2,4))


def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average= total / len(numbers)
    return average

my_numbers = [ 12,13,15,18]
print(calculate_average(my_numners))

# def calculate_average(numbers):
    #return sum(numbers) / len(numbers)


def check_password(password):
    return len(password) >= 8 and not password.isdigit()

user_word = input("Enter your password :")
if check_password(user_word):
    print("Password is strong")
else:
    print("Password is weak")





