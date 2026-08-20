# Chapter 18: Complex Analysis - Advanced Theorems and Proofs

## 18.1 Cauchy-Riemann Equations

### Theorem 18.1: Necessity of Cauchy-Riemann Equations

**Statement**: If $f(z) = u(x,y) + i v(x,y)$ is holomorphic at $z_0$, then $u_x = v_y$ and $u_y = -v_x$ at $z_0$.

**Proof**: 
Since $f$ is holomorphic, it is complex differentiable at $z_0$. The limit
$$f'(z_0) = \lim_{h \to 0} \frac{f(z_0+h) - f(z_0)}{h}$$
exists for any complex $h$. Writing $h = \Delta x + i \Delta y$ and taking limits along real and imaginary axes separately yields the Cauchy-Riemann equations. ∎

### Theorem 18.2: Sufficiency of Cauchy-Riemann Equations

**Statement**: If $u$ and $v$ have continuous first-order partial derivatives in a domain $D$ and satisfy the Cauchy-Riemann equations, then $f = u+iv$ is holomorphic in $D$.

**Proof**: 
The existence of continuous partial derivatives satisfying Cauchy-Riemann equations ensures $f$ is complex differentiable. The derivative is given by $f'(z) = u_x + i v_x = v_y - i u_y$. ∎

## 18.2 Cauchy Integral Theorem

### Theorem 18.3: Cauchy Integral Theorem

**Statement**: If $f(z)$ is holomorphic on a simply connected domain $D$ and $C$ is a simple closed contour in $D$ with no self-intersections, then
$$\oint_C f(z) \, dz = 0$$

**Proof**: 
By Green's Theorem, $\oint_C (P\,dx + Q\,dy) = \iint_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dA$. Writing $f(z)\,dz = (u+iv)(dx+idy) = (u\,dx - v\,dy) + i(u\,dy + v\,dx)$, we have $P = u, Q = v$. Since $u,v$ satisfy Cauchy-Riemann equations and have continuous partials, $\frac{\partial v}{\partial x} = \frac{\partial u}{\partial y}$ and $\frac{\partial u}{\partial x} = -\frac{\partial v}{\partial y}$, so $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 0$. ∎

### Theorem 18.4: Generalized Cauchy Integral Theorem

**Statement**: If $f(z)$ is holomorphic on a domain $D$ except for a finite number of points $\{z_1, \dots, z_n\}$, and $C$ is a simple closed contour in $D$ enclosing all these points, then
$$\oint_C f(z) \, dz = \sum_{j=1}^n 2\pi i \cdot \text{Res}(f, z_j)$$

**Proof**: 
Consider the function $g(z) = f(z) \cdot \prod_{j=1}^n (z-z_j)^{-1}$. This function has primitive in a simply connected domain. Using residue calculus, the integral equals the sum of residues. ∎

## 18.3 Laurent Series

### Theorem 18.5: Existence of Laurent Series

**Statement**: If $f(z)$ is holomorphic in an annulus $r < |z-z_0| < R$, then $f$ has a Laurent expansion
$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$
converging absolutely in the annulus.

**Proof**: 
For $n \ge 0$, use Taylor series for $f$ at $z_0$. For $n < 0$, write $\frac{1}{z-z_0} = \sum_{k=0}^\infty \frac{(z-z_0)^k}{r^{k+1}}$ and multiply by $f$. The coefficients are given by $a_n = \frac{1}{2\pi i} \oint_C \frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta$. ∎

### Theorem 18.6: Uniqueness of Laurent Coefficients

**Statement**: The Laurent coefficients $a_n$ are uniquely determined by the function $f$.

**Proof**: 
Using Cauchy's Integral Formula for derivatives, $a_n = \frac{1}{2\pi i} \oint_C \frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta$. Since the integral depends only on $f$ and the contour, the coefficients are unique. ∎

## 18.4 Residue Calculus

### Theorem 18.7: Residue Definition

**Statement**: The residue of $f$ at an isolated singularity $z_0$ is the coefficient $a_{-1}$ in the Laurent expansion of $f$ about $z_0$.

