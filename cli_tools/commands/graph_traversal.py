# Import necessary types
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from rich import print as rprint  # Using rich for potentially colored output
from app.manager import SessionManager, ResponseReader
from app.services.graph_traversal import GraphTraversal

# Define available traversal types based on GraphTraversal methods
# Excludes video_service methods for simplicity here, could be added
AVAILABLE_TRAVERSALS = [
    'find_ancestors',
    'get_remotest_ancestor',
    'find_descendants',
    'get_leaf_descendants',
    'get_lightweight_relationships',
    'get_dependants',
    'get_children',
    'get_parent',
    'get_series_ancestry',
]

# Help text explaining filters
FILTER_HELP = """
Optional filters (only apply to 'find_ancestors' and 'find_descendants'):
  --referent_type_filter REF_TYPE [REF_TYPE ...]
                        Filter results by one or more Referent Types.
  --relationship_type_filter REL_TYPE [REL_TYPE ...]
                        Filter results by one or more Relationship Types.
  --structural_type_filter STRUCT_TYPE [STRUCT_TYPE ...]
                        Filter results by one or more Structural Types.
  --extended_family     Include extended family (only for 'find_descendants').
"""


def register(subparsers, interactive: bool = False):
    """
    Registers the 'traverse' subcommand for performing graph traversals on EIDR IDs.

    This sets up the command-line interface for various graph traversal operations,
    allowing specification of the starting ID, the type of traversal, optional filters,
    and output formatting.

    Args:
        subparsers: The subparser object from `ArgumentParser.add_subparsers()`.

    Returns:
        None: Modifies the parser structure in place.
    """
    # Create a subparser for the 'traverse' command with RawTextHelpFormatter
    # to preserve the formatting of the epilog (filter help)
    traverse_parser = subparsers.add_parser(
        'traverse',
        help="Perform graph traversal operations starting from an EIDR ID.",
        formatter_class=RawTextHelpFormatter,  # Keep filter help formatting
        epilog=FILTER_HELP  # Add filter explanation at the end of help msg
    )

    # --- Required Arguments ---
    traverse_parser.add_argument(
        'traversal_type',
        choices=AVAILABLE_TRAVERSALS,
        help="The type of graph traversal to perform."
    )
    traverse_parser.add_argument(
        'id',
        help="The starting EIDR ID (e.g., '10.5240/XXXX-...') for the traversal."
    )

    # --- Optional Filter Arguments (Applicable to specific traversals) ---
    # Note: Runtime logic in handle() should ideally check if filters are used
    # with compatible traversal_type values.
    traverse_parser.add_argument(
        '--referent_type_filter',
        nargs='+',  # Expect one or more values
        # type=ReferentType, # Ideally, map strings to your enum/type
        help="Filter by Referent Type(s). (for find_ancestors/descendants)"
    )
    traverse_parser.add_argument(
        '--relationship_type_filter',
        nargs='+',
        # type=RelationshipType,
        help="Filter by Relationship Type(s). (for find_ancestors/descendants)"
    )
    traverse_parser.add_argument(
        '--structural_type_filter',
        nargs='+',
        # type=CreationStructuralType,
        help="Filter by Structural Type(s). (for find_ancestors/descendants)"
    )
    traverse_parser.add_argument(
        '--extended_family',
        action='store_true',  # Boolean flag
        help="Include extended family. (for find_descendants)"
    )

    # --- Optional Output Arguments ---
    traverse_parser.add_argument(
        "--format",
        choices=["json", "xml", "std_out"],
        default="std_out",
        required=False,
        help="Format for displaying or saving the traversal results.",
    )
    traverse_parser.add_argument(
        "--output",
        required=False,
        help="Path to save results. If omitted, prints to standard output.",
    )

    # Set the handler function for the 'traverse' command
    traverse_parser.set_defaults(func=handle)


def handle(args: Namespace, session_manager: SessionManager):
    """
    Handles the execution of the 'traverse' command.

    Instantiates the GraphTraversal service, calls the appropriate traversal method
    based on `args.traversal_type`, and handles the response (printing results
    or errors).

    Args:
        args (Namespace): Parsed command-line arguments.
        session_manager (SessionManager): Instance for interacting with the backend.

    Returns:
        None: Prints results or errors to standard output/file.
    """
    # Instantiate the traversal service, potentially passing the SessionManager
    # or relying on SessionManager to provide a driver/client.
    # The exact instantiation depends on your GraphTraversal design.
    # If GraphTraversal needs the ID upfront, pass args.id. If methods take it, don't pass here.
    try:
        # Assuming GraphTraversal doesn't need the ID in constructor here
        traversal_service = GraphTraversal(driver=session_manager.driver)
        # Alternative if ID is needed at init:
        # traversal_service = GraphTraversal(doi=args.id, session_manager=session_manager)
    except Exception as e:
        rprint(f"[red]Error initializing GraphTraversal service: {e}[/red]")
        return  # Or raise

    # Prepare arguments for the specific traversal method
    traversal_args = {'doi': args.id}

    # Select the method to call based on traversal_type
    method_to_call = getattr(traversal_service, args.traversal_type, None)

    if not method_to_call:
        rprint(f"[red]Error: Unknown traversal type '{args.traversal_type}'[/red]")
        return  # Or raise appropriate error
    # Attach filters to traversal_args if applicable
    attach_filter(args, traversal_args)
    # Add filters only if they are provided and relevant for the selected method
    # (Simplistic check: assumes only find_ancestors/descendants use filters)
    # Call the selected traversal method
    try:
        rprint(f"[blue]Executing traversal:[/blue] {args.traversal_type} for ID {args.id}...")
        result_reader, error = method_to_call(**traversal_args)
        if error is not None:
            rprint(f"[red]Error For{args.id}\nReason: {error}.[/red]")
            return
        results = result_reader.get_simple_metaData()
        rprint(f"[green]Traversal successful! Found {len(results)} results.[/green]")
        for i in range(len(results)):
            rprint(f"[cyan]Result {i + 1}:[/cyan]")
            rprint(results[i])
    except Exception as e:
        rprint(f"[red]An unexpected error occurred during traversal execution: {e}[/red]")


def attach_filter(args, traversal_args):
    if args.traversal_type in ['find_ancestors', 'find_descendants']:
        if args.referent_type_filter:
            traversal_args['referent_type_filter'] = args.referent_type_filter
        if args.relationship_type_filter:
            traversal_args['relationship_type_filter'] = args.relationship_type_filter
        if args.structural_type_filter:
            traversal_args['structural_type_filter'] = args.structural_type_filter
        if args.traversal_type == 'find_descendants' and args.extended_family:
            traversal_args['extended_family'] = True  # Add boolean flag if set

    elif args.referent_type_filter or args.relationship_type_filter or args.structural_type_filter or args.extended_family:
        rprint(
            f"[yellow]Warning:[/yellow] Filter arguments provided but may not be applicable for traversal type '{args.traversal_type}'.")
