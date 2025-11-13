numberInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numberInput.split()]
newList = []
for i in range(len(numbers)):
    if numbers[i] != 0 :
        temp = numbers[i] * -1
        newList.append(temp)
    else:
        print("0 doesn't have an oppsite")

print(f"the new list is {newList}")