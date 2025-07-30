from matplotlib.axes import Axes


def _format_axes(
    ax: Axes,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    show_legend: bool = True,
    force_origin: bool = False,
    remove_margins: bool = False,
) -> None:
    """
    Applies standard formatting to the axes.

    Args:
        ax (Axes): Axes object.
        title (str): Plot title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        show_legend (bool): Whether to show the legend.
        force_origin (bool): Whether to force axes to start at zero.
        remove_margins (bool): Whether to remove margins around the plot.
    """
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.minorticks_on()
    ax.tick_params(
        which="both",
        direction="in",
        bottom=True,
        top=True,
        left=True,
        right=True,
    )

    if show_legend:
        _, labels = ax.get_legend_handles_labels()
        if labels and any(labels):
            ax.legend()

    if force_origin:
        ax.set_xlim(left=0)
        ax.set_ylim(bottom=0)

    if remove_margins:
        ax.margins(x=0, y=0)
