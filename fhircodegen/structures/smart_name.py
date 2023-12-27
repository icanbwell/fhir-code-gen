import dataclasses


@dataclasses.dataclass
class SmartName:
    """
    This class is used to store multiple name representations of a FHIR entity
    """

    # the original name
    name: str
    # the cleaned name
    cleaned_name: str
    # the name in snake case
    snake_case_name: str
