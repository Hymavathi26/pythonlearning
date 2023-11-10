# set1={1,2,3,4,5,5,6,4,1}
# set2={1,3,4,7,8,9,10,20,4,5}
#
# #union()---to combined all sets in a one
# my_set=set1.union(set2)
# print(my_set)
#
# my_set2=set1.difference(set2)    #returns unique values from set1
# print(my_set2)
# my_set2=set2.difference(set1)    #return unique values from set2
# print(my_set2)
#
# myset=set1.intersection(set2)
# print(myset)
#
# set1={1,2,3,4,5}
# set2={2,3,4}
# subset=set1.issubset(set2)
# print(subset)
# subset1=set2.issubset(set1)
# print(subset1)
#
#
# set1 = set([1, 2, 3, 4, 5, 6,
#             7, 8, 9, 10, 11, 12])
# print(set1)
#
# set1.remove(3)
# set1.pop()         #remove first value in the sequence
# print(set1)
#
# myset=set(["hyma","raju","chaitra"])
# print(myset)

num=20
def multiply_by_10(n):
    n*=10
    num=n      #changing the value inside the function
    print("value of num inside function" , num)
    return num

op=multiply_by_10(num)
print(op)
print("value of num outside the function" ,num)

list = [10, 20, 30]
#tuple = (2, 3, 4)
print(list)

def mul_by10(a):
    a[0] *= 10
    a[1] *= 10
    #a[2] *= 10

print(list)
mul_by10(list)
#mul_by10(tuple)     #tuple does not support item assignment
print(list)
#print(tuple)

def sayHello():
    print("Hello")


sayHello()

op = sayHello()
print(op)


a = max(45,33,3)
print(a)


