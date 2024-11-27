# The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
# 1
# 1     1
# 1     2       1
# 1     3       3       "1"
# 1     4       "6"     4       1
# 1     "5"     10      10      5       1
# "1"   6       15      20      15      6       1
# Write a recursive program to calculate the Fibonacci numbers, using Pascal's triangle.

def solve(n, fib_pos):
    if n == 1:
        return ([1], 1 if fib_pos == 1 else 0)
    prev_line, cur_sum = solve(n-1, fib_pos)
    new_line = [1]
    for i in range(len(prev_line)-1):
        new_line.append(prev_line[i] + prev_line[i+1])
    new_line.append(1)
    if fib_pos - n < n:
        cur_sum += new_line[fib_pos - n]
    return (new_line, cur_sum)

n = int(input())
for i in range(n):
    print(solve(i+1, i+1)[1])

# INPUT
# 10
# OUTPUT
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55