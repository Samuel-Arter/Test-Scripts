import math
from itertools import count


def filters():
    while True:
        try:

            num_1 = int(input("insert a number between 0 and 1000000: ").strip())

            if num_1 in range(0, 1000000):
                break
            else:
                print("cannot enter integer less than 0 or greater than 1000000")

        except ValueError:
            print("only insert numbers")

    while True:
        try:

            num_2 = int(input("insert a number greater than the number previously entered and less then 1000000: "))

            if num_2 in range(num_1 + 1, 1000000):
                break
            else:
                print("integer entered must be greater than previously entered integer")

        except ValueError:
            print("only insert numbers")

    return num_1, num_2


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def sum_primes(num):
    total_sum = 0
    for n in range(2, num):
        if is_prime(n):
            total_sum += n

    return total_sum


def primes_in_range(start, stop):
    prime_list = []
    for n in range(start, stop):
        if is_prime(n):
            prime_list.append(n)

    prime_string = ', '.join(map(str, prime_list))

    return prime_string


def next_prime(n):

    for i in count(n + 1):
        if is_prime(i):
            return i


if __name__ == "__main__":
    num1, num2 = filters()
    print("--"*40)
    print(f"{num1} is prime?: {is_prime(num1)}")
    print(f"the sum of all prime numbers up to {num1} is: {sum_primes(num1)}")
    print(f"the next prime number after {num1} is: {next_prime(num1)}")
    print(f"all the primes sitting in the range {num1} and {num2} are: {primes_in_range(num1, num2)}")
