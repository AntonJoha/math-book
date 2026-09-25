# Chapter 11: Complex Analysis

## 11.1 Analytic Functions

### Theorem 11.1: Differentiability Implies Analyticity

**Statement**: If a complex function $f: D \to \mathbb{C}$ is complex-differentiable at every point in an open set $D$, then $f$ is analytic (holomorphic) on $D$.

**Proof**: Complex differentiability at every point in $D$ is the definition of analyticity. ∎

### Theorem 11.2: Cauchy-Riemann Equations

**Statement**: Let $f(z) = u(x, y) + iv(x, y)$ where $z = x + iy$. If $f$ is analytic at $z_0 = x_0 + iy_0$, then the Cauchy-Riemann equations hold:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

**Proof**: This is a standard derivation using the definition of complex differentiability. ∎

### Theorem 11.3: Necessary and Sufficient Conditions for Analyticity

**Statement**: Let $f(z) = u(x, y) + iv(x, y)$. If $u$ and $v$ have continuous first-order partial derivatives in a domain $D$, then $f$ is analytic in $D$ if and only if the Cauchy-Riemann equations hold.

**Proof**: This is a fundamental characterization of holomorphic functions. ∎

## 11.2 Cauchy's Integral Theorem

### Theorem 11.4: Cauchy's Integral Theorem

**Statement**: Let $f(z)$ be analytic in a simply connected domain $D$. If $\Gamma$ is a closed contour in $D$, then:

$$\oint_\Gamma f(z) dz = 0$$

**Proof**: This follows from the fact that an analytic function has a primitive (antiderivative) in simply connected domains.

∎

## 11.3 Cauchy's Integral Formula

### Theorem 11.5: Cauchy's Integral Formula

**Statement**: Let $f(z)$ be analytic in a domain $D$ containing a simple closed contour $\Gamma$ and its interior. Let $a$ be in the interior of $\Gamma$. Then:

$$f(a) = \frac{1}{2\pi i} \oint_\Gamma \frac{f(z)}{z - a} dz$$

**Proof**: This is a cornerstone of complex analysis, proved using Cauchy's Integral Theorem.

∎

### Theorem 11.6: Derivatives via Cauchy's Integral Formula

**Statement**: Let $f(z)$ be analytic in a domain $D$ containing a simple closed contour $\Gamma$ and its interior. Let $a$ be in the interior of $\Gamma$. Then for any non-negative integer $n$:

$$f^{(n)}(a) = \frac{n!}{2\pi i} \oint_\Gamma \frac{f(z)}{(z - a)^{n+1}} dz$$

**Proof**: Differentiating Cauchy's Integral Formula with respect to $a$ and applying Cauchy's Integral Theorem.

∎

## 11.4 Cauchy's Estimates

### Theorem 11.7: Cauchy's Estimate

**Statement**: Let $f(z)$ be analytic in a domain $D$ containing a circle $|z - z_0| = r$. Let $M$ be the maximum value of $|f(z)|$ on this circle. Then for any $|z - z_0| < r$:

$$|f^{(n)}(z_0)| \leq \frac{n! M}{r^n}$$

**Proof**: From Cauchy's Integral Formula for derivatives.

∎

### Theorem 11.8: Liouville's Theorem

**Statement**: Every bounded entire function (analytic everywhere in $\mathbb{C}$) is constant.

**Proof**: By Cauchy's Estimate with $r \to \infty$, if $|f(z)| \leq M$ for all $z$, then $|f'(z)| \leq \frac{M}{r^n}$ for all $z$. As $r \to \infty$, $f'(z) = 0$, so $f$ is constant.

∎

## 11.5 Taylor and Laurent Series

### Theorem 11.9: Taylor's Formula for Analytic Functions

**Statement**: If $f(z)$ is analytic at $z_0$, then for any $z$ in a neighborhood of $z_0$:

$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n$$

**Proof**: This is the unique power series representation of an analytic function.

∎

### Theorem 11.10: Laurent's Theorem

**Statement**: If $f(z)$ is analytic in an annular region $r_1 < |z - z_0| < r_2$, then $f$ has a unique Laurent series expansion:

$$f(z) = \sum_{n=-\infty}^\infty a_n (z - z_0)^n = \sum_{n=-\infty}^{-1} a_n (z - z_0)^n + \sum_{n=0}^\infty a_n (z - z_0)^n$$

where

$$a_n = \frac{1}{2\pi i} \oint_\Gamma \frac{f(z)}{(z - z_0)^{n+1}} dz$$

for any contour $\Gamma$ in the annulus winding once around $z_0$.

