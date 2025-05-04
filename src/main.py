import os

from features.dwg_conversion.contracts import BatchFileConverter
from features.dwg_conversion.models import AppSettings, ConversionSettings
from features.dwg_conversion.utilities import BatchDxfConverter

from features.dxf_processing.contracts import CadDiagramHelper
from features.dxf_processing.utilities import DxfCadDiagramHelper


def main():
    """
    Main entry point for running the DXF conversion and extracting layer names.

    - Loads application settings from a JSON file.
    - Converts DWG files to DXF format using the settings.
    - For each resulting DXF file, retrieves and prints the layer names.

    The function expects a `settings.json` file to be present in the specified
    path, and it will use this to configure the DXF conversion process.

    Returns:
        None
    """
    # Run the ODA File Converter
    app_settings: AppSettings = AppSettings.from_file("settings.json")
    dxf_file_paths = dwg_convert_dxf(app_settings.conversion)

    for file_path in dxf_file_paths:
        cad_doc_wrapper = get_dxf_document_wrapper(file_path)
        print(cad_doc_wrapper.get_layer_names())


def dwg_convert_dxf(conversion_settings: ConversionSettings):
    """Converts dwg files into dxf format
    Attributes:
        conversion_settings (ConversionSettings):
            A model containing the settings relevant to the conversion process
    """
    batch_converter: BatchFileConverter = BatchDxfConverter(conversion_settings)
    batch_converter.process()
    result = [
        os.path.join(conversion_settings.output_folder, filename)
        for filename in os.listdir(conversion_settings.output_folder)
    ]
    return result


def get_dxf_document_wrapper(dxf_file_path: str) -> CadDiagramHelper:
    """Gets the wrapper for the dxf document
    Attributes:
        file_path (string): A string representing the filepath to the dxf file
    """
    cad_doc_wrapper: CadDiagramHelper = DxfCadDiagramHelper(dxf_file_path)
    return cad_doc_wrapper


if __name__ == "__main__":
    main()
