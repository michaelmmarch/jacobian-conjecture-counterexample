# Jacobian Conjecture — Counterexample (Alpoge, July 20 2026)

## Source

Levent Alpoge (@__alpoge__), posted July 20 2026:
https://x.com/__alpoge__/status/2079028340955197566

Credits Akhil (Mathew) for posing the question and Claude Fable for computational assistance.

## The counterexample

The map F: C^3 -> C^3 defined by:

    F(x,y,z) = ( (1+xy)^3 z + y^2 (1+xy)(4+3xy),
                  y + 3x (1+xy)^2 z + 3x y^2 (4+3xy),
                  2x - 3x^2 y - x^3 z )

has:

1. **Jacobian determinant = -2** (constant, nonzero — satisfies JC hypothesis)
2. **Three distinct preimages of (-1/4, 0, 0)**:
   - (0, 0, -1/4)
   - (1, -3/2, 13/2)
   - (-1, 3/2, 13/2)

Both claims verified symbolically (sympy), by cofactor expansion, by hand at
multiple points, and by complete solution of the fiber. The fiber over (-1/4,0,0)
has *exactly* three points.

The map generically has degree 3: the fiber over (a, 0, 0) is:
- (0, 0, a)
- (±1/(2√(-a)), ∓3√(-a), -26a)

These coalesce / escape to infinity as a -> 0, confirming the map is not proper.

## Structural notes

Let w = (1+xy)^2 z + y^2(4+3xy). Then:
- F_1 = (1+xy) · w
- F_2 = y + 3x · w
- F_3 = x · (2 - 3xy - x^2 z)

The first two components share the common factor w. The third component is
independent. The map has degree 7 (via the x^3 y^3 z term in F_1).

### How it was likely constructed (reconstructed by Claude in conversation with Sriram)

Source: https://claude.ai/share/22abed98-d9af-43c5-9881-b19e009a07b0

**1. Forced shape from partial results.**
Campbell's theorem: Galois Keller maps are invertible. Quadratic extensions are
automatically Galois, so degree 2 is impossible. Minimum generic degree is 3,
with S_3 monodromy (non-Galois). The map must be non-proper (proper étale maps
of C^n are covers, and C^n is simply connected).

**2. The seed: Vitushkin's rational "counterexample".**
F = (x^2 y^6 + 2xy^2, xy^3 + 1/y) on C^2 has constant Jacobian -2 and identifies
(-3,-1) with (1,1) — but has a pole, so it proves nothing. Alpoge's map fixes
exactly this defect: both have det = -2, and the mechanism is composing two maps
with non-constant Jacobians δ and -2/δ that cancel. In 2D the reciprocal forces
denominators; the third variable provides room to absorb them polynomially.

**3. Affine-linear in z.**
The map is F = A(x,y) + z·B(x,y) with B = (s^3, 3xs^2, -x^3) where s = 1+xy.
The s^2 factor in front of z is precisely the Jacobian factor being cancelled
polynomially instead of rationally.

**4. The Z/2 equivariance trick.**
The map satisfies F(-x, -y, z) = (F_1, -F_2, -F_3). This symmetry is an ansatz
that makes non-injectivity automatic: every point on the curve {F_2 = F_3 = 0}
collides with its mirror image. The pair (±1, ∓3/2, 13/2) lives there, while
(0, 0, -1/4) sits on the symmetry axis, completing the 2+1 fiber — the signature
of a non-Galois cubic.

**5. CAS closes the system.**
The equivariance converts "find a non-injective Keller map" (hopeless to search
directly) into "solve a finite algebraic system on a symmetric, z-linear ansatz"
— a Gröbner-basis grind, plausibly what Fable spent its tokens on.

**Recipe summary:** theorems → forced shape; Vitushkin → cancellation mechanism
and the constant -2; equivariance → non-injectivity for free; CAS → close the
system.

### Fiber geometry

Eliminating z gives x^3 F_1 + s^3 F_3 = xs(2+xy), so preimages of (a,b,c) are
cut out by a conic and a cubic in the (x,s)-plane whose excess intersections were
arranged to escape to infinity.

## What this settles

