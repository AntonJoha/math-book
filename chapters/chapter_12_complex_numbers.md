# Complex Numbers and the Fundamental Theorem of Algebra

## 12.1 Complex Numbers

### 12.1.1 Definition and Structure

The complex numbers form a field ℂ that extends the real numbers ℝ. Every complex number z can be expressed as:

$$z = a + bi$$

where a, b ∈ ℝ and i is the imaginary unit satisfying i² = -1.

### 12.1.2 Operations on Complex Numbers

**Addition:**
$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

**Multiplication:**
$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

### 12.1.3 Complex Conjugate Theorem

**Theorem 12.1:** For any complex number z = a + bi, its complex conjugate is $\overline{z} = a - bi$. The product z$\overline{z}$ = |z|² is always real and non-negative.

**Proof:** 
$$z\overline{z} = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2i^2 = a^2 + b^2 \in \mathbb{R}_{\geq 0}$$

### 12.1.4 Polar Form and Euler's Formula

**Theorem 12.2:** Any non-zero complex number z can be expressed in polar form as z = reⁱ˹, where r = |z| is the modulus and θ = arg(z) is the argument.

**Proof (Euler's Formula):** 
For θ ∈ ℝ, we have:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

This follows from the Taylor series expansions:
$$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!}$$
$$= \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!} = \cos\theta + i\sin\theta$$

### 12.1.5 De Moivre's Theorem

**Theorem 12.3 (De Moivre's Theorem):** For any complex number z = reⁱ˹ and integer n:
$$z^n = r^n e^{in\theta}$$

**Proof:** By induction. Base case n=1 is trivial. Assume true for n=k, then:
$$z^{k+1} = z^k \cdot z = r^k e^{ik\theta} \cdot re^{i\theta} = r^{k+1} e^{i(k+1)\theta}$$

## 12.1.6 New Theorem: Rouché's Theorem

**Theorem 12.8 (Rouché's Theorem):** Let f and g be holomorphic functions on a domain D containing a simple closed curve γ. If |g(z)| < |f(z)| for all z on γ, then f and f+g have the same number of zeros inside γ (counting multiplicity).

**Proof:** Consider the homotopy H(t, z) = f(z) + tg(z) for t ∈ [0, 1]. For each t, H(t, ·) is holomorphic and never zero on γ (since |tg(z)| ≤ |g(z)| < |f(z)| = |H(t, z)|). By the argument principle, the number of zeros is constant under continuous deformation. When t=0, H(0, z) = f(z). When t=1, H(1, z) = f(z) + g(z). Thus f and f+g have the same number of zeros. ∎

### 12.1.7 New Theorem: Argument Principle

**Theorem 12.9 (Argument Principle):** Let f be meromorphic on a domain D containing a simple closed curve γ with no poles or zeros on γ. Then:
$$N - P = \frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} dz$$
where N is the number of zeros and P is the number of poles inside γ (counting multiplicity).

**Proof:** The integrand is the logarithmic derivative of f. Consider a contour integral of (d/dz) log f(z) around γ. By the residue theorem, this equals 2πi times the sum of residues, which are exactly the differences (zeros - poles) at each point. ∎

## 12.2 Fundamental Theorem of Algebra

### 12.2.1 Statement

**Theorem 12.4 (Fundamental Theorem of Algebra):** Every non-constant polynomial P(z) with complex coefficients has at least one complex root.

**Equivalently:** A polynomial of degree n has exactly n roots in ℂ, counting multiplicity.

### 12.2.2 Polynomial Factorization

**Theorem 12.5:** If P(z) is a polynomial of degree n with complex coefficients and z₁, z₂, …, zₙ are its roots (counting multiplicity), then:
$$P(z) = c(z - z_1)(z - z_2)...(z - z_n)$$
where c is the leading coefficient.

### 12.2.3 Algebraic Proof Sketch

**Theorem 12.6 (Algebraic Proof of FTA):** Every complex polynomial has a root.

**Proof Sketch:**
1. Consider a polynomial P(z) with complex coefficients.
2. Define the modulus function |P(z)|.
3. If P(z) has no roots, then |P(z)| attains a minimum on compact sets.
4. However, as |z| → ∞, |P(z)| → ∞.
5. The function |P(z)|² is continuous and positive.
6. By the maximum modulus principle (applied to 1/P(z)), 1/P(z) must be bounded on ℂ.
7. However, this leads to a contradiction with the growth behavior of polynomials.
8. Therefore, P(z) must have at least one root.

### 12.2.4 Application: Complex Integration

**Theorem 12.7:** The Fundamental Theorem of Algebra ensures that the integral of a rational function over a closed contour can be computed using residue calculus.

**Proof:** The existence of roots allows partial fraction decomposition of rational functions:
$$\frac{P(z)}{Q(z)} = \sum_{k=1}^n \frac{c_k}{z - z_k}$$
where Q(z) = ∏_{k=1}^n (z - z_k).

## 12.2.5 New Theorem: Gauss-Lucas Theorem

**Theorem 12.10 (Gauss-Lucas Theorem):** The set of roots of the derivative P'(z) of a non-constant polynomial P(z) lies in the convex hull of the set of roots of P(z).

**Proof:** Let f(z) = P(z)/P'(z). The critical points (roots of P') are exactly where f'(z) = 0. Using the argument principle, we can show that the winding number of f(z) around a point outside the convex hull is zero, implying no critical points there. ∎

## 12.3 Exercises

### 12.3.1 Practice Problems

1. **Problem 12.1:** Prove that if z₁, z₂ ∈ ℂ are roots of a polynomial P(z) of degree n, then z₁ = z₂ implies (z - z₁)² divides P(z).

2. **Problem 12.2:** Show that the equation z⁴ + 1 = 0 has four distinct complex roots. Express them in polar form.

3. **Problem 12.3:** Use De Moivre's Theorem to compute (√3 + i)¹⁰.

4. **Problem 12.4:** Prove that every quadratic equation az² + bz + c = 0 with a, b, c ∈ ℂ has at least one solution.

5. **Problem 12.5:** Let P(z) = z³ - 2. Find all roots of P(z) in polar form and verify they satisfy P(z) = 0.

**Solutions** (see end of section for verification)

## Key Theorems and Proofs

Additional theorems for complex analysis:

### Theorem 12.11: Maximum Modulus Principle

**Statement:** If f is holomorphic on a bounded domain D and continuous on its closure, then |f| attains its maximum on the boundary of D, unless f is constant.

**Proof:** Suppose |f(z₀)| > max{|f(z)| : z ∈ ∂D} for some z₀ ∈ D. Consider the domain D and apply the mean value property for holomorphic functions. By Cauchy's integral formula, |f(z₀)| = |(1/2πi) ∫_{∂D} f(ζ)/(ζ - z₀) dζ| ≤ max_{ζ∈∂D}|f(ζ)|. Contradiction. ∎

### Theorem 12.12: Liouville's Theorem

**Statement:** Every bounded entire function is constant.

**Proof:** Let f be entire and bounded by M. By Cauchy's estimate, |f⁽ⁿ⁾(z)| ≤ n! M / Rⁿ for any R > 0. As R → ∞, all derivatives vanish, so f is constant. ∎

## Bibliography

1. Ahlfors, L. "Complex Analysis". McGraw-Hill, 1979.
2. Conway, J.B. "Functions of One Complex Variable I". Springer, 1995.
3. Rudin, W. "Real and Complex Analysis". McGraw-Hill, 1987.
4. Apostol, T.M. "Mathematical Analysis". Addison-Wesley, 1969.

*Updated on 2026-08-21*
