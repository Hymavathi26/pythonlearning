#continue

for num in range(1,10):
    if num%2==0:
        print(f"Found even number : {num}")
        continue
    print(f"found odd number : {num}")

#pass

for i in range(1,10):
    if i==5:
        pass
    else:
        print(i)