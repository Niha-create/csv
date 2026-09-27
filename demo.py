

# a=int(input("enter your number 1:"));
# b=int(input("enter your number 2:"));
# print("your sum is:",a+b)

# i=0
# while i<10:
#     print(i) 
#     i+=1;


# voterid=True
# age=18
# if age>=18:
#     if voterid:
#       print("your are eligiblen for vote")
# else:
#     print("voter id not availablity")    


# day=1
# match day:
#    case 1:
#       print("monday")
#    case 2:
#       print("tuesday")
#    case 3:
#       print("wednesday")
#    case _:
#       print("invalid choice")
# i=0    
# for i in range(10,0,-1):
#    if i ==5:
#       break
#    if i==7:
#       continue
      
#    print(i)

# list

fruits=["apple","mango","blueberry"]
fruits.append("orange")
fruits.pop(2)
fruits.insert(0,"pineapple")
print(fruits.count("mango"))
fruits.reverse()
print(fruits[0])
print(fruits)
print(type(fruits))

# tuple

course=("java","python","marn")
print(course)
print(type(course))

# dictionary

college={
    "name":"fathima",
    "reg":2011545,
    "department":"Bca"
}
print(college["name"])
print(college["reg"])
print(college["department"])
print(college)
print(type(college))

rows=10
for i in range(1,rows+1):
    for j in range(i):
      print("*",end="")
    print()


a={10,50,45,30}
b={50,80,70,30}
print(a|b)
print(a&b)
print(a^b)
print(a-b)
print(b-a)


