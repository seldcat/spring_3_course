import os


def main():
    root_path = input()
    dir1_name = input()
    dir2_name = input()

    print(os.path.join(root_path, dir1_name, dir2_name))


if __name__ == '__main__':
    main()
