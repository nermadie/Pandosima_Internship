# Write a function which implements the Pascal's triangle:
# 1
# 1     1
# 1     2     1
# 1     3     3     1
# 1     4     6     4     1
# 1     5     10    10    5    1

def solve(n):
    if n == 1:
        print(1)
        return [1]
    prev_line = solve(n-1)
    new_line = [1]
    for i in range(len(prev_line)-1):
        new_line.append(prev_line[i] + prev_line[i+1])
    new_line.append(1)
    print(' '.join(map(str, new_line)))
    return new_line

n = int(input())
solve(n)

# INPUT
# 6
# OUTPUT
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1