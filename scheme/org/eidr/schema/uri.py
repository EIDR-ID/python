from dataclasses import dataclass

from scheme.org.eidr.schema.alternate_idtype import AlternateIdtype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class Uri(AlternateIdtype):
    """a URI for us is scheme://dns name/data [# query] [#fragment] scheme
    starts with a character, then (char digit + - .)* limited to total of 12 the regular
    expression for the domain requires at least one . in the domain, and supports 2-4
    character top level domains the other pieces of the domain are alphanumeric first
    char, alphanumeric or dash in the middle, alphanumeric last char, maximum 63
    characters data is slash-separated, with an optional trailing slash. legal
    characters are 0-9a-zA-Z _ - . ~ ! $ ampersand ' ( ) * + , ; = @ : optional query is
    as data, with the addition of / and ? optional fragment is as query data differences
    from full URI: -- limit on scheme length -- must have domain name, can't have
    userinfo@host:port -- dns names only, not IP addresses -- there must be /something
    after the domain"""

    class Meta:
        name = "URI"
