import numpy as np
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from plotter.core.multiplot import Multiplot
from plotter.core.plot import LinePlot


def test_multiplot():
    x: np.ndarray = np.array([0, 1, 2, 3])
    y: np.ndarray = np.array([0, 1, 4, 9])
    z: np.ndarray = np.array([0, 1, 16, 36])

    quadratic_plot: LinePlot = LinePlot(
        x,
        y,
        label="Quadratic",
    )

    cubic_plot: LinePlot = LinePlot(
        x,
        z,
        label="Cubic",
    )

    multiplot: Multiplot = Multiplot(
        [quadratic_plot, cubic_plot],
        title="Test",
        xlabel="X",
        ylabel="Y",
    )

    axes: list[Axes] = multiplot.fig.axes
    assert len(axes) == 1

    assert axes[0].get_title() == "Test"
    assert axes[0].get_xlabel() == "X"
    assert axes[0].get_ylabel() == "Y"

    lines: list[Line2D] = axes[0].get_lines()
    assert len(lines) == 2

    np.testing.assert_array_equal(lines[0].get_xdata(), x)
    np.testing.assert_array_equal(lines[0].get_ydata(), y)
    assert lines[0].get_label() == "Quadratic"

    np.testing.assert_array_equal(lines[1].get_xdata(), x)
    np.testing.assert_array_equal(lines[1].get_ydata(), z)
    assert lines[1].get_label() == "Cubic"
