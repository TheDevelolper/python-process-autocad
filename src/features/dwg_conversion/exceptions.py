class InputFilesNotFoundException(Exception):
    """Exception raised when no input files matching a glob filter are found for processing."""

    def __init__(self, directory_path: str, glob: str):
        # Store the directory_path and add a custom message
        self.directory_path = directory_path
        self.message = (
            f"No input files matching {glob} were found in directory {directory_path}."
        )
        super().__init__(self.message)



    def __init__(self, directory_path: str):
        # Store the directory_path and add a custom message
        self.directory_path = directory_path
        self.message = f"No input files found in directory {directory_path}."
        super().__init__(self.message)
