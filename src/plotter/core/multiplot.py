import matplotlib.pyplot as plt

from plotter.core.drawable import Drawable
from plotter.core.plot import Plot
from plotter.utils import _format_axes


class Multiplot(Drawable):
    """
    Class for creating a multiplot.
    """

    def __init__(
        self,
        plots: list[Plot],
        figsize: tuple[float, float] = (6.4, 4.8),
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
        self._fig, ax = plt.subplots(figsize=figsize)

        for plot in plots:
            plot.draw(ax)

        _format_axes(
            ax,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            show_legend=show_legend,
            force_origin=force_origin,
            remove_margins=remove_margins,
        )

        plt.tight_layout()

        super().__init__(self._fig)
