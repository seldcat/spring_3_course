from abc import ABC, abstractmethod
from typing import Callable


class Object:
    def __init__(self, cost: int, income: int, square: int) -> None:
        self.cost = cost
        self.income = income
        self.square = square

    def __str__(self) -> str:
        return f'({self.cost}, {self.income}, {self.square})'


class StrategyBase(ABC):
    @abstractmethod
    def compare(self, obj1: Object, obj2: Object) -> bool:
        pass

    @abstractmethod
    def second_compare(self, obj1: Object, obj2: Object) -> bool:
        pass

    def select(self, objects: list[Object]) -> Object:
        return max(objects, key=lambda obj: obj.cost)


class StrategyIncome(StrategyBase):
    def compare(self, obj1: Object, obj2: Object) -> bool:
        return (obj1.income / obj1.cost) >= (obj2.income / obj2.cost)

    def second_compare(self, obj1: Object, obj2: Object) -> bool:
        strategy = StrategySquare()
        return strategy.compare(obj1, obj2)


class StrategySquare(StrategyBase):
    def compare(self, obj1: Object, obj2: Object) -> bool:
        return (obj1.square / obj1.cost) >= (obj2.square / obj2.cost)

    def second_compare(self, obj1: Object, obj2: Object) -> bool:
        strategy = StrategyIncome()
        return strategy.compare(obj1, obj2)


class Context:
    def __init__(self, strategy: StrategyBase, budget: int, objects: list[Object]) -> None:
        self.strategy = strategy
        self.total_income = 0
        self.total_square = 0
        self.budget = budget
        self.objects = objects

    def set_strategy(self, strategy: StrategyBase) -> None:
        self.strategy = strategy

    def build_objects(self) -> None:
        reasonable_objects = self._find_max_objects(self.strategy.compare, self.objects)

        if len(reasonable_objects) > 1:
            reasonable_objects = self._find_max_objects(self.strategy.second_compare, reasonable_objects)

        selected_object = self.strategy.select(reasonable_objects)

        self.budget = self.budget - selected_object.cost + selected_object.income
        self.total_income += selected_object.income
        self.total_square += selected_object.square

        print(f'Selected: {str(selected_object)}, Money: {self.budget}, Income: {self.total_income}, Square: {self.total_square}')

    def _find_max_objects(self, compare_method: Callable[[Object, Object], bool], objects: list[Object]) -> list[Object]:
        current_max = objects[0]
        for obj in self.objects:
            if (compare_method(obj, current_max) and obj.cost <= self.budget):
                current_max = obj
        return list(filter(lambda obj: obj == current_max, objects))


def main() -> None:
    m, n = map(int, input().split())
    objects = [Object(*map(int, input().split())) for _ in range(n)]

    context = Context(StrategyIncome(), m, objects)

    income_strategy, square_strategy = map(int, input().split())
    for _ in range(income_strategy):
        context.build_objects()

    context.set_strategy(StrategySquare())

    for _ in range(square_strategy):
        context.build_objects()


if __name__ == '__main__':
    main()
