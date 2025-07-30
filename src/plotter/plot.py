from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from matplotlib.axes import Axes

from .base import Renderable
from .style import DEFAULT_FIGSIZE


class Plot(Renderable, ABC):
    """
    Abstract base class for creating plots.
    """

    def __init__(
        self,
        **kwargs: Any,
    ):
        """
        Initializes a plot.

        Args:
            **kwargs (Any): Keyword arguments forwarded to Renderable.
        """
        super().__init__(**kwargs)

        self.render(self.ax)
        self.finalize()

    @abstractmethod
    def draw(
        self,
        ax: Axes,
    ) -> None:
        """
        Abstract method to draw the plot on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        pass

    def render(
        self,
        ax: Axes,
    ) -> None:
        """
        Renders the plot on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        self.draw(ax)
        self._finalize_axes(ax)


class LinePlot(Plot):
    """
    Class for creating a line plot.
    """

    def __init__(
        self,
        x: np.ndarray,
        y: np.ndarray,
        label: str = "",
        color: str = "C0",
        figsize: tuple[float, float] = DEFAULT_FIGSIZE,
        title: str = "",
        xlabel: str = "",
        ylabel: str = "",
        show_legend: bool = True,
        force_origin: bool = False,
        remove_margins: bool = False,
    ):
        """
        Initializes a line plot.

        Args:
            x (np.ndarray): X-axis data.
            y (np.ndarray): Y-axis data.
            label (str): Label for the line.
            color (str): Color of the line.
            figsize (tuple[float, float]): Figure size in inches.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
            show_legend (bool): Whether to show the legend.
            force_origin (bool): Whether to force axes to start at zero.
            remove_margins (bool): Whether to remove margins around the plot.
        """
        self._x: np.ndarray = x
        self._y: np.ndarray = y
        self._label: str = label
        self._color: str = color

        super().__init__(
            figsize=figsize,
            title=title,
            xlabel=xlabel,
            ylabel=ylabel,
            show_legend=show_legend,
            force_origin=force_origin,
            remove_margins=remove_margins,
        )

    def draw(
        self,
        ax: Axes,
    ) -> None:
        """
        Draws the plot on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        ax.plot(
            self._x,
            self._y,
            label=self._label,
            color=self._color,
        )
