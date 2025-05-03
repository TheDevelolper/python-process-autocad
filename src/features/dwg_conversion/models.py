"""Defines data models for application settings and file conversion configuration.

This module includes:
- `ConversionSettings`: Holds the configuration required for batch file conversion.
- `AppSettings`: Loads and wraps application settings from a JSON file.
"""

import json
from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class AppSettings:
    """Represents the application settings loaded from a configuration file.

    Attributes:
        conversion (ConversionSettings): Configuration specific to the file conversion process.
    """

    def __init__(self, conversion: Dict[str, Any]):
        self.conversion: ConversionSettings = ConversionSettings(**conversion)

    @staticmethod
    def load(file_path: str):
        """loads the settings from a file"""
        with open(file_path, "r") as f:
            settings_dict = json.load(f)
            result: AppSettings = AppSettings(**settings_dict)
            return result


class ConversionSettings:
    """Holds settings related to the file conversion process.

    Attributes:
        oda_converter_path (str): Path to the ODA File Converter executable.
        input_folder (str): Directory containing input files to convert.
        output_folder (str): Directory where converted files will be saved.
        output_version (str): Target DWG/DXF version (e.g., 'ACAD2018').
        output_file_type (str): Output file type ('DWG' or 'DXF').
        recurse_input_folder (str): '1' to include subfolders; '0' otherwise.
        audit_files (str): '1' to audit files during conversion; '0' otherwise.
        input_file_filter (str): File name pattern to match input files (e.g., '*.DWG').
    """

    def __init__(
        self,
        oda_converter_path: str,
        input_folder: str,
        output_folder: str,
        output_version: str,
        output_file_type: str,
        recurse_input_folder: str,
        audit_files: str,
        input_file_filter: str,
    ):

        self.oda_converter_path: str = oda_converter_path
        self.input_folder: str = input_folder
        self.output_folder: str = output_folder
        self.output_version: str = output_version
        self.output_file_type: str = output_file_type
        self.recurse_input_folder: str = recurse_input_folder
        self.audit_files: str = audit_files
        self.input_file_filter: str = input_file_filter
