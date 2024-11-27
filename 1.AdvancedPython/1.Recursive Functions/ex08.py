# The tribonacci numbers are like the Fibonacci numbers, but instead of starting with two predetermined terms, the sequence starts with three predetermined terms and each term afterwards is the sum of the preceding three terms. The first few tribonacci numbers are:

# 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, ...
# The tetranacci numbers start with four predetermined terms, each term afterwards being the sum of the preceding four terms. The first few tetranacci numbers are:

# 0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490, 2872, 5536, 10671, 20569, 39648, ...
# This continues in the same way for pentanacci, hexanacci, heptanacci, octanacci, and so on.

# Write a function for the tribonacci and tetranacci numbers.

def get_k_fibonacci(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    return sum(get_k_fibonacci(n-i, k) for i in range(1, k+1))

print(get_k_fibonacci(10, 3)) # 44
# 0, 0, 1, 1, 2, 4, 7, 13, 24, 44
print(get_k_fibonacci(10, 4)) # 29
# 0, 0, 0, 1, 1, 2, 4, 8, 15, 29