import sys
from functools import lru_cache

sys.setrecursionlimit(3333)  # estimated by trial and error

@lru_cache()
def solution(n):
    n = int(n)

    if n <= 2:
        return n - 1

    if n % 2 == 0:
        return solution(n // 2) + 1

    return min(solution(n + 1), solution(n - 1)) + 1
