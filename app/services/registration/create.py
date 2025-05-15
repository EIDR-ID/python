from pathlib import Path
from typing import Union

from app.scheme.org.eidr.schema import DedupModeType
from app.services.registration.interface import RegistrationService

from app.scheme.org.eidr.schema.create_edit_data_type import CreateEditDataType
from app.scheme.org.eidr.schema.create_composite_data_type import CreateCompositeDataType
from app.scheme.org.eidr.schema.create_type import CreateType
from app.scheme.org.eidr.schema.create_basic_data_type import CreateBasicDataType
from app.scheme.org.eidr.schema.create_series_data_type import CreateSeriesDataType
from app.scheme.org.eidr.schema.create_episode_data_type import CreateEpisodeDataType
from app.scheme.org.eidr.schema.create_manifestation_data_type import CreateManifestationDataType
from app.scheme.org.eidr.schema.create_clip import CreateClipDataType
from app.scheme.org.eidr.schema.create_compilation_data_type import CreateCompilationDataType
from app.scheme.org.eidr.schema.create_season_data_type import CreateSeasonDataType
from app.scheme.org.eidr.schema.create_interactive_data_type import CreateInteractiveDataType
from app.scheme.org.eidr.schema.operation_type import OperationType
from app.util import dict_to_instance, from_json


class Create(RegistrationService):
    """
        Implements the creation operation of the registration service.
        Attributes:
            record: The record to be created - can be of any create_type.
    """

    def __init__(
            self,
            record: Union[
                CreateBasicDataType,
                CreateSeriesDataType,
                CreateInteractiveDataType,
                CreateSeasonDataType,
                CreateEpisodeDataType,
                CreateManifestationDataType,
                CreateClipDataType,
                CreateCompositeDataType,
                CreateEditDataType,
                CreateCompilationDataType,
            ],
            dedupe_mode: DedupModeType | None = None
    ):
        self.record = record
        self.dedupe_mode = dedupe_mode
        self.type_mapping = {
            CreateBasicDataType: CreateType(basic=self.record),
            CreateSeriesDataType: CreateType(series=self.record),
            CreateSeasonDataType: CreateType(season=self.record),
            CreateInteractiveDataType: CreateType(interactive=self.record),
            CreateEpisodeDataType: CreateType(episode=self.record),
            CreateManifestationDataType: CreateType(manifestation=self.record),
            CreateEditDataType: CreateType(edit=self.record),
            CreateClipDataType: CreateType(clip=self.record),
            CreateCompilationDataType: CreateType(compilation=self.record),
            CreateCompositeDataType: CreateType(composite=self.record),
        }
        super().__init__()

    @classmethod
    def from_json(cls, file_path: Path, clazz_type, dedupe_mode: DedupModeType | None = None) -> 'Create':
        """
        Initialize this class from a JSON file
        :param file_path: The path to the JSON file
        :type clazz_type: dataclass type
        :param dedupe_mode: deduplication mode, only applicable for create and modify operations
        :return:
            Create: An instance of the Create class.
        """
        if not isinstance(file_path, Path):
            raise TypeError(f"Expected 'file_path' to be of type Path, but got {type(file_path)}")
        elif not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        rec_dict: dict = from_json(file_path)
        record_instance = dict_to_instance(rec_dict, clazz_type)
        return cls(record=record_instance, dedupe_mode=dedupe_mode)

    def validate(self) -> bool:
        return type(self.record) in self.type_mapping.keys()

    def objectify(self) -> None:
        self.obj = OperationType(
            create=self.type_mapping.get(type(self.record)),
            dedup_mode=self.dedupe_mode
        )
