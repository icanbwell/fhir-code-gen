import dataclasses
from typing import List, Optional, Set

from fhircodegen.structures.fhir_property import FhirProperty
from fhircodegen.structures.fhir_value_set_concept import FhirValueSetConcept


@dataclasses.dataclass
class FhirEntity:
    """
    This class stores a fhir entity which can be:
    1. Resource
    2. Backbone Element
    3. Complex Type

    """

    fhir_name: str
    cleaned_name: str
    name_snake_case: str
    properties: List[FhirProperty]
    documentation: List[str]
    type_: Optional[str]
    is_back_bone_element: bool
    base_type: Optional[str]
    base_type_list: List[str]
    source: str
    is_value_set: bool = False

    # if this entity is a value set, this is the list of concepts
    value_set_concepts: Optional[List[FhirValueSetConcept]] = None

    value_set_url: Optional[str] = None
    is_basic_type: bool = False
    value_set_url_list: Optional[Set[str]] = None
    is_resource: bool = False
    is_extension: bool = False
    properties_unique: Optional[List[FhirProperty]] = None
