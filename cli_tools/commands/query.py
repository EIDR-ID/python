from typing import Dict

from InquirerPy import inquirer
from rich import print
from argparse import ArgumentParser, Namespace, ArgumentTypeError
from cli_tools.commands.common import *
from cli_tools.commands.resolve import handle
from app.manager import (
    SessionManager,
    Query,
    ServiceQuery,
    PartyQuery,
    RegistryRequest,
)

results = []


# Helper function to convert string arguments to boolean
def str_to_bool(value):
    """Converts a string representation of truth to true, and false to false.
    Raises ArgumentTypeError if the value is not a recognized boolean string.
    """
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError(f"Boolean value expected, got: {value}")


base_object_query_args = {
    'structural_type': {
        'help': "Filter by the structural type of the object.",
        'choices': ["Abstraction", "Performance", "Digital", "Physical"]
    },
    'mode': {
        'help': "Filter by the mode of the object (e.g., how it's experienced).",
        'choices': ["Visual", "AudioVisual", "Audio", "Other"]
    },
    'referent_type': {
        'help': "Filter by the type of the referent."
    },
    'resource_name': {
        'help': "Filter by the primary resource name."
    },
    'alternate_resource_name': {
        'help': "Filter by an alternative resource name."
    },
    'original_language': {
        'help': "Filter by the original language of the resource."
    },
    'dubbed_language': {
        'help': "Filter by a language the resource is dubbed into."
    },
    'associated_org': {
        'help': "Filter by an associated organization (e.g., by ORG ID)."
    },
    'release_date': {
        'help': "Filter by the release date (e.g., 'YYYY-MM-DD')."
    },
    'country_of_origin': {
        'help': "Filter by the country of origin (e.g., 'US', 'GB')."
    },
    'status': {
        'help': "Filter by the status of the resource (e.g., 'Active', 'Deprecated')."
    },
    'approximate_length': {
        'help': "Filter by the approximate length or duration."
    },
    'alternate_id': {
        'help': "Filter by an alternative identifier (e.g., ISAN, EIDR)."
    },
    'display_name': {
        'help': "Filter by the display name."
    },
    'credits': {
        'help': "Filter based on credits information."
    },
    'registrant_extra': {
        'help': "Filter based on extra information provided by the registrant."
    },
    'description': {
        'help': "Filter by text within the object's description."
    }
}

party_query_args = {
    'id': {
        'help': "Filter by the party's unique identifier."
    },
    'display_name': {
        'help': "Filter by the party's display name."
    },
    'sort_name': {
        'help': "Filter by the party's sortable name."
    },
    'organization_id': {
        'help': "Filter by the associated organization's ID (if applicable)."
    },
    'id_type': {
        'help': "Filter by the type of identifier used (e.g., 'EIDRPartyID', 'ORCID')."
    },
    'alternate_party_name': {
        'help': "Filter by an alternative name for the party."
    },
    'contact_name': {
        'help': "Filter by the name of the contact person."
    },
    'primary_email': {
        'help': "Filter by the primary email address."
    },
    'alternate_email': {
        'help': "Filter by an alternative email address."
    },
    'contact_address': {
        'help': "Filter by the contact address information."
    },
    'contact_phone': {
        'help': "Filter by the contact phone number."
    },
    'active': {
        'help': "Filter by the active status of the party (e.g., 'true', 'false', 'yes', 'no').",
        'type': str_to_bool,  # Use the custom boolean type converter
        'metavar': 'BOOLEAN'  # Shows <BOOLEAN> in help instead of the function name
    },
    'party_account_name': {
        'help': "Filter by the party's account name within a system."
    },
    'allowed_roles': {
        'help': "Filter by roles the party is allowed to have."
    }
}

service_query_args = {
    'id': {
        'help': "Filter by service ID."
    },
    'display_name': {
        'help': "Filter by the service's display name."
    },
    'alternate_service_name': {
        'help': "Filter by an alternative name for the service."
    },
    'description': {
        'help': "Filter by text within the service description."
    },
    'other_affiliation': {
        'help': "Filter by other affiliations associated with the service."
    },
    'active': {
        'help': "Filter by the active status of the service (e.g., 'true', 'false', 'yes', 'no').",
        'type': str_to_bool,
        'metavar': 'BOOLEAN'
    },
    'primary_time_zone': {
        'help': "Filter by the primary time zone of the service (e.g., 'UTC', 'America/New_York')."
    },
    'region': {
        'help': "Filter by the geographical region of the service."
    },
    'primary_audio_language': {
        'help': "Filter by the primary audio language supported by the service (e.g., 'en', 'es')."
    },
    'delivery_model': {
        'help': "Filter by the delivery model of the service (e.g., 'Streaming', 'Download')."
    }
}



