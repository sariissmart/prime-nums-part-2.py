number = int(input("Enter a positive number: "))
a = 0
b = 1
fibonacci_sequence = []
while a <= number:
    fibonacci_sequence.append(a)
    a, b = b, a + b

print(fibonacci_sequence)
