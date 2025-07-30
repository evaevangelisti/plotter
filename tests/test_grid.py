import numpy as np
import pytest
from matplotlib.axes import Axes

from plotter.core.base import Renderable
from plotter.core.grid import Grid
from plotter.core.multiplot import Multiplot
from plotter.core.plot import LinePlot, Plot


@pytest.fixture(
    params=[
        [
            {
                "type": LinePlot,
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
                "type": LinePlot,
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
    ]
)
def grid(
    request,
) -> Grid:
    renderables: list[Renderable] = []

    for renderable in request.param:
        if "plots" in renderable:
            plots: list[Plot] = []

            for plot in renderable["plots"]:
                plots.append(
                    plot["type"](
                        x=plot["x"],
                        y=plot["y"],
                        label=plot["label"],
                        color=plot["color"],
                    )
                )

            renderables.append(
                Multiplot(
                    plots,
                    title=renderable["title"],
                    xlabel=renderable["xlabel"],
                    ylabel=renderable["ylabel"],
                )
            )
        else:
            renderables.append(
                renderable["type"](
                    x=renderable["x"],
                    y=renderable["y"],
                    label=renderable["label"],
                    color=renderable["color"],
                    title=renderable["title"],
                    xlabel=renderable["xlabel"],
                    ylabel=renderable["ylabel"],
                )
            )

    return Grid(renderables)


def test_grid(
    grid: Grid,
):
    axes: list[Axes] = grid.fig.axes
    assert len(axes) == len(grid._renderables)
