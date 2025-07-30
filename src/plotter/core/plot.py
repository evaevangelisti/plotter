from abc import ABC, abstractmethod
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

from plotter.core.drawable import Drawable
from plotter.utils import _format_axes


class Plot(Drawable, ABC):
    """
    Abstract base class for creating plots.
    """

    def __init__(
        self,
        figsize: tuple[float, float] = (6.4, 4.8),
        title: str = "",
        xlabel: str = "",
        ylabel: str = "",
        show_legend: bool = True,
        force_origin: bool = False,
        remove_margins: bool = False,
    ):
        """
        Initializes a plot.

        Args:
            figsize (tuple[float, float]): Figure size in inches.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
            show_legend (bool): Whether to show the legend.
            force_origin (bool): Whether to force axes to start at zero.
            remove_margins (bool): Whether to remove margins around the plot.
        """
        self._title: str = title
        self._xlabel: str = xlabel
        self._ylabel: str = ylabel
        self._show_legend: bool = show_legend
        self._force_origin: bool = force_origin
        self._remove_margins: bool = remove_margins

        self._fig, ax = plt.subplots(figsize=figsize)
        self.render(ax)

        plt.tight_layout()

        super().__init__(self._fig)

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
        _format_axes(
            ax,
            title=self._title,
            xlabel=self._xlabel,
            ylabel=self._ylabel,
            show_legend=self._show_legend,
            force_origin=self._force_origin,
            remove_margins=self._remove_margins,
        )


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
        **kwargs: Any,
    ):
        """
        Initializes a line plot.

        Args:
            x (np.ndarray): X-axis data.
            y (np.ndarray): Y-axis data.
            label (str): Label for the line.
            color (str): Color of the line.
            **kwargs: Any: Additional keyword arguments for the plot.
        """
        self._x: np.ndarray = x
        self._y: np.ndarray = y
        self._label: str = label
        self._color: str = color

        super().__init__(**kwargs)

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
