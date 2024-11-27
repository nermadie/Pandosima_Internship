# Write a recursive function fib_indexfib(), which returns the index of a number in the Fibonacci sequence, if the number is an element of this sequence, and returns -1 if the number is not contained in it, i.e.
# fib(fib_index(n)) => n

def fib(n):
    if n == 1 or n == 2:
        return 1
    prev, cur = 1, 1
    for i in range(n-2):
        prev, cur = cur, prev + cur
    return cur

def fib_index(n, start=0):
    if fib(start) == n:
        return start
    if fib(start) > n:
        return -1
    return fib_index(n, start+1)


print(fib(10)) # 55
print(fib_index(55)) # 10