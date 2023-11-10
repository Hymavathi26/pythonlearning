# # filter
# # filter--filtering the elements, which are less or equal to the list.
# # it is used in functions
#
# # print even numbers from the number list by using filter
#
#Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # create function
# def is_even(num):
#     return num % 2 == 0
#
# Even_numbers = filter(is_even, Numbers)
# print(Even_numbers)
#
# Even_num_list=list(Even_numbers)
# print(Even_num_list)

# numbers=[1,-1,-5,7,8,20,-30,40]
# #print only positive numbers
# def is_positive(list):
#     return list>0
# positive_numbers=filter(is_positive,numbers)      #passing the function name ,filtering elements variable name
# print(positive_numbers)
#
# pos_numbers_list=list(positive_numbers)
# print(pos_numbers_list)

words=["banana", "apple","cherry","straberry","kiwi"]
min_length=6
def check_len(word):
    #return len(word) > 6   directly assign lengh of the words    (or)
     return len(word) > min_length

op=list(filter(check_len,words))
print(op)

fruits=("banana","kiwi","guava","plum")
min_len=4

def check_length(fru):
    return len(fru) > min_len

output=list(filter(check_length,fruits))
print(output)


