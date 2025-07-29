import numpy as np
from matplotlib.lines import Line2D

from plotter.core.plot import LinePlot


def test_lineplot():
    x: np.ndarray = np.array([0, 1, 2, 3])
    y: np.ndarray = np.array([0, 1, 4, 9])

    plot: LinePlot = LinePlot(
        x,
        y,
        label="Quadratic",
        title="Test",
        xlabel="X",
        ylabel="Y",
    )

    lines: list[Line2D] = plot._ax.get_lines()
    assert len(lines) == 1

    line: Line2D = lines[0]
    np.testing.assert_array_equal(line.get_xdata(), x)
    np.testing.assert_array_equal(line.get_ydata(), y)
    assert line.get_label() == "Quadratic"

    assert plot._ax.get_title() == "Test"
    assert plot._ax.get_xlabel() == "X"
    assert plot._ax.get_ylabel() == "Y"
