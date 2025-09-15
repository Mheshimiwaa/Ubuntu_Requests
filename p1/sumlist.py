numbers_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(i) for i in numbers_input.split()]
total = sum(numbers)
print("Sum of the numbers:", total)
