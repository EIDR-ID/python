from rich import print
from app.manager import (
    SessionManager,
    Query,
    ServiceQuery,
    PartyQuery,
    RegistryRequest,
)
from argparse import ArgumentParser, Namespace


def register_service_query(parser: ArgumentParser):
    """
    Registers command-line arguments specific to querying Service objects.

    This function defines optional arguments that correspond to the attributes
    of a Service object, allowing users to filter service queries based on these criteria.

    Args:
        parser (ArgumentParser): The argparse parser to which the arguments will be added.
            This is typically a subparser dedicated to service queries.
    """
    # Add arguments corresponding to Service object attributes
    parser.add_argument('--id', help="Filter by service ID.")
    parser.add_argument('--display_name', help="Filter by the service's display name.")
    parser.add_argument('--alternate_service_name', help="Filter by an alternative name for the service.")
    parser.add_argument('--description', help="Filter by text within the service description.")
    parser.add_argument('--other_affiliation', help="Filter by other affiliations associated with the service.")
    parser.add_argument('--active', help="Filter by the active status of the service (e.g., 'true' or 'false').") # Assuming boolean-like string
    parser.add_argument('--primary_time_zone', help="Filter by the primary time zone of the service (e.g., 'UTC', 'America/New_York').")
    parser.add_argument('--region', help="Filter by the geographical region of the service.")
    parser.add_argument('--primary_audio_language', help="Filter by the primary audio language supported by the service (e.g., 'en', 'es').")
    parser.add_argument('--delivery_model', help="Filter by the delivery model of the service (e.g., 'Streaming', 'Download').")


def register_query(parser: ArgumentParser):
    """
    Registers command-line arguments specific to querying BaseObjectData objects.

    This function defines optional arguments corresponding to the attributes
    of a generic BaseObjectData (or similar core object), allowing users to
    filter queries based on these criteria.

    Args:
        parser (ArgumentParser): The argparse parser to which the arguments will be added.
            This is typically a subparser dedicated to base object queries.
    """
    # Add arguments corresponding to BaseObjectData attributes
    parser.add_argument('--structural_type', choices=["Abstraction", "Performance", "Digital", "Physical"], help="Filter by the structural type of the object.")
    parser.add_argument('--mode', choices=["Visual", "AudioVisual", "Audio", "Other"], help="Filter by the mode of the object (e.g., how it's experienced).")
    parser.add_argument('--referent_type', help="Filter by the type of the referent.")
    parser.add_argument('--resource_name', help="Filter by the primary resource name.")
    parser.add_argument('--alternate_resource_name', help="Filter by an alternative resource name.")
    parser.add_argument('--original_language', help="Filter by the original language of the resource.")
    parser.add_argument('--dubbed_language', help="Filter by a language the resource is dubbed into.")
    parser.add_argument('--associated_org', help="Filter by an associated organization (e.g., by ORG ID).")
    parser.add_argument('--release_date', help="Filter by the release date (e.g., 'YYYY-MM-DD').")
    parser.add_argument('--country_of_origin', help="Filter by the country of origin (e.g., 'US', 'GB').")
    parser.add_argument('--status', help="Filter by the status of the resource (e.g., 'Active', 'Deprecated').")
    parser.add_argument('--approximate_length', help="Filter by the approximate length or duration.")
    parser.add_argument('--alternate_id', help="Filter by an alternative identifier (e.g., ISAN, EIDR).")
    parser.add_argument('--display_name', help="Filter by the display name.") # Note: Duplicated in other register functions, potentially context-specific
    parser.add_argument('--credits', help="Filter based on credits information.")
    parser.add_argument('--registrant_extra', help="Filter based on extra information provided by the registrant.")
    parser.add_argument('--description', help="Filter by text within the object's description.")


