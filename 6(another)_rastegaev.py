# src/main.py

def count_digits(n):
    return len(str(abs(n)))

def compare_digits(a, b):
    if count_digits(a) > count_digits(b):
        return f"{a} has more digits than {b}"
    elif count_digits(a) < count_digits(b):
        return f"{b} has more digits than {a}"
    else:
        return f"{a} and {b} have the same number of digits"

# Example usage:
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print(compare_digits(a, b))

