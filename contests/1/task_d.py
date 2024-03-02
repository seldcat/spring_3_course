import sys
from math import log


def gcd(a: int, b: int) -> int:
    # greatest common divisor
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    # least common multiple of two numbers
    return a * b // gcd(a, b)


def calc(*args: int, **kwargs) -> int:
    base = kwargs.get('log', 0)

    result_lcm = args[0]
    for number in args[1:]:
        result_lcm = lcm(result_lcm, number)

    return log(result_lcm, base) if base else result_lcm


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
