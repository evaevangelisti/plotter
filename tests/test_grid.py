import numpy as np
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from plotter.core.grid import Grid
from plotter.core.plot import LinePlot


def test_grid():
    x: np.ndarray = np.array([0, 1, 2, 3])
    y: np.ndarray = np.array([0, 1, 4, 9])
    z: np.ndarray = np.array([0, 1, 16, 36])

    quadratic_plot: LinePlot = LinePlot(
        x,
        y,
        label="Quadratic",
        title="Test - Quadratic",
        xlabel="X",
        ylabel="Y",
    )

    cubic_plot: LinePlot = LinePlot(
        x,
        z,
        label="Cubic",
        title="Test - Cubic",
        xlabel="X",
        ylabel="Z",
    )

    grid: Grid = Grid([quadratic_plot, cubic_plot], ncols=2)

    axes: list[Axes] = grid._fig.axes
    assert len(axes) == 2

    quadratic_lines: list[Line2D] = axes[0].get_lines()
    assert len(quadratic_lines) == 1

    np.testing.assert_array_equal(quadratic_lines[0].get_xdata(), x)
    np.testing.assert_array_equal(quadratic_lines[0].get_ydata(), y)
    assert quadratic_lines[0].get_label() == "Quadratic"

    assert axes[0].get_title() == "Test - Quadratic"
    assert axes[0].get_xlabel() == "X"
    assert axes[0].get_ylabel() == "Y"

    cubic_lines: list[Line2D] = axes[1].get_lines()
    assert len(cubic_lines) == 1

    np.testing.assert_array_equal(cubic_lines[0].get_xdata(), x)
    np.testing.assert_array_equal(cubic_lines[0].get_ydata(), z)
    assert cubic_lines[0].get_label() == "Cubic"

    assert axes[1].get_title() == "Test - Cubic"
    assert axes[1].get_xlabel() == "X"
    assert axes[1].get_ylabel() == "Z"
