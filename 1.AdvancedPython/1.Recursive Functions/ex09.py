# What if somebody wants to check the parameters in a recursive function? For example the factorial function. Okay, please write a recursive version of factorial, which checks the parameters. Maybe you did it in a perfect way, but maybe not. Can you improve your version? Get rid of unnecessary tests?

def get_factorial(n):
    def inner_get_factorial(n):
        if n == 1:
            return 1
        return n * inner_get_factorial(n-1)
    if n < 0 or int(n) != n:
        raise ValueError("The number must be non-negative and integer.")
    if n == 0:
        return 1
    return inner_get_factorial(n)

print(get_factorial(5)) # 120
print(get_factorial(0)) # 1
print(get_factorial(-1)) # ValueError: The number must be non-negative and integer.