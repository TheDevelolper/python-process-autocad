import subprocess

from features.dwg_conversion.contracts import BatchFileConverter
from features.dwg_conversion.models import ConversionSettings


class BatchDxfConverter(BatchFileConverter):
    """
    Handles batch conversion of CAD files to DXF format using the ODA File Converter.

    Attributes:
        settings (ConversionSettings): Configuration used for the batch conversion process.
    """

    def __init__(self, settings: ConversionSettings):
        self.settings: ConversionSettings = settings

    def process(self):
        subprocess.run(
            [
                self.settings.oda_converter_path,
                self.settings.input_folder,
                self.settings.output_folder,
                self.settings.output_version,
                self.settings.output_file_type,
                self.settings.recurse_input_folder,
                self.settings.audit_files,
                self.settings.input_file_filter,
            ],
            check=True,
        )
