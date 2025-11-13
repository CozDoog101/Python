num = int(input("Enter a number (5 < num < 15): "))

if num <= 5 or num >= 15:
    print("The number must be between 5 and 15!")
else:
    sumPositive = 0
    countPositive = 0
    sumNegative = 0
    countNegative = 0
    sumAll = 0
    countAll = 0
    countPosRem3 = 0
    sumDiv15 = 0
    countDiv15 = 0

    for i in range(num):
        n = int(input("Enter a number: "))
        sumAll += n
        countAll += 1

        if n > 0:
            sumPositive += n
            countPositive += 1
            if n % 6 == 3:
                countPosRem3 += 1
        elif n < 0:
            sumNegative += n
            countNegative += 1

        if n % 15 == 0:
            sumDiv15 += n
            countDiv15 += 1

    avgPositive = sumPositive / countPositive if countPositive > 0 else 0
    avgNegative = sumNegative / countNegative if countNegative > 0 else 0
    avgAll = sumAll / countAll if countAll > 0 else 0
    avgDiv15 = sumDiv15 / countDiv15 if countDiv15 > 0 else 0

    print("Average of positive numbers:", avgPositive)
    print("Average of negative numbers:", avgNegative)
    print("Average of all numbers:", avgAll)
    print("Average of numbers divisible by 3 and 5:", avgDiv15)
    print("Count of positive numbers with remainder 3 when divided by 6:", countPosRem3)
