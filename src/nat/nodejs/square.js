class Zero {
  constructor() {}
}

class Add1 {
  constructor(prev) { this.prev = prev }
}

function zero() {
  return new Zero()
}

function add1(prev) {
  return new Add1(prev)
}

function two() {
  return add1(add1(zero()))
}

function add(target, addend) {
  if (target instanceof Zero)
    return addend
  else if (target instanceof Add1)
    return add1(add(target.prev, addend))
}

function mul(target, mulend) {
  if (target instanceof Zero)
    return zero()
  else if (target instanceof Add1)
    return add(mul(target.prev, mulend), mulend)
}

function square(x) {
  return mul(x, x)
}

square(square(square(square(two()))))
