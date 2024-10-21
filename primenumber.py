import math
from itertools import count


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
    print(next_prime(13))
