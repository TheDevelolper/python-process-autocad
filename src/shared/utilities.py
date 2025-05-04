import glob
import os
from typing import List, Optional


class FileSystemHelper:
    """Shared helper functions for handling directories and files"""

    @staticmethod
    def get_dir_files(directory: str, pattern: Optional[str] = None) -> List[str]:
        """Gets a list of files in the given directory matching the provided pattern.

        If no pattern is provided, all files in the directory will be returned.

        Args:
                directory (str): The file path of the directory to search.
                pattern (Optional[str], optional): A file pattern (e.g., "*.dwg") to match files.
                        If None, all files in the directory are returned. Defaults to None.

        Returns:
                List[str]: A list of file paths that match the given pattern, or all files if no pattern is provided.

        Example:
                get_dir_files("/path/to/directory", "*.dwg") -> ['file1.dwg', 'file2.dwg']
                get_dir_files("/path/to/directory") -> ['file1.txt', 'file2.jpg', ...]
        """

        if pattern is None:
            pattern = "*"

        return glob.glob(os.path.join(directory, pattern))
