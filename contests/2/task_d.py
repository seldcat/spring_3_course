from collections import Counter


def find_repeated_words(sentence: str) -> str:
    words = sentence.lower().split()
    word_counts = Counter(words)

    res = [word for word, count in word_counts.items() if word and count == 2]

    return ' '.join(sorted(res))


def main():
    print(find_repeated_words(input()))


if __name__ == '__main__':
    main()
