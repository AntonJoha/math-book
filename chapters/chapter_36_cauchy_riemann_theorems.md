# Chapter 36: Cauchy-Riemann Theorems and Holomorphic Functions

## 36.1 Preliminaries: Complex Differentiability

Let $f: D \subseteq \mathbb{C} \to \mathbb{C}$ be a complex-valued function defined on an open set $D \subseteq \mathbb{C}$. We write $f(z) = u(x,y) + iv(x,y)$ where $z = x+iy$ and $u,v: \mathbb{R}^2 \to \mathbb{R}$ are the real and imaginary parts.

**Definition 36.1.** A function $f$ is **complex differentiable** (or holomorphic) at $z_0 \in D$ if the limit
$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$
exists.

**Theorem 36.1 (Complex Differentiability implies Real Differentiability).**
Let $f = u + iv$ be complex differentiable at $z_0 = x_0 + iy_0$. Then $u$ and $v$ are real differentiable at $(x_0, y_0)$, and the Jacobian matrix of $f = (u,v): \mathbb{R}^2 \to \mathbb{R}^2$ is
$$J_f = \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix} = \begin{pmatrix} \text{Re}(f'(z_0)) & -\text{Im}(f'(z_0)) \\ \text{Im}(f'(z_0)) & \text{Re}(f'(z_0)) \end{pmatrix}.$$

*Proof.* See standard texts on complex analysis. $\square$

**Theorem 36.2 (Cauchy-Riemann Equations).**
Let $f = u + iv$ be complex differentiable at $z_0$. Then $u_x, u_y, v_x, v_y$ exist at $(x_0, y_0)$ and satisfy:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.$$

*Proof.* From $f'(z_0) = \lim_{h \to 0} \frac{f(z_0+h) - f(z_0)}{h}$, we consider $h$ real ($f(z_0+h)-f(z_0) \approx f_x(x_0,y_0)h$) and $h = iy$ imaginary ($f(z_0+iy)-f(z_0) \approx f_y(x_0,y_0)(-y) = f_y(x_0,y_0)i(-y)$). Comparing the two limits gives the Cauchy-Riemann equations. $\square$

**Theorem 36.3 (Sufficiency of Cauchy-Riemann).**
Let $u, v$ have continuous partial derivatives on an open set $D$. If $u_x = v_y$ and $u_y = -v_x$ on $D$, then $f = u + iv$ is holomorphic on $D$.

*Proof.* The existence of continuous partial derivatives satisfying C-R equations ensures the limit defining $f'(z)$ exists and equals $u_x + i v_x$. $\square$

## 36.2 The Cauchy Integral Theorem

**Definition 36.2.** A domain $D \subseteq \mathbb{C}$ is **simply connected** if every simple closed curve in $D$ can be continuously shrunk to a point while remaining entirely in $D$.

**Theorem 36.4 (Cauchy Integral Theorem).**
Let $f$ be holomorphic on a simply connected domain $D$. For any closed piecewise-smooth curve $\gamma$ in $D$,
$$\oint_\gamma f(z) \, dz = 0.$$

*Proof.* This is a fundamental result of complex analysis. See standard proofs using homotopy invariance or Green's theorem. $\square$

**Theorem 36.5 (Fundamental Theorem of Calculus in $\mathbb{C}$).**
Let $f$ be holomorphic on a domain $D$ and $\gamma$ be any piecewise-smooth curve in $D$ from $z_0$ to $z_1$. Then
$$\int_\gamma f(z) \, dz = F(z_1) - F(z_0)$$
where $F' = f$ on $D$.

*Proof.* Define $F(z) = \int_{z_0}^z f(w) \, dw$ along paths in $D$. By the Cauchy Integral Theorem, this is path-independent. Then $F'(z) = f(z)$. $\square$

## 36.3 Cauchy's Integral Formula

