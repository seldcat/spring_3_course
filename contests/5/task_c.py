from enum import Enum


class Cell(Enum):
    EMPTY = '.'
    NO_TREASURE = 'X'
    TREASURE = '$'

    def __str__(self) -> str:
        return self.value


class Model:
    def __init__(self) -> None:
        self.map: list[list[Cell]] = []
        self.treasures: set[tuple[int, int]] = set()

    def initialize(self, n: int, m: int) -> None:
        self.map = [[Cell.EMPTY for _ in range(m)] for _ in range(n)]

    def add_treasure(self, x: int, y: int) -> None:
        self.treasures.add((x, y))

    def examine(self, x: int, y: int) -> None:
        if (x, y) in self.treasures:
            self.map[x][y] = Cell.TREASURE
        else:
            self.map[x][y] = Cell.NO_TREASURE


class View:
    @staticmethod
    def print(map_data: list[list[Cell]]) -> None:
        for row in map_data:
            print(''.join(str(cell) for cell in row))
        print()


class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()

    def read_map(self) -> None:
        n, m = map(int, input().split())
        self.model.initialize(n, m)
        for _ in range(int(input())):
            x, y = map(int, input().split())
            self.model.add_treasure(x, y)

    def do_examinations(self) -> None:
        for _ in range(int(input())):
            x, y = map(int, input().split())
            self.model.examine(x, y)
            self.view.print(self.model.map)


def main() -> None:
    controller = Controller()
    controller.read_map()
    controller.do_examinations()


if __name__ == '__main__':
    main()
