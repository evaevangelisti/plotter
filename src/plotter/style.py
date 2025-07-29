from typing import Any

import matplotlib as mpl
import matplotlib.pyplot as plt

DEFAULT_RC: dict[str, Any] = {
    # Font settings
    # ----------------
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 9,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    # Line and tick styling
    # ----------------
    "lines.linewidth": 1.0,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.direction": "in",
    "ytick.direction": "in",
    # Figure and background appearance
    # ----------------
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.grid": False,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    # Export compatibility
    # ----------------
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
}


def get_style() -> mpl.RcParams:
    """
    Returns the current Matplotlib RC parameters.

    Returns:
        mpl.RcParams: Matplotlib RC parameters.
    """
    return mpl.rcParams.copy()


def set_style(
    rc: dict[str, Any] = DEFAULT_RC,
    font: str = "sans-serif",
) -> None:
    """
    Sets Matplotlib RC parameters.

    Args:
        rc (dict[str, Any]): Dictionary of Matplotlib RC parameters.
        font (str): Font family.
    """
    mpl.rcParams.update(rc)
    plt.rcParams["font.family"] = font
