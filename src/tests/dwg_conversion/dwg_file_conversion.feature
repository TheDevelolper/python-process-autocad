Feature: DWG File Conversion

Scenario: oda converter was not found
    Given the oda path "src/tests/test_data/empty" is provided
    When the conversion is performed
    Then a meaningful error 'ODA Converter was not found at path "src/tests/test_data/empty". Please check it's installed and that correct path was provided.' is provided

Scenario: missing dwg file
    Given the dwg is not present in directory "src/tests/test_data/empty"
    When the conversion is performed
    Then 1 exceptions are raised
    And a meaningful error 'No input files matching *.DWG were found in directory "src/tests/test_data/empty".' is provided