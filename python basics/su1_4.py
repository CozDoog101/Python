a = int(input("First number: "))
b = int(input("Second number: "))

sum = 0
count = 0
start = min(a, b)
"""
    start = 0
    if a < b:
        start = a
    else:

"""
end = max(a, b)

for i in range(start, end + 1):
    sum += i
    count += 1

print(f"The sum of numbers is: {sum}")
print(f"The count of numbers is: {count}")
