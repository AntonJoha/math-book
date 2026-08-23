# Chapter 130: Complex Numbers - Advanced Theorems and Proofs

## 130.1 Fundamental Complex Analysis: Advanced Theorems

### Theorem 130.1 (Liouville's Theorem)
**Statement:** Every bounded entire function is constant.

**Proof:** Let $f: \mathbb{C} \to \mathbb{C}$ be entire and bounded, i.e., $|f(z)| \leq M$ for all $z \in \mathbb{C}$. By the Cauchy integral formula, for any disk $D(z_0, R)$, we have
$$f'(z_0) = \frac{1}{2\pi i} \oint_{|z-z_0|=R} \frac{f(z)}{(z-z_0)^2} dz$$
Taking the modulus and using the bound $|f(z)| \leq M$, we get
$$|f'(z_0)| \leq \frac{1}{2\pi R} \cdot 2\pi R \cdot \frac{M}{R} = \frac{M}{R}$$
As $R \to \infty$, we have $f'(z_0) = 0$. Since $z_0$ is arbitrary, $f$ is constant.

**Corollary:** There are no non-constant entire functions that are bounded.

### Theorem 130.2 (Maximum Modulus Principle)
**Statement:** If $f$ is holomorphic on a domain $D$ and $|f(z)|$ achieves a maximum at an interior point $z_0 \in D$, then $f$ is constant.

**Proof:** Let $U$ be a neighborhood of $z_0$. Since $|f(z)|$ achieves a maximum at $z_0$, $|f(z)| \leq |f(z_0)|$ for all $z \in U$. By the Open Mapping Theorem, if $f$ is non-constant and holomorphic on $U$, then $f(U)$ is open, so there exists $w \in f(U)$ with $|w| > |f(z_0)|$, contradicting the assumption.

**Corollary:** Let $f$ be holomorphic on a compact domain $\overline{D}$ with $D$ the interior. Then $|f(z)|$ achieves its maximum on the boundary $\partial D$.

**Theorem 130.3** (Minimum Modulus Principle)
**Statement:** If $f$ is holomorphic on a domain $D$ and $f(z) \neq 0$ for all $z \in D$, then $|f(z)|$ achieves a minimum at an interior point $z_0 \in D$ if and only if $f$ is constant.

**Proof:** Consider $1/f$, which is holomorphic on $D$ since $f(z) \neq 0$. By the Maximum Modulus Principle applied to $1/f$, $|1/f(z)|$ achieves a maximum at $z_0$ if and only if $f$ is constant. This is equivalent to $|f(z)|$ achieving a minimum at $z_0$.

## 130.2 Conformal Mappings: Advanced Theorems

### Theorem 130.4 (Riemann Mapping Theorem)
**Statement:** Let $D$ be a simply connected domain in $\mathbb{C}$ with $D \neq \mathbb{C}$. Then there exists a biholomorphic function $f: D \to \mathbb{D}$ (where $\mathbb{D}$ is the unit disk).

**Proof:** The Riemann Mapping Theorem is proved using the method of exhaustion, Schwarz-Christoffel mappings, or by constructing the function via conformal invariance of the hyperbolic metric.

### Theorem 130.5 (Schwarz Lemma)
**Statement:** Let $f: \mathbb{D} \to \mathbb{D}$ be holomorphic with $f(0) = 0$. Then $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$, and $|f'(0)| \leq 1$. If $|f(z_0)| = |z_0|$ for some $z_0 \neq 0$, or $|f'(0)| = 1$, then $f$ is a rotation, i.e., $f(z) = e^{i\theta}z$ for some $\theta \in \mathbb{R}$.

**Proof:** By the open mapping theorem, $f(\mathbb{D})$ is open, so there exists $w \in f(\mathbb{D})$ with $|w| < 1$. By the maximum modulus principle, $|f(z)| \leq 1$ for all $z \in \mathbb{D}$. The proof uses the properties of holomorphic functions and the maximum modulus principle.

### Theorem 130.6 (Schwarz-Pick Theorem)
**Statement:** Let $f: \mathbb{D} \to \mathbb{D}$ be holomorphic. Then for all $z, w \in \mathbb{D}$,
$$\left|\frac{f(z) - f(w)}{1 - \overline{f(w)}f(z)}\right| \leq \left|\frac{z - w}{1 - \overline{w}z}\right|$$
and
$$|f'(z)| \leq \frac{1 - |f(z)|^2}{1 - |z|^2}$$
Equality holds in the first inequality if and only if $f$ is a Möbius transformation, and equality in the second inequality if and only if $f$ is a rotation.

**Proof:** The Schwarz-Pick theorem is proved using the hyperbolic metric on the unit disk.

