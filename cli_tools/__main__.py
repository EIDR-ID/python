import argparse
from rich import print
from app.manager import SessionManager
from cli_tools.commands import (
    resolve,
    query,
    graph_traversal,
)
from InquirerPy import inquirer

session = SessionManager.from_default()


def main():
    # Step 1: peek at the command only (don't register yet)
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("command", nargs="?")  # allow missing
    args, unknown = pre_parser.parse_known_args()

    # Step 2: if missing, prompt user for it
    if not args.command:
        args.command = inquirer.select(
            message="Pick a command to run:",
            choices=['resolve', 'query', 'service_query', 'party_query', 'traverse']
        ).execute()
        interactive = True
    else:
        interactive = False


    # Step 3: build full parser using final interactive value
    parser = build_parser(interactive=interactive)
    args = parser.parse_args([args.command] + unknown)

    # Step 4: run it
    args.func(args, session, interactive=interactive)


def build_parser(interactive=False):
    print(interactive)
    parser = argparse.ArgumentParser(description="🚀 EIDR CLI")
    subparsers = parser.add_subparsers(dest="command", required=False)
    resolve.register(subparsers=subparsers, interactive=interactive)
    query.register(subparsers=subparsers, interactive=interactive)
    graph_traversal.register(subparsers=subparsers, interactive=interactive)
    return parser


if __name__ == "__main__":
    main()
