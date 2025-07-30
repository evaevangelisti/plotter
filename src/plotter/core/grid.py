import matplotlib.pyplot as plt

from plotter.core.drawable import Drawable
from plotter.core.plot import Plot


class Grid(Drawable):
    """
    Class for creating a grid of plots.
    """

    def __init__(
        self,
        plots: list[Plot],
        ncols: int = 3,
        figsize: tuple[float, float] | None = None,
    ):
        """
        Initializes a grid of plots.

        Args:
            plots (list[Plot]): List of Plot objects.
            ncols (int): Number of columns in the grid.
            figsize (tuple[float, float] | None): Figure size in inches.
        """
        self._fig, axes = plt.subplots(
            nrows := (len(plots) + ncols - 1) // ncols,
            ncols,
            figsize=figsize or (6.4 * ncols, 4.8 * nrows),
        )

        axes = axes.flat if hasattr(axes, "flat") else [axes]

        for plot, ax in zip(plots, axes):
            plot.render(ax)

        for ax in axes[len(plots) :]:
            ax.set_visible(False)

        plt.tight_layout()

        super().__init__(self._fig)
