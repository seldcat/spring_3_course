import sys
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')


def decorator(out: str) -> Callable[..., Callable[P, R]]:
    def inner_decorator(func: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for i, arg in enumerate(args):
                print(f'{i}: {arg}')
            result = func(*args, **kwargs)
            print(f'{out}: {result}')
            return result
        return wrapper
    return inner_decorator


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
