# Write a recursive Python function that returns the sum of the first n integers. (Hint: The function will be similiar to the factorial function!)
def solve(n, cur_sum):
    if n == 1:
        return 1 + cur_sum
    return solve(n-1, cur_sum + n)

n = int(input())
print(solve(n, 0))

# INPUT
# 5
# OUTPUT
# 15