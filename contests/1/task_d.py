import math
import sys


def calc(*args: int, **kwargs: int) -> float:
    base = kwargs.get('log', 0)
    lcm = math.lcm(*args)
    if base != 0:
        return math.log(lcm, float(base))
    else:
        return lcm


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
