from typing import Any

from matplotlib.axes import Axes

from plotter.core.base import Renderable
from plotter.core.plot import Plot


class Multiplot(Renderable):
    """
    Class for creating a multiplot.
    """

    def __init__(
        self,
        plots: list[Plot],
        **kwargs: Any,
    ):
        """
        Initializes a multiplot.

        Args:
            plots (list[Plot]): List of Plot objects.
            **kwargs (Any): Additional keyword arguments for the multiplot.
        """
        super().__init__(**kwargs)

        self._plots: list[Plot] = plots

        self.render(self.ax)
        self.finalize()

    def render(
        self,
        ax: Axes,
    ) -> None:
        """
        Renders the multiplot on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        for plot in self._plots:
            plot.draw(ax)

        self._finalize_axes(ax)
