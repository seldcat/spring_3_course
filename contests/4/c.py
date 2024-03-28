import random
import string
import sys


def generate_password(length: int, digits: bool = False, uppercase_letters: bool = False, special_symbols: bool = False) -> str:
    symbols = string.ascii_lowercase
    if digits:
        symbols += string.digits
    if uppercase_letters:
        symbols += string.ascii_uppercase
    if special_symbols:
        symbols += string.punctuation

    min_length = 1 + int(digits) + int(uppercase_letters) + int(special_symbols)
    if length < min_length:
        raise ValueError("Not enough length")

    password = random.choice(string.ascii_lowercase)
    if digits:
        password += random.choice(string.digits)
    if uppercase_letters:
        password += random.choice(string.ascii_uppercase)
    if special_symbols:
        password += random.choice(string.punctuation)

    remaining_length = length - min_length
    password += ''.join(random.choices(symbols, k=remaining_length))

    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)


def main():
    exec(sys.stdin.read())


if __name__ == '__main__':
    main()
