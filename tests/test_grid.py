import numpy as np
import pytest
from matplotlib.axes import Axes

from plotter import Grid, LinePlot, Multiplot
from plotter.base import Renderable
from plotter.plot import Plot


@pytest.fixture(
    params=[
        [
            {
                "type": LinePlot,
                "x": np.array([0, 1, 2, 3]),
                "y": np.array([0, 1, 4, 9]),
                "label": "Quadratic",
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
                    },
                    {
                        "type": LinePlot,
                        "x": np.array([0, 1, 2, 3]),
                        "y": np.array([0, 1, 8, 27]),
                        "label": "Cubic",
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
