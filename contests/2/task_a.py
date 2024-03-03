def resolve_dns_query(dns_database: dict[str, str], query: str) -> str:
    return dns_database.get(query, 'PUSTO')


def main():
    n, m = map(int, input().split())

    dns_database: dict[str, str] = {}
    for _ in range(n):
        domain, ip_address = input().split()
        dns_database[domain] = ip_address

    for _ in range(m):
        print(resolve_dns_query(dns_database, input()))


if __name__ == '__main__':
    main()
