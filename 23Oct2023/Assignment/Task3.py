#Create a Function with a Parameter which can do x^y(binary function)

def power(x,y):
    return x**y

print(power(3,4))
#or

def power(x,y):
    result=x**y
    return result

result=power(2,3)
print(result)

#bby using binary function

def binaryfunc(x,y):
    return x^y
x=int(input("enter x value: \n"))
y=int(input("enter y value: \n"))
print(binaryfunc(x,y))