**Theorem 36.6 (Cauchy's Integral Formula).**
Let $f$ be holomorphic on a domain $D$ containing a closed disk $\overline{D(a,r)} \subseteq D$. For any $z_0 \in \text{int}(D(a,r))$ and any closed curve $\gamma$ positively oriented enclosing $z_0$,
$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz.$$

*Proof.* Let $D(z, \epsilon)$ be a small circle around $z_0$. By Cauchy's Integral Theorem, $\oint_{\gamma - D(z,\epsilon)} f(z)/(z-z_0) \, dz = 0$, so
$$\oint_\gamma = \oint_{D(z,\epsilon)}$$
Then parameterize $\oint_{D(z,\epsilon)}$ and evaluate directly. $\square$

**Theorem 36.7 (Cauchy's Integral Formula for Derivatives).**
Under the same hypotheses as Theorem 36.6, for any non-negative integer $n$,
$$f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z - z_0)^{n+1}} \, dz.$$

*Proof.* Differentiate under the integral sign (justified by uniform convergence). $\square$

**Corollary 36.8 (Analyticity).**
If $f$ is complex differentiable at every point of a domain $D$, then $f$ is infinitely differentiable and holomorphic on $D$.

## 36.4 Applications of Cauchy's Integral Formula

**Theorem 36.9 (Series Expansion).**
Let $f$ be holomorphic on $\overline{D(a,r)}$. Then for any $z \in D(a,r)$,
$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (z-a)^n,$$
where the series converges absolutely for $|z-a| < r$.

*Proof.* Use Cauchy's Integral Formula for $f^{(n)}(a)$ and rearrange. $\square$

**Theorem 36.10 (Liouville's Theorem).**
Let $f: \mathbb{C} \to \mathbb{C}$ be entire and bounded. Then $f$ is constant.

*Proof.* By Cauchy's Integral Formula, $|f'(z)| \leq \frac{M}{r}$ for large $r$. As $r \to \infty$, $f'(z) = 0$. $\square$

**Theorem 36.11 (Maximum Modulus Principle).**
Let $f$ be holomorphic on a domain $D$. Then $|f|$ cannot attain a local maximum in the interior of $D$ unless $f$ is constant.

*Proof.* By Cauchy's Integral Formula, $|f(z)| \leq \frac{1}{2\pi} \oint_\gamma \frac{|f(\zeta)|}{|\zeta - z|} \, |\!d\zeta|$. $\square$

**Theorem 36.12 (Phragmén-Lindquist Theorem).**
Let $D$ be a simply connected domain. If $f$ is holomorphic on $D$, continuous on $\overline{D}$, and $|f(z)| \leq M$ on $\partial D$, then $|f(z)| \leq M$ on $\overline{D}$.

**Theorem 36.13 (Argument Principle).**
Let $f$ be holomorphic on a domain $D$ containing a closed curve $\gamma$ and its interior. Let $z_0$ be a zero of $f$ (counting multiplicity) and $p$ be a pole of $f$. Then
$$N - P = \frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz,$$
where $N$ and $P$ are the numbers of zeros and poles inside $\gamma$.

**Theorem 36.14 (Open Mapping Theorem).**
Let $f$ be holomorphic and non-constant on a domain $D$. Then $f(D)$ is an open set.

*Proof.* If $f(z_0) = w$, then by the local expansion $f(z) = f(z_0) + f'(z_0)(z-z_0) + \dots$, $f$ maps a neighborhood of $z_0$ to a neighborhood of $w$. $\square$

## 36.5 The Residue Theorem

**Definition 36.15.** The **residue** of $f$ at an isolated singularity $z_0$ is
$$\text{Res}(f, z_0) = \frac{1}{2\pi i} \oint_\gamma f(z) \, dz,$$
where $\gamma$ is a small positively oriented circle around $z_0$.

**Theorem 36.16 (Residue Theorem).**
Let $f$ be holomorphic on a domain $D$ containing finitely many isolated singularities $z_1, \dots, z_n$ and a closed curve $\gamma$ in $D$ enclosing all $z_k$. Then
$$\oint_\gamma f(z) \, dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k).$$

**Theorem 36.17 (Computing Residues).**
If $f(z) = \sum_{n=-\infty}^\infty a_n (z-z_0)^n$ is the Laurent series of $f$ at $z_0$, then
$$\text{Res}(f, z_0) = a_{-1}.$$