The Jacobian conjecture (Keller, 1939 — Smale's problem #16) is FALSE.

Statement: if F: C^n -> C^n is a polynomial map with det(JF) a nonzero constant,
then F is a polynomial automorphism.

Alpoge's map satisfies the hypothesis (det JF = -2) and violates the conclusion
(not injective, hence not an automorphism).

### GPT-5.6 structural analysis: "Weighted Quotients of Keller Maps" (same day)

Source: https://x.com/ThomasCabaret84/status/2079122383655342118
(Thomas Cabaret, screenshots of GPT-5.6 output — saved as PNGs in this folder)

GPT-5.6 produced a full 4-page paper within hours of the announcement, going
beyond verification to provide structural framework.

**The G_m action.** The Z/2 symmetry is part of a full multiplicative group action:
- Source: λ·(x,y,z) = (λx, λ⁻¹y, λ⁻²z)  [weights (1,-1,-2)]
- Target: λ★(P,Q,R) = (λ⁻²P, λ⁻¹Q, λR)  [weights (-2,-1,1)]

Alpoge's map is equivariant: F(λ·(x,y,z)) = λ★F(x,y,z).

**Invariant rings.** Source invariants: k[ν,v] where ν = xy, v = x²z.
Target invariants: k[a,b] where a = PR², b = QR. Both quotients are affine planes.

**Normal form (Lemma 2.1).** Weighted equivariant maps have: x²P = α(ν,v),
xQ = β(ν,v), R = xγ(ν,v). The quotient map is Φ = (αγ², βγ): A² → A².

**Theorem 3.1 (Jacobian reduction).** det Jac(Φ) = γ² det Jac(F).
The geometric degrees of F and Φ agree. This reduces the 3D problem to 2D.

**Corollary 3.2 (Exact correction).** For weighted-equivariant Keller maps:
  F is automorphism ⟺ quotient Φ is birational ⟺ [k(ν,v) : k(a,b)] = 1.
A computable, coefficient-level criterion.

**Applied to Alpoge's map (Section 4).** Setting r = 1+ν, c = 2-3ν-v, q = cr:
- x²P = α = r(r+1-cr²),  xQ = β = 4r+2-3cr²
- Quotient factors as (ν,v) →ρ (q,c) →ψ (a,b)
  - ρ(ν,v) = ((2-3ν-v)(1+ν), 2-3ν-v)     [birational, not proper]
  - ψ(q,c) = (q²+cq-q³, 4q+2c-3q²)       [finite, degree 3]
- Jacobian factors cancel against the orbit-direction factor.
- Non-properness set: 27A²C² - 18ABC + 16A + B³C - B² = 0

This explains *why* the map works: the torus quotient retains the generic
multiplicity. The 3D map = 1D orbit direction + 2D quotient dynamics. The orbit
direction contributes a predictable Jacobian factor but doesn't change the number
of generic sheets.

### Geometric interpretation: "forgetting the marked point" (Andy Jiang / GPT)

Source: https://x.com/davikrehalt/status/2079175065695035442

This gives the coordinate-free meaning of Alpoge's map. The polynomial formula
is just the coordinate expression for a completely natural geometric operation.

**Setup.** Think of P^1 as a line (the Riemann sphere / complex projective line).

- Sym^k(P^1) = the space of unordered k-tuples of points on P^1.
  Sym^2(P^1) ≅ P^2, Sym^3(P^1) ≅ P^3.
  (Think: an unordered triple {a,b,c} on P^1 is the same as a degree-3
  polynomial up to scaling, which has 4 coefficients, so it lives in P^3.)

- P^1 × Sym^2(P^1) = "a marked point p, plus an unordered pair {q,r}."

**The map.** π: P^1 × Sym^2(P^1) → Sym^3(P^1) sends (p, {q,r}) ↦ {p,q,r}.
In words: "forget which of the three points was marked."

**Why it's 3-to-1.** Given a triple {a,b,c}, there are exactly 3 ways to choose
which point to mark: (a,{b,c}), (b,{a,c}), or (c,{a,b}). This is the generic
fiber of π.

**Why it's étale.** Away from the ramification locus R (where two or more points
coincide), forgetting a label is a local isomorphism — nearby triples with
different markings stay distinct.

**Getting to affine space.** Choose a hyperplane H ⊂ Sym^3(P^1) ≅ P^3 that is
"tangent but not osculating to the small diagonal" (a careful choice of
hyperplane at infinity). Then:
  X := (P^1 × Sym^2(P^1)) \ (R ∪ π^{-1}(H)) ≅ A^3  (≅ C^3)
  Y := Sym^3(P^1) \ H ≅ A^3                          (≅ C^3)
The restricted map π|_X : A^3 → A^3 is Alpoge's counterexample.

**What this explains:**
- Degree 3: three ways to mark a point in a triple.
- Étale (constant nonzero Jacobian): forgetting a label is locally trivial.
- Not proper: we removed closed subsets from projective varieties.
- Non-Galois monodromy: the fiber is S_3/S_2 (three cosets of the stabilizer
  of the marked point). S_2 is not normal in S_3, so the covering is not
  Galois — exactly what Campbell's theorem requires for a counterexample.
