dict={"a":1,"b":2,"c":3}

print(dict.pop('a'))      #return 1 ,this is remove from dict
print(dict)               #{'b': 2, 'c': 3}
#print(dict.pop())      #TypeError: pop expected at least 1 argument, got 0


#Api testing---json so we can use dictionary which is similar data type as Json

#print(dir(dict()))

#print(dir(dict()))

#how to iterate over the dict
for k,v in dict.items():
    print(k,v)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    # print(k)
    # print(v)
    print(k,v,end="\n")

for k in knights.keys():
    print("print all keys from knight dict :", k ,end="\n")

for v in knights.values():
    print("print all values from knight dict : ", v,end="\n")