def register_party_query(parser: ArgumentParser):
    """
    Registers command-line arguments specific to querying Party objects.

    This function defines optional arguments corresponding to the attributes
    of a Party object (representing individuals or organizations), allowing
    users to filter party queries based on these criteria.

    Args:
        parser (ArgumentParser): The argparse parser to which the arguments will be added.
            This is typically a subparser dedicated to party queries.
    """
    # Add arguments corresponding to Party object attributes
    parser.add_argument('--id', help="Filter by the party's unique identifier.")
    parser.add_argument('--display_name', help="Filter by the party's display name.")
    parser.add_argument('--sort_name', help="Filter by the party's sortable name.")
    parser.add_argument('--organization_id', help="Filter by the associated organization's ID (if applicable).")
    parser.add_argument('--id_type', help="Filter by the type of identifier used (e.g., 'EIDRPartyID', 'ORCID').")
    parser.add_argument('--alternate_party_name', help="Filter by an alternative name for the party.")
    parser.add_argument('--contact_name', help="Filter by the name of the contact person.")
    parser.add_argument('--primary_email', help="Filter by the primary email address.")
    parser.add_argument('--alternate_email', help="Filter by an alternative email address.")
    parser.add_argument('--contact_address', help="Filter by the contact address information.")
    parser.add_argument('--contact_phone', help="Filter by the contact phone number.")
    # Use type=bool for boolean flags is often tricky with argparse.
    # Consider using action='store_true'/'store_false' or a choices approach ('true', 'false').
    # Here, we keep the original type=bool but note it might need adjustment depending on desired CLI behavior.
    parser.add_argument('--active', type=bool, help="Filter by the active status of the party (e.g., True/False).")
    parser.add_argument('--party_account_name', help="Filter by the party's account name within a system.")
    parser.add_argument('--allowed_roles', help="Filter by roles the party is allowed to have.")


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
        required=False,     # This option is not mandatory
    )
    # Option to specify an output file path
    parser.add_argument(
        "--output",
        required=False,     # This option is not mandatory
        help="Path to a file where the query results should be saved. If omitted, results go to standard output (respecting --format).",
    )
    # Option to control the number of results per page (pagination)
    parser.add_argument(
        "--page_size",
        help="Maximum number of results to retrieve per page.",
        default=5,          # Default page size
        type=int,           # Expect an integer value
    )
    # Option to specify the desired page number (pagination)
    parser.add_argument(
        "--page_num",
        help="The specific page number of results to retrieve (1-based index).",
        default=1,          # Default to the first page
        type=int,           # Expect an integer value
    )


def handle_query(args: Namespace, session_manager: SessionManager):
    """
    Handles the execution of a BaseObjectData query.

    Constructs a query expression from the command-line arguments,
    creates a Query object with pagination details, sends the query
    using the SessionManager, and outputs the results.

    Args:
        args (Namespace): An object containing the parsed command-line arguments,
                          including filters, pagination, and format options.
        session_manager (SessionManager): An instance used to execute the query
                                          against the registry or backend system.

    Returns:
        None: This function typically triggers output via `output_query` rather
              than returning data directly.
    """
    # Construct the specific query expression using provided arguments
    query_expression = Query.base_obj_expression(
        structural_type=args.structural_type,
        mode=args.mode,
        referent_type=args.referent_type,
        resource_name=args.resource_name,
        alternate_resource_name=args.alternate_resource_name,
        original_language=args.original_language,
        dubbed_language=args.dubbed_language,
        associated_org=args.associated_org,
        release_date=args.release_date,
        country_of_origin=args.country_of_origin,
        status=args.status,
        approximate_length=args.approximate_length,
        alternate_id=args.alternate_id,
        display_name=args.display_name,
        credits=args.credits,
        registrant_extra=args.registrant_extra,
        description=args.description,
    )

    # Create the main Query object, including the expression and pagination settings
    q = Query(
        expression=query_expression,
        page_num=args.page_num,
        page_size=args.page_size,
    )

    # Package the query into a RegistryRequest (assuming this structure is required)
    request = RegistryRequest(
        operations=[q] # Embed the query within the request operations list
    )

    # Execute the query using the session manager
    # The `_` suggests the second return value (e.g., status code, metadata) is ignored here.
    result, _ = session_manager.query(request)

    # Pass the results and arguments to the output handler
    output_query(args, result)


