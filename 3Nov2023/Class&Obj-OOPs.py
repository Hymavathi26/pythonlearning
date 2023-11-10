# #class and object in python
#
# #Person-Class name
# #Attribute--> (state of the class)-->Name,age,ph_num,Height,gender etc
# #Method-->( Beheaviour or praporty)-->Run(),sleep(),fight(),eat(),learn(),hear(),sing(),think()
#
class Person:
    #attributes
    name=None
    age=None
    ph_no=None
    gender=None

    #methods
    def sleep(self):
        print("sleep")
    def think(self):
        print("thinking")
    def eat(self):
        print("eating")

hyma_obj=Person()
hyma_obj.name="name is hyma"
hyma_obj.age=26
hyma_obj.ph_no=6356235689
hyma_obj.gender="Femal"

print(hyma_obj)
hyma_obj.sleep()

raj_obj=Person()
raj_obj.name="Raju"
print(raj_obj)
raj_obj.think()

#
#

