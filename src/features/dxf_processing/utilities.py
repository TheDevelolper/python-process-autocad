import ezdxf

from typing import List
from features.dxf_processing.contracts import CadDiagramHelper


class DxfCadDiagramHelper(CadDiagramHelper):
    """Wrapper facade to provide targeted functionality for processing DXF files."""

    def __init__(self, dxf_file_path: str):
        self.dxf_file_path = dxf_file_path
        self.doc = ezdxf.readfile(dxf_file_path)  # type: ignore

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
