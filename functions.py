# definition 
# def Sum(a,b):   #function declaration
#     return (a+b)  #function body
# #function calling 
# #Sum(5,16)
# x = int(input("Enter the first number:"))
# y = int(input("Enter the second number:"))
# #function calling
# result = Sum(x,y)
# print("Sum :",result)
# z = -5
# print(abs(z))
# print(list(range(1,6)))
# print(zip(range(1,6)))

'''Grading System'''
# def Student_info(name,sem,grade):
#     print(f'{name} | Semester: {sem} | Grade : {grade}')

# Student_info('Bob',2,'A')
# Student_info(grade ="B",sem =3,name="Alice")
# def Power(base,exp=2):
#     return base ** exp

# print(Power(3))

# '''*args all Arguments-  Variable Positional Arguments'''
# def Total(*numbers):
#     print(type(numbers))
#     return sum(numbers)
# print(Total(12,13))
# print(Total(14,15,56,25))

#global Keyword
# counter=0
# def increment():
#     global counter
#     counter +=1

# # function call
# increment()
# increment()
# print(counter)
#non-local
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count+=1
#         print('inner count',count)
#     inner()
#     inner()
#     print("outer count:",count)
# outer()

#LAMBDA
#Regular function nameless function

# def square(x):
#     return(x*x)

#lambda Function 
# square = lambda x:x*x
# add = lambda a,b : a+b
# #Regular function call

# print(square(5))
# print(add(10,20))

# students = [
#     {'name':'Bob','marks':85},
#     {'name':'Alice','marks':95},
#     {'name':'John','marks':92}
# ]

# # Sorting using lambda
# ranked = sorted(students,key=lambda student:student["marks"])
# for student in ranked:
    # print(student["name"],student["marks"])

#mapping & filter
# num = [1,2,3,4,5]

# squares = list(map(lambda x: x**2,num))
# doubles = list (map(lambda x: x*2,num))
# mystr = list (map(lambda x: str(x),num))

# even = list(filter(lambda x : x%2 == 0,num))
# odd = list(filter(lambda x: x%2!=0,num))
# smallest = list(filter(lambda x:x<5,num))

# print(squares)
# print(doubles)
# print(mystr)
# print(even)
# print(odd)
# print(smallest)

# factorial  5 ! = 5 x 4 x3 x2 x1 = 120
# def Factorial(num):
#     if num == 0 or num==1:
#         return 1
#     return num * Factorial(num-1)
# print(Factorial(5))
# print(Factorial(0))

# def Sum_Digit(n):
#     if n<10:
#         return n
#     return n%10 +Sum_Digit(n//10)

# print(Sum_Digit(12345))

#Binary Search a list is devided into two parts 
def bin_srch(arr,key,lb,ub):
    if lb>ub:
        return -1
    mid = (lb+ub)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] <key:
        return bin_srch(arr,key,mid+1,ub)
    else:
        return bin_srch(arr,key,lb,mid-1)
arr =[2,5,8,12,16,23,38,56]
print(bin_srch(arr,23,0,len(arr)-1))