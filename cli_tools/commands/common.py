from argparse import ArgumentParser, Namespace
from typing import Dict
from InquirerPy import inquirer


def add_common_options(parser: ArgumentParser):
    """
    Adds common command-line options used across different query types.

    These options typically control output formatting, destination, and pagination.

    Args:
        parser (ArgumentParser): The argparse parser (or subparser) to which
            the common options will be added.
    """
    # Option to specify the output format
    parser.add_argument(
        "--format",
        help="Format for displaying the query results.",
        choices=["json", "xml", "std_out"],  # Available output formats
        default="std_out",  # Default format is standard output text
        required=False,  # This option is not mandatory
    )
    # Option to specify an output file path
    parser.add_argument(
        "--output",
        required=False,  # This option is not mandatory
        help="Path to a file where the query results should be saved. If omitted, results go to standard output (respecting --format).",
    )
    # Option to control the number of results per page (pagination)
    parser.add_argument(
        "--page_size",
        help="Maximum number of results to retrieve per page.",
        default=5,  # Default page size
        type=int,  # Expect an integer value
    )
    # Option to specify the desired page number (pagination)
    parser.add_argument(
        "--page_num",
        help="The specific page number of results to retrieve (1-based index).",
        default=1,  # Default to the first page
        type=int,  # Expect an integer value
    )


def interactive_fill_args(arg_defs: Dict[str, dict]) -> Dict[str, str]:
    """
    Interactive prompt loop for filling in args defined in arg_defs.
    arg_defs is a dict like: {"field": {"help": "...", "type": str, ...}}

    Returns: dict of {field_name: user_input}
    """
    args = {}

    while True:
        # Build menu showing filled and unfilled fields
        choices = [
                      f"{key}: {val}" for key, val in args.items()
                  ] + [
                      f"{key}: <empty>" for key in arg_defs if key not in args
                  ] + ["[ Done ]"]

        selected = inquirer.select(
            message="Fill in fields (⏎ to edit):",
            choices=choices,
            cycle=False
        ).execute()

        if selected == "[ Done ]":
            break

        field = selected.split(":")[0]
        field_type = arg_defs[field].get("type", str)
        raw_input = inquirer.text(message=f"Enter {field}:").execute()

        # Optionally cast to correct type
        try:
            args[field] = field_type(raw_input)
        except ValueError:
            print(f"⚠️  Invalid {field_type.__name__}, try again.")
            continue

    return args


def interactive_check(interactive: bool, args: Namespace, query_args: Dict[str, dict]):
    if interactive:
        filled = interactive_fill_args(query_args)
        for key, value in filled.items():
            setattr(args, key, value)


def filter_args(args: Namespace, function_call: callable) -> dict:
    """
    Filter the args based on the definitions provided in arg_defs.
    Only include keys that are present in arg_defs.
    """
    # Get the argument definitions from the function's signature
    arg_defs = function_call.__annotations__
    # Filter the args based on the definitions
    filtered_args = {key: value for key, value in vars(args).items() if key in arg_defs}
    return filtered_args


def register_args(parser: ArgumentParser, args_def: dict):
    """
    Adds arguments to a parser from a shared args definition dictionary.
    """
    for arg_name, arg_params in args_def.items():
        parser.add_argument(f'--{arg_name}', **arg_params)
