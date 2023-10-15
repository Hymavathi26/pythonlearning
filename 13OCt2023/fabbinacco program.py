def febo(num):
    a=0
    b=1
    if num<=0:
        print("enter positive numbers only")
    else:
        print(a,b,end=' ')
        for i in range(2,num+1):
            c=a+b
            a=b
            b=c
            print(c,end=' ')
num=int(input("Enter fabbinacco number:"))
febo(num)
