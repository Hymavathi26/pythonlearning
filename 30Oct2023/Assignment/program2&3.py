#Find the intersection and union of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print(set1)
print(set2)
#print(set1,set2 ,end="\n")

print("Intersection of sets :",set1.intersection(set2))     #{3,4,5}
print("union of sets :",set1.union(set2))            #{1, 2, 3, 4, 5, 6, 7}

# Program 3:
# duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
print("print list with duplicate values :" ,my_list)

new_list=list(set(my_list))
print("print list with unique values : ",new_list)         #[1, 2, 3, 4, 5]
