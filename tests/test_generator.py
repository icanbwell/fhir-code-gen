from pprint import pprint

from fhircodegen.fhir_xml_schema_parser import FhirXmlSchemaParser


def test_generator() -> None:
    fhir_entities = FhirXmlSchemaParser.generate_classes(
        filter_to_resource="SubscriptionStatus",
    )

    # noinspection PyUnusedLocal
    # account_entity: FhirEntity = [
    #     e for e in fhir_entities if e.fhir_name == "SubscriptionStatus"
    # ][0]
    # now print the result
    for fhir_entity in fhir_entities:
        pprint(fhir_entity)
