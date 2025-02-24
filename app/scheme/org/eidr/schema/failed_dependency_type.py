from dataclasses import dataclass, field

from    .asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class FailedDependencyType:
    """This has a list of items on which this item depends but have failed to
    register.

    It will have at least one, but is not guaranteed to have all of them.
    The IDs will be of the form LOCAL:
    """

    class Meta:
        name = "failedDependencyType"

    dependency: list[AssetDoitype] = field(
        default_factory=list,
        metadata={
            "name": "Dependency",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
        },
    )
