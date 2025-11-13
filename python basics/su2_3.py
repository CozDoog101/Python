m = int(input("Enter number of elements: "))
dictionary = {}

for i in range(m):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value {i+1}: ")
    dictionary[key] = value

print(f"Dictionary : {dictionary}")   

keyToSearch = input("Key to search: ")
if keyToSearch in dictionary:
    print(f"key is in the dictionary: {dictionary}")
else:
    print(f"key isn't in dictionary: ")

changeKey = input("Enter key to change: ")
if changeKey in dictionary:
    newValue = input("Enter new Value: ")
    dictionary[key] = newValue
    print(f"key changed; new dictionary: {dictionary}")

deletedKey = input("Enter key to delete: ")
if deletedKey in dictionary:
    del dictionary[deletedKey]
    print(f"key deleted; new dictionary: {dictionary}")

print(f"all keys: {dictionary.keys()}")
print(f"all values: {dictionary.values()}")

sortedKeys = sorted(dictionary.keys())
for i in dictionary:
    print(f"{i}: {dictionary[i]}", end = " ")

