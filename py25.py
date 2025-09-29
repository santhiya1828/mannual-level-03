

n = int(input("Enter the number of rows: "))


for i in range(n, 0, -1):
    print(" " * (i - 1) + "*")


for i in range(2, n + 1):
    print(" " * (i - 1) + "*")
