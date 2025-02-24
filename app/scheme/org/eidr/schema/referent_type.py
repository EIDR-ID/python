from enum import Enum

__NAMESPACE__ = "http://www.eidr.org/schema"


class ReferentType(Enum):
    """
    :cvar SERIES: Use for an item that consists of separate pieces. The
        pieces can be ordered or unordered.
    :cvar PODCAST: A variant of Series with distinct de-duplication
        behavior.
    :cvar SEASON: Convolutedly defined, this is a container for items
        that belong together and are released separately over a defined
        period of time. (Defined by example, this is a season of a TV
        series.) The items can be ordered or unordered
    :cvar TV: Use for anything that was first aired on any form of TV
        (broadcast, cable, satellite.)
    :cvar MOVIE: Use for a work that was first seen in a theatrical
        setting
    :cvar SHORT: Use for shorter works. Ideally, a TV show should not be
        described with this, but ads, outtakes, bonus content, and
        theatrical shorts can be.
    :cvar WEB: Use for work that was first presented on the web
    :cvar COMPILATION: Used for an item that contains mutiple entire
        other objects. See CompilationClassType for examples.
    :cvar INTERACTIVE_MATERIAL: Use for interactive material, such as
        DVD menus or on-line games. ‘abstract’ could be used for
        interactive material that is the conceptual basis for different
        implementations.
    :cvar SUPPLEMENTAL: Use for trailers, value-added material, and
        other promotional material, which are otherwise cannot be made
        children of assets.
    """

    SERIES = "Series"
    PODCAST = "Podcast"
    SEASON = "Season"
    TV = "TV"
    MOVIE = "Movie"
    SHORT = "Short"
    WEB = "Web"
    COMPILATION = "Compilation"
    INTERACTIVE_MATERIAL = "Interactive Material"
    SUPPLEMENTAL = "Supplemental"
