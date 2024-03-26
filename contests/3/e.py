import json
import sys
from itertools import groupby
from typing import Callable, Iterable, Tuple

Record = dict[str, str]
Records = Iterable[Record]
Mapper = Callable[[Record], Iterable[Tuple[str, int]]]
Reducer = Callable[[str, Iterable[int]], int]


def map_reduce(
    records: Records,
    key: str,
    mapper: Mapper,
    reducer: Reducer
) -> 'list[Tuple[str, int]]':
    mapped_records = (mapper(record) for record in records)
    flattened_mapped_records = (item for sublist in mapped_records for item in sublist)
    sorted_mapped_records = sorted(flattened_mapped_records, key=lambda x: x[0])
    grouped_records = groupby(sorted_mapped_records, key=lambda x: x[0])
    reduced_records = ((key, reducer(key, (record[1] for record in records))) for key, records in grouped_records)
    return list(reduced_records)


def mapper(record: Record) -> Iterable[Tuple[str, int]]:
    words = record['data'].split()
    weight = int(record['weight'])
    for word in words:
        yield word, weight


def reducer(key: str, weights: Iterable[int]) -> int:
    return sum(weights)


def main() -> None:
    records: list[dict[str, str]] = []
    for line in sys.stdin:
        record: dict[str, str] = json.loads(line.strip())
        records.append(record)

    result = map_reduce(records, 'data', mapper, reducer)

    for word, total_weight in result:
        print(f'{word} {total_weight}')


if __name__ == '__main__':
    main()
