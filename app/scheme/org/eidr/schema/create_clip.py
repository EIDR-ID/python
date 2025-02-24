from dataclasses import dataclass

from    .create_clip_data_type import CreateClipDataType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class CreateClip(CreateClipDataType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
