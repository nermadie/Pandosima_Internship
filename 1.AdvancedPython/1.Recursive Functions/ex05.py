# Implement a recursive function in Python for the sieve of Eratosthenes.

# The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created by the ancient Greek mathematician Eratosthenes. The algorithm to find all the prime numbers less than or equal to a given integer n:

# Create a list of integers from two to n: 2, 3, 4, ..., n
# Start with a counter i set to 2, i.e. the first prime number
# Starting from i+i, count up by i and remove those numbers from the list, i.e. 2i, 3i, 4*i, etc..
# Find the first number of the list following i. This is the next prime number.
# Set i to the number found in the previous step
# Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
# All the numbers, which are still in the list, are prime numbers
# You can easily see that we would be inefficient, if we strictly used this algorithm, e.g. we will try to remove the multiples of 4, although they have been already removed by the multiples of 2. So it's enough to produce the multiples of all the prime numbers up to the square root of n. We can recursively create these sets.

def get_primes(n):
    if n <= 1:
        return []
    prev_primes = get_primes(int(n**0.5))
    composite_numbers = set(c for p in prev_primes for c in range(p*2, n+1, p))
    primes = [x for x in range(2, n+1) if x not in composite_numbers]
    return primes

n = int(input())
print(get_primes(n))

# INPUT
# 100
# OUTPUT
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]