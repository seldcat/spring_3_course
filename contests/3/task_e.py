import json
import sys
from itertools import groupby
from typing import Any, Callable, Iterable

Record = dict[Any, Any]
Records = Iterable[Record]
Mapper = Callable[[Record], Iterable[tuple[Any, Any]]]
Reducer = Callable[[Any, Iterable[int]], int]


def map_reduce(
    records: Records,
    key: str,
    mapper: Mapper,
    reducer: Reducer
) -> 'list[tuple[Any, int]]':
    mapped_records = (mapper(record) for record in records)
    flattened_mapped_records = (item for sublist in mapped_records for item in sublist)
    sorted_mapped_records = sorted(flattened_mapped_records, key=lambda x: x[0])
    grouped_records = groupby(sorted_mapped_records, key=lambda x: x[0])
    reduced_records = ((key, reducer(key, (record[1] for record in records))) for key, records in grouped_records)
    return list(reduced_records)


def mapper(record: Record) -> Iterable[tuple[Any, int]]:
    words = record['data'].split()
    weight = int(record['weight'])
    for word in words:
        yield word, weight


def reducer(key: Any, weights: Iterable[int]) -> int:
    return sum(weights)


def main() -> None:
    records: list[dict[str, str]] = []
    for line in sys.stdin:
        record: dict[str, str] = json.loads(line.strip())
        records.append(record)

    result = map_reduce(records, 'data', mapper, reducer)

    for word, total_weight in result:
        print(f"{word} {total_weight}")


if __name__ == "__main__":
    main()