

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - 1) + "* " * i)


for i in range(n - 1, 0, -1):
    print(" " * (n - 1) + "* " * i)
