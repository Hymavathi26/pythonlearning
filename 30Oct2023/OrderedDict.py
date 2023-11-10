# #ordereddictionary
# #key-value pair based on the order of insertion
#
# #dict--it will not keep the order of insertion
# #orderdict--it will keep the order of insertion
#
# #list,tuple,set,dict,ordereddict -----uses in API automation and Selenium
#
# #selenium--insert the web elemenets into dict
# #if we want to keep the order---login elements,dashboard elements etc
#
#
# #OrderedDict
from collections import OrderedDict
od=OrderedDict()    #create empty ordereddict
od["a"]=10          #update values into empt orderd dict
od["c"]=50
od["b"]=100
od["d"]=30

print(od)           # it returns  OrderedDict([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

keys=od.keys()
print(keys)         #odict_keys(['a', 'b', 'c', 'd'])
items=od.items()
print(items)        #odict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

keys_sorted=sorted(keys)
print("after sorted",keys_sorted)
values=od.values()
print(values)

values_sorted=sorted(values)
print("After sorted values:",values_sorted)
key_sort_rev=sorted(keys,reverse=True)
print(key_sort_rev)
val_sort_rev=sorted(values,reverse=True)
print(val_sort_rev)

#
# from collections import OrderedDict
# od =  OrderedDict()
# od['a'] = 45
# od['c'] = 78
# od['b'] = 97
# od['d'] = 31
#
# print(od)
#
#
keys = list(od.keys())
print(keys)
keys_sort=sorted(keys)
print(keys_sort)
#
# keys_sort_rev=sorted(keys, reverse=True)
# print(keys_sort_rev)

#update vales by using index
od2=OrderedDict()

od2[keys_sort[0]]=2
od2[keys_sort[1]]=10
od2[keys_sort[1]]=9
od2[keys_sort[2]]=5

print(od2)