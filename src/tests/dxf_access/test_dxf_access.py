from ast import Assert
from pathlib import Path
from typing import Dict, Any
from pytest_bdd import scenarios, given, when, then, parsers

import pytest

from features.dxf_access.utilities import DxfCadDiagramWrapper

FEATURE_FILE_NAME = "dxf_access.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE_PATH = str(BASE_DIR.joinpath(FEATURE_FILE_NAME))

scenarios(FEATURE_FILE_PATH)


@pytest.fixture
def context() -> Dict[str, Any]:
    """Fixture to store shared state for the BDD steps."""
    result: Dict[str, Any] = {}
    return result


@given(parsers.parse('the dxf path "{dxf_path}" is provided'))
def given_the_dxf_path_is_provided(context: Dict[str, Any], dxf_path: str):
    """given the dxf path is provided."""
    context["dxf_path"] = dxf_path


@when("the layers are accessed")
def when_the_layers_are_accessed(context: Dict[str, Any]):
    """When the layers are accessed."""
    dxf_path = str(context["dxf_path"])
    context["dxf_layers"] = DxfCadDiagramWrapper(dxf_path).get_layer_names()


@then(parsers.parse("the number of layers should be {expected_layer_count:d}"))
def then_the_number_of_layers_should_be(
    context: Dict[str, Any], expected_layer_count: int
):
    """Asserts that the number of layers is as expected"""
    dxf_layers = context["dxf_layers"]
    assert len(dxf_layers) == expected_layer_count


# # TODO: I'll implement this later
# # Scenario: dxf not found
# #     Given the oda path "src/tests/test_data/empty" is provided
# #     When the conversion is performed
# #     Then a meaningful error 'ODA Converter was not found at path "src/tests/test_data/empty". Please check it's installed and that correct path was provided.' is provided
