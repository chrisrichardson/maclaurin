
import math
from math import factorial

class Maclaurin(object):

    def evaluate(self, n, x):
        return sum(self.term(i) * x**i for i in range(n))


class Sin(Maclaurin):

    def term(self, i):
        val = 0.0
        if (i % 2 == 1):
            m = (i - 1) // 2
            val = (-1.0)**m / factorial(i)
        return val
