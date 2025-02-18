from dataclasses import dataclass

from scheme.org.eidr.schema.bulk_status_file_type import BulkStatusFileType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkIngestStatusFile(BulkStatusFileType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
