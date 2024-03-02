def main():
    n = int(input())

    hours, minutes, seconds = n // 3600, (n % 3600) // 60, n % 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")


if __name__ == '__main__':
    main()
