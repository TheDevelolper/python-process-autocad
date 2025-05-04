class InputFilesNotFoundException(Exception):
    """Exception raised when no input files matching a glob filter are found for processing."""

    def __init__(self, directory_path: str, glob: str):
        # Store the directory_path and add a custom message
        self.directory_path = directory_path
        self.message = (
            f"No input files matching {glob} were found in directory {directory_path}."
        )
        super().__init__(self.message)


class OdaConverterNotFoundException(Exception):
    """Exception raised when the ODA Converter was not found"""

    def __init__(self, directory_path: str):
        # Store the directory_path and add a custom message
        self.directory_path = directory_path
        self.message = f"ODA Converter was not found at path {directory_path}. Please check it's installed and that correct path was provided."
        super().__init__(self.message)
