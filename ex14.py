class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name} and Age : {self.age}")


class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def show_salary(self):
        print(f"Salary : {self.salary}")


emp1 = Employee("Roozbeh",34,5000)
emp1.show_info()
emp1.show_salary()



class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * ( self.radius ** 2)

shapes = [
    Rectangle(10, 5),
    Circle(4)
]

for shape in shapes:
    print (f" Area : {shape.area()}")

