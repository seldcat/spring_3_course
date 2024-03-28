import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    subparsers = parser.add_subparsers(dest="mode", help="Mode of operation")

    generate_parser = subparsers.add_parser("generate", help="Generate inverted graphs")
    generate_parser.add_argument("-m", "--model", required=True, choices=["aig", "mig", "xaig", "xmig"], help="Model of inverted graphs")
    generate_parser.add_argument("-n", "--variables", type=int, required=True, help="Number of variables")
    group = generate_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-c", "--complexity", type=int, help="Complexity of the inverted graph")
    group.add_argument("-d", "--depth", type=int, help="Depth of the inverted graph")

    check_parser = subparsers.add_parser("check", help="Check inverted graphs")
    check_parser.add_argument("-a", "--algorithm", choices=["simple", "full"], default="simple", help="Algorithm for checking inverted graphs")
    check_parser.add_argument("circuits", nargs="+", help="Files with inverted graphs to check")

    return parser.parse_args()


print(parse_args())
