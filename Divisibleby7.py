# prints all numbers in [0,1000] that are divisible by 7 and whose digits sum to a number that is divisible by 3

numbers = []

def sum_of_digits(n):
    sum = 0
    for i in range(len(str(n))):
        sum += (n//10 ** i) % 10
    return sum

for i in range(1001):
    if i % 7 == 0 and sum_of_digits(i) % 3 == 0:
        numbers.append(i)
    else:
        continue

for num in numbers:
    print(num)