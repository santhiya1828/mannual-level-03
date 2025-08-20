print("Prime Number Generation")
print("--------")

SN = int(input("Enter the starting number: "))
EN = int(input("Enter the ending number: "))
print("RESULT")

for n in range(SN, EN + 1):
    if n < 2:
        continue  # skip numbers less than 2
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number.")
