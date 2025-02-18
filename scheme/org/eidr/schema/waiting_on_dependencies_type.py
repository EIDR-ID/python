from dataclasses import dataclass, field

from scheme.org.eidr.schema.asset_doitype import AssetDoitype

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class WaitingOnDependenciesType:
    """This has a list of items on which this item depends.

    It will have at least one, but is not (in the 1.0 registry) guaranteed to have all of them.
    The Dependency will be of the form LOCAL:
    """

    class Meta:
        name = "waitingOnDependenciesType"

    dependency: list[AssetDoitype] = field(
        default_factory=list,
        metadata={
            "name": "Dependency",
            "type": "Element",
            "namespace": "http://www.eidr.org/schema",
            "min_occurs": 1,
        },
    )
