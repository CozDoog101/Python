numbersInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numbersInput.split()]
print(3*numbers)
for i in numbers:
    print(i)

searchedNumber = int(input("Number to be searched: "))
for i in numbers:
    if i == searchedNumber:
        print(f"{searchedNumber} is in the list")
    else:
        print("number isn't in list")

numbers.sort()
print(numbers)

maxNum = numbers.max()
print(maxNum)

deleteByIndex = int(input("Index to delete: "))
if 0 <= deleteByIndex <= len(numbers):
    numbers.pop(deleteByIndex)
print(f"{deleteByIndex} is removed: {numbers}")

changeByIndex = int(input("Index to be change: "))
if 0 <= changeByIndex <= len(numbers):
    temp = int(input("New value: "))
    numbers[changeByIndex] = temp
print(f"New list :{numbers}")