### Theorem 130.7 (Möbius Transformations)
**Statement:** The Möbius transformations $f(z) = \frac{az + b}{cz + d}$ with $ad - bc \neq 0$ map circles and lines to circles and lines.

**Proof:** Möbius transformations are compositions of translations, dilations, rotations, and inversions. Since translations, dilations, and rotations map circles and lines to circles and lines, and inversions map circles and lines to circles and lines, the theorem follows.

## 130.3 Series and Integration: Advanced Theorems

### Theorem 130.8 (Cauchy's Integral Theorem)
**Statement:** Let $\gamma$ be a simple closed contour and $f$ be holomorphic on and inside $\gamma$. Then
$$\oint_\gamma f(z) dz = 0$$

**Proof:** By the deformation theorem for contours, we can deform $\gamma$ to any other contour that encloses the same singularities. Since $f$ is holomorphic on and inside $\gamma$, there are no singularities, so the integral is zero.

**Corollary (Cauchy's Integral Formula):** Let $f$ be holomorphic on and inside a simple closed contour $\gamma$, and let $z_0$ be inside $\gamma$. Then
$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} dz$$

**Proof:** The corollary is proved by considering the function $f(z)/(z-z_0)$ and using the residue theorem.

### Theorem 130.9 (Cauchy's Residue Theorem)
**Statement:** Let $\gamma$ be a simple closed contour and $f$ be meromorphic on and inside $\gamma$. Then
$$\oint_\gamma f(z) dz = 2\pi i \sum \text{Res}(f, z_k)$$
where $z_k$ are the poles of $f$ inside $\gamma$.

**Proof:** The Residue Theorem is proved using the local behavior of meromorphic functions near their poles.

### Theorem 130.10 (Mittag-Leffler Theorem)
**Statement:** Let $\Omega$ be a domain in $\mathbb{C}$ and let $\{a_n\}$ be a sequence of distinct points in $\Omega$ with no accumulation point in $\Omega$. Let $h_n$ be holomorphic functions on $\Omega \setminus \{a_n\}$ with poles only at $a_n$. Then there exists a meromorphic function $f$ on $\Omega$ with prescribed principal parts at each $a_n$.

**Proof:** The Mittag-Leffler theorem is proved using the properties of entire functions and the construction of the meromorphic function as an infinite product.

## 130.4 Applications: Advanced Theorems

### Theorem 130.11 (Argument Principle)
**Statement:** Let $\gamma$ be a simple closed contour and $f$ be holomorphic on and inside $\gamma$ with no zeros or poles on $\gamma$. Then
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} dz = N - P$$
where $N$ is the number of zeros and $P$ is the number of poles of $f$ inside $\gamma$, both counted with multiplicity.

**Proof:** The Argument Principle is proved using the fact that $\log f(z)$ is locally holomorphic except at the zeros and poles of $f$.

**Corollary:** Let $f$ be holomorphic and analytic on a compact domain $\overline{D}$ with $D$ the interior. Let $z_0 \in D$ be a point such that $f(z_0) \neq f(z)$ for any $z \in \partial D$. Then the number of zeros of $f$ in $D$, counted with multiplicity, is equal to the winding number of $f$ around the boundary of $f(D)$.

### Theorem 130.12 (Rouché's Theorem)
**Statement:** Let $\gamma$ be a simple closed contour and let $f$ and $g$ be holomorphic on and inside $\gamma$. If $|g(z)| < |f(z)|$ for all $z \in \gamma$, then $f$ and $f + g$ have the same number of zeros inside $\gamma$, both counted with multiplicity.

**Proof:** Rouché's theorem is proved using the Argument Principle and the fact that if $|g(z)| < |f(z)|$ on $\gamma$, then $f(z)$ and $f(z) + g(z)$ never have the same value for any $z \in \gamma$.

**Corollary:** Let $f(z) = z^n + a_{n-1} z^{n-1} + \dots + a_0$ be a polynomial. Then the number of zeros of $f$ in a disk $D(z_0, R)$ is equal to the winding number of $f$ around the boundary of the disk.

**Theorem 130.13** (Great Picard Theorem)
**Statement:** Let $f$ be holomorphic in a punctured neighborhood of an essential singularity $z_0$. Then $f$ takes every complex value (with at most one exception) infinitely often in any neighborhood of $z_0$.

**Proof:** The Great Picard theorem is proved using the properties of essential singularities and the Casorati-Weierstrass theorem.

**Theorem 130.14** (Little Picard Theorem)
**Statement:** An entire function that is not a polynomial must take every complex value infinitely often, with at most one exception.

**Proof:** The Little Picard theorem is proved using the Great Picard theorem and the properties of entire functions.

*Updated on 2026-08-23*
