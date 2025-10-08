numberInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numberInput.split()]
maxNum = numbers[0]
#biggestNum= max(numbers)
#print(f"The biggest number is : {biggestNum}")
for i in range(len(numbers)): #range(nimbers[i:])
    if maxNum < numbers[i]:
        maxNum = numbers[i]

print(f"The biggest number is : {maxNum}")
