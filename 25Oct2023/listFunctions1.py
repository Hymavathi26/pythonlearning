squares=[1,4,6,9,16,25,1,25]
#index=[0,1,2,3,4,5,6]
#rev_index=[-6,-5,-4,-3,-2,-1]

print(squares[0])
print(squares.count(1))
print(squares.count(25))
print(squares[-1])


#real live
#list of web elements
# element1=driver.findelement('email')
# element2=driver.findelement("pW")
# element3=driver.findelement("Submit")
# list_element=[element1,element2,element3]
# list_element[0].click()

list=[]
if not list:
    print("empty")
else:
    print("list not empty")


print(squares.pop(1))     #pop() will remove index value
print(squares)

squares.remove(1)       #remove() will remove the value in the list not index
print(squares)

# test_list=[1,2,3,4,5,6,6]
# print("the original list is: ",  str(test_list))

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))




