# #count vowels and consonant in a goven string
#
# input_string=input("Enter a string: \n")
# vowel_count=0
# consonant_count=0
#
# vowels=set("AEIOUaeiou")
# for char in input_string:
#     #if char.isalpha():
#         if char in vowels:
#             vowel_count+=1
#         else:
#             consonant_count+=1
# print("number of vowels : " , vowel_count)
# print("number of consonant is : " , consonant_count)
#
# #by using function
def count_vowels_and_consonant(input_string):
#  initialize the counters for vowel and consonant
    count_vowels=0
    count_consonant=0
#   Define a set of vowels for case-insensitive matching
    vowels=set("AEIOUaeiou")
#  Iterate through the characters in the input string
    for char in input_string:
        if char in vowels:
            count_vowels+=1
        else:
            count_consonant+=1

    return count_vowels,count_consonant

input_string=input("enter a string: \n")

#call the function and get the count
#count_vowels,count_consonant=count_vowels_and_consonant(input_string)       #or

count_vowels=count_vowels_and_consonant(input_string)
count_consonant=count_vowels_and_consonant(input_string)

print("number of vowels:", count_vowels)
print("Number of consonant:",count_consonant)

