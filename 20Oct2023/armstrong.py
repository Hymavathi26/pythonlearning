#armstrong program

def is_armstrong(number):
    num_str=str(number)
    num_digit=len(num_str)

    sum_of_digit=sum(int(digit) ** num_digit for digit in num_str)
    return sum_of_digit==number

number=int(input("enter number"))

print("number is armstring number",number)
if is_armstrong(number):
    print("number is armstrong number",number)
else:
    print("number is not armstrong number",number)