def main():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())

    area = abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    print(f'The area of the triangle is {area:.2f}')


if __name__ == '__main__':
    main()
