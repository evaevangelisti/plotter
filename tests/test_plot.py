import numpy as np
import pytest
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from plotter.core.plot import LinePlot


@pytest.fixture(
    params=[
        {
            "x": np.array([0, 1, 2, 3]),
            "y": np.array([0, 1, 4, 9]),
            "label": "Quadratic",
            "color": "C0",
            "title": "Test - Quadratic",
            "xlabel": "X",
            "ylabel": "Y",
            "show_legend": True,
            "force_origin": False,
            "remove_margins": False,
        },
        {
            "x": np.array([0, 1, 2, 3]),
            "y": np.array([0, 1, 16, 36]),
            "label": "Cubic",
            "color": "C1",
            "title": "Test - Cubic",
            "xlabel": "X",
            "ylabel": "Y",
            "show_legend": True,
            "force_origin": False,
            "remove_margins": False,
        },
    ]
)
def line_plot(
    request,
) -> LinePlot:
    return LinePlot(
        x=request.param["x"],
        y=request.param["y"],
        label=request.param["label"],
        color=request.param["color"],
        title=request.param["title"],
        xlabel=request.param["xlabel"],
        ylabel=request.param["ylabel"],
    )


def test_lineplot(
    line_plot: LinePlot,
) -> None:
    axes: list[Axes] = line_plot.fig.axes
    assert len(axes) == 1

    assert axes[0].get_title() == line_plot._title
    assert axes[0].get_xlabel() == line_plot._xlabel
    assert axes[0].get_ylabel() == line_plot._ylabel

    lines: list[Line2D] = axes[0].get_lines()
    assert len(lines) == 1

    np.testing.assert_array_equal(lines[0].get_xdata(), line_plot._x)
    np.testing.assert_array_equal(lines[0].get_ydata(), line_plot._y)
    assert lines[0].get_label() == line_plot._label
