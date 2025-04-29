from rich import print

from app.manager import SessionManager


def register(subparsers):
    resolve_parser = subparsers.add_parser(
        'resolve',
        help="resolve a EIDR ID"
    )
    resolve_parser.add_argument(
        'id',
        help="EIDR ID to resolve"
    )
    resolve_parser.add_argument(
        "--format",
        help="Format to out put files",
        choices=["json", "xml", "std_out"],
        default="std_out",
        required=False,
    )
    resolve_parser.add_argument(
        "--output",
        required=False,
        help="Path to output results otherwise print to std out",
    )
    resolve_parser.set_defaults(func=handle)


def handle(args, session_manager: SessionManager):
    result = session_manager.resolve(args.id)
    print(f"[green]✅ {result}[/green]")
