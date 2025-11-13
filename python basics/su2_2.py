n = int(input("Enter a number :"))
words = []
for i in range(n):
    word = input(f"Enter string {i+1}: ")
    words.append(word)
print(f"lists of strings {words}")

longestWord = max(words)
print("Longest string is: ", longestWord)

old = input("Enter word to replace: ")
new = input("Enter new word: ")
for i in range(len(words)):
    if words[i] == old:
        words[i] = new
print(f"The replacemented word is : {words}")

wordToDelete = input("Enter word to delete: ")
if wordToDelete in words:
    words.remove(wordToDelete)
    print(f"word deleted; new list: {words}")
else:
    print("word isn't in list")

position = int(input("Enter position to insert : "))
newWord = input("Enter word to insert: ")
if 0 <= position <= len(words):
    words.insert(position, newWord)
print("new list:", words)
    

