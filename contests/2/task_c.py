import string
import json


def get_tokens(input_string: str) -> list[str]:
    tokens: set[str] = set()
    current_token = ''

    for char in input_string:
        if char.isalnum():
            current_token += char
        elif char in string.punctuation:
            if current_token:
                tokens.add(current_token)
                current_token = ''
            tokens.add(char)
        elif current_token:
            tokens.add(current_token)
            current_token = ''

    if current_token:
        tokens.add(current_token)

    sorted_tokens = sorted(tokens)
    return sorted_tokens


def main():
    print(json.dumps(get_tokens(input())))


if __name__ == '__main__':
    main()
