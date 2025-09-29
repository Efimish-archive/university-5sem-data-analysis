import sys
sys.setrecursionlimit(100000000)
from functools import cache

@cache
def ways(n, lowest = 9999):
    result = 0

    for i in [1, 2, 5, 10]:
        if i <= lowest:
            if n - i == 0:
                result += 1
            elif n - i > 0:
                result += ways(n - i, i)

    return result

print(ways(int(input())))
