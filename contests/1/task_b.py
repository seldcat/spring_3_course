from typing import Tuple


def length(x: Tuple[float, float], y: Tuple[float, float]) -> float:
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5


def main():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())

    a = length((x1, y1), (x2, y2))
    b = length((x1, y1), (x3, y3))
    c = length((x3, y3), (x2, y2))

    semi_p = (a + b + c) / 2
    area = (semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))**0.5

    print(f"The area of the triangle is {area:.2f}")


if __name__ == '__main__':
    main()
