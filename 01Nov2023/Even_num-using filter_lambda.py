numbers=[1,2,3,4,5,6,7,8,9,10,20]
even_numbers=list(filter(lambda numbers:numbers%2==0,numbers))

print(even_numbers)

#by using map
Even_num=list(map(lambda numbers:print(numbers) if numbers%2==0 else None,numbers))
print(Even_num)       # this statement returns  [None, None, None, None, None, None, None, None, None, None, None]