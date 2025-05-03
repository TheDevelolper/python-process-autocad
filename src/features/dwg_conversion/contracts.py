from abc import ABC, abstractmethod


class BatchFileConverter(ABC):
    """
    Abstract base class for batch file conversion tools.

    Subclasses must implement the `process` method to define
    how the batch conversion should be executed.
    """

    @abstractmethod
    def process(self):
        """
        Executes the conversion process.

        Raises:
            subprocess.CalledProcessError: If the external conversion command fails.
        """
        pass
