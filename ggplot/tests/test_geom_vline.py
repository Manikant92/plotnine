from __future__ import absolute_import, division, print_function

import pandas as pd
import pytest

from .. import ggplot, aes, geom_vline, geom_point
from ..utils.exceptions import GgplotError
from .conftest import cleanup

df = pd.DataFrame({
        'xintercept': [1, 2],
        'x': [0.5, 3],
        'y': [-1, 1],
        'z': range(2)
    })


@cleanup
def test_aesthetics():
    p = (ggplot(df) +
         geom_point(aes('x', 'y')) +
         geom_vline(aes(xintercept='xintercept'), size=2) +
         geom_vline(aes(xintercept='xintercept+.1', alpha='z'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.2',
                        linetype='factor(z)'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.3',
                        color='factor(z)'),
                    size=2) +
         geom_vline(aes(xintercept='xintercept+.4', size='z')))

    assert p == 'aesthetics'


@cleanup
def test_aes_inheritance():
    with pytest.raises(GgplotError):
        p = (ggplot(df, aes('x', 'y', xintercept='xintercept')) +
             geom_point() +
             geom_vline(size=2))
        print(p)
