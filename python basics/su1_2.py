import math
n = int(input("Enter a number: "))
sumTotal = 0
minOdd = math.inf # 9999999999999999999
maxEven = -math.inf # -99999999999999999
countEven = 0 
countOdd = 0 

for i in range(1, n+1):
    if i % 2 == 0:
        if i > maxEven:
            maxEven = i
        countEven += 1
    else:
        if i < minOdd:
            minOdd = i
        countOdd += 1  
    sumTotal += i

print(f"Biggest number : {maxEven}")
print(f"Smallest number : {minOdd}")
print(f"Even number : {countEven}")
print(f"Odd number : {countOdd}")
