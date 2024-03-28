import re
import sys


def main():
    content = sys.stdin.read()
    replaced_content = re.sub(r'CalcDistance\(([^,]+),(\s*)([^,]+),(\s*)([^,]+),(\s*)([^)]+)\)',
                              r'GeoDistance(\1,\2\5,\4\3,\6\7)',
                              content)
    print(replaced_content)


if __name__ == '__main__':
    main()
