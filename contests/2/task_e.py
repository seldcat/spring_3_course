import json
import copy
import sys

RecursiveDict = dict[str, 'int | RecursiveDict']


def modify_config(
        original_config: RecursiveDict,
        modifications: list[str]
) -> list[RecursiveDict]:

    modified_configs: list[RecursiveDict] = []

    for modification in modifications:
        current_config: RecursiveDict = copy.deepcopy(original_config)

        path, value = modification.split()
        keys = path.split('/')

        current_dict: RecursiveDict = current_config
        for key in keys[:-1]:
            if key not in current_dict:
                current_dict[key] = {}
            current_dict = current_dict[key]

        current_dict[keys[-1]] = int(value)
        modified_configs.append(current_config)

    return modified_configs


def main():
    lines: list[str] = []
    for line in sys.stdin:
        lines.append(line.strip())

    original_config: RecursiveDict = json.loads(lines[0])
    modifications: list[str] = lines[1:]

    for config in modify_config(original_config, modifications):
        print(json.dumps(config, ensure_ascii=False))


if __name__ == '__main__':
    main()
