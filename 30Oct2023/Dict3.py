#Automation tester--API and web automation

dict={"a":10,"b":30,"c":40}
print(dict)

for k,v in dict.items():
    if k == 'b':
        print("b found in dict!!!")

op= 'b' in dict
op2= 'd' in dict
print(op)
print(op2)
#Assign boolean value as a key in dictionary
dictionary={True:1234}
print(dictionary)
updated_dict=dictionary[True]=4567
print(updated_dict)

api_resonse = {
    "first_name" : "hymavathi",
    "age": 26,
    "last_name":"kothapalle",
    "email":"hymaraj21@gmail.com",
    "password":"test@1234",
    "commission":10,
    "roles":[4
            ]
}

print(api_resonse)
print(type(api_resonse))

for key,value in api_resonse.items():
    print(key,value)

print(api_resonse["password"])
print(api_resonse.get("password"))

api_resonse["age"]=25
print(api_resonse)