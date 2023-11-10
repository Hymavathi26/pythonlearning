# my_list=[True,"hyma",23,45.6]
# print(my_list)
# my_list.sort()    #TypeError: '<' not supported between instances of 'str' and 'bool'
#not supported sort when combination of diff data types in a list

squares=[1,4,9,16,25]
l=squares
l2=squares.copy()
print(squares)
# print(l)
# print(l2)

squares[0]=33
print(squares)
print(l)       #ref variable will change
print(l2)      #copied variable is not affected returns origial list

