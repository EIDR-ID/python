import argparse
from rich import print
from app.manager import SessionManager
from cli_tools.commands import(
    resolve,
    query,
    graph_traversal,
)

session = SessionManager.from_default()


def main():
    parser = argparse.ArgumentParser(description="🚀EIDR CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    resolve.register(subparsers=subparsers)
    query.register(subparsers=subparsers)
    graph_traversal.register(subparsers=subparsers)

    args = parser.parse_args()
    args.func(args, session)


if __name__ == "__main__":
    main()
