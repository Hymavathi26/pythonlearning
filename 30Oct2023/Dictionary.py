#dictionary in python
#key vale pain

#dict is very close to the json format

name="hymavathi"
#key=name
#value=hymavathi

#a dict is a unordered collection of data in a key value pair format
#it is defined with curly barces{} and it consiste os keys and their associated values

#set{} ---values--returns only unique values
#dict=key values

my_dict = {}
mydict = dict()

phone_book={"batsman":4582754685,"superman":4521368965,"wonder":5263485985}
print(phone_book)
print(len(phone_book))

#print(phone_book[key])
# we can access element by key only
#keys should be strings in dict

print(phone_book["batsman"])
print(phone_book["wonder"])

phone_book2=dict(batsman=123,cersei=234,GB=323)   #assign values like when we use dict() function
print(phone_book2)
print(phone_book2['GB'])
print(phone_book2.get('GB'))
print(phone_book2.get("batsman"))

hyma_details={"name":"hyma","age":26,"is_femail":True,"address":"Hyd"}  #key should be in string
print(hyma_details)

#by using dict() funxtion
hyma_details1=dict(name="hyma",age=26,Is_femail=True,Address="Hyd")
print(hyma_details1)

hyma_details1["name"]
hyma_details1.get("age")
print(hyma_details1)
