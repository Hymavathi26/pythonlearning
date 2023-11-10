# map and filter in the list

# Map functions  (where we will go from one item and apply a function)
numbers = [1, 2, 3, 4, 5]
# sq_numbers=[1,4,9,16,25]
# sq = lambda x: x * x
# sq_numbers = []
# for i in numbers:
#     sq_numbers.append(sq(i))
# print(sq_numbers)
#
# def threetimes(a):
#     return a**3
# result=threetimes(3)
# print(result)

#Map function
sq_numbers3=list(map(lambda x: x*3 ,numbers))
sq_numbers2=list(map(lambda x: x*2 , numbers))
print(sq_numbers3)
print(sq_numbers2)



