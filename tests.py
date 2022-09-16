
from maclaurin import Sin
import math


def test_sin():
    w = Sin()
    assert abs(w.evaluate(10, 0.5) - math.sin(0.5)) < 1e-10
