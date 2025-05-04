import glob
import os
from typing import List, Optional


class FileSystemHelper:
    """Shared helper functions for handling directories and files"""

    @staticmethod
    def path_exists(path: str) -> bool:
        """Test whether a path exists. Returns False for broken symbolic links"""  # Copied this from path.exists docstring
        result = os.path.exists(path)
        return result

    @staticmethod
    def get_dir_files(path: str, pattern: Optional[str] = None) -> List[str]:
        """Gets a list of files in the given path matching the provided pattern.

        If no pattern is provided, all files in the path will be returned.

        Args:
                path (str): The file path of the path to search.
                pattern (Optional[str], optional): A file pattern (e.g., "*.dwg") to match files.
                        If None, all files in the path are returned. Defaults to None.

        Returns:
                List[str]: A list of file paths that match the given pattern, or all files if no pattern is provided.

        Example:
                get_dir_files("/path/to/path", "*.dwg") -> ['file1.dwg', 'file2.dwg']
                get_dir_files("/path/to/path") -> ['file1.txt', 'file2.jpg', ...]
        """

        if pattern is None:
            pattern = "*"

        return glob.glob(os.path.join(path, pattern))