def handle_service_query(args: Namespace, session_manager: SessionManager):
    """
    Handles the execution of a Service query.

    Constructs a service query expression from the command-line arguments,
    creates a ServiceQuery object with pagination details, sends the query
    using the SessionManager, and outputs the results.

    Args:
        args (Namespace): An object containing the parsed command-line arguments.
        session_manager (SessionManager): An instance used to execute the query.

    Returns:
        None: Outputs results via `output_query`.
    """
    # Construct the specific service query expression
    query_expression = ServiceQuery.service_expression(
        id=args.id,
        display_name=args.display_name,
        alternate_service_name=args.alternate_service_name,
        description=args.description,
        other_affiliation=args.other_affiliation,
        active=args.active,
        primary_time_zone=args.primary_time_zone,
        region=args.region,
        primary_audio_language=args.primary_audio_language,
        delivery_model=args.delivery_model,
    )

    # Create the ServiceQuery object with expression and pagination
    query = ServiceQuery(
        page_number=args.page_num, # Note: Parameter name might differ (page_number vs page_num)
        page_size=args.page_size,
        expression=query_expression
    )

    # Execute the service-specific query using the session manager
    result = session_manager.service_query(query)

    # Output the results
    output_query(args, result)


def handle_party_query(args: Namespace, session_manager: SessionManager):
    """
    Handles the execution of a Party query.

    Constructs a party query expression from the command-line arguments,
    creates a PartyQuery object with pagination details, sends the query
    using the SessionManager, and outputs the results.

    Args:
        args (Namespace): An object containing the parsed command-line arguments.
        session_manager (SessionManager): An instance used to execute the query.

    Returns:
        None: Outputs results via `output_query`.
    """
    # Construct the specific party query expression
    query_expression = PartyQuery.party_expression(
        id=args.id,
        display_name=args.display_name,
        sort_name=args.sort_name,
        organization_id=args.organization_id,
        id_type=args.id_type,
        alternate_party_name=args.alternate_party_name,
        contact_name=args.contact_name,
        primary_email=args.primary_email,
        alternate_email=args.alternate_email,
        contact_address=args.contact_address,
        contact_phone=args.contact_phone,
        active=args.active,
        party_account_name=args.party_account_name,
        allowed_roles=args.allowed_roles,
    )

    # Create the PartyQuery object with expression and pagination
    query = PartyQuery(
        expression=query_expression,
        page_size=args.page_size,
        page_number=args.page_num # Note: Parameter name might differ (page_number vs page_num)
    )

    # Execute the party-specific query using the session manager
    result = session_manager.party_query(query)

    # Output the results
    output_query(args, result)


def register(subparsers):
    """
    Registers the main query commands and their respective subcommands/arguments.

    This function sets up the command-line interface structure for different
    types of queries (BaseObjectData, Service, Party) by creating subparsers
    and associating them with specific argument registration functions and handlers.

    Args:
        subparsers: The subparser object obtained from `ArgumentParser.add_subparsers()`.
                    This is used to define distinct sub-commands.

    Returns:
        None: Modifies the parser structure in place.
    """
    # --- Base Object Query Subcommand ---
    # Create a subparser for the 'query' command
    query_parser = subparsers.add_parser(
        'query',
        help="Construct and execute a query for BaseObjectData." # More descriptive help
    )
    # Register arguments specific to BaseObjectData queries
    register_query(query_parser)
    # Add the common options (format, output, pagination) to this subparser
    add_common_options(query_parser)
    # Set the function to call when the 'query' command is used
    query_parser.set_defaults(func=handle_query)

    # --- Service Query Subcommand ---
    # Create a subparser for the 'service_query' command
    service_parser = subparsers.add_parser(
        'service_query',
        help="Construct and execute a query for Service objects."
    )
    # Register arguments specific to Service queries
    register_service_query(service_parser)
    # Add the common options to this subparser
    add_common_options(service_parser)
    # Set the function to call when the 'service_query' command is used
    service_parser.set_defaults(func=handle_service_query)

    # --- Party Query Subcommand ---
    # Create a subparser for the 'party_query' command
    party_parser = subparsers.add_parser(
        'party_query',
        help="Construct and execute a query for Party objects."
    )
    # Register arguments specific to Party queries
    register_party_query(party_parser)
    # Add the common options to this subparser
    add_common_options(party_parser)
    # Set the function to call when the 'party_query' command is used
    party_parser.set_defaults(func=handle_party_query)


def output_query(args, result):
    if args.format == "std_out":
        print(f"[blue]Generated Query:[/blue]\n{result}")
