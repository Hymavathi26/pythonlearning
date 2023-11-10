tuple=()
tuple1=(1,2,3,4,5)
tuple2=(["hyma","raju","chaitra"])   #assign multiple strings in a tuple list
print(type(tuple2))
print(tuple)
print(tuple1)
print(tuple2)
tuple2[1]="raj"
print(tuple2)

# tuple1[0]=10
# print( tuple1)    #Not change the values in tuple

#read using index321
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])

#Merging tuples
hero1=("batman","bruce wayne")
hero2=("wonder women","diana prince")
awesome_team=hero1+hero2
print(awesome_team)

hero1=["batman","bruce wayne"]
hero2=["wonder women","diana prince"]
awesome_team=hero1+hero2
print(awesome_team)

tuplee=(1,2,3)
tuplee1=(4,5,6)
tuple3=tuplee+tuplee1
print(tuple3)

x=10
a,b=10,20
x,y,z=10,30,60
q,r,s=(100,200,300)      #tuple assign to multiple values
print(a,b)
print(q,r,s)

#Nested tuples
hero1=("batman","bruce wayne")
hero2=("wonder women","diana prince")
awesome_team=(hero1,hero2)       #nested
print(awesome_team)
# print(hero1[0][0])      #returns 'b'
# print(hero1[0][1])      #returns 'a'
print(len(awesome_team))    #(('batman', 'bruce wayne'), ('wonder women', 'diana prince'))
                            #         0                              1
print(awesome_team[0])      #('batman', 'bruce wayne')
                            #   [0][0]    [0][1]
print(awesome_team[1])      #('wonder women', 'diana prince')
                            #   [1][0]           [1][1]

print(awesome_team[0][1])    #bruce wayne
print(awesome_team[1][1])    #dianina prince

#search in tuple
cities=("lundon","hyderabad","UK","USA","AP")
print("lundon" in cities)
print("hyderabad" in cities)



