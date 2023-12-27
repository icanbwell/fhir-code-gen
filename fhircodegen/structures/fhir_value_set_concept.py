import dataclasses
from typing import Optional


@dataclasses.dataclass
class FhirValueSetConcept:
    """
    This class stores a value set concept

    """

    code: str
    display: Optional[str]
    cleaned_display: Optional[str]
    definition: Optional[str]
    source: str
    value_set_url: str
