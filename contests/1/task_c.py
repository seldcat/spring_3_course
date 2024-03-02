import sys


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    for line in sys.stdin:
        n = int(line)
        if is_prime(n):
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")


if __name__ == '__main__':
    main()
