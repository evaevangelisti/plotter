from typing import Any

from matplotlib.axes import Axes

from plotter.core.base import Renderable
from plotter.core.plot import Plot
from plotter.style import DEFAULT_FIGSIZE


class Multiplot(Renderable):
    """
    Class for creating a multiplot.
    """

    def __init__(
        self,
        plots: list[Plot],
        figsize: tuple[float, float] = DEFAULT_FIGSIZE,
        title: str = "",
        xlabel: str = "",
        ylabel: str = "",
        show_legend: bool = True,
        force_origin: bool = False,
        remove_margins: bool = False,
    ):
        """
        Initializes a multiplot.

        Args:
            plots (list[Plot]): List of Plot objects.
            figsize (tuple[float, float]): Figure size in inches.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
            show_legend (bool): Whether to show the legend.
            force_origin (bool): Whether to force axes to start at zero.
            remove_margins (bool): Whether to remove margins around the plot.
        """
        super().__init__(
            figsize=figsize,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            show_legend=show_legend,
            force_origin=force_origin,
            remove_margins=remove_margins,
        )

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
