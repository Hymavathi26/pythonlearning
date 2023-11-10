# List--collection of items-it allows duplicate
my_list = [1, 2, 3]
my_list1 = [1, 2, "hyma", 23.5]  # list allows diff type of data types
print("initial list : " , my_list)

#indexing
print("Element at index 0 : ",my_list[0])

#changing an element
my_list[1]=20
print("list after chaning element :" ,my_list)

#append()
my_list.append(4)
print("list after appending : ", my_list)

#Extend()
my_list.extend([5,6,7])
print("after extend the list : ",my_list)

#insert()
my_list.insert(1,'hyma')
print("list after inserting 'hyma' at index 1 : " ,my_list)

#remove()
my_list.remove('hyma')
print("list after removing : ",my_list)

#copylist
my_copy_list = my_list.copy()
print("list after coping : " ,my_copy_list)

#clear
my_list.clear()
print(my_list)

print(my_copy_list)
#sort()
my_copy_list.sort()
print(my_copy_list)

#reverse()
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])

print(len(my_copy_list))
my_list=my_copy_list.copy()
print(my_list)
my_list.remove(4)
print(my_list)


