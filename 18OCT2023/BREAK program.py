# 1-10 --break when value of count =5
count=0
while count<=10:
    print(count)
    if count>=5:
        break
    count+=1

for x in range(1,10,1):
    print(x)
    if x==5:
        break

print("for loop is finished")
