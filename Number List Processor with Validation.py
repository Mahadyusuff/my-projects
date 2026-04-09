numbers = input("Enter a list of numbers separated by commas: ")
numbers = numbers.split(",")
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
valid_numbers = []
for num in numbers:
    n = safe_int(num.strip())
    if n is not None:
        valid_numbers.append(n)

squares = [num ** 2 for num in valid_numbers]
evens = [num for num in valid_numbers if num % 2 == 0]

print("Valid numbers:", valid_numbers)
print("Squares:", squares)
print("Even numbers:", evens)
