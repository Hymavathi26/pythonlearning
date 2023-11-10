# number=input("Enter number:\n")
# sum=0
# for digit in number:
#     sum=sum+int(digit)
# print(f"sum of digits : {sum}")
#
# digit=12345
# mod1=digit%10
# print(mod1)
# digit=1234
# mod2=digit%10
# print(mod2)
# digit=123
# mod3=digit%10
# print(mod3)
# digit=12
# mod4=digit%10
# print(mod4)
# digit=1
# mod5=digit%10
# print(mod5)

num=int(input("Enter your number :\n"))
sum=0
while num!=0:
    digit=num%10
    sum=sum+digit
    num//=10           #num=int(num/10)

print(sum)
