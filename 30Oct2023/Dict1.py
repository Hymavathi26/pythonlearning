my_dict = {"a": 1, "b": 20, "c": 30, "a": 90}
print(my_dict)
print("length of dict :", len(my_dict))
# if we have a duplicate key, latest value of key will be used

# print all keys and all values from dict
keys = my_dict.keys()
values = my_dict.values()
items=my_dict.items()

print(keys)
print(values)
print(items)

# get all the keys into list
keys_list = list(keys)
print(keys_list)
values_list = list(values)
print(values_list)

#read keys by using index
print(keys_list[0])
print(keys_list[1])
print(keys_list[2])

#clear the dict
# my_dict.clear()
# print(my_dict)        #returns empty dict

#copy the dict
copy_my_dict=my_dict.copy()
print(copy_my_dict)

#we want to print all dict values by using item() funvtion
print(my_dict.items())

#convert dictionary into set()
set_dict=set(my_dict)
print(set_dict)     #returns only keys       {'a', 'b', 'c'}
set_dict=set(my_dict.items())
print(my_dict)      #returns key and value   {'a': 90, 'b': 20, 'c': 30}





