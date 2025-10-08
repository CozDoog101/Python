print("****Palindrome Checker****")
word = input("Enter your word: ")
reversedWord = word[::-1] # for reversing strings /
if word.lower() == reversedWord.lower():
    print(f"The word {word} is indeed a palindrome")
else:
    print(f"The word {word} is NOT a palindrome")
    