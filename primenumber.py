import math
from itertools import count


def filters():
    while True:
        try:

            integer1 = int(input("insert a number between 0 and 1000000: ").strip())

            if integer1 in range(0, 1000000):
                break
            else:
                print("cannot enter integer less than 0 or greater than 1000000")

        except ValueError:
            print("only insert numbers")

    while True:
        try:

            integer2 = int(input("insert a number greater than the number previously entered and less then 1000000: "))

            if integer2 in range(integer1 + 1, 1000000):
                break
            else:
                print("integer entered must be greater than previously entered integer")

        except ValueError:
            print("only insert numbers")

    return integer1, integer2


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
    integer1, integer2 = filters()
    print("--"*40)
    print(f"{integer1} is prime?: {is_prime(integer1)}")
    print(f"the sum of all prime numbers up to {integer1} is: {sum_primes(integer1)}")
    print(f"the next prime number after {integer1} is: {next_prime(integer1)}")
