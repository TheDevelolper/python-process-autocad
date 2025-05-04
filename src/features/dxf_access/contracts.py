from abc import ABC, abstractmethod
from typing import List


class CadDiagramHelper(ABC):
    """
    Abstract base class that defines the interface for accessing CAD diagram metadata.
    """

    @abstractmethod
    def get_layer_names(self) -> List[str]:
        """
        Returns a list of layer names present in the CAD diagram.

        Returns:
            List[str]: The names of all layers in the diagram.
        """
        pass
