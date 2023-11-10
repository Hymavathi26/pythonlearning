# num=int(input("Enter number: \n"))
# factorial=1
# if factorial>=1:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"Factorial of {num} is : {factorial}")

#or
num=int(input("Enter number: \n"))
if num<0:
    print("factorial is not possible for negative")
else:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
print("fact is :",fact)


