
n = int(input("enter a 6-digit number:"))
reversedN = 0

for i in range(6):
    digit = n % 10
    n //= 10
    reversedN += digit * (10 ** (5 - i))

print(f"The reversed number is:{reversedN}")
