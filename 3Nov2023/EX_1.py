class My_class:
    def print_frst_name_with_last_name(self,frst_name,last_name,age):
        print("your name is " + frst_name,last_name,age)

hyma_obj_ref=My_class()
hyma_obj_ref.print_frst_name_with_last_name("hymavathi","k",26)


#take a input from user

class Car:
    color=None
    model=None

    def car_details(self):
        print("your car details are",self.color,self.model)

car_color=input("Enter car color :")
car_model=input("Enter car model :")


car_obj_ref=Car()

car_obj_ref.color=car_color
car_obj_ref.model=car_model

car_obj_ref.car_details()





