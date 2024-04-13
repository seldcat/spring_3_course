import sys
from typing import Literal

BooleanVector = list[Literal[0, 1]]


class BooleanFunction:
    def __init__(self, truth_table: BooleanVector):
        if not self._power_of_two(len(truth_table)):
            raise ValueError('Truth table length is not a power of two')

        self.truth_table = truth_table
        self.arity = self._calculate_arity(truth_table)

    @staticmethod
    def _power_of_two(n: int) -> bool:
        return n > 1 and (n & (n - 1) == 0)

    @staticmethod
    def _calculate_arity(v: BooleanVector) -> int:
        return len(v).bit_length() - 1

    def __str__(self) -> str:
        variables = ', '.join([f'x{i}' for i in range(1, self.arity + 1)])
        return f'f({variables}) = {tuple(self.truth_table)}'

    def __call__(self, args: BooleanVector) -> int:
        if len(args) != self.arity:
            raise ValueError('Arity mismatch')
        index: int = int(''.join(map(str, args)), 2)
        return self.truth_table[index]

    def __add__(self, other: 'BooleanFunction') -> 'BooleanFunction':
        if self.arity != other.arity:
            raise ValueError('Arity mismatch')
        xor_table: BooleanVector = [(a + b) % 2 for a, b in zip(self.truth_table, other.truth_table)]
        return BooleanFunction(xor_table)

    def __mul__(self, other: 'BooleanFunction') -> 'BooleanFunction':
        if self.arity != other.arity:
            raise ValueError('Arity mismatch')
        mul_table: BooleanVector = [a * b for a, b in zip(self.truth_table, other.truth_table)]
        return BooleanFunction(mul_table)


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
