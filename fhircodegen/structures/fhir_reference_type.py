import dataclasses
from typing import List


@dataclasses.dataclass
class FhirReferenceType:
    """
    This class represents a reference type
    """

    # list of resources that can be the target of this reference
    target_resources: List[str]
    path: str
