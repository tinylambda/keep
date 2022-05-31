import operator


a = -1
b = 5.0
c = 2
d = 6


print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

print("\nPositive/Negative:")
print("abs(a): ", operator.abs(a))
print("neg(a): ", operator.neg(a))
print("neg(b): ", operator.neg(b))
print("pos(a): ", operator.pos(a))
print("pos(b): ", operator.pos(b))

print("\nArithmetic:")
print("add(a, b): ", operator.add(a, b))
print("floordiv(a, b): ", operator.floordiv(a, b))
print("floordiv(d, c): ", operator.floordiv(d, c))
print("mod(a, b): ", operator.mod(a, b))
print("mul(a, b): ", operator.mul(a, b))
print("pow(c, d): ", operator.pow(c, d))
print("sub(b, a): ", operator.sub(b, a))
print("truediv(a, b): ", operator.truediv(a, b))
print("truediv(d, c): ", operator.truediv(d, c))

print("\nBitwise:")
print("and_(c, d): ", operator.and_(c, d))
print("invert(c): ", operator.invert(c))
print("lshift(c, d): ", operator.lshift(c, d))
print("or_(c, d): ", operator.or_(c, d))
print("rshift(d, c): ", operator.rshift(d, c))
print("xor(c, d): ", operator.xor(c, d))
