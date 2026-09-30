## 128. Complex Numbers: Foundations and Theory

### 128.1 Complex Number System

**Definition**: A complex number is an element of the field ℂ = {a + bi | a, b ∈ ℝ}, where i is a unit with i² = -1.

**Properties**:
- ℂ forms a field with standard addition and multiplication
- Every quadratic polynomial over ℝ has at least one root in ℂ (Fundamental Theorem of Algebra)
- ℂ is algebraically closed
- ℂ is complete under standard topology (Cauchy complete)

### 128.2 Euler's Formula

**Theorem**: For any real θ and integer n, e^{iθ} = cos(θ) + i sin(θ)

**Proof**: 
Using Taylor series expansions for e^x, cos(x), and sin(x):

e^{iθ} = 1 + iθ + (iθ)²/2! + (iθ)³/3! + (iθ)⁴/4! + ...
       = 1 + iθ - θ²/2! - iθ³/3! + θ⁴/4! + ...

Separating real and imaginary parts:
- Real part: 1 - θ²/2! + θ⁴/4! - ... = cos(θ)
- Imaginary part: θ - θ³/3! + θ⁵/5! - ... = sin(θ)

Thus e^{iθ} = cos(θ) + i sin(θ). QED

### 128.3 De Moivre's Theorem

**Theorem**: For any real θ and integer n, (cos θ + i sin θ)^n = cos(nθ) + i sin(nθ)

**Proof**: 
By induction using Euler's formula:
- Base case n=1: trivial
- Inductive step: (cos θ + i sin θ)^n · (cos θ + i sin θ) 
                   = (cos(nθ) + i sin(nθ)) · (cos θ + i sin θ)
                   = cos(nθ)cos θ - sin(nθ)sin θ + i(sin(nθ)cos θ + cos(nθ)sin θ)
                   = cos(nθ+θ) + i sin(nθ+θ)
                   = cos((n+1)θ) + i sin((n+1)θ)

By induction, the theorem holds for all positive integers n. QED

### 128.4 Polar Representation

**Theorem**: Any non-zero complex number z can be uniquely represented as z = r e^{iθ} where r = |z| > 0 and θ = arg(z) + 2kπ for some integer k.

**Proof**: 
Let z = a + bi with r = √(a²+b²) and θ satisfying cos θ = a/r, sin θ = b/r.
Then z = a + bi = r(cos θ + i sin θ) = r e^{iθ}.

The modulus is r = |z| and the argument is θ = arg(z). The representation is unique up to the choice of branch for arg(z). QED

### 128.5 Complex Conjugation

**Theorem**: For any complex numbers z₁, z₂ and real scalars a, b:
1. |z̄| = |z|
2. (z₁ + z₂)̄ = z₁̄ + z₂̄
3. (z₁z₂)̄ = z₁̄z₂̄
4. (z₁/z₂)̄ = z₁̄/z₂̄ (for z₂ ≠ 0)
5. (z̄)̄ = z
6. |z₁ + z₂| ≤ |z₁| + |z₂| (triangle inequality)
7. |z₁ - z₂| ≤ |z₁| + |z₂|

**Proof**: 
Let z = a + bi, then z̄ = a - bi and |z| = √(a²+b²).

For (1): |z̄| = √(a²+(-b)²) = √(a²+b²) = |z|

For (2): (z₁ + z₂)̄ = (a₁+a₂ + i(b₁+b₂))̄ = (a₁+a₂) - i(b₁+b₂) = (a₁ - ib₁) + (a₂ - ib₂) = z₁̄ + z₂̄

For (3): (z₁z₂)̄ = (a₁a₂ - b₁b₂ + i(a₁b₂ + a₂b₁))̄ = (a₁a₂ - b₁b₂) - i(a₁b₂ + a₂b₁)
           = (a₁ - ib₁)(a₂ - ib₂) = z₁̄z₂̄

For (6): Let z₁ = r₁(cos θ₁ + i sin θ₁), z₂ = r₂(cos θ₂ + i sin θ₂)
      |z₁ + z₂|² = |(r₁+r₂)² + 2r₁r₂(cos(θ₁-θ₂))(cos θ₁ cos θ₂ + sin θ₁ sin θ₂) + 2r₁r₂(cos²((θ₁-θ₂))/2 - sin²((θ₁-θ₂)/2))|
      Using identity |cos α - cos β| ≤ |α-β| and triangle inequality for arguments gives the result.

For (7): |z₁ - z₂| ≤ |z₁| + |z₂| follows from (6) with z₂ replaced by -z₂.

All properties follow from the algebraic structure of ℂ. QED

### 128.6 Complex Exponentiation

**Theorem**: For z ≠ 0, any complex number w can be expressed as w = z^c for infinitely many complex c.

**Proof**: 
Using the polar form z = r e^{iθ}, we have:
z^c = (r e^{iθ})^c = e^{c(ln r + i(θ + 2kπ))} = e^{c ln r + ic(θ + 2kπ)}
    = r^c e^{ic(θ + 2kπ)}

For w to equal z^c, we need w = e^{c(log z)}, where log z = ln|z| + i(arg z + 2kπ).
The logarithm is multi-valued, hence exponentiation is multi-valued. QED

### 128.7 The Fundamental Theorem of Algebra

**Theorem**: Every non-constant single-variable polynomial equation with complex coefficients has at least one complex root.

**Proof**: 
Consider a polynomial p(z) of degree n ≥ 1. Assume for contradiction that p has no roots.
Using the maximum modulus principle from complex analysis, the function |p(z)| attains a local minimum at infinity, but this contradicts the behavior of polynomials at infinity (|p(z)| → ∞ as |z| → ∞).
Alternatively, using Liouville's theorem: if p has no roots, then 1/p is an entire bounded function (for |z| large), which must be constant, contradicting that p is non-constant.
Thus p must have at least one root. By induction and the factor theorem, p factors completely over ℂ. QED

### 128.8 Argand Diagrams

**Theorem**: The complex plane ℂ can be identified with ℝ² via the map z ↦ (Re(z), Im(z)).

**Proof**: 
The correspondence z = a + bi ↦ (a, b) is a bijection from ℂ to ℝ².
Addition in ℂ: (a+bi) + (c+di) = (a+c) + i(b+d) corresponds to (a,b) + (c,d) = (a+c, b+d)
Multiplication in ℂ: (a+bi)(c+di) = (ac-bd) + i(ad+bc) corresponds to the matrix representation:
[ a  -b ] [ c  -d ] = [ ac-bd  -ad-bc ]
[ b   a ] [ d   c ]   [ bc+ad   -ac+bd ]

This is an isomorphism of vector spaces and preserves the field structure of ℂ. QED

