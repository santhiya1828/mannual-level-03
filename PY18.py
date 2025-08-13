print("SUM OF GIVEN NUMBERS")
print("-------------------")

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

if start > end:
    print("Starting value should be less than or equal to ending value.")
else:
    total = 0
    process = ""
    count = 0
    for i in range(start, end + 1):
        total += i
        count += 1  
        process += str(i)
        if i != end:
            process += " + "

    print(f"The process is: {process} = {total}")
    print(f"The sum from {start} to {end} is: {total}")
    print("The count value:", count)
