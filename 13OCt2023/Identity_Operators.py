# Is    --it returns True if both values are in the same object
# is not --It returs True if both valus are not in the same objects
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)
print(id(x),id(y))
print(x is not y)
