print("Prime Number Checking")
print("--------------")

n = int(input("Enter The Number: "))
print("RESULT")

if n < 2:
    print(f"{n} is not a prime number.")
else:
    count = 0
    for i in range(2, n):
        if (n % i) == 0:
            count += 1
            break
    if count == 0:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

      
