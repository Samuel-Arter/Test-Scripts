def fibonacci(n):
    sequence = []

    for i in range(n + 1):

        if i == 0:
            sequence.append(0)

        elif i == 1:
            sequence.append(1)

        elif i > 1:
            number = sequence[i - 1] + sequence[i - 2]
            sequence.append(number)

    return sequence

print(fibonacci(5))
