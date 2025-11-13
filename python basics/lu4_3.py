numberInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numberInput.split()]
numbersToRemove = int(input("Ënter a number: "))

sortedList = sorted(numbers)
if len(sortedList) > numbersToRemove:

    for i in range(numbersToRemove):
        sortedList.remove(sortedList[0])

    print("the new list is:", end=' ')
    for i in range(len(sortedList) - 1):
        print(f"{sortedList[i]}", end= ", ")
    print(f"{sortedList[i+1]}")

else:
     print("not enough numbers in list ")
