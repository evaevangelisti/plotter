import numpy as np
import pytest
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from plotter.core.multiplot import Multiplot
from plotter.core.plot import LinePlot, Plot


@pytest.fixture(
    params=[
        {
            "plots": [
                {
                    "type": LinePlot,
                    "x": np.array([0, 1, 2, 3]),
                    "y": np.array([0, 1, 4, 9]),
                    "label": "Quadratic",
                    "color": "C0",
                },
            ],
            "title": "Test - Single Multiplot",
            "xlabel": "X",
            "ylabel": "Y",
            "show_legend": True,
            "force_origin": False,
            "remove_margins": False,
        },
        {
            "plots": [
                {
                    "type": LinePlot,
                    "x": np.array([0, 1, 2, 3]),
                    "y": np.array([0, 1, 4, 9]),
                    "label": "Quadratic",
                    "color": "C0",
                },
                {
                    "type": LinePlot,
                    "x": np.array([0, 1, 2, 3]),
                    "y": np.array([0, 1, 8, 27]),
                    "label": "Cubic",
                    "color": "C1",
                },
            ],
            "title": "Test - Multiplot",
            "xlabel": "X",
            "ylabel": "Y",
            "show_legend": True,
            "force_origin": False,
            "remove_margins": False,
        },
    ]
)
def multiplot(
    request,
) -> Multiplot:
    plots: list[Plot] = []

    for plot in request.param["plots"]:
        plots.append(
            plot["type"](
                x=plot["x"],
                y=plot["y"],
                label=plot["label"],
                color=plot["color"],
            )
        )

    return Multiplot(
        plots,
        title=request.param["title"],
        xlabel=request.param["xlabel"],
        ylabel=request.param["ylabel"],
    )


def test_multiplot(
    multiplot: Multiplot,
) -> None:
    axes: list[Axes] = multiplot.fig.axes
    assert len(axes) == 1

    assert axes[0].get_title() == multiplot._title
    assert axes[0].get_xlabel() == multiplot._xlabel
    assert axes[0].get_ylabel() == multiplot._ylabel

    lines: list[Line2D] = axes[0].get_lines()
    assert len(lines) == len(multiplot._plots)
