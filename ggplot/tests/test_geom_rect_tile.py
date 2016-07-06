from __future__ import absolute_import, division, print_function

import pandas as pd

from .. import ggplot, aes, geom_rect, geom_tile, labs, theme
from .conftest import cleanup

n = 4

df = pd.DataFrame({
        'xmin': range(1, n*2, 2),
        'xmax': range(2, n*2+1, 2),
        'ymin': [1] * n,
        'ymax': [2] * n,
        'z': range(n)
    })

# geom_rect and geom_tile are similar but
# parameterised different
# for geom_tile
df['x'] = df['xmin'] + 0.5
df['y'] = df['ymin'] + 0.5


@cleanup
def test_aesthetics():
    # leave enough room for the legend
    _theme = theme(facet_spacing={'right': 0.8})

    # rect
    p = (ggplot(df, aes(xmin='xmin', xmax='xmax',
                        ymin='ymin', ymax='ymax')) +
         geom_rect() +
         geom_rect(aes(ymin='ymin+2', ymax='ymax+2',
                       alpha='z'),
                   show_legend=False) +
         geom_rect(aes(ymin='ymin+4', ymax='ymax+4',
                       fill='factor(z)')) +
         geom_rect(aes(ymin='ymin+6', ymax='ymax+6',
                       color='factor(z+1)'), size=2) +
         geom_rect(aes(ymin='ymin+8', ymax='ymax+8',
                       linetype='factor(z+2)'),
                   color='yellow', size=2) +
         _theme +
         # for comparison with geom_tile which
         # has labels by default
         labs(x='x', y='y'))

    assert p == 'aesthetics'

    # tile
    p = (ggplot(df, aes('x', 'y', width=1, height=1)) +
         geom_tile() +
         geom_tile(aes(y='y+2', alpha='z'),
                   show_legend=False) +
         geom_tile(aes(y='y+4', fill='factor(z)')) +
         geom_tile(aes(y='y+6', color='factor(z+1)'), size=2) +
         geom_tile(aes(y='y+8', linetype='factor(z+2)'),
                   color='yellow', size=2) +
         _theme)

    assert p == 'aesthetics'
