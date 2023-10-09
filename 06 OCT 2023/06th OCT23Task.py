#Task2:Take a user from input and print a table
n=int(input("Enter number: "))
print(f'Table of {n} is :')

print(f'{n} X 1 = {n*1}')
print(f'{n} X 2 = {n*2}')
print(f'{n} X 3 = {n*3}')
print(f'{n} X 4 = {n*4}')
print(f'{n} X 5 = {n*5}')
print(f'{n} X 6 = {n*6}')
print(f'{n} X 7 = {n*7}')
print(f'{n} X 8 = {n*8}')
print(f'{n} X 9 = {n*9}')
print(f'{n} X 10 = {n*10}')

#using for loop
n=int(input("Enter the number to print the table for: "))
for i in range(1,11,1):
    print(n, "*",i,'=',n*i)


#Task3:list of all functions for the string data types
s = "Hyma is a Good Tester"
print(len(s))
print(type(s))

#Testing strings:
print(s.isalnum())	   #Checks if all characters in the string are alphanumeric.
print(s.isalpha())	   #Checks if all characters in the string are alphabetic.
print(s.isascii())	   #Returns True if all characters in the string are ascii characters
print(s.isdecimal())   #Returns True if all characters in the string are decimals
print(s.isdigit())	   #Checks if all characters in the string are digits.
print(s.isidentifier()) #Returns True if the string is an identifier
print(s.islower())	    #Returns True if all characters in the string are lower case
print(s.isnumeric())     #Returns True if all characters in the string are numeric
print(s.isprintable())   #Returns True if all characters in the string are printable
print(s.isspace())	    #Returns True if all characters in the string are whitespaces
print(s.istitle())	   #Returns True if the string follows the rules of a title
print(s.isupper())	   #Returns True if all characters in the string are upper case

#Searching for substrings:

print(s.endswith("Tester"))
print(s.startswith("hyma"))      # Checks if the string starts with a specified prefix.
print(s.startswith("chaitra"))  #  Checks if the string ends with a specified suffix.
#str.find(substring)            #Searches for a substring and returns the index of its first occurrence (or -1 if not found).
print(s.find("bad"))     # -1 (if not fount string)
print(s.find("Good"))     # returns 10 (Searches the string for a specified value and returns the last position of where it was found)
print(s.count("a"))
print(s.strip())	      #Removes leading and trailing whitespace characters.
print(s.split())	      #Splits a string into a list of substrings based on whitespace by default (can specify a separator).

#Converting strings:

print(s.capitalize())        #Capitalizes the first character of the string.
print(s.title())            #Capitalizes the first character of each word in the string.
print(s.lower())            #Converts all characters in a string to lowercase.
print(s.upper())            # Converts all characters in a string to uppercase.
print(s.swapcase())         #waps the case of characters (Exapmle:uppercase to lowercase and vice versa).
#print(s.replace("old","new")) #Replaces occurrences of a substring with another substring.
print(s.replace("Good","Excellent"))

#str(int_value)
#example
a=20
print(type(a))
string=str(a)
print(type(string))
#str(float_value)
b= 34.8
print(type(b))
string1=str(b)
print(type(string1))

#string formatting
name="hyma"
age=26
#f-strings
print(f"My name is {name} and I am {age} years old")
#str.format
print("My name is {} and I am {} years old.".format(name,age))

