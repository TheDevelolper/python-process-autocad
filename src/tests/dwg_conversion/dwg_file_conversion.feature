Feature: DWG File Conversion

# Scenario: oda is not installed

Scenario: missing dwg file
    Given the dwg is not present in directory "src/tests/test_data/empty"
    When the conversion is performed
    Then a meaningful error 'No input files found in directory "src/tests/test_data/empty".' is provided
