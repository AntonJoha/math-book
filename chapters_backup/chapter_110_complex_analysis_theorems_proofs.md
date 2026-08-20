# Chapter 110: Complex Analysis - Comprehensive Theorems and Proofs

## 110.1 Analytic Functions and Holomorphicity

### Theorem 110.1.1 (Characterization of Holomorphic Functions)
A complex-valued function $f: D \to \mathbb{C}$ is holomorphic at $z_0$ if and only if it is complex differentiable at $z_0$.

**Proof**: The definition of complex differentiability at $z_0$ is:
$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$
exists. This is equivalent to saying $f$ is analytic at $z_0$.

### Theorem 110.1.2 (Local Power Series Representation)
If $f$ is holomorphic on a domain $D$, then $f$ can be represented locally as a convergent power series around each point $z_0 \in D$.

**Proof**: Consider the Taylor series of $f$ at $z_0$:
$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n$$
For holomorphic functions, this series converges to $f(z)$ in some neighborhood of $z_0$.

### Theorem 110.1.3 (Uniqueness of Holomorphic Extension)
If $f$ and $g$ are holomorphic on a domain $D$ and $f(z) = g(z)$ on a subset of $D$ with an accumulation point, then $f = g$ on all of $D$.

**Proof**: Let $S = \{z \in D : f(z) = g(z)\}$. $S$ contains an accumulation point. By the identity theorem for holomorphic functions, $f - g$ is zero on a connected component containing $S$, hence $f = g$ on $D$.

## 110.3: Advanced Complex Analysis Theorems

### Theorem 110.3.1 (Poincaré Conjecture - Complex Version)
**Statement:** Every compact, simply connected complex surface is the complexification of a smooth manifold.

**Proof:** Using Chern classes and properties of complex vector bundles.

### Theorem 110.3.2 (Hartogs' Extension Theorem)
**Statement:** A holomorphic function on the punctured ball in ℂ^n (n ≥ 2) extends to the whole ball.

**Proof:** Using Osgood's theorem and properties of holomorphic functions in several variables.

### Theorem 110.3.3 (Fatou's Theorem on Bounded Functions)
**Statement:** Every bounded analytic function on the unit disk has radial limits almost everywhere on the boundary.

**Proof:** Using Carathéodory's theorem and properties of boundary behavior.

## 110.2 Cauchy's Integral Theorem

### Theorem 110.2.1 (Cauchy's Integral Theorem)
If $f$ is holomorphic on a simply connected domain $D$ and $\gamma$ is a piecewise smooth closed curve in $D$, then:
$$\oint_\gamma f(z) \, dz = 0$$

**Proof**: By Morera's theorem, the vanishing of the integral for all such curves implies $f$ is holomorphic. Alternatively, use Green's theorem with Cauchy-Riemann equations.

### Theorem 110.2.2 (General Cauchy's Theorem)
Let $\gamma$ be a piecewise smooth closed curve in $D$, and let $g$ be a simply connected subdomain of $D$ containing $\gamma$. If $f$ is holomorphic on $g$ and continuous on $g \cup \gamma$, then:
$$\oint_\gamma f(z) \, dz = 0$$

## 110.4 Residue Theory

### Theorem 110.4.1 (Residue Theorem)
Let $f$ be holomorphic on a domain $D$ containing a finite collection of piecewise smooth simple closed curves $\gamma_1, \dots, \gamma_n$ forming a union of non-intersecting boundaries of regions in $D$. If $a_1, \dots, a_k$ are the poles of $f$ inside $\bigcup \gamma_i$, then:
$$\oint_{\bigcup \gamma_i} f(z) \, dz = 2\pi i \sum_{j=1}^k \text{Res}(f, a_j)$$

**Proof**: Let $g(z) = f(z) - \sum_{j=1}^k \frac{\text{Res}(f, a_j)}{z - a_j}$. Then $g$ is holomorphic inside each $\gamma_i$, and the integral vanishes by Cauchy's theorem.

### Theorem 110.4.2 (Residue at Isolated Singularity)
Let $f$ have an isolated singularity at $z_0$. Then $\text{Res}(f, z_0) = \frac{1}{2\pi i} \oint_\gamma f(z) \, dz$ where $\gamma$ is a small circle around $z_0$.

## 110.5 Argument Principle

### Theorem 110.5.1 (Argument Principle)
Let $f$ be holomorphic on a domain $D$ containing a piecewise smooth simple closed curve $\gamma$ and its interior. If $f$ has no zeros or poles on $\gamma$, then:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = N - P$$
where $N$ and $P$ are the numbers of zeros and poles of $f$ inside $\gamma$, counted with multiplicity.

**Proof**: The integrand is the derivative of the logarithmic derivative of $f$. By homotopy invariance of the integral, it equals the change in argument of $f$ divided by $2\pi$.

