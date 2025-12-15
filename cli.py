# cli.py

from parser import parse_sql, SQLParserError
from engine import execute_query, SQLEngineError


def print_result(result):
    if isinstance(result, int):
        print("\nCOUNT")
        print("-----")
        print(result)
        return

    if not result:
        print("No results found")
        return

    headers = result[0].keys()
    print("\n" + "  ".join(headers))
    print("-" * 30)
    for row in result:
        print("  ".join(str(v) for v in row.values()))


def main():
    print("Mini SQL Engine (type 'exit' to quit)")
    while True:
        query = input("\nsql> ")
        if query.lower() in ("exit", "quit"):
            break
        try:
            parsed = parse_sql(query)
            result = execute_query(parsed)
            print_result(result)
        except (SQLParserError, SQLEngineError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
