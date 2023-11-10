#functions
#a function is a resuable set of operations
#1.Builtin functions-which are created by python so that we can use them without creating own
#Ex:len(),min(),max(),type() etc
#2.Custom Functions :we can create a function which is a block of code,any one can reuse it

# a=int(input('Enter a :\n'))
# b=int(input("Enter b :\n"))
# print(a+b)
#
# #write some code
# def sum(a,b):
#     return a+b
# print(sum(a,b))
# print(sum(20,40))
# print(sum(30,50))

def SayHello():
    print("Hi")

SayHello() #call the function



def SayHelloToYou(name):
    print("my name is", name)
SayHelloToYou("chaitra")

min(34,56)


def inCompleteFunction(*args):
    print(type(args))
    #this code is incomplete
    print("hi, I am working on it. Please wait for 5 years to complete this")
    pass
inCompleteFunction(1)
inCompleteFunction(1,2)
inCompleteFunction(1,2,3)
inCompleteFunction(1,2,3,4,5,6,6,6,6,6)





