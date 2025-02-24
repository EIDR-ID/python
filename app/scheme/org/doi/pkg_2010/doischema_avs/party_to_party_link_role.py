from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class PartyToPartyLinkRole(Enum):
    """Allowed values for a role which one party plays in a link to another party.

    Where roles have complementary pairs (for example, parent-child or
    member-memberOrganization) only one of these is included in this
    list, and this role should be associated in the linkedParty element
    with the appropriate party.

    :cvar CORPORATE_SUBSIDIARY: An Organization which is a subsidiary of
        another Organization.
    :cvar DIVISION_OR_DEPARTMENT: An Organization which is a division or
        department of another Organization.
    :cvar MARRIAGE_PARTNER: An Individual who is married to another
        Individual.
    :cvar MEMBER: A Party which is a member of an Organization.
    :cvar PARENT: An Individual who is the parent of another Individual.
    :cvar SIBLING: An Individual who is a brother or sister of another
        Individual.
    """

    CORPORATE_SUBSIDIARY = "CorporateSubsidiary"
    DIVISION_OR_DEPARTMENT = "DivisionOrDepartment"
    MARRIAGE_PARTNER = "MarriagePartner"
    MEMBER = "Member"
    PARENT = "Parent"
    SIBLING = "Sibling"
