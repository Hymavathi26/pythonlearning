dict=dict(a=1,b=2,c=3,d=4)
print(dict)
val=dict.pop('a')    #remove a value
print(val)
print(dict)

#popitem() ---popitem is used to remove and return an arbitary key-value pair(as a tuple) from the dictionary
val2=dict.popitem()
print(val2)
print(dict.popitem())
print(dict)
dict['a']=20     #delete 'a' value and again update 'a' value to the dictionary
print(dict)
dict['c']=val2       #Re-assign same value to the dictionary(previous deleted value)
print(dict)
# del dict
# print(dict)        #return class type if we use dict()

my_dict = {'a': 1, 'b': 2, 'c': 3}
#del my_dict
#print(my_dict)       #showing not defined error bcoz already the dictionary has been deleted

my_dict['a']=8
print(my_dict)



