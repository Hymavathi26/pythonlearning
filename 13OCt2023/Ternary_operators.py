#If else
#x>18 ---Watch movie
#x<18  --Not allowed to watch movie

age=int(input("Enter age:\n"))
result='yes' if age>18 else 'no'
print(result)

x=5
y=10
max_value=x if x>y else y
print(max_value)