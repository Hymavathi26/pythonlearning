#Function--without class we can create function
def add(a,b):
    return a+b

print(add(10,30))


#Method--with in class we can create method
#methos is collection of variables

class Addition:
    def add(self,a,b):
        return a+b

adding_obj=Addition()
adding_obj.add(10,30)
print(adding_obj)
