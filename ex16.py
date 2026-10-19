sum_three = lambda a,b,c : a + b + c
print(sum_three(1,3,5))



nums = [1,2,3,4]

new_nums = list(map(lambda x : x ** 3, nums))
print(new_nums)



names = ["Ali", "Mohammad", "Reza", "Sara"]
new_names = list(filter(lambda x : len(x) > 0,names))
print(new_names)


numbers = [1,2,3,4,5,6,7,8]
result = list(map(lambda x : x ** 2, filter(lambda x : x % 2 != 0,numbers)))
print(result)
