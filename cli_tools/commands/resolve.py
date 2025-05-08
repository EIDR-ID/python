# Import necessary types
from argparse import ArgumentParser, Namespace
from rich import print  # Using rich for potentially colored output

# Import SessionManager from the application's manager module
from app.manager import SessionManager


def register(subparsers, interactive: bool = False):
    """
    Registers the 'resolve' subcommand and its associated arguments.

    This function sets up the command-line interface for resolving an EIDR ID.
    It defines the necessary arguments like the ID itself and output formatting options.

    Args:
        subparsers: The subparser object obtained from `ArgumentParser.add_subparsers()`.
                    Used to define the 'resolve' sub-command.

    Returns:
        None: Modifies the parser structure in place.
        :param subparsers:
        :param interactive:
    """
    # Create a subparser for the 'resolve' command
    resolve_parser = subparsers.add_parser(
        'resolve',
        help="Resolve an EIDR ID to retrieve its associated metadata."  # More descriptive help
    )

    # --- Required Arguments ---
    # Add the mandatory EIDR ID argument
    resolve_parser.add_argument(
        'id',  # Positional argument
        help="The EIDR ID (e.g., '10.5240/XXXX-XXXX-XXXX-XXXX-XXXX-C') to resolve."
    )

    # --- Optional Arguments ---
    # Option to specify the output format
    resolve_parser.add_argument(
        "--format",
        help="Format for displaying or saving the resolved data.",
        choices=["json", "xml", "std_out"],  # Available output formats
        default="std_out",  # Default format is standard output text
        required=False,  # Option is not mandatory
    )
    # Option to specify an output file path
    resolve_parser.add_argument(
        "--output",
        required=False,  # Option is not mandatory
        help="Path to a file where the resolved data should be saved. If omitted, results are printed to standard output (respecting --format).",
    )

    # Set the default function to be called when the 'resolve' command is used
    resolve_parser.set_defaults(func=handle)


def handle(args: Namespace, session_manager: SessionManager):
    """
    Handles the execution of the 'resolve' command.

    Retrieves the EIDR ID from the parsed arguments, uses the SessionManager
    to resolve it, and then prints the result to standard output or potentially
    saves it based on format/output args (though current implementation only prints).

    Args:
        args (Namespace): An object containing the parsed command-line arguments,
                          including the EIDR 'id' and format/output options.
        session_manager (SessionManager): An instance used to interact with the
                                          EIDR registry or backend system.

    Returns:
        None: This function primarily produces output via printing or potentially
              calling an output helper function.
    """
    # Extract the EIDR ID from the arguments
    eidr_id_to_resolve = args.id

    # Use the session manager to perform the resolution
    # It's assumed session_manager.resolve returns the resolved data structure/object
    # The exact format of 'result' depends on the SessionManager implementation
    print(args)
    result = session_manager.resolve(eidr_id_to_resolve)

    # --- Output Handling ---
    # Basic implementation: print directly using rich
    # TODO: Integrate with a more robust output function (like output_query from the previous example)
    #       to handle different formats (json, xml) and file output (--output).
    if args.output or args.format != "std_out":
        # Placeholder: Call a dedicated output function if format is not std_out or output file is specified
        # output_query(args, result) # Assuming output_query handles formatting and file writing
        # Temporary fallback if output_query isn't implemented/used here:
        if args.output:
            print(
                f"[yellow]Warning:[/yellow] File output (--output) or specific formatting (--format {args.format}) requested, but only basic printing is implemented here. Result for ID {eidr_id_to_resolve}:")
            print(result)  # Print raw result
        else:
            # If format is json/xml but no output file, could potentially print formatted string
            # For now, just print raw result
            print(
                f"[yellow]Warning:[/yellow] Formatting (--format {args.format}) requested, but only basic printing is implemented here. Result for ID {eidr_id_to_resolve}:")
            print(result)

    else:
        # Default behavior: print to stdout using rich format
        print(f"[green]✅ Resolved Data for {eidr_id_to_resolve}:[/green]")
        # Printing the raw result object. Rich might pretty-print it depending on the object type.
        print(result)
