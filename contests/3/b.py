from typing import Generator


def generate_binary_sets(n: int) -> Generator['list[int]', None, None]:
    if n == 0:
        yield []
    else:
        for bit in generate_binary_sets(n - 1):
            yield bit + [0]
            yield bit + [1]


def main() -> None:
    n: int = int(input())
    for binary_set in generate_binary_sets(n):
        print('(' + ', '.join(map(str, binary_set)) + ')')


if __name__ == '__main__':
    main()
