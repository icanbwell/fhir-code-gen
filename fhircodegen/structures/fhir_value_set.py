import dataclasses
from typing import List, Set

from fhircodegen.structures.fhir_value_set_concept import FhirValueSetConcept


@dataclasses.dataclass
class FhirValueSet:
    """
    This class stores a value set
    """

    id_: str
    # original name
    name: str
    # name in fhir schema
    fhir_name: str
    # name formatted in snake case
    name_snake_case: str
    # name cleaned for use in javascript
    cleaned_name: str
    # list of concepts associated with this valueset
    concepts: List[FhirValueSetConcept]
    url: str
    value_set_url: str
    value_set_url_list: Set[str]
    documentation: List[str]
    source: str
