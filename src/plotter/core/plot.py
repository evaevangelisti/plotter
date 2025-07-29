from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


class Plot(ABC):
    """
    Abstract class for Matplotlib plots.
    """

    def __init__(
        self,
        figsize: tuple[float, float] = (8, 5),
        title: str = "",
        xlabel: str = "",
        ylabel: str = "",
        force_origin: bool = True,
        remove_margins: bool = True,
    ):
        """
        Initializes the plot with common parameters.

        Args:
            figsize (tuple[float, float]): Figure size in inches.
            title (str | None): Plot title.
            xlabel (str | None): X-axis label.
            ylabel (str | None): Y-axis label.
            force_origin (bool): Whather to force axes to start at zero.
            remove_margins (bool): Whether to remove margins around the plot.
        """
        self._title: str = title
        self._xlabel: str = xlabel
        self._ylabel: str = ylabel
        self._force_origin: bool = force_origin
        self._remove_margins: bool = remove_margins

        self._fig, self._ax = plt.subplots(figsize=figsize)
        self._plot(self._ax)
        self._format(self._ax)
        plt.tight_layout()

    @abstractmethod
    def _plot(
        self,
        ax: Axes,
    ) -> None:
        """
        Abstract method to plot data on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        pass

    def _format(
        self,
        ax: Axes,
    ) -> None:
        """
        Applies standard formatting to the axes.

        Args:
            ax (Axes): Axes object.
        """
        ax.set_title(self._title)
        ax.set_xlabel(self._xlabel)
        ax.set_ylabel(self._ylabel)

        ax.minorticks_on()
        ax.tick_params(
            which="both",
            direction="in",
            bottom=True,
            top=True,
            left=True,
            right=True,
        )

        _, labels = ax.get_legend_handles_labels()
        if labels and any(labels):
            ax.legend()

        if self._force_origin:
            ax.set_xlim(left=0)
            ax.set_ylim(bottom=0)

        if self._remove_margins:
            ax.margins(x=0, y=0)

    def draw(
        self,
        ax: Axes,
    ) -> Axes:
        """
        Draws the plot on the given axes.

        Args:
            ax (Axes): Axes object.

        Returns:
            Axes: Modifided axes object.
        """
        self._plot(ax)
        self._format(ax)

        return ax

    def show(
        self,
    ) -> None:
        """
        Shows the plot.
        """
        self._fig.show()
        plt.close(self._fig)

    def save(
        self,
        output_path: str | Path,
    ) -> None:
        """
        Saves the plot to the specified output path.

        Args:
            output_path (str | Path): Path to save the plot.
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self._fig.savefig(Path(output_path))


class LinePlot(Plot):
    """
    A class for creating line plots using Matplotlib.
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
        Initializes a line plot with the given data.

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

    def _plot(
        self,
        ax: Axes,
    ) -> None:
        """
        Plots the line on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        ax.plot(
            self._x,
            self._y,
            label=self._label,
            color=self._color,
        )