**Theorem 36.18 (Partial Fraction Decomposition).**
Let $P(z)$ and $Q(z)$ be polynomials with $Q(z)$ having distinct roots $r_1, \dots, r_n$. Then
$$\frac{P(z)}{Q(z)} = \sum_{k=1}^n \frac{c_k}{z-r_k} + R(z),$$
where $R(z)$ is a polynomial of degree $\deg(P) - \deg(Q)$ if $\deg(P) \geq \deg(Q)$, otherwise $R = 0$.

**Theorem 36.19 (Rational Function Integration).**
Let $R(z)$ be a rational function. The integral of $R(z)$ over the unit circle can be computed using the Residue Theorem, and
$$\int_0^{2\pi} R(e^{i\theta}) \, d\theta = 2\pi \sum \text{Re}(\text{Res}(R(e^{iz}), z_k)),$$
summing over poles inside the unit circle.

**Theorem 36.20 (Contour Integration on Real Line).**
Let $R(z)$ be a rational function with denominator having degree at least two higher than numerator. If $R(z)$ has no poles in the upper half-plane, then
$$\int_{-\infty}^\infty R(x) \, dx = 2\pi i \sum \text{Res}(R(z), z_k)$$
where $z_k$ are poles in the upper half-plane.

**Theorem 36.21 (Branch Point Analysis).**
Let $f(z) = z^\alpha$ where $\alpha \notin \mathbb{Z}$. The function has a branch point at $z=0$ and infinity. A branch cut is necessary, typically along the negative real axis.

**Theorem 36.22 (Keyhole Contour Integration).**
Let $f(z) = \frac{\log z}{z^2+1}$. Integrating around a keyhole contour avoiding the branch cut on $(-\infty, 0)$, we find
$$\int_0^\infty \frac{\log x}{x^2+1} \, dx = \frac{\pi^2}{4}.$$

**Theorem 36.23 (Infinite Product Expansion).**
If $f$ is entire and $f(0) \neq 0$, then there exists an entire function $g$ such that
$$f(z) = f(0) \prod_{n=1}^\infty \left(1 - \frac{z}{a_n}\right) e^{z/a_n + \frac{z^2}{2a_n^2} + \dots + \frac{z^k}{k a_n^k}}$$
where $a_n$ are the non-zero zeros of $f$.

**Theorem 36.24 (Weierstrass Factorization Theorem).**
Every entire function $f$ of finite order can be written as
$$f(z) = e^{P(z)} z^m \prod_{n=1}^\infty E_p\left(\frac{z}{a_n}\right)$$
where $E_p(w) = (1-w)e^{w + w^2/2 + \dots + w^p/p}$, $P$ is a polynomial, and $m$ is the multiplicity of $z=0$ as a root.

## 36.6 Additional Problems and Exercises

**Exercise 36.25.** Prove that the integral of $\frac{1}{1+z^n}$ over the unit circle is $2\pi i/n$ for $n > 0$.

**Exercise 36.26.** Show that if $f$ is holomorphic on $\mathbb{C}$ and satisfies $|f(z)| \leq C(1+|z|)^n$ for some $n < 1$, then $f$ is constant.

**Exercise 36.27.** Let $f$ be holomorphic on the unit disk. Prove that
$$\sum_{n=1}^\infty |a_n|^2 \leq \frac{1}{2\pi} \int_0^{2\pi} |f(e^{i\theta})|^2 \, d\theta,$$
where $f(z) = \sum a_n z^n$.

**Exercise 36.28.** Prove that if $f$ is holomorphic on the upper half-plane and bounded, then
$$f(z) = -i \int_{-\infty}^\infty \frac{f(t)}{t-z} \, dt.$$

**Exercise 36.29.** Let $S$ be the area of a region $D \subseteq \mathbb{C}$. Prove that
$$\frac{1}{2\pi i} \oint_{\partial D} \bar{z} \, dz = S.$$

**Exercise 36.30.** Let $f$ be holomorphic on $D$. Prove that
$$\int_D |f'(z)|^2 \, dA = \frac{1}{2} \iint_D |f(z)|^2 \, dA$$
is not generally true, and give counterexamples.


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

---

*Updated on 2026-06-10*
