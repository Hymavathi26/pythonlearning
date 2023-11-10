#Create a Lambda expression to triple power 2 ** 3 a number

inputdata=int(input("enter number: \n"))
triplelambda=lambda inputdata:inputdata**3
print(triplelambda(inputdata))

#  or

inputdata=int(input("Enter number: \n"))
x=lambda x:x**3
result=x(inputdata)
print(f'triple power of {inputdata} is {result}')


sumlambda=lambda x,y:x+y
print("addition of x,y ",sumlambda(3,4))




