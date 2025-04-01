from typing import Union

from app.services.interface import ServiceBase

from app.scheme.org.eidr.schema.create_edit_data_type import CreateEditDataType
from app.scheme.org.eidr.schema.create_composite_data_type import CreateCompositeDataType
from app.scheme.org.eidr.schema.create_type import CreateType
from app.scheme.org.eidr.schema.creation_type import CreationType
from app.scheme.org.eidr.schema.create_basic_data_type import CreateBasicDataType
from app.scheme.org.eidr.schema.create_series_data_type import CreateSeriesDataType
from app.scheme.org.eidr.schema.create_episode_data_type import CreateEpisodeDataType
from app.scheme.org.eidr.schema.create_manifestation_data_type import CreateManifestationDataType
from app.scheme.org.eidr.schema.create_clip import CreateClipDataType
from app.scheme.org.eidr.schema.create_compilation_data_type import CreateCompilationDataType
from app.scheme.org.eidr.schema.create_season_data_type import CreateSeasonDataType
from app.scheme.org.eidr.schema.create_interactive_data_type import CreateInteractiveDataType
from app.scheme.org.eidr.schema.operation_type import OperationType

class Create(ServiceBase):

    """
        Implements the creation operation of the registration service.
        Attributes:
            record: The record to be created - can be of any create_type.
    """
    name = 'register'

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
            ]
    ):
        self.record = record
        self.__type_mapping = {
            CreateBasicDataType: CreateType(basic=self.record, type_value=CreationType.CREATE_BASIC),
            CreateSeriesDataType: CreateType(series=self.record, type_value=CreationType.CREATE_SERIES),
            CreateSeasonDataType: CreateType(season=self.record, type_value=CreationType.CREATE_SEASON),
            CreateInteractiveDataType: CreateType(interactive=self.record, type_value=CreationType.CREATE_INTERACTIVE),
            CreateEpisodeDataType: CreateType(episode=self.record, type_value=CreationType.CREATE_EPISODE),
            CreateManifestationDataType: CreateType(manifestation=self.record, type_value=CreationType.CREATE_MANIFESTATION),
            CreateEditDataType: CreateType(edit=self.record, type_value=CreationType.CREATE_EDIT),
            CreateClipDataType: CreateType(clip=self.record, type_value=CreationType.CREATE_CLIP),
            CreateCompilationDataType: CreateType(compilation=self.record, type_value=CreationType.CREATE_COMPILATION),
            CreateCompositeDataType: CreateType(composite=self.record, type_value=CreationType.CREATE_COMPOSITE),
        }
        super().__init__()
    def validate(self) -> bool:
        return any([isinstance(self.record,create_type) for create_type in self.__type_mapping.keys()])

    def objectify(self) -> None:
        for record_type,create_type in self.__type_mapping.items():
            if isinstance(self.record, record_type):
                self.obj = OperationType(
                    create=create_type,
                )
                break