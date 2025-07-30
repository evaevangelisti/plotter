from .base import Exportable, Renderable
from .style import DEFAULT_FIGSIZE


class Grid(Exportable):
    """
    Class for creating a grid of renderables.
    """

    def __init__(
        self,
        renderables: list[Renderable],
        ncols: int = 3,
        figsize: tuple[float, float] | None = None,
    ):
        """
        Initializes a grid of renderables.

        Args:
            renderables (list[Renderable]): List of Renderable objects.
            ncols (int): Number of columns in the grid.
            figsize (tuple[float, float] | None): Figure size in inches.
        """
        super().__init__(
            nrows=(nrows := (len(renderables) + ncols - 1) // ncols),
            ncols=ncols,
            figsize=figsize or (DEFAULT_FIGSIZE[0] * ncols, DEFAULT_FIGSIZE[1] * nrows),
        )

        self._renderables = renderables

        for renderable, ax in zip(self._renderables, self.axes):
            renderable.render(ax)

        for ax in self.axes[len(self._renderables) :]:
            ax.set_visible(False)

        self.finalize()
