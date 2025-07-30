from pathlib import Path

import matplotlib.pyplot as plt

from plotter.core.plot import Plot


class Grid:
    """
    Class for creating a grid of plots.
    """

    def __init__(
        self,
        plots: list[Plot],
        ncols: int = 3,
        figsize: tuple[float, float] = (10, 6),
    ):
        """
        Initializes a grid of plots.

        Args:
            plots (list[Plot]): List of Plot objects.
            ncols (int): Number of columns in the grid.
            figsize (tuple[float, float]): Figure size in inches.
        """
        self._fig, axes = plt.subplots(
            nrows := (len(plots) + ncols - 1) // ncols,
            ncols,
            figsize=figsize or (6.4 * ncols, 4.8 * nrows),
        )

        axes = axes.flat if hasattr(axes, "flat") else [axes]

        for plot, ax in zip(plots, axes):
            plot.draw(ax)

        for ax in axes[len(plots) :]:
            ax.set_visible(False)

        plt.tight_layout()

    def show(
        self,
    ) -> None:
        """
        Shows the grid of plots.
        """
        self._fig.show()
        plt.close(self._fig)

    def save(
        self,
        output_path: str | Path,
    ) -> None:
        """
        Saves the grid to the specified output path.

        Args:
            output_path (str | Path): Output path.
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self._fig.savefig(Path(output_path))