- The Z/2 symmetry: swapping the unmarked pair {q,r} is trivial (they're
  unordered), but acts nontrivially on the source coordinates.
- The specific coefficients: not engineered, but forced by the geometry.

**Accessible analogy.** Imagine three people standing in a room. You photograph
them and label one as "the speaker." The map π is "erase the label." Given an
unlabeled photo, there are three possible labelings — that's the 3-to-1 fiber.
The map is locally invertible (if people are far apart, small perturbations
preserve who's closest to the podium), but globally ambiguous. Alpoge's
polynomial formula is just the coordinate algebra for this operation, after
choosing the right coordinates on both sides.

### Cusp catastrophe interpretation (Claude artifact)

Source: https://claude.ai/public/artifacts/f6f4706a-c4d9-4630-b454-859057c08527

The 2D quotient map (from the GPT-5.6 reduction) can be visualized by plotting
the input w as height over the output (P, Q) plane. The resulting surface is a
**cusp catastrophe** — the standard object in bifurcation theory for exactly this
pattern: smooth everywhere, yet multi-valued over a wedge-shaped "pleated" region.

- Inside the pleat: three different heights (inputs) above one ground point (output).
- Outside: only one.
- The fold curve (bright edge) is the discriminant locus.
- The counterexample is the P = 0 slice through this surface.

Sliding the slice past roughly P ≈ 0.16, the count drops from 3 to 1 — the
slicing plane leaves the pleated region entirely.

This connects the counterexample to well-studied phenomena in optics (caustics),
structural engineering (buckling), and phase transitions. The folding is not
exotic — it's a completely standard bifurcation shape, hiding inside a polynomial
map with constant Jacobian.

### Naskręcki's unified exposition (Jupyter Book + Manim)

Source: https://x.com/nasqret/status/2079384176269177188

Bartosz Naskręcki created a repository with a Jupyter Book and Manim-animated
video tutorial, uniformly explaining the three approaches (Alpoge, Andy Jiang,
Aaron Lou). Landing page and GitHub repo linked from the tweet.

## Threads to explore

### 1. Consequences — what falls with the conjecture
- [ ] Dixmier conjecture (Belov-Kanel & Kontsevich 2007: JC equivalent to DC)
- [ ] Connections to the Markus-Yamabe conjecture (already false for n >= 2)
- [ ] Bass-Connell-Wright / Yagzhev reduction: JC is equivalent to JC for cubic
      homogeneous maps — what does the induced cubic counterexample look like?
- [ ] Implications for the Cremona group and birational geometry
- [ ] Impact on commutative algebra (locally nilpotent derivations, etc.)

### 2. Understanding the construction
- [ ] How was the map found? What family was being explored?
- [ ] Role of the w-factorization — is there a geometric interpretation?
- [ ] Can it be decomposed as a composition of simpler maps?
- [ ] Connection to known classes: de Jonquières maps, Nagata-type maps?

### 3. Sharpness and minimality
- [ ] Is degree 7 minimal? Can JC fail at degree 3, 4, 5, 6?
- [ ] Is n=3 minimal? (JC is true for n=1; verified for n=2 up to degree 100)
- [ ] What is the smallest degree counterexample in each dimension?

### 4. The fiber structure
- [ ] Full discriminant locus (where the fiber has < 3 points)
- [ ] Topology of the map as a branched covering
- [ ] Image of F — is it all of C^3? (Ax's theorem requires injectivity)

### 5. Community response
- [ ] Track formal verification efforts (Lean/Coq)
- [ ] Track expert commentary and follow-up papers
- [ ] Track downstream retractions / revisions of conditional results

## Verification script

```python
from sympy import symbols, Matrix, simplify, Rational, expand, det

x, y, z = symbols('x y z')
u = 1 + x*y

F1 = u**3 * z + y**2 * u * (4 + 3*x*y)
F2 = y + 3*x * u**2 * z + 3*x * y**2 * (4 + 3*x*y)
F3 = 2*x - 3*x**2 * y - x**3 * z

F = Matrix([F1, F2, F3])
J = F.jacobian([x, y, z])

# Jacobian determinant
assert simplify(J.det()) == -2

# Three preimages of (-1/4, 0, 0)
for p in [(0,0,-1/4), (1,-3/2,13/2), (-1,3/2,13/2)]:
    v = F.subs([(x,p[0]),(y,p[1]),(z,p[2])])
    assert v == Matrix([-1/4, 0, 0])
```
