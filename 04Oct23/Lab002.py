# list=[1,20,30,40]
# print(max(list))
#
# list= [2,3,4,5,6]
# print(min(list))
#
# list3= [1,2,3,4]
# list3.append(5)
# print(list3)
#
# #Average of all numbers in a list
# list=[1,2,3,4,5,6]
# average=sum(list)/len(list)
# print(average)
# #(or) using loop
# list4=[1,2,3,4,5,6]
# total=0
# for num in list4:
#     total+=num
# average=total/len(list4)
# print(average)

#multiplying numbers ina list
# from functools import reduce
# list1=[1,2,3]
# list2=[3,4]
# result1=reduce((lambda x, y: x*y),list1)
# result2=reduce((lambda x, y: x*y),list2)
# print(result1)
# print(result2)

from operator import *
list1=[1,2,3,4]
m=1
for i in list1:
    m=mul(i, m)
print(m)
