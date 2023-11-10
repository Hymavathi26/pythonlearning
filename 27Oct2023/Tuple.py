#list :list is mutable-its content can be changed
# my_list=[1,2,3,4,5]
# print(my_list)
# my_list[0]=30
# print(my_list)
# print(type(my_list))
#
# #tuple-tuple is immutable- no modification
# tuple=(1,2,3,4,5)
# car=("ford GT","raptor","Lambo","Lambo")
# car2=("Ford GT",True,"Lambo")
# print(type(car))

#tuple[0]="tata"  #type error

#tuple()--its content cannot be chaned , list-[]-- its content can be changed!
#list can be converted into tuple vice versa

list1=[1,2,3,45]
print(tuple(list1))

list1 = [1, 2, 3, 4, 5, 6]
print(tuple(list1))

tuple1=(1,2,3,43,5,6)
print(type(tuple1))
list=list(tuple1)
print(list)
print(type(list))
tuple2=tuple(list)
print(type(tuple2))
print(tuple2)




