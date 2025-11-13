n = int(input("Enter the first num "))
listLen = int(input("Enter the len of the list num"))
listOfNumbers = []
temp = n
listOfNumbers.append(temp)
for i in range(1,listLen ):
    temp += n
    listOfNumbers.append(temp)

print(listOfNumbers)
