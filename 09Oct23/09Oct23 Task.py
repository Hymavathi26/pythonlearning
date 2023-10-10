#create a program  to takle i/p from user by adding 2 or 3 duplicates and print non duplicate names

name =[]
for i in range(1,5):
    String=input("Enter name: \n")
    name.append(String)
    print(name)

set1=set(name)
print(set1)


