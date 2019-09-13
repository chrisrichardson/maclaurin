
from math import factorial


class Maclaurin(object):

    def evaluate(self, n, x):
        return sum(self.term(i) * x**i for i in range(n))


class Sin(Maclaurin):

    def term(self, i):
        val = 0.0
        if (i % 2 == 1):
            m = (i - 1) // 2
            val = (-1)**m / factorial(i)
        return val


class Exp(Maclaurin):

    def term(self, i):
        return 1 / factorial(i)

class Log1(Maclaurin):
    def term(self, i):
        if i == 0:
            return 0
        return (-1)**(i + 1) / i
