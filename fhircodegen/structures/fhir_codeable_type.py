import dataclasses


@dataclasses.dataclass
class FhirCodeableType:
    """
    This class represents a codeable type
    """

    codeable_type: str
    path: str
    codeable_type_url: str
    is_codeable_concept: bool = False
