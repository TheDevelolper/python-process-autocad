Feature: DWG File Conversion

# Scenario: oda is not installed

Scenario: missing dwg file
    Given the dwg is not present
    When the conversion is performed
    Then a meaningful error should be provided

# Scenario: test one
#     Given the number is 1
#     When the check is made
#     Then the result should be false

