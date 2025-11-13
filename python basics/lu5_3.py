def newList(number, listOfNumbers):
    newListResult = []
    for i in listOfNumbers:
        if number < i:
            newListResult.append(0)
        else:
            newListResult.append(i)
    return newListResult
def newList2(number, listOfNumbers):

    for i in listOfNumbers:
        if number < i:
            i = 0
    

number = int(input("Enter a number: "))
listInput = input("Enter numbers separated by spaces: ")
listOfNumbers = [int(x) for x in listInput.split()]

resultList = newList2(number, listOfNumbers)
print(f"The new list is: {resultList}")
