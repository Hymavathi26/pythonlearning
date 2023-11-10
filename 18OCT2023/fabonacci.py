# print("Fabonacci series: ")
num = int(input("Enter num: \n"))
a = 0
b = 1
if num <= 1:
    print("enter only positive numbers")
else:
    print(a, b, end=" ")
    for i in range(2, num + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

# or
a, b = 0, 1
while a < 20:
    print(a, end=" ")
    a, b = b, a + b

num=int(input("\nEnter number: \n"))
a,b=0,1
if num<0:
    print("invalid input")
else:
    for i in range(2,num+1):
        print(a,end=' ')
        a,b=b,a+b

