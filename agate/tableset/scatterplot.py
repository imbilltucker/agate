#!/usr/bin/env python
# pylint: disable=W0212

import leather

from agate import utils


def scatterplot(self, x=0, y=1, path=None, width=None, height=None):
    """
    Render a lattice/grid of scatterplots using `leather`.

    :param x:
        The name or index of a column to plot as the x axis of the chart.
        Defaults to the first column in the table.
    :param y:
        The name or index of a column to plot as the y axis of the chart.
        Defaults to the second column in the table.
    :param path:
        If specified, the resulting SVG will be saved to this location. If
        :code:`None` and running in IPython, then the SVG will be rendered
        inline. Otherwise, the SVG data will be returned as a string.
    :param width:
        The width of the output SVG.
    :param height:
        The height of the output SVG.
    """
    chart = leather.Lattice(shape=leather.Dots())
    chart.add_x_axis(name=x)
    chart.add_y_axis(name=y)
    chart.add_many(self.values(), x=x, y=y, titles=self.keys())

    return chart.to_svg(path=path, width=width, height=height)
