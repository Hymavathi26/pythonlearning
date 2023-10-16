# # Grade calculator
# score = float(input("Enter score:\n"))
# grade = None
# if score >= 90 and score <= 100:
#     grade = 'A'
# elif score >= 80 and score <= 90:
#     grade = 'B'
# elif score >= 70 and score <= 79:
#     grade = 'C'
# elif score >= 60 and score <= 69:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f'the grade is : {grade}')

a=float(input("Enter the score: "))
if 90<= a <=100:
    result="A"
elif 80<= a <=89:
    result = "B"
elif 70<= a <=79:
    result = "C"
elif 60<= a <=69:
    result = "D"
else:
    result = "F"
print(f"The grade for the marks {a} is {result}")