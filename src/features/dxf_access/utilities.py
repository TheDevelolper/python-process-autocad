import ezdxf

from typing import List
from features.dxf_access.contracts import CadDiagramWrapper


class DxfCadDiagramWrapper(CadDiagramWrapper):
    """Wrapper facade to provide targeted functionality for processing DXF files."""

    def __init__(self, dxf_path: str):
        self.dxf_path = dxf_path
        self.doc = ezdxf.readfile(dxf_path)  # type: ignore

    def get_layer_names(self) -> List[str]:
        """
        Retrieves the names of all layers in the DXF document.

        Iterates over the layers in the DXF document and returns a list
        of layer names as strings.

        Returns:
            List[str]: A list of layer names from the DXF document.
        """
        layer_names: List[str] = [layer.dxf.name for layer in self.doc.layers]
        return layer_names
