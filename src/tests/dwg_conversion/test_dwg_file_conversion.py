from pathlib import Path
from typing import Dict, Any
from pytest_bdd import scenarios, given, when, then, parsers

import pytest

from features.dwg_conversion.models import AppSettings, ConversionSettings
from features.dwg_conversion.utilities import BatchDxfConverter

FEATURE_FILE_NAME = "dwg_file_conversion.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE_PATH = str(BASE_DIR.joinpath(FEATURE_FILE_NAME))

scenarios(FEATURE_FILE_PATH)


@pytest.fixture
def context() -> Dict[str, Any]:
    """Fixture to store shared state for the BDD steps."""
    result: Dict[str, Any] = {}
    result["app_settings"] = AppSettings.from_file("settings.json")
    result["exceptions"] = []
    return result


@given(parsers.parse("the dwg is not present in directory {directory}"))
def given_the_dwg_is_not_present(context: Dict[str, Any], directory: str):
    """Given the dwg is not present.
    Overrides the default app settings to specify an empty to scan for dwg files
    """
    app_settings: AppSettings = context["app_settings"]
    app_settings.conversion.input_folder = directory


@when("the conversion is performed")
def when_conversion_is_performed(context: Dict[str, Any]):
    """When the conversion is performed."""
    app_settings: AppSettings = context["app_settings"]
    conversion_settings: ConversionSettings = app_settings.conversion
    converter = BatchDxfConverter(conversion_settings)
    try:
        converter.process()
    except Exception as e:
        context["exceptions"].append(e)


@then(parsers.parse("a meaningful error '{expected_error}' is provided"))
def then_meaningful_error_is_provided(context: Dict[str, Any], expected_error: str):
    """Then a meaningful error is provided."""
    exceptions = context["exceptions"]

    assert len(exceptions) == 1
    assert str(exceptions[0]) == expected_error
