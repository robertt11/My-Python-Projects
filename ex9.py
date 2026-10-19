def sum_numbers(args):
    return sum(args)

print(sum_numbers(40,50,70))
print(sum_numbers(2,5,6,7))

#def sum_numbers(*aegs):
#    total = 0
#    for i in args:
#    total += i
#    return total


def create_profile(**kwargs):
    for key,value in kwargs.items():
    print(f"{key} : {value}")

create_profile(name="Roozbeh",age=34,city="shiraz")



def calculator(operation,*args):
    if operation == "add":
       return sum(args)
    elif operation == "multiply":
       total = 1
       for i in args:
       total *= i
      return total
    else:
      return "incorect value"

print(calculator("add",20,3,4))
print(calculator("multiply",2,4))
print(calculator("ali",12,35))


app_name = "My_App"

def show_app():
    print(app_name)

show_app()

