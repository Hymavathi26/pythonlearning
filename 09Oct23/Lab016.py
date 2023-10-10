#string
name ="Hymavathi"

#string is immutable in nature--- We cannot change object, once create object
result=name.capitalize()
print(result)

result2=name.upper()
print(result2)
print(id(name))          #both ids are change so thats why string is immutable
print(id(result2))

#swapcase
result3=name.swapcase()
print(result3)

#title
string="hello world!!!"
print(string.title())     #starting letter of the the each word become a capital

#replace
text="Hyma is a good tester"
print(text.replace("good","Excellent"))

#count()
name="Hyma is a good tester"
print(name.count("o"))       #returns how many times o letter will be present in the test

#fing()
name="Hello pyhton"
print(name.find("p"))    #P is start from 6 th of the index


