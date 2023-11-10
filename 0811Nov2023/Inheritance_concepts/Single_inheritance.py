#to acquiring all the propertes from one class to another class
#single inheritance---90% we use this method

#Use all properties,variables and methods from base class or parent class by the subclass or child class
class animal:
    def car(self):
        print("lamborgani")

    def speak(self):
        print("animal can speak")

class dog(animal):
    pass

DOG=dog()
DOG.car()        #use all methods from class animal
DOG.speak()


#EX2:

class father:
    bank_blc=100     #class variable
    def one_bhk(self):
        print("use it son")

class son(father):
    pass   #i will wite the code in future so i just pass the code

s=son()
print(s.bank_blc)     #output is 100

s.one_bhk()
