import sys
from typing import Callable, ParamSpec


P = ParamSpec('P')


def decorator(out: str) -> Callable[..., object]:
    def inner_decorator(func: Callable[P, object]) -> Callable[P, object]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> object:
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
