products=[
    {"name":"laptop" , "price":1000},           #[0]
    {"name":"smartphone" , "price":3000},       #[1]
    {"name":"tablet" , "price":100},            #[2]
    {"name":"headphone" , "price":300}          #[3]
    ]

print(type(products))
print(type(products[0]))
print(len(products))                #length is 4

#print(products[0])       #name,price

#print <500 price list
#print length>6

def is_affordable(items):
    return items["price"] <500

def is_affordable_name(items):
    return len(items["name"])>6

affordable_items=list(filter(is_affordable,products))
print((affordable_items))

affordable_item_name=list(filter(is_affordable_name,products))
print("affordable item names from products", affordable_item_name)    #[{'name': 'smartphone', 'price': 3000}, {'name': 'headphone', 'price': 300}]


# #print name of affordable_items
# print(affordable_items[0]["name"])
#
# #print name and price of affordbale items
# print(affordable_items[0]["name"] + str(affordable_items[0]["price"]))   #tablet100  #conver int into str then concatenate
# print(affordable_items[1]["name"] + str(affordable_items[1]["price"]))        #headphone300

#by using for loop
for i in affordable_items:
    print("affordable items:",i["name"],i["price"])

for i in affordable_item_name:
    print("affordable item names :",i["name"],i["price"])



#print list of numbers greaterthan 10
numlist=[1,45,3,-6,-8,30,40,100,-9]
list_of_num_greater_10=list(filter(lambda number:number >10,numlist))
print(list_of_num_greater_10)


num_tuple=(1,3,4,5,6,10,5,8)
def is_even(num):
    return num%2==0

even_numbers=list(filter(is_even,num_tuple))
print(even_numbers)