name = input("enter your name").strip().capitalize()
print(name)


word = input("enter your word").split()
print(len(word))



words = input("enter your word").replace("bad","***")
print(words)


number = input("Write Your Number")
if number.isdigit():
    print("its Digit")
else:
    print("its not digit")

"""# print("its digit" if number.itsdigit() else: "its not digit")"""



user_profile = {}
name = input("enter your name").strip().title()
age = input("enter your age")

user_profile[name] = age
print(user_profile)


