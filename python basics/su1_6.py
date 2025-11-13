n = int(input("Enter a number: "))
sum = 0
multi = 1

for i in range(1, n+1):
    if i > 0:
        sum += i
        multi *= i
    
print(f"the sum of positive num is: {sum}")
print(f"the multyply of positive num is: {multi}")