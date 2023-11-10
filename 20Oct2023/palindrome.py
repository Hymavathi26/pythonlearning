# string=input("Enter number: \n")
# if (string==string[::-1]):
#     print("given string is palindeome")
# else:
#     print("Not palindrome")
#
# #by using function
# def hello():
#     print("code that you want to execute")
# hello()
#
# # function with passing one argument
# def funcwithparam(a):
#     return a**3
# output=funcwithparam(3)
# print(output)
#
# # by using function polinmdrome
# def reverse_string(input_string):
#     reverse_str = ''
#     for c in input_string:
#         reverse_str = c + reverse_str
#     return reverse_str
#
# original_string = "NAMAN"
# rev_string = reverse_string(original_string)  #call the function
# print(rev_string)
#
# if original_string==rev_string:
#     print("polindrome")
# else:
#     print("not polindrome")
#
#
# #by using builtin functions like slicing
# original_str="MALAYALAM"
# def is_polindrome(original_str):
#     rev_str=original_str[::-1]
#     print(rev_str)
#     if original_str==rev_str:
#         print("polindrome")
#     else:
#         print("not polindrom")
# is_polindrome(original_str)
#
#
# # BY USING reversed() function
# original_string="HYMA"
#
# def rev_str(original_string):
#     return ''.join(reversed(original_string))  #USING REVERSED() FUNCTION
#
# reverse_string=rev_str(original_string)
# print(reverse_string)
#
#
#
#
#
#
def is_armstrong_number(number):
    # Convert the number to a string to count its digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return sum_of_digits == number

# Get user input
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number and print the result
if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
