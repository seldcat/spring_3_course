import sys
from typing import Generator


def repeating_generator() -> Generator[str, str, None]:
    count: int = 1
    received_string: str = ''
    while True:
        received_string = yield received_string
        if received_string:
            received_string *= count
        count += 1


def main():
    generator = repeating_generator()
    next(generator)
    for line in sys.stdin:
        print(generator.send(line.strip()))


if __name__ == "__main__":
    main()
