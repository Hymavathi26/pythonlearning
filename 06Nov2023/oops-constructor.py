# #constructor-->constructor invoke the function at the time of obj creation it self
# #__init__(self)--->this is the key word
#
# class car:
#     def __init__(self,make,model):    #default constuructor
#         self.make=make      #instance variable
#         self.model=model    #instance variable
#         print("i will cal the first")
#
#
#     def start_engine(self):
#         print("Starting a car ",self.make,self.model)
#
# car1=car("Toyota","camry")
# car2=car("Honda", "civic")
#
# car1.start_engine()
# car2.start_engine()
#
# print(id(car1))
# print(id(car2))
#
#
# #Ex2:
class Person:
    def __init(self):
        print("I can use you ")

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("you created an object with name and age")

    def printDetails1(self):
        print("Your details are :",self.name,self.age)

    def printDetails2(self):
        print("your details areb ",self.name * 2)

hyma=Person("hymavathi",26)
hyma.printDetails1()

raj=Person("raju",30)
raj.printDetails2()


