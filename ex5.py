cities = ("shiraz","teh","esf","yazd","mshd")
print(cities[0])
print(cities[4])


data = ("Roozbeh",34,"Shiraz")
name,age,city = data
print(f"Name : {name} , Age : {age} , City : {city}")


my_list = [12,23,34,45,65]
my_tuple = tuple(my_list)
print(len(my_tuple))

new_list = [1,1,2,2,3,3,4,5,6]
my_set = set(new_list)
print(my_set)


a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


c = [1,2,3,4,5]
d = [4,5,6,7,8]
common = set(c) & set(d)
print(common)



