def SumOfNumbers(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

numbersInput = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numbersInput.split()]
result = SumOfNumbers(numbers)
print(result)