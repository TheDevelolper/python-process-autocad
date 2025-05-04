from pathlib import Path
from typing import Dict, Any
from pytest_bdd import scenarios, given, when, parsers

import pytest

from features.dwg_conversion.models import AppSettings, ConversionSettings
from features.dwg_conversion.utilities import BatchDxfConverter

# ! These imports are used inside the testing framework
# * Please don't remove then unless you really know what you're doing
# pylint: disable=unused-import
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from tests.shared.exception_handling import *  # NOSONAR

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


@given(parsers.parse("the oda path {path} is provided"))
def given_the_incorrect_oda_path_is_provided(context: Dict[str, Any], path: str):
    """Given the dwg is not present.
    Overrides the default app settings to specify an empty to scan for dwg files
    """
    app_settings: AppSettings = context["app_settings"]
    app_settings.conversion.oda_converter_path = path


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
