class Zero:
    pass


class Add1:
    def __init__(self, prev):
        self.prev = prev


def iszero(target):
    return isinstance(target, Zero)


def zero():
    return Zero()


def add1(prev):
    return Add1(prev)


def two():
    return add1(add1(zero()))


def add(target, addend):
    if (iszero(target)):
        return addend
    else:
        return add1(add(target.prev, addend))


def mul(target, mulend):
    if (iszero(target)):
        return zero()
    else:
        return add(mul(target.prev, mulend), mulend)

def square(x):
    return mul(x, x)

import sys

sys.setrecursionlimit(10000000)

square(square(square(square(two()))))
