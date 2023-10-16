# n=int(input("ENter number\n"))
# print(f'table of {n} is :')
#
# print(f"2X1={n*1}")
# print(f'2X1={n*2}')
#
# #or
# print(f'{n}X3={n*3}')
# print(f'{n}X4={n*4}')
#
# #or
# print('2X5={}'.format(n*5))
# #By using % operator
# print('2X1=%s' %2*1)
#
# name="hyma"
# age=26
# print(f'My name is {name} and  i am {age} years old')
# print('My name is {} and iam {} years old' .format(name,age))
# #print("My name is %s and ia m %s years old" %%nameage)

#prime number
# num=int(input("Entyer number:\n"))
# for i in range(2,num):
#     if num % i==0:
#         print(num, "is not prime")
#         break
# else:
#     print(num, "is prime")

# first_number=int(input("Enter number1:\n"))
# last_number=int(input("Enter last number:\n"))
# for num in range(first_number,last_number+1):
#     if num>1:
#         for i in range(2,num):
#             if num % i ==0:
#                 print(num,"is not a prime")
#                 break
#     else:
#         print(num,"is prime")

#fabinacci number:
# num=int(input("Enter number:\n"))
# a=0
# b=1
# if num<=0:
#     print('Enter positive number\n')
# else:
#     print(a,b,end=' ')
#     for i in range(2,num+1):
#         c=a+b
#         print(c,end=' ')
#         a,b=b,c
#
# num=int(input("\nEnter number:\n"))
# a=0
# b=1
# count=1
# if num<=1:
#     print("enter positive numbers only")
# else:
#     while count<=num:
#         print(a,end=" ")
#         count+=1
#         c = a + b
#         a = b
#         b = c
#
# print("\nfabonnacci number\n")
# def feb(n):
#     a=0
#     b=1
#     if n<=0:
#         print("Enter positive numbers only")
#     else:
#         print(a,b,end='')
#         for i in range(2,n):
#             c=a+b
#             print(c,end='  ')
#             a = b
#             b = c
# feb(20)

#Sum of numbers
num=input("Enter number:\n")
sum=0
for digit in num:
    #if digit.isdigit():
        sum+=int(digit)
print(f'sum of digits is: {sum}')




