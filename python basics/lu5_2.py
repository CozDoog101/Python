def Palindrome(number):
    reversedNumber = number[::-1] 
    if number.lower() == reversedNumber.lower():
        return 1
    else:
        return 0

number = int(input("Enter your number: "))

result = Palindrome(str(number))
print(result)