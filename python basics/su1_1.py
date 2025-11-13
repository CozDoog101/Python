n = int(input("Enter a number: "))
sumTotal = 0
sumOdd = 0
sumEven = 0
countOdd = 0 

for i in range(1, n+1):
    if i % 2 == 0:
        sumEven += i
    else:
        sumOdd += i
        countOdd += 1  
    sumTotal += i

if countOdd > 0:
    avg = sumOdd / countOdd
else:
    avg = 0 

print(f"The sum of even numbers is: {sumEven}")
print(f"The average of odd numbers is: {avg}")
print(f"The total sum is: {sumTotal}")
