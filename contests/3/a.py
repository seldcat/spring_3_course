import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def binomial_coefficient(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n
    if k > n / 2:
        k = n - k
    return binomial_coefficient(n - 1, k) + binomial_coefficient(n - 1, k - 1)


def main() -> None:
    n: int
    k: int
    n, k = map(int, input().split())
    print(binomial_coefficient(n, k))


if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    main()
