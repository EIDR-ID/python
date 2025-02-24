from dataclasses import dataclass

__NAMESPACE__ = "http://www.eidr.org/schema"


@dataclass
class ReadyToSubmitType:
    """
    This type has no data -- it is just an indicator that things are ready to go.
    """

    class Meta:
        name = "readyToSubmitType"
