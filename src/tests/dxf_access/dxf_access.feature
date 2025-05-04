Feature: DXF Access 

Scenario: Can get layers from dxf
    Given the dxf path "src\tests\test_data\dxf_file\example.dxf" is provided
    When the layers are accessed
    Then the number of layers should be 15
