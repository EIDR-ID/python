from dataclasses import dataclass

from scheme.org.eidr.schema.bulk_ingest_file_type import BulkIngestFileType

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class BulkIngestFile(BulkIngestFileType):
    class Meta:
        namespace = "http://www.eidr.org/schema"
