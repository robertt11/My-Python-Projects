class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} Says Woof!!!")

dog1 = Dog("R","AA")
dog2 = Dog("S","BB")

dog1.bark()
dog2.bark()



class Calculator:
    def add (self,a,b):
        return a + b
    def subtract (self,a,b):
        return a - b
    def multiply (self,a,b):
        return a * b

my_calc = Calculator()
print("sum",my_calc.add(10,5))
print("sub",my_calc.subtract(2,9))
print("mul",my_calc.multiply(3,8))

# az __init__ estfade nkardim chon
#sefat khas ya monhaseri ndare va  b
#hame khasiatash niaz darim