## 110.6 Maximum Modulus Principle

### Theorem 110.6.1 (Maximum Modulus Principle)
If $f$ is holomorphic on a domain $D$ and continuous on $\overline{D}$, where $D$ is bounded, then $\max_{z \in \overline{D}} |f(z)| = \max_{z \in \partial D} |f(z)|$.

**Proof**: If $|f(z_0)| = M > \max_{z \in \partial D} |f(z)|$ for some $z_0 \in D$, then $f(D)$ contains an open neighborhood of $f(z_0)$. But this contradicts the maximum being attained at an interior point.

### Theorem 110.6.2 (Open Mapping Theorem)
If $f$ is holomorphic and non-constant on a domain $D$, then $f(D)$ is open.

**Proof**: The open mapping theorem follows from the fact that holomorphic functions are locally open mappings.

## 110.7 Conformal Mappings

### Theorem 110.7.1 (Riemann Mapping Theorem)
Let $D$ be a simply connected proper subset of the complex plane. Then there exists a biholomorphic map $f: D \to \mathbb{D}$ (the unit disk).

**Proof**: This is a deep result requiring the use of normal families and Montel's theorem.

### Theorem 110.7.2 (Schwarz Lemma)
Let $f: \mathbb{D} \to \mathbb{D}$ be holomorphic with $f(0) = 0$. Then $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$, and $|f'(0)| \leq 1$. If either $|f(z_0)| = |z_0|$ for some $z_0 \neq 0$ or $|f'(0)| = 1$, then $f(z) = e^{i\theta} z$ for some real $\theta$.

**Proof**: Consider the function $g(z) = \frac{f(z) - f(0)}{1 - \overline{f(0)}f(z)/|f(0)|}$. Use the maximum modulus principle.

## 110.8 Series Expansions

### Theorem 110.8.1 (Laurent Series)
Let $f$ be holomorphic on an annulus $A = \{z : r < |z - z_0| < R\}$. Then $f$ can be represented by a Laurent series:
$$f(z) = \sum_{n=-\infty}^\infty a_n (z - z_0)^n$$
converging absolutely on $A$.

**Proof**: Using contour integration and Cauchy's integral formula for derivatives.

### Theorem 110.8.2 (Taylor Series Convergence)
If $f$ is holomorphic at $z_0$, then its Taylor series converges to $f(z)$ in the largest disk centered at $z_0$ containing no singularities of $f$.

## 110.9 Special Functions

### Theorem 110.9.1 (Euler's Formula)
For real $t$: $e^{it} = \cos t + i \sin t$.

**Proof**: From the power series definition of $e^z$, $e^{it} = \sum \frac{(it)^n}{n!}$. Separate real and imaginary parts.

### Theorem 110.9.2 (Euler-Mascheroni Constant)
The limit $\gamma = \lim_{n \to \infty} \left(\sum_{k=1}^n \frac{1}{k} - \ln n\right)$ exists and defines the Euler-Mascheroni constant $\gamma \approx 0.57721$.

## 110.10 Additional Theorems

### Theorem 110.10.1 (Winding Number Formula)
For a continuous function $f: [0, 1] \to \mathbb{C} \setminus \{0\}$, the winding number around 0 is:
$$n(f(0), f(1), 0) = \frac{1}{2\pi i} \oint_\gamma \frac{dz}{z}$$

### Theorem 110.10.2 (Möbius Transformations)
The group of Möbius transformations $M = \{z \mapsto \frac{az+b}{cz+d} : ad-bc \neq 0\}$ acts transitively on $\hat{\mathbb{C}}$.

### Theorem 110.10.3 (Phragmén–Lindelöf Principle)
Let $D$ be a sector of the complex plane. If a holomorphic function $f$ is bounded on the boundary of $D$ and grows at most exponentially within $D$, then $f$ is bounded on all of $D$.

### Theorem 110.10.4 (Picard's Little Theorem)
The only omittable values of an entire function are $0$ and $\infty$.

**Proof**: Use the classification of singularities and the Casorati-Weierstrass theorem.

## 110.11 References and Further Reading

1. L. Ahlfors, *Complex Analysis*, 3rd ed., McGraw-Hill, 1979.
2. J. B. Conway, *Functions of One Complex Variable I*, Springer, 1995.
3. W. Rudin, *Real and Complex Analysis*, McGraw-Hill, 1986.
4. E. Hille, *Analytic Function Theory I*, American Mathematical Society, 1959.
5. N. Stein and R. Shakarchi, *Complex Analysis*, Princeton University Press, 2003.
6. H. M. Edwards, *Riemann's Zeta Function*, Dover, 1974.

*Updated on 2026-06-10*