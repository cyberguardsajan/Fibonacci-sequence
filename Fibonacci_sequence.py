def fibonacci(n):
    sequence = []
    a, b = 0, 1


    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

n_terms = 20
fib_sequence = fibonacci(n_terms)
print(f"First {n_terms} terms of the Fibonacci sequence: {fib_sequence}")
