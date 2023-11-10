# def sayHello():
#     print("hello...")
#
# sayHello()


# def funcwithparam(a):
#     return a**3
#
# #print(funcwithparam(6))
# output=funcwithparam(4)
# print(output)

#Lambda expression
# def doubleofme(value):
#     return value*2

#lambda function
#lambda arguments:expression

# output=lambda value: value*2
# print(output(2))             #returns 4

# def sayhello(name):
#     print("Your name is ",name)
#
# sayhello("hyma")
# sayhello("chaitra")

#Instead of above program we can reduce the programming lines by using lambda
# sayhellolambda=lambda name: print("your name is ",name)
# sayhellolambda("raj")
# sayhellolambda("udvita")

original_str="MADAM"
reverse_str=lambda original_string:original_str[::-1]
#print(reverse_str(original_str))
#
# if reverse_str("MADAM")==original_str:
#     print("polindrome")
# else:
#     print("Not a polindrome")
#
# sub=lambda x,y : print("substaration of x,y is :", x-y)
# print(sub(5,3))

#a lambda function that add two numbers
#add=lambda x,y:print("addition of two numbers",x+y)

add=lambda x,y:x+y
print("addition of two numbers",add(4,6))

#a lambda function that square a number
square=lambda x: x**2
print("square a number",square(5))

#a lambda function that checks if a number is even
even_number=lambda x:x%2==0
print("evening number is",even_number(10))        #evening number is True

#check even numbers in a list by using filter
numbers=[1,2,3,4,5,6,7,8,9,10,20]
even_numbers=list(filter(lambda num:num%2==0,numbers))
print(even_numbers)

#by using map
Numbers=[3,6,9,7,8,10]
_=list(map(lambda x:print(x)if x%2==0 else None,Numbers))
#print(EvenNumbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# _= list(map(lambda x: print(x) if x % 2 == 0 else None, numbers))

#by using for loop,inside lambda function
even_num=[1,3,5,6,48,9]
for num in even_num:
    if (lambda num:num%2==0)(num):
        print("even number",num)
    else:
        print("number is odd",num)
