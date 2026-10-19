cubes = [x**3 for x in range(1,11)]
print(cubes)


words = ["python", "is", "fun", "and", "powerful"]

long_words = [w for w in words if len(w) > 3]
print(long_words)


nums = [-5, 3, -1, 8, 0, -2, 4]

posotive = [n for n in nums if n > 0]
print(posotive)


name = input("Enter your name")

upper_letters = [char.upper() for char in name]
print(upper_letters)



users = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 15},
    {"name": "Reza", "age": 25}
]

adult_name = [user["name"] for user in users if user["age"] >= 18]
print(adult_name)

