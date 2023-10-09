def print_2_table(n):
    for i in range(1, n + 1):
        result = 2 * i
        print(f"2 x {i:2d} = {result:2d}")

try:
    n = int(input("Enter the number of times you want to print the 2 times table: "))
    print_2_table(n)
except ValueError:
    print("Invalid input. Please enter a valid number.")
