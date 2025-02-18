from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class CreationToCreationLinkRole(Enum):
    """Allowed values for roles played by a Creation in relation to another
    Creation.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar ALTERNATE_CONTENT: A SupplementalResource in an AudioVisual
        Creation which is synchronized to the original Creation (for
        example, an alternate audio track or camera angle).
    :cvar CHAPTER: A Chapter of the linked Creation (that is, a formal
        subdivision of lexical Creation).
    :cvar CLIP: A short excerpt of a longer Audio or AudioVisual
        Creation, often made for promotional or preview purposes but
        which may also be made available commercially.
    :cvar CUE_SHEET: A Cue Sheet for the linked Creation (that is, a
        metadata file identifying Creations (typically music) which are
        included in a TVProgramme, CD, DVD or other Audio or AudioVisual
        Creation).
    :cvar DERIVATION: A Creation made, in whole or part, from the linked
        Creation. Derivation is the most general term to cover all forms
        of adaptation, versioning, performing, fixing and abstracting of
        one Creation from another, and can be used when the specific
        type of derived relationship is undefined or unclear.
    :cvar EDIT: A recorded Performance of a Film or other AudioVisual
        Creation. A Creation playing the role of Edit always has the
        structuralType of 'Performance'.
    :cvar EDITION: A published version of a textual or visual Creation
        in which some of the original form and/or content has been re-
        ordered, changed or omitted.
    :cvar EPISODE: An Episode of a linked Creation (that is, a Part of a
        Series broadcast as a single complete programme).
    :cvar FIXATION: A persistent Manifestation of the linked Creation.
        Fixations include all types of digital files or physical
        carriers on or in which content is fixed by digital or analogue
        methods.
    :cvar IS_SAME_AS: A Creation that is the same as the linked
        Creation.
    :cvar PART: A Creation that is part of (that is, wholly contained
        within) the linked Creation (for example, an illustration within
        a book, a volume of an encyclopaedia). This is a generic value
        which may be used when a more appropriate specific part role
        (such as chapter) is not available.
    :cvar PERFORMANCE: A Performance of the linked Creation (for
        example, a recorded performance of a musical work).
    :cvar PROMOTIONAL_RESOURCE: A Creation which promotes the use of the
        linked Creation.
    :cvar SEASON: A Season of the linked Series.
    :cvar SHARES_CONTENT: A Creation that shares some content with the
        linked Creation (for example, two books which have common
        Chapters, or a TV show that contains an excerpt of a Film).
    :cvar SUPPLEMENTAL_RESOURCE: A Creation which accompanies the linked
        Creation (this includes, for example, all kinds of preface or
        epilogue in a textual Creation, or trailers or outtakes in an
        Audiovisual Creation).
    :cvar TAKES_CONTENT: A Creation that contains content coming from
        one or more places in the linked Creation (for example, a text
        which contains some paragraphs from a pre-existing text). The
        content may or may not be identified as a distinct Part.
    :cvar TRANSLATION: A Translation of the linked Creation (that is,
        whose words are expressed in a different language from its
        Source).
    :cvar UNDEFINED: A Creation with a relationship with the linked
        Creation which is unknown or not covered by the available
        options.
    :cvar VERSION: A Version of the linked Creation (that is, a version
        which updates and replaces the previous version).
    """

    ALTERNATE_CONTENT = "AlternateContent"
    CHAPTER = "Chapter"
    CLIP = "Clip"
    CUE_SHEET = "CueSheet"
    DERIVATION = "Derivation"
    EDIT = "Edit"
    EDITION = "Edition"
    EPISODE = "Episode"
    FIXATION = "Fixation"
    IS_SAME_AS = "IsSameAs"
    PART = "Part"
    PERFORMANCE = "Performance"
    PROMOTIONAL_RESOURCE = "PromotionalResource"
    SEASON = "Season"
    SHARES_CONTENT = "SharesContent"
    SUPPLEMENTAL_RESOURCE = "SupplementalResource"
    TAKES_CONTENT = "TakesContent"
    TRANSLATION = "Translation"
    UNDEFINED = "Undefined"
    VERSION = "Version"
