#create a program  to takle i/p from user by adding 2 or 3 duplicates and print non duplicate names

name =[]
for i in range(1,5):
    String=input("Enter name: \n")
    name.append(String)
    print(name)

set1=set(name)
print(set1)
#without using loop
a=input("Enter name: \n")
b=input("Eneter name2: \n")
c=input("Enter third name: \n")
d=input("Enter fourth name :\n")
list1=[a,b,c,d]
set=set(list1)
print(set)