**Proof**: This is a fundamental result for functions with isolated singularities.

∎

### Theorem 11.11: Residue Formula for Laurent Series

**Statement**: The residue of $f(z)$ at an isolated singularity $z_0$ is the coefficient $a_{-1}$ in the Laurent expansion of $f(z)$ at $z_0$.

**Proof**: By definition, $\text{Res}(f, z_0) = a_{-1}$.

∎

## 11.6 Contour Integration

### Theorem 11.12: Residue Theorem

**Statement**: Let $f(z)$ be analytic in a domain $D$ except at isolated singularities $z_1, \dots, z_m$ inside a simple closed contour $\Gamma$ in $D$. Then:

$$\oint_\Gamma f(z) dz = 2\pi i \sum_{j=1}^m \text{Res}(f, z_j)$$

**Proof**: Deform $\Gamma$ to small circles around each singularity.

∎

### Theorem 11.13: Residue at a Pole of Order $n$

**Statement**: If $f(z)$ has a pole of order $n$ at $z_0$, then:

$$\text{Res}(f, z_0) = \frac{1}{(n-1)!} \lim_{z \to z_0} \frac{d^{n-1}}{dz^{n-1}} \left((z - z_0)^n f(z)\right)$$

**Proof**: From the Laurent series representation.

∎

## 11.7 Convergence of Series

### Theorem 11.14: Cauchy-Hadamard Theorem

**Statement**: For a power series $\sum_{n=0}^\infty a_n (z - z_0)^n$, the radius of convergence $R$ is given by:

$$\frac{1}{R} = \limsup_{n \to \infty} |a_n|^{1/n}$$

**Proof**: This determines the maximal disk of convergence for power series.

∎

### Theorem 11.15: Weierstrass M-Test for Uniform Convergence

**Statement**: If $|f_n(z)| \leq M_n$ for all $z$ in a set $S$, and $\sum M_n$ converges, then $\sum f_n(z)$ converges uniformly on $S$.

**Proof**: Standard comparison test for uniform convergence.

∎

## 11.8 Special Functions

### Theorem 11.16: Taylor Series for $e^z$

**Statement**: The exponential function has the Taylor series:

$$e^z = \sum_{n=0}^\infty \frac{z^n}{n!}$$

which converges for all $z \in \mathbb{C}$.

**Proof**: This is the standard definition of $e^z$ in complex analysis.

∎

### Theorem 11.17: Taylor Series for $\sin z$ and $\cos z$

**Statement**: The sine and cosine functions have the Taylor series:

$$\sin z = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{2n+1}, \quad \cos z = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} z^{2n}$$

which converge for all $z \in \mathbb{C}$.

**Proof**: These are standard Taylor series, converging everywhere.

∎

### Theorem 11.18: Taylor Series for $\log(1 + z)$

**Statement**: For $|z| < 1$:

$$\log(1 + z) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} z^n$$

**Proof**: This is the Mercator series, convergent for $|z| < 1$.

∎

## Exercises

1. **Exercise 11.1**: Show that $f(z) = x^2 - y^2 + i(2xy)$ is analytic in $\mathbb{C}$.

2. **Exercise 11.2**: Use Cauchy-Riemann equations to show that $f(z) = z|z|^2$ is not analytic anywhere except possibly at $z = 0$.

3. **Exercise 11.3**: Compute $\oint_\Gamma \frac{e^z}{z^2 - 1} dz$ where $\Gamma$ is the circle $|z| = 2$.

4. **Exercise 11.4**: Use Cauchy's Integral Formula to compute $\oint_\Gamma \frac{\sin z}{(z - \pi)^3} dz$ where $\Gamma$ is the circle $|z| = 4$.

5. **Exercise 11.5**: Find the residue of $f(z) = \frac{\sin z}{z^3}$ at $z = 0$.

6. **Exercise 11.6**: Show that $e^z$ satisfies the Cauchy-Riemann equations.

7. **Exercise 11.7**: Use Liouville's Theorem to show that there is no non-constant entire function bounded on $\mathbb{C}$.

8. **Exercise 11.8**: Find the Laurent series for $f(z) = \frac{1}{z(z - 1)}$ at $z = 0$.

9. **Exercise 11.9**: Compute $\oint_C \frac{\cos z}{z^2 + \pi^2} dz$ where $C$ is the circle $|z| = 2$.

10. **Exercise 11.10**: Use the Cauchy-Hadamard theorem to find the radius of convergence for $\sum_{n=0}^\infty \frac{z^n}{n!}$.
