#1. Write a Python program to find the largest number in a list.

list=[1,2,4,5,7,8,9,20,10]
print(list)
print("Max number in the list is : ",max(list))

#2.Write a Python program to find the smallest number in a list.

print("Min number in the list is :",min(list))

#3.Write a Python program to sum all numbers in a list.

print("sum of all numbers in the list is :",sum(list))

#4. Write a Python program to multiply all numbers in a list
list=[1,2,3,4]
result=1
for i in list:
    result*=i
print("the product of the numbers in the list is :",result)


#by using def function
def multiply_list(numbers):
    result=1
    for i in numbers:
        result*=i
    return result

numbers=[4,5,6]
result1=multiply_list(numbers)
print("the product of numbers in the list is:",result1)

#5. Write a Python program to count the number of strings in a list where the string length is 2 or
# more and the first and last character are the same.