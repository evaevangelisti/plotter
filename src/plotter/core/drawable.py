from abc import ABC
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class Drawable(ABC):
    """
    Abstract base class for drawable objects.
    """

    def __init__(
        self,
        fig: Figure,
    ):
        """
        Initializes a drawable object.

        Args:
            fig (Figure): Matplotlib Figure object.
        """
        self._fig: Figure = fig

    @property
    def fig(self) -> Figure:
        """
        Returns the matplotlib Figure object.

        Returns:
            Figure: Matplotlib Figure object.
        """
        return self._fig

    def show(
        self,
    ) -> None:
        """
        Shows a drawable object.
        """
        self._fig.show()
        plt.close(self._fig)

    def save(
        self,
        output_path: str | Path,
    ) -> None:
        """
        Saves a drawable object to the specified output path.

        Args:
            output_path (str | Path): Output path.
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self._fig.savefig(Path(output_path))
