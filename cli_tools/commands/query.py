from rich import print
from app.manager import (
    SessionManager,
    Query,
    ServiceQuery,
    PartyQuery,
    RegistryRequest,
)
from argparse import ArgumentParser


def add_common_options(parser):
    """
    Add common options to the parser.
    :param parser:
    :return:
    """
    parser.add_argument(
        "--format",
        help="Format to output the query",
        choices=["json", "xml", "std_out"],
        default="std_out",
        required=False,
    )
    parser.add_argument(
        "--output",
        required=False,
        help="Path to output the query results",
    )
    parser.add_argument(
        "--page_size",
        help="Number of results per page",
        default=5,
        type=int,
    )
    parser.add_argument(
        "--page_num",
        help="The page to return",
        default=1,
        type=int,
    )


def register_service_query(parser: ArgumentParser):
    """
    Register the service query command and its subcommands.
    :param parser:
    :return:
    """
    parser.add_argument('--id')
    parser.add_argument('--display_name')
    parser.add_argument('--alternate_service_name')
    parser.add_argument('--description')
    parser.add_argument('--other_affiliation')
    parser.add_argument('--active')
    parser.add_argument('--primary_time_zone')
    parser.add_argument('--region')
    parser.add_argument('--primary_audio_language')
    parser.add_argument('--delivery_model')


def register_query(parser: ArgumentParser):
    """
    Register the query command and its subcommands.
    :param parser:
    :return:
    """
    # Add all base_obj_expression params as optional arguments
    parser.add_argument('--structural_type', choices=["Abstraction", "Performance", "Digital", "Physical"])
    parser.add_argument('--mode', choices=["Visual", "AudioVisual", "Audio", "Other"])
    parser.add_argument('--referent_type')
    parser.add_argument('--resource_name')
    parser.add_argument('--alternate_resource_name')
    parser.add_argument('--original_language')
    parser.add_argument('--dubbed_language')
    parser.add_argument('--associated_org')
    parser.add_argument('--release_date')
    parser.add_argument('--country_of_origin')
    parser.add_argument('--status')
    parser.add_argument('--approximate_length')
    parser.add_argument('--alternate_id')
    parser.add_argument('--display_name')
    parser.add_argument('--credits')
    parser.add_argument('--registrant_extra')
    parser.add_argument('--description')


def register_party_query(parser: ArgumentParser):
    """
    Register the party query command and its subcommands.
    :param parser:
    :return:
    """
    # Add all party_expression params as optional arguments
    parser.add_argument('--id')
    parser.add_argument('--display_name')
    parser.add_argument('--sort_name')
    parser.add_argument('--organization_id')
    parser.add_argument('--id_type')
    parser.add_argument('--alternate_party_name')
    parser.add_argument('--contact_name')
    parser.add_argument('--primary_email')
    parser.add_argument('--alternate_email')
    parser.add_argument('--contact_address')
    parser.add_argument('--contact_phone')
    parser.add_argument('--active', type=bool)
    parser.add_argument('--party_account_name')
    parser.add_argument('--allowed_roles')


def register(subparsers):
    """
    Register the query command and its subcommands.
    :param subparsers:
    :return:
    """
    query_parser = subparsers.add_parser(
        'query',
        help="Construct a BaseObjectData query expression"
    )
    register_query(query_parser)
    # Add common options to both parsers
    query_parser.set_defaults(func=handle_query)
    add_common_options(query_parser)

    # Add all service_expression params as optional arguments
    service_parser = subparsers.add_parser(
        'service_query',
        help="Construct a Service query expression"
    )
    register_service_query(service_parser)
    service_parser.set_defaults(func=handle_service_query)
    add_common_options(service_parser)

    # Add all party_expression params as optional arguments
    party_parser = subparsers.add_parser(
        'party_query',
        help="Construct a Party query expression"
    )
    add_common_options(party_parser)
    register_party_query(party_parser)
    party_parser.set_defaults(func=handle_party_query)


def handle_query(args, session_manager: SessionManager):
    """
    Handle the query command.
    :param args:
    :param session_manager:
    :return: result
    """
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

    q = Query(
        expression=query_expression,
        page_num=args.page_num,
        page_size=args.page_size,
    )
    request = RegistryRequest(
        operations=[q]
    )
    result, _ = session_manager.query(request)
    output_query(args, result)


def handle_service_query(args, session_manager: SessionManager):
    """
    Handle the service query command.
    :param args:
    :param session_manager:
    :return:
    """
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
    query = ServiceQuery(
        page_number=args.page_num,
        page_size=args.page_size,
        expression=query_expression
    )
    result = session_manager.service_query(query)

    output_query(args, result)


def handle_party_query(args, session_manager: SessionManager):
    """
    Handle the party query command.
    :param args:
    :param session_manager:
    :return:
    """
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
    query = PartyQuery(
        expression=query_expression,
        page_size=args.page_size,
        page_number=args.page_num
    )
    result = session_manager.party_query(query)
    output_query(args, result)


def output_query(args, result):
    if args.format == "std_out":
        print(f"[blue]Generated Query:[/blue]\n{result}")
