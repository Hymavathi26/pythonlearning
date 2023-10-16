# Difference between = and == operator
# =  for assigning the values
# == for checking the condition is true or false
# Task1:
a = 10
b = 20
print(a == b)

# ** operation
a = 2
b = 3
print(2 ** 3)

# ^ operator
print(a ^ b)  # it will take values in the binary case

# Task2:  #find area of the circle with formala (3.14*r^2)
radies = float(input("Enter radies number:\n"))
area = 3.14 * radies ** 2
print(area)

a = 10
b = 20
if a > b:
    print("a is greather than b")
elif a < b:
    print("a is lessthan b")
else :
    print("a is equal to b")

#maximum of three numbers using ternatory operator
num1=int(input("Enter num1:\n"))
num2=int(input("Enter num2:\n"))
num3=int(input("Enter num3:\n"))
result=num1 if (num1>num2 and num1>num3) else num2 if (num2 >num3) else num3
print(f'the max of {num1},{num2},and{num3} is: {result}',end="\n")



print(f'the square of{num1} is: {num1**2}')
print(f'The cube of num3 is : {num3**3}' ,end="\n\n")
#calculate square and cube of the given number
num=int(input("Enter num:\n"))
square=num**2
cube=num**3
print(square)
print(cube)


