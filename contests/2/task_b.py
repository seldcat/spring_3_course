import json
from typing import TypeAlias

RecursiveList: TypeAlias = list['int | RecursiveList']


def expand(data: RecursiveList) -> list[int]:
    result: list[int] = []
    for item in data:
        if isinstance(item, int):
            result.append(item)
        else:
            result.extend(expand(item))

    return result


def main():
    print(expand(json.loads(input())))


if __name__ == '__main__':
    main()
