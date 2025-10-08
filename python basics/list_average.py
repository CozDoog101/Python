numbersInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numbersInput.split()]
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
