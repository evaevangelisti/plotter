from abc import ABC, abstractmethod
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from plotter.style import DEFAULT_FIGSIZE


class Exportable(ABC):
    """
    Abstract base class for exportable objects.
    """

    def __init__(
        self,
        nrows: int = 1,
        ncols: int = 1,
        figsize: tuple[float, float] = DEFAULT_FIGSIZE,
    ):
        """
        Initializes an exportable object.

        Args:
            nrows (int): Number of rows in the figure.
            ncols (int): Number of columns in the figure.
            figsize (tuple[float, float]): Figure size in inches.
        """
        self._fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        self._axes: list[Axes] = [axes] if isinstance(axes, Axes) else list(axes.flat)

    @property
    def fig(
        self,
    ) -> Figure:
        """
        Returns the matplotlib Figure object.

        Returns:
            Figure: Matplotlib Figure object.
        """
        return self._fig

    @property
    def axes(
        self,
    ) -> list[Axes]:
        """
        Returns the list of Matplotlib Axes objects.

        Returns:
            list[Axes]: List of Matplotlib Axes objects.
        """
        return self._axes

    def finalize(
        self,
    ) -> None:
        """
        Finalizes the exportable object.
        """
        plt.tight_layout()

    def show(
        self,
    ) -> None:
        """
        Shows an exportable object.
        """
        self._fig.show()
        plt.close(self._fig)

    def save(
        self,
        output_path: str | Path,
    ) -> None:
        """
        Saves an exportable object to the specified output path.

        Args:
            output_path (str | Path): Output path.
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self._fig.savefig(Path(output_path))


class Renderable(Exportable, ABC):
    """
    Abstract base class for renderable objects.
    """

    def __init__(
        self,
        figsize: tuple[float, float] = DEFAULT_FIGSIZE,
        title: str = "",
        xlabel: str = "",
        ylabel: str = "",
        show_legend: bool = True,
        force_origin: bool = False,
        remove_margins: bool = False,
    ):
        """
        Initializes a renderable object.

        Args:
            figsize (tuple[float, float]): Figure size in inches.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
            show_legend (bool): Whether to show the legend.
            force_origin (bool): Whether to force axes to start at zero.
            remove_margins (bool): Whether to remove margins around the plot.
        """
        super().__init__(figsize=figsize)

        self._title: str = title
        self._xlabel: str = xlabel
        self._ylabel: str = ylabel
        self._show_legend: bool = show_legend
        self._force_origin: bool = force_origin
        self._remove_margins: bool = remove_margins

    @property
    def ax(self) -> Axes:
        """
        Returns the first Axes object from the list of axes.

        Returns:
            Axes: First Axes object.
        """
        return self._axes[0]

    def _finalize_axes(
        self,
        ax: Axes,
    ) -> None:
        """
        Finalizes the given axes.

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

        if self._show_legend:
            _, labels = ax.get_legend_handles_labels()
            if labels and any(labels):
                ax.legend()

        if self._force_origin:
            ax.set_xlim(left=0)
            ax.set_ylim(bottom=0)

        if self._remove_margins:
            ax.margins(x=0, y=0)

    @abstractmethod
    def render(
        self,
        ax: Axes,
    ) -> None:
        """
        Abstract method to render the plot on the given axes.

        Args:
            ax (Axes): Axes object.
        """
        pass
