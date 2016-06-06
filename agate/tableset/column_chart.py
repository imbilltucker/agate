#!/usr/bin/env python
# pylint: disable=W0212

import leather

from agate import utils


def column_chart(self, label=0, value=1, path=None, width=None, height=None):
    """
    Render a lattice/grid of column charts using `leather`.

    :param label:
        The name or index of a column to plot as the labels of the chart.
        Defaults to the first column in the table.
    :param value:
        The name or index of a column to plot as the values of the chart.
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
    chart = leather.Lattice(shape=leather.Columns())
    chart.add_x_axis(name=label)
    chart.add_y_axis(name=value)
    chart.add_many(self.values(), x=label, y=value, titles=self.keys())

    return chart.to_svg(path=path, width=width, height=height)
