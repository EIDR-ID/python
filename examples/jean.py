from pathlib import Path

from xsdata.models.datatype import XmlDuration

from app.manager import SessionManager
from app.services import Query, RegistryRequest
from app.util import generate_template_fill, generate_templates, TemplateType, from_json

inherited = {  # The following fields are inherited from the parent object, no need to fill them
    "BaseObjectData": {
        "OriginalLanguage": None,
        "AlternateID": None,
        "VersionLanguage": None,
        "AssociatedOrg": None,
        "CountryOfOrigin": None,
        "RegistrantExtra": None,
        "Credits": None,
        "AlternateResourceName": None
    }
}


def episode_helper(num: int, parent: str):
    return {
        "ExtraObjectMetadata": {
            "EpisodeInfo": {
                "SequenceInfo": {
                    "Parent": {
                        "value": parent
                    },
                    "DistributionNumber": {
                        "value": str(num),
                        "domain": "MEM.com"
                    },
                    "HouseSequence": None,
                    "AlternateNumber": None
                },
                "TimeSlot": "21:00:00"
            }
        }
    }


def gen_ep(name: str, extra_info: dict = None):
    if not extra_info:
        extra_info = {}
    name_info = {
        "BaseObjectData": {
            "ResourceName": {
                "value": name,
                "titleClass": "release",
                "systemGenerated": False
            },
            "ReleaseDate": "2025-05+03:30",
            "ApproximateLength": "PT24M"
        },
    }
    f = generate_template_fill(TemplateType.CREATE_EPISODE, [name_info, inherited, extra_info])
    generate_templates(Path(f'./eps/{name}'), [TemplateType.CREATE_EPISODE], fill=[f])


def make_episodes(names: list[str], series_id: str = "FILL THIS"):
    for i, name in enumerate(names):
        f = episode_helper(i + 1, series_id)
        gen_ep(name, extra_info=f)


def upload():
    for folder in ["If There's a Kroon, There's a Way", "A Kroon for Every Season", "Under the Kroon Light"]:
        from_json(Path(f'eps/{folder}/create_episode.json'))


if __name__ == "__main__":
    make_episodes(["If There's a Kroon, There's a Way", "A Kroon for Every Season", "Under the Kroon Light"])
    ...
