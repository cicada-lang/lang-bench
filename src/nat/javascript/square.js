class Zero {
  constructor() {}
}

class Add1 {
  constructor(prev) { this.prev = prev }
}

function iszero(target) {
  return target instanceof Zero
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
  if (iszero(target))
    return addend
  else
    return add1(add(target.prev, addend))
}

function mul(target, mulend) {
  if (iszero(target))
    return zero()
  else
    return add(mul(target.prev, mulend), mulend)
}

function square(x) {
  return mul(x, x)
}

square(square(square(square(two()))))
