a = int(input("First number: "))
b = int(input("Second number: "))
n = int(input("Number to check: "))

if  a >= n >= b:
    print(f"yes {n} is between {a} and {b}")
else:
    print(f"no {n} isn't between {a} and {b}")

if  a <= n <= b:
    print(f"yes {n} is between {a} and {b}")
else:
    print(f"no {n} isn't between {b} and {a}")
