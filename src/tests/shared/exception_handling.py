from pytest_bdd import parsers, then
from typing import Dict, Any


@then(parsers.parse("{exception_count:d} exceptions are raised"))
def then_number_of_exceptions_raised_are_expected(
    context: Dict[str, Any], exception_count: int
):
    """The number of exceptions raised should be as expected"""
    exceptions = context["exceptions"]

    assert len(exceptions) == exception_count


@then(parsers.parse("a meaningful error '{expected_error}' is provided"))
def then_meaningful_error_is_provided(context: Dict[str, Any], expected_error: str):
    """Then a meaningful error is provided."""
    exceptions = context["exceptions"]

    assert str(exceptions[0]) == expected_error
