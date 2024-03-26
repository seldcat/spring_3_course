import json
import sys
from typing import Iterable, TextIO, TypeVar, Dict

Record = Dict[str, str]
T = TypeVar('T')


def read_tsv(file: TextIO) -> Iterable[Record]:
    header = file.readline().strip().split('\t')
    for line in file:
        values = line.strip().split('\t')
        yield dict(zip(header, values))


def make_batches(iterable: Iterable[T], n: int) -> Iterable['list[T]']:
    batch: list[T] = []
    for item in iterable:
        batch.append(item)
        if len(batch) == n:
            yield batch
            batch = []
    if batch:
        yield batch


def main() -> None:
    with open(sys.argv[1], 'r') as file:
        records = read_tsv(file)

        batches = make_batches(records, 4)

        for batch in batches:
            print(json.dumps(batch))


if __name__ == '__main__':
    main()
