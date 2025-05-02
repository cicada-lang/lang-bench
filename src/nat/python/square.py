class Zero:
    pass

class Add1:
    def __init__(self, prev):
        self.prev = prev

def zero():
    return Zero()


def add1(prev):
    return Add1(prev)


def two():
    return add1(add1(zero()))


def add(target, addend):
    if (isinstance(target, Zero)):
        return addend
    elif (isinstance(target, Add1)):
        return add1(add(target.prev, addend))


def mul(target, mulend):
    if (isinstance(target, Zero)):
        return zero()
    elif (isinstance(target, Add1)):
        return add(mul(target.prev, mulend), mulend)

def square(x):
    return mul(x, x)

import sys

sys.setrecursionlimit(10000000)

square(square(square(square(two()))))