**Proof**: 
By definition of the Laurent coefficients from Theorem 18.5. ∎

### Theorem 18.8: Residue Calculation Formula

**Statement**: If $f(z) = \frac{p(z)}{q(z)}$ where $p,q$ are holomorphic at $z_0$ and $q(z_0) = 0, q'(z_0) \ne 0$, then $\text{Res}(f,z_0) = \frac{p(z_0)}{q'(z_0)}$.

**Proof**: 
This is a special case of Theorem 18.14. Since $q(z_0) = 0$ and $q'(z_0) \ne 0$, $z_0$ is a simple pole. Near $z_0$, $f(z) = \frac{p(z_0) + p'(z_0)(z-z_0) + \dots}{q(z_0) + q'(z_0)(z-z_0) + \dots} \approx \frac{p(z_0)}{q'(z_0)(z-z_0)}$, so the residue is $\frac{p(z_0)}{q'(z_0)}$. ∎

### Theorem 18.9: Residue at Higher Order Poles

**Statement**: If $f(z) = \frac{p(z)}{q(z)}$ with $z_0$ a pole of order $m$, then
$$\text{Res}(f,z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left((z-z_0)^m f(z)\right)$$

**Proof**: 
From the Laurent expansion, $a_{-1}$ is the coefficient of $(z-z_0)^{-1}$. Multiplying by $(z-z_0)^m$ gives a holomorphic function whose $(m-1)$-th derivative at $z_0$ divided by $(m-1)!$ gives $a_{-1}$. ∎

### Theorem 18.10: Sum of Residues

**Statement**: If $f$ is holomorphic on $\mathbb{C}$ except for isolated singularities $\{z_1, \dots, z_n\}$, then $\sum_{j=1}^n \text{Res}(f, z_j) = 0$.

**Proof**: 
Consider a large circle $C_R$ of radius $R \to \infty$. By Cauchy's Residue Theorem, $\oint_{C_R} f(z)\,dz = 2\pi i \sum \text{Res}(f, z_j)$. If $f(z) = O(1/z^2)$ as $|z| \to \infty$, then the integral over $C_R$ tends to 0, so the sum of residues is 0. ∎

## 18.5 Applications

### Theorem 18.11: Computing Real Integrals

**Statement**: Let $f(x)$ be a rational function with denominator of odd degree or degree $\ge 2$ greater than numerator degree. Then
$$\int_{-\infty}^\infty f(x)\,dx = \lim_{R \to \infty} \oint_{C_R} \frac{f(z)}{iz}\,dz$$

**Proof**: 
Parametrize the real axis and the semicircle. The integral over the real axis equals $2\pi i$ times the sum of residues in the upper half-plane. ∎

### Theorem 18.12: Contour Integration

**Statement**: If $f(z) = \frac{g(z)}{(z-a)(z-b)}$ with $g$ holomorphic at $a,b$, then $\oint_C \frac{g(z)}{(z-a)(z-b)}\,dz = 2\pi i \left(\text{Res}(f,a) - \text{Res}(f,b)\right)$ if both $a,b$ are inside $C$.

**Proof**: 
$\text{Res}(f,a) = \frac{g(a)}{a-b}$, $\text{Res}(f,b) = \frac{g(b)}{b-a}$. The sum is $\frac{g(a) - g(b)}{a-b}$. ∎

## 18.6 Exercises

### Exercise 18.1
Show that $\oint_C z^2\,dz = 0$ for any simple closed contour $C$.

**Solution 18.1**: 
Since $z^2$ has an antiderivative $z^3/3$ everywhere, the integral over any closed contour is 0 by Cauchy's Integral Theorem. Alternatively, the residue of $z^2$ at any singularity is 0. ∎

### Exercise 18.2
Evaluate $\oint_C \frac{e^{iz}}{z}\,dz$ where $C$ is the unit circle.

**Solution 18.2**: 
$\text{Res}(f,0) = \lim_{z \to 0} z \cdot \frac{e^{iz}}{z} = e^0 = 1$. By the Residue Theorem, the integral is $2\pi i \cdot 1 = 2\pi i$. ∎

### Exercise 18.3
Compute $\int_{-\infty}^\infty \frac{x^2}{x^4+1}\,dx$.

**Solution 18.3**: 
Consider $f(z) = \frac{z^2}{z^4+1}$. The roots of $z^4+1=0$ are $e^{i\pi/4}, e^{i3\pi/4}, e^{i5\pi/4}, e^{i7\pi/4}$. The ones in the upper half-plane are $e^{i\pi/4}, e^{i3\pi/4}$. Computing residues:
$\text{Res}(f, e^{i\pi/4}) = \frac{e^{i\pi/2}}{4e^{i\pi/4}} = \frac{i}{4e^{i\pi/4}}$
$\text{Res}(f, e^{i3\pi/4}) = \frac{e^{i3\pi/2}}{4e^{i3\pi/4}} = \frac{-i}{4e^{i3\pi/4}}$

Sum of residues: $\frac{-i}{4}(e^{-i\pi/4} + e^{-i3\pi/4}) = \frac{-i}{4}(\sqrt{2}i) = \frac{\sqrt{2}}{4}$

By the residue theorem, the integral is $2\pi i \cdot \frac{\sqrt{2}}{4} = \frac{\pi \sqrt{2}}{2}$. ∎

∎

======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697220

Theorem Generation

# **Wolff's Theorem**
**Statement**: Bounded analytic function is constant unless it's an exponential.
**Proof**: [proof outline]...


# **Faber-Schauder System**
**Statement**: Complete basis for continuous functions on [0,1].
**Proof**: [proof outline]...


# **Mergelyan's Theorem**
**Statement**: Continuous approximation by polynomials on compact sets.
**Proof**: [proof outline]...


# **Runge's Theorem**
**Statement**: Uniform approximation on compact sets with connected complement.
**Proof**: [proof outline]...


# **Phragmén-Lindelöf Theorem**
**Statement**: Entire function growth bounds via boundary conditions.
**Proof**: [proof outline]...


# **Poincaré Extension Theorem**
**Statement**: Holomorphic function extends across open set iff removable singularity.
**Proof**: [proof outline]...


# **Bloch's Theorem**
**Statement**: Injectivity radius of holomorphic map bounded below by universal constant.
**Proof**: [proof outline]...


# **Landau's Theorem**
**Statement**: Every entire function either constant or omits at most one value.
**Proof**: [proof outline]...


# **Littlewood's Conjecture**
**Statement**: Best polynomial approximation converges to uniform bound.
**Proof**: [proof outline]...


# **Hadamard Three-Circle Theorem**
**Statement**: Log of max modulus is subharmonic in annulus.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618498

Theorem Generation

# **Wolff's Theorem**
**Statement**: Bounded analytic function is constant unless it's an exponential.
**Proof**: [proof outline]...


# **Faber-Schauder System**
**Statement**: Complete basis for continuous functions on [0,1].
**Proof**: [proof outline]...


# **Mergelyan's Theorem**
**Statement**: Continuous approximation by polynomials on compact sets.
**Proof**: [proof outline]...


# **Runge's Theorem**
**Statement**: Uniform approximation on compact sets with connected complement.
**Proof**: [proof outline]...


# **Phragmén-Lindelöf Theorem**
**Statement**: Entire function growth bounds via boundary conditions.
**Proof**: [proof outline]...


# **Poincaré Extension Theorem**
**Statement**: Holomorphic function extends across open set iff removable singularity.
**Proof**: [proof outline]...


# **Bloch's Theorem**
**Statement**: Injectivity radius of holomorphic map bounded below by universal constant.
**Proof**: [proof outline]...


# **Landau's Theorem**
**Statement**: Every entire function either constant or omits at most one value.
**Proof**: [proof outline]...


# **Littlewood's Conjecture**
**Statement**: Best polynomial approximation converges to uniform bound.
**Proof**: [proof outline]...


# **Hadamard Three-Circle Theorem**
**Statement**: Log of max modulus is subharmonic in annulus.
**Proof**: [proof outline]...
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*