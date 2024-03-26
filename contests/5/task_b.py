import sys
from abc import ABC, abstractmethod


class NormalForm(ABC):
    def __init__(self) -> None:
        self.clauses: list[list[int]] = []

    def add_clause(self, clause: list[int]) -> None:
        for var_num in clause:
            if var_num == 0:
                raise ValueError('Variable number is 0')
        self.clauses.append(clause)

    @staticmethod
    def check_values(values: dict[int, int]) -> None:
        for var_num, value in values.items():
            if var_num < 1:
                raise ValueError('Key is less than 1')
            if value not in {0, 1}:
                raise ValueError('Value should be 0 or 1')

    @abstractmethod
    def __call__(self, values: dict[int, int]) -> int:
        pass


class DNF(NormalForm):
    def __call__(self, values: dict[int, int]) -> int:
        self.check_values(values)
        answer = 0
        for clause in self.clauses:
            clause_answer = 1
            for var_num in clause:
                if abs(var_num) not in values:
                    raise ValueError(f'Variable {abs(var_num)} is not found')
                if var_num > 0:
                    clause_answer &= values[var_num]
                else:
                    clause_answer &= not values[abs(var_num)]
            answer |= clause_answer
        return answer


class CNF(NormalForm):
    def __call__(self, values: dict[int, int]) -> int:
        self.check_values(values)
        answer = 1
        for clause in self.clauses:
            clause_answer = 0
            for var_num in clause:
                if abs(var_num) not in values:
                    raise ValueError(f'Variable {abs(var_num)} is not found')
                if var_num > 0:
                    clause_answer |= values[var_num]
                else:
                    clause_answer |= not values[abs(var_num)]
            answer &= clause_answer
        return answer


if __name__ == '__main__':
    exec(sys.stdin.read())
