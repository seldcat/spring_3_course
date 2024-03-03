import json


def list_to_dict(input_list: list[str]) -> dict[str, str]:
    return {element: str(int(element)**2)
            for element in input_list if element.isdigit()}


def main():
    print(json.dumps(list_to_dict(json.loads(input())), ensure_ascii=False))


if __name__ == '__main__':
    main()