def handle_query(args: Namespace, session_manager: SessionManager, interactive=False):
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
    #  If running interactively, prompt for missing values
    interactive_check(interactive,args=args,query_args=base_object_query_args)
    filtered_args = filter_args(args, Query.base_obj_expression)
    print(args, filtered_args)
    # Construct the specific query expression using provided arguments
    query_expression = Query.base_obj_expression(**filtered_args)
    # Create the main Query object, including the expression and pagination settings
    q = Query(
        expression=query_expression,
        page_num=args.page_num,
        page_size=args.page_size,
    )
    # Package the query into a RegistryRequest (assuming this structure is required)
    request = RegistryRequest(operations=[q])
    # Execute the query using the session manager
    # The `_` suggests the second return value (e.g., status code, metadata) is ignored here.
    result, _ = session_manager.query(request)

    # Pass the results and arguments to the output handler

    results.extend(query.as_dict() for query in result)
    output_query(args, result)
    new_page(args, session_manager)
    return result


def handle_service_query(args: Namespace, session_manager: SessionManager, interactive=False):
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
    interactive_check(interactive,args=args,query_args=service_query_args)
    filtered_args = filter_args(args, ServiceQuery.service_expression)
    print(args, filtered_args)
    # Construct the specific service query expression
    query_expression = ServiceQuery.service_expression(**filtered_args)
    # Create the ServiceQuery object with expression and pagination
    query = ServiceQuery(
        page_number=args.page_num,  # Note: Parameter name might differ (page_number vs page_num)
        page_size=args.page_size,
        expression=query_expression
    )
    # Execute the service-specific query using the session manager
    result = session_manager.service_query(query)

    # Output the results
    output_query(args, result)
    return result


def handle_party_query(args: Namespace, session_manager: SessionManager, interactive=False):
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
    #  If running interactively, prompt for missing values
    interactive_check(interactive,args=args,query_args=party_query_args)
    expression_args = filter_args(args, PartyQuery.party_expression)
    print(args,expression_args)
    # Construct the specific party query expression
    query_expression = PartyQuery.party_expression(**expression_args)

    # Create the PartyQuery object with expression and pagination
    query = PartyQuery(
        expression=query_expression,
        page_size=args.page_size,
        page_number=args.page_num  # Note: Parameter name might differ (page_number vs page_num)
    )

    # Execute the party-specific query using the session manager
    result = session_manager.party_query(query)

    # Output the results
    output_query(args, result)
    return result


def register(subparsers, interactive=False):
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
        help="Construct and execute a query for BaseObjectData."  # More descriptive help
    )

    # Register arguments specific to BaseObjectData queries
    register_args(query_parser, base_object_query_args)
    # Add the common options (format, output, pagination) to this subparser
    add_common_options(query_parser)
    # Set the function to call when the 'query' command is used
    query_parser.set_defaults(func=handle_query)

    # --- Service Query Subcommand ---
    service_parser = subparsers.add_parser(
        'service_query',
        help="Construct and execute a query for Service objects."
    )
    # Create a subparser for the 'service_query' command
    # Register arguments specific to Service queries
    register_args(service_parser, service_query_args)
    # Add the common options to this subparser
    add_common_options(service_parser)
    # Set the function to call when the 'service_query' command is used
    service_parser.set_defaults(func=handle_service_query)

    # --- Party Query Subcommand ---
    party_parser = subparsers.add_parser(
        'party_query',
        help="Construct and execute a query for Party objects."
    )
    # Create a subparser for the 'party_query' command
    # Register arguments specific to Party queries
    register_args(party_parser, party_query_args)
    # Add the common options to this subparser
    add_common_options(party_parser)
    # Set the function to call when the 'party_query' command is used
    party_parser.set_defaults(func=handle_party_query)


def output_query(args,result):
    if args.format == "std_out":
        for query_index, query in enumerate(results):
            page_offset = args.page_size * (args.page_num - 1)
            print(f"""[cyan]\nQuery Result {(query_index + 1) + page_offset}:[/cyan]""")
            for key, value in query.items():
                print(f"[green]{key}:[/green] {value}")



def new_page(args, session_manager: SessionManager):
    """
    Prompts the user to choose between 'Next Page' and 'Resolve', then enter a number.
    Updates args.page_num and re-calls the selected function with updated args.
    """
    while True:
        try:
            action = inquirer.select(
                message="Choose action:",
                choices=["Page", "Resolve"],
            ).execute()

            user_input = inquirer.number(
                message=f"Enter number for {action}:",
            ).execute()

            if not user_input or int(user_input) <= 0:
                print("Please enter a number greater than 0.")
                continue

            user_input = int(user_input)
            print(results)
            if action == "Page":
                args.func(args, session_manager)
            elif action == "Resolve":
                query = results[user_input - 1]
                args.id = query['id']
                handle(args, session_manager)

            break  # Exit after successful run

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")
            raise e
