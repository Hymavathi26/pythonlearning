class Person:
    def __init__(self,name,age):
        self.__name=name         #private instance variable
        self.__age=age           #private instance variale

    def get_name(self):
        return self.__name
        return self.__age

    def set_name(self,name,age):
        if name=="john":
            print("dont set the name")
        else:
            self.__name=name
            self.__age=age

    def print_details(self):
        print("your details : ",self.__name, self.__age)


person=Person("hyma",26)      #it will call the __init__ with name,age
person.print_details()
#print(person._name)    #not access directly bcoz it is private variable


#how to change it get and set?
#get-->fetch the data
#set-->By using constructor set the value

#person.set_name('john',31)     #your details :  hyma 26
person.set_name("raj",30)      # by using this we will update the name -->your details :  raj 26

name=person.get_name()      #raj
print("After update name is ", name)

person.print_details()      ##your details :  raj 26

#Ex1:getter method()
class Student:
    def __init__(self,name):
        self.__name=name


    def get_name(self):       #A getter method is used to retrieve the value of an attribute.
        return self.__name    # adding any necessary logic before returning the value.

student=Student("student name is hyma")
print(student.get_name())       # it give output as "student name is hyma"

#setter method:
#A setter method is used to modify the value of an attribute.
#It allows you to control the modification process, applying any necessary checks or
# transformations before setting the new value.

class STUDENT:
    def __init__(self,name):
        self.__name=name
        print("before update name is :",name)

    def set_name(self,new_name):
        self.__name=new_name
        print("after updated name is :",new_name)

STD=STUDENT("raju")        #before
STD.set_name("Chaitra")    # after updated value



