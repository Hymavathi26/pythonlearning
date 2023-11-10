#Car-- class name
#objects--Tesla,lambo

#self is an special variable that is used within the contex of OOP
#it is reference to the instance to the class
#access and manipulate the attributes and methods of that instance /object

class Car:
    name=None
    color=None
    speed=None
    model=None
    engine=None

    def start_rngine(self):
        print("Starting the enginee")

    def drive(self):
        print("driving")

    def car_break(self):
        print("Break")

    def who_is_driving(self):
        print("who is driving --> ", self.name)

tesla_obj_ref=Car()    #this is the instance of class--object
labmo_obj_ref=Car()    #this is the instance of class--object

tesla_obj_ref.name= "Tesla"
labmo_obj_ref.name= "lambo"

tesla_obj_ref.who_is_driving()
labmo_obj_ref.who_is_driving()




