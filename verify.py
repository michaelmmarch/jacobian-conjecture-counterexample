#!/usr/bin/env python3
"""
Jacobian Conjecture Counterexample (Alpoge, July 20 2026)
Verification: confirms det(JF) = -2 and the three preimages of (-1/4, 0, 0)
"""

from sympy import symbols, Matrix, simplify, Rational, expand

x, y, z = symbols('x y z')
u = 1 + x * y

F1 = u**3 * z + y**2 * u * (4 + 3 * x * y)
F2 = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
F3 = 2 * x - 3 * x**2 * y - x**3 * z

F = Matrix([F1, F2, F3])
J = F.jacobian([x, y, z])

print("=" * 60)
print("Jacobian Conjecture Counterexample — Verification")
print("=" * 60)

# 1. Jacobian determinant
det_val = simplify(J.det())
print(f"\n1. Jacobian determinant: {det_val}")
assert det_val == -2, f"FAIL: expected -2, got {det_val}"
print("   PASS: det(JF) = -2 (constant, nonzero)")

# 2. Three preimages of (-1/4, 0, 0)
preimages = [
    (0, 0, Rational(-1, 4)),
    (1, Rational(-3, 2), Rational(13, 2)),
    (-1, Rational(3, 2), Rational(13, 2)),
]

print(f"\n2. Preimages of (-1/4, 0, 0):")
for p in preimages:
    val = F.subs([(x, p[0]), (y, p[1]), (z, p[2])])
    result = (val[0], val[1], val[2])
    print(f"   F({p[0]}, {p[1]}, {p[2]}) = {result}")
    assert result == (Rational(-1, 4), 0, 0), f"FAIL at {p}"

print("   PASS: all three map to (-1/4, 0, 0)")

# 3. Points are distinct
print(f"\n3. Points are distinct:")
print(f"   x-coordinates: {preimages[0][0]}, {preimages[1][0]}, {preimages[2][0]}")
assert len(set(p[0] for p in preimages)) == 3
print("   PASS: three distinct points")

print(f"\n{'=' * 60}")
print("All checks passed. The map satisfies the Jacobian conjecture")
print("hypothesis (det JF = -2, a nonzero constant) but is not injective")
print("(three preimages). This is a counterexample.")
print("=" * 60)
