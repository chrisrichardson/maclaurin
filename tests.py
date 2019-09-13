
from maclaurin import Sin, Exp, Log1
import math


def test_sin():
    w = Sin()
    assert abs(w.evaluate(10, 0.5) - math.sin(0.5)) < 1e-10


def test_exp():
    w = Exp()
    assert abs(w.evaluate(20, 0.5) - math.exp(0.5)) < 1e-10

def test_log1():
    w = Log1()
    assert abs(w.evaluate(50, 0.5) - math.log(1.5)) < 1e-10
