from abc import ABC, abstractmethod
from typing import Any

import numpy as np
from matplotlib.axes import Axes

from plotter.core.base import Renderable


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
            **kwargs (Any): Additional keyword arguments for the plot.
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
        **kwargs: Any,
    ):
        """
        Initializes a line plot.

        Args:
            x (np.ndarray): X-axis data.
            y (np.ndarray): Y-axis data.
            label (str): Label for the line.
            color (str): Color of the line.
            **kwargs (Any): Additional keyword arguments for the line plot.
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
