list = ["a","b","c","d","e"]
print(list[0])
print(list[-1])
print(len(list))


x = []
x.append("a")
x.append("b")
x.append("c")
x.insert(1,"d")
x.remove("c")
print(x)

numbers = [12,13,15,17]
sum = 0
for number in numbers:
    sum += number
print(sum)

y = [ 15,18,19,265,1000]
print(max(y))

name =[ "ali","mohamad","sina","asghar","mehdi"]
ask = input("Write your name")
if ask in name:
    print("Correct")
else:
    print("In Correct")

numeric =[13,145,1098,-1,50]
numeric.sort()
print(numeric)
numeric.sort(reverse=True)
print(numeric)


avg = [ 10,20 ,34 ,46]
sum = 0
for i in avg:
    sum += i 
print(sum/len(avg))

