from enum import Enum

__NAMESPACE__ = "http://www.doi.org/2010/DOISchemaAVS"


class CreationType(Enum):
    """Allowed Values for types of Creation.

    This is an open set. Other values may be registered with the IDF by
    any Registration Authority.

    :cvar ARTICLE: A non-fictional text in prose form (typically between
        a few paragraphs and a few pages in length) included with others
        in a Publication to provide information and/or opinion.
    :cvar BLOG: A blog (weblog) on a website.
    :cvar BLOG_ENTRY: An entry in a Blog.
    :cvar BOOK: A non serial Creation, capable of being expressed in
        printed form with multiple bound pages and covers, published
        with a distinct Title and not as part of another Publication
        unless it is set of similar Resources. A DOI applied at this
        level may refer to a Book which appears in physical, digital and
        audio forms.
    :cvar BOOK_CHAPTER: A Chapter of a Book.
    :cvar BOOK_SERIES: A Series of Books.
    :cvar CHAPTER: A formal subdivision of a lexical Creation.
    :cvar CLINICAL_TRIAL_PROTOCOL: A chronological Report on a series of
        events which is a part of a clinical trial.
    :cvar CLIP: A short excerpt of a longer Audio or AudioVisual
        Creation, often made for promotional or preview purposes but
        which may also be made available commercially.
    :cvar CONFERENCE_PROCEEDINGS: A Publication consisting of
        contributions presented at a conference.
    :cvar CONFERENCE_PROCEEDINGS_SERIES: A Series of
        ConferenceProceedings.
    :cvar COURSE_PACK: A collection of journal articles, BookChapters
        and/or other components making up reading materials for an
        academic course.
    :cvar CRYSTAL_STRUCTURE: A Dataset describing the structure of a
        crystal.
    :cvar CUE_SHEET: A metadata file identifying Creations (typically
        music) which are included in a TVProgramme, CD, DVD or other
        Audio or AudioVisual Creation.
    :cvar DATASET: A Set of numeric and related data (typically
        associated with scientific research).
    :cvar DICTIONARY_ENTRY: An entry in a dictionary.
    :cvar EBOOK: A Book published in downloadable digital form.
    :cvar ENCYCLOPAEDIA_ENTRY: An entry in an encyclopaedia.
    :cvar FIGURE: An image, table or other graphical feature which is an
        integral part of a lexical work.
    :cvar FILM: An AudioVisual Creation, normally of at least 40 minutes
        duration, first played in a movie theatre (in the US) or a
        cinema (in most of the rest of the world), or released directly
        to video.
    :cvar INTERACTIVE_RESOURCE: A Visual Creation not intended to be
        viewed in linear fashion (for example, DVD menus, interactive TV
        overlays, customized players).
    :cvar JOURNAL: A Periodical principally consisting of Articles
        contributed by expert authors, with a specific theme, subject
        area and target audience, normally of a scholarly, scientific
        and/or technical nature.
    :cvar JOURNAL_ARTICLE: An Article in a Journal.
    :cvar JOURNAL_ISSUE: A collection of Articles published together in
        one or more fixations representing a single issue of a Journal.
        Typically a journal issue will be identified with a specific
        date of publication.
    :cvar JOURNAL_VOLUME: A numbered Set of JournalIssues, normally
        representing the issues published in a specific period such as a
        calendar year.
    :cvar LEARNING_OBJECT: A Resource for use in teaching and learning.
    :cvar MEDICAL_CASE_REPORT: A Report on a medical case.
    :cvar MOVING_IMAGE: A moving Image.
    :cvar PERIODICAL: A Serial whose issues normally are published at
        regular intervals.
    :cvar PRINTED_BOOK: A Book published in printed form.
    :cvar REPORT: A lexical Creation containing statements about
        event(s) or state(s) in the past or present.
    :cvar REPORT_CHAPTER: A Chapter of a Report.
    :cvar REPORT_SERIES: A Series of Reports.
    :cvar RESTRICTED: A Creation identified within a restricted DOI
        Application Profile for which kernel metadata values are not
        generally available.
    :cvar SEASON: A sub-grouping of an Audio or AudioVisual Series.
    :cvar SERIAL: A Creation whose parts are published sequentially in
        time.
    :cvar SERIAL_ISSUE: A collection of Articles published together in
        one or more fixations representing a single issue of a Serial.
        Typically a serial issue will be identified with a specific date
        of publication.
    :cvar SERIES: A Set of related Creations published sequentially,
        typically under some common Name.
    :cvar SHORT_FILM: A complete AudioVisual Creation (that is, not a
        Clip or Excerpt), of no more than 40 minutes duration, that was
        not made for television.
    :cvar STANDARD: A formal standard adopted by ISO or another
        recognized standards body.
    :cvar STANDARD_SERIES: A Series of Standards.
    :cvar STILL_IMAGE: A still Image.
    :cvar SUPPLEMENTAL_RESOURCE: A Creation which accompanies another
        Creation (this includes, for example, all kinds of preface or
        epilogue in a textual Creation, or trailers or outtakes in an
        Audiovisual Creation).
    :cvar THESIS: A lexical Creation written for the attainment of a
        degree or award from an academic institution.
    :cvar TV_PROGRAMME: An AudioVisual Creation made for, or first
        broadcast on, television.
    :cvar WEB_RESOURCE: A Creation made for, or first published on, the
        World Wide Web.
    :cvar WEBSITE: A website.
    """

    ARTICLE = "Article"
    BLOG = "Blog"
    BLOG_ENTRY = "BlogEntry"
    BOOK = "Book"
    BOOK_CHAPTER = "BookChapter"
    BOOK_SERIES = "BookSeries"
    CHAPTER = "Chapter"
    CLINICAL_TRIAL_PROTOCOL = "ClinicalTrialProtocol"
    CLIP = "Clip"
    CONFERENCE_PROCEEDINGS = "ConferenceProceedings"
    CONFERENCE_PROCEEDINGS_SERIES = "ConferenceProceedingsSeries"
    COURSE_PACK = "CoursePack"
    CRYSTAL_STRUCTURE = "CrystalStructure"
    CUE_SHEET = "CueSheet"
    DATASET = "Dataset"
    DICTIONARY_ENTRY = "DictionaryEntry"
    EBOOK = "Ebook"
    ENCYCLOPAEDIA_ENTRY = "EncyclopaediaEntry"
    FIGURE = "Figure"
    FILM = "Film"
    INTERACTIVE_RESOURCE = "InteractiveResource"
    JOURNAL = "Journal"
    JOURNAL_ARTICLE = "JournalArticle"
    JOURNAL_ISSUE = "JournalIssue"
    JOURNAL_VOLUME = "JournalVolume"
    LEARNING_OBJECT = "LearningObject"
    MEDICAL_CASE_REPORT = "MedicalCaseReport"
    MOVING_IMAGE = "MovingImage"
    PERIODICAL = "Periodical"
    PRINTED_BOOK = "PrintedBook"
    REPORT = "Report"
    REPORT_CHAPTER = "ReportChapter"
    REPORT_SERIES = "ReportSeries"
    RESTRICTED = "Restricted"
    SEASON = "Season"
    SERIAL = "Serial"
    SERIAL_ISSUE = "SerialIssue"
    SERIES = "Series"
    SHORT_FILM = "ShortFilm"
    STANDARD = "Standard"
    STANDARD_SERIES = "StandardSeries"
    STILL_IMAGE = "StillImage"
    SUPPLEMENTAL_RESOURCE = "SupplementalResource"
    THESIS = "Thesis"
    TV_PROGRAMME = "TvProgramme"
    WEB_RESOURCE = "WebResource"
    WEBSITE = "Website"
