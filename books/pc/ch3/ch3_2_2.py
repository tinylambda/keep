from decimal import Decimal
from decimal import localcontext


a = Decimal("4.2")
b = Decimal("2.1")
c = a + b
print(c)

print(a + b == c)

print("-" * 64)

a = Decimal("1.3")
b = Decimal("1.7")
print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)
