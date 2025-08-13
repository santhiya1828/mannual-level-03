print("SUM OF N NUMBERS")
print("--------------------")
n = int(input("Enter a number: "))
total = 0
process = ""

for i in range(1, n + 1):
    total += i
    process += str(i)
    if i != n:
        process += " + "

print(f"The process is: {process} = {total}")
print(f"The sum of first {n} numbers is: {total}")
