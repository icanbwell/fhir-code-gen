import dataclasses
from typing import List, Optional

from fhircodegen.structures.smart_name import SmartName


@dataclasses.dataclass
class FhirProperty:
    """
    This class represents a property of a FHIR entity
    """

    name: str
    fhir_name: str
    javascript_clean_name: str
    type_: str
    cleaned_type: str
    type_snake_case: str
    optional: bool
    is_list: bool
    documentation: List[str]
    fhir_type: Optional[str]

    # if this property is a reference, this is the list of target resources
    reference_target_resources: List[SmartName]
    reference_target_resources_names: List[str]

    is_back_bone_element: bool
    is_basic_type: bool
    codeable_type: Optional[SmartName]
    is_resource: bool = False
    is_extension: bool = False
    is_code: bool = False
    is_complex: bool = False
    name_suffix: Optional[str] = None
    is_v2_supported: bool = False
