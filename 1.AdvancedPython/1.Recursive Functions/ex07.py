# The sum of the squares of two consecutive Fibonacci numbers is also a Fibonacci number, e.g. 2 and 3 are elements of the Fibonacci sequence and 22 + 33 = 13 corresponds to Fib(7).Use the previous function to find the position of the sum of the squares of two consecutive numbers in the Fibonacci sequence.

# Mathematical explanation: Let a and b be two successive Fibonacci numbers with a prior to b. The Fibonacci sequence starting with the number "a" looks like this:

#     0              a
#     1              b
#     2          a + b
#     3     a + 2b
#     4    2a + 3b
#     5        3a + 5b
#     6        5a + 8b
# We can see that the Fibonacci numbers appear as factors for a and b. The n-th element in this sequence can be calculated with the following formula:

# Fib(n) = Fib(n-1) * a + Fib(n) * b

# From this we can conclude that for a natural number n, n>1, the following holds true:

# Fib(n-1) * a + Fib(n) * b = Fib(2n-1)