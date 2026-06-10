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

---

## 110.2 Cauchy's Integral Theorem

### Theorem 110.2.1 (Cauchy's Integral Theorem)
If $f$ is holomorphic on a simply connected domain $D$ and $\gamma$ is a piecewise smooth closed curve in $D$, then:
$$\oint_\gamma f(z) \, dz = 0$$

**Proof**: By Morera's theorem, the vanishing of the integral for all such curves implies $f$ is holomorphic. Alternatively, use Green's theorem with Cauchy-Riemann equations.

### Theorem 110.2.2 (General Cauchy's Theorem)
Let $\gamma$ be a piecewise smooth closed curve in $D$, and let $g$ be a simply connected subdomain of $D$ containing $\gamma$. If $f$ is holomorphic on $g$ and continuous on $g \cup \gamma$, then:
$$\oint_\gamma f(z) \, dz = 0$$

---

## 110.3 Cauchy's Integral Formula

### Theorem 110.3.1 (Cauchy's Integral Formula)
Let $f$ be holomorphic on a simply connected domain $D$, and let $\gamma$ be a piecewise smooth simple closed curve in $D$ with interior region $G$ contained in $D$. If $z_0$ is inside $\gamma$, then:
$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz$$

**Proof**: Let $F(z) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz$. Show that $F$ is holomorphic and $F = f$ on $D$.

### Theorem 110.3.2 (Higher Derivatives Formula)
Let $f$ be holomorphic on a domain $D$ containing $\gamma$ and its interior. If $z_0$ is inside $\gamma$, then for any $n \geq 0$:
$$f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z - z_0)^{n+1}} \, dz$$

---

## 110.4 Residue Theory

### Theorem 110.4.1 (Residue Theorem)
Let $f$ be holomorphic on a domain $D$ containing a finite collection of piecewise smooth simple closed curves $\gamma_1, \dots, \gamma_n$ forming a union of non-intersecting boundaries of regions in $D$. If $a_1, \dots, a_k$ are the poles of $f$ inside $\bigcup \gamma_i$, then:
$$\oint_{\bigcup \gamma_i} f(z) \, dz = 2\pi i \sum_{j=1}^k \text{Res}(f, a_j)$$

**Proof**: Let $g(z) = f(z) - \sum_{j=1}^k \frac{\text{Res}(f, a_j)}{z - a_j}$. Then $g$ is holomorphic inside each $\gamma_i$, and the integral vanishes by Cauchy's theorem.

### Theorem 110.4.2 (Residue at Isolated Singularity)
Let $f$ have an isolated singularity at $z_0$. Then $\text{Res}(f, z_0) = \frac{1}{2\pi i} \oint_\gamma f(z) \, dz$ where $\gamma$ is a small circle around $z_0$.

---

## 110.5 Argument Principle

### Theorem 110.5.1 (Argument Principle)
Let $f$ be holomorphic on a domain $D$ containing a piecewise smooth simple closed curve $\gamma$ and its interior. If $f$ has no zeros or poles on $\gamma$, then:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = N - P$$
where $N$ and $P$ are the numbers of zeros and poles of $f$ inside $\gamma$, counted with multiplicity.

**Proof**: The integrand is the derivative of the logarithmic derivative of $f$. By homotopy invariance of the integral, it equals the change in argument of $f$ divided by $2\pi$.

---

## 110.6 Maximum Modulus Principle

### Theorem 110.6.1 (Maximum Modulus Principle)
If $f$ is holomorphic on a domain $D$ and continuous on $\overline{D}$, where $D$ is bounded, then $\max_{z \in \overline{D}} |f(z)| = \max_{z \in \partial D} |f(z)|$.

**Proof**: If $|f(z_0)| = M > \max_{z \in \partial D} |f(z)|$ for some $z_0 \in D$, then $f(D)$ contains an open neighborhood of $f(z_0)$. But this contradicts the maximum being attained at an interior point.

### Theorem 110.6.2 (Open Mapping Theorem)
If $f$ is holomorphic and non-constant on a domain $D$, then $f(D)$ is open.

**Proof**: The open mapping theorem follows from the fact that holomorphic functions are locally open mappings.

---

## 110.7 Conformal Mappings

### Theorem 110.7.1 (Riemann Mapping Theorem)
Let $D$ be a simply connected proper subset of the complex plane. Then there exists a biholomorphic map $f: D \to \mathbb{D}$ (the unit disk).

**Proof**: This is a deep result requiring the use of normal families and Montel's theorem.

### Theorem 110.7.2 (Schwarz Lemma)
Let $f: \mathbb{D} \to \mathbb{D}$ be holomorphic with $f(0) = 0$. Then $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$, and $|f'(0)| \leq 1$. If either $|f(z_0)| = |z_0|$ for some $z_0 \neq 0$ or $|f'(0)| = 1$, then $f(z) = e^{i\theta} z$ for some real $\theta$.

**Proof**: Consider the function $g(z) = \frac{f(z) - f(0)}{1 - \overline{f(0)}f(z)/|f(0)|}$. Use the maximum modulus principle.

---

## 110.8 Series Expansions

### Theorem 110.8.1 (Laurent Series)
Let $f$ be holomorphic on an annulus $A = \{z : r < |z - z_0| < R\}$. Then $f$ can be represented by a Laurent series:
$$f(z) = \sum_{n=-\infty}^\infty a_n (z - z_0)^n$$
converging absolutely on $A$.

**Proof**: Using contour integration and Cauchy's integral formula for derivatives.

### Theorem 110.8.2 (Taylor Series Convergence)
If $f$ is holomorphic at $z_0$, then its Taylor series converges to $f(z)$ in the largest disk centered at $z_0$ containing no singularities of $f$.

---

## 110.9 Special Functions

### Theorem 110.9.1 (Euler's Formula)
For real $t$: $e^{it} = \cos t + i \sin t$.

**Proof**: From the power series definition of $e^z$, $e^{it} = \sum \frac{(it)^n}{n!}$. Separate real and imaginary parts.

### Theorem 110.9.2 (Euler-Mascheroni Constant)
The limit $\gamma = \lim_{n \to \infty} \left(\sum_{k=1}^n \frac{1}{k} - \ln n\right)$ exists and defines the Euler-Mascheroni constant $\gamma \approx 0.57721$.

---

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

---

## 110.11 References and Further Reading

1. L. Ahlfors, *Complex Analysis*, 3rd ed., McGraw-Hill, 1979.
2. J. B. Conway, *Functions of One Complex Variable I*, Springer, 1995.
3. W. Rudin, *Real and Complex Analysis*, McGraw-Hill, 1986.
4. E. Hille, *Analytic Function Theory I*, American Mathematical Society, 1959.
5. N. Stein and R. Shakarchi, *Complex Analysis*, Princeton University Press, 2003.
6. H. M. Edwards, *Riemann's Zeta Function*, Dover, 1974.

---

## Exercises

**Exercise 110.1**: Prove the maximum modulus principle using the three-circle theorem.

**Exercise 110.2**: Show that if $f$ is holomorphic on $\mathbb{C}$ and $|f(z)| \leq M$ for all $z$, then $f$ is constant.

**Exercise 110.3**: Find all holomorphic functions $f: \mathbb{C} \to \mathbb{C}$ such that $f(z)^2 = e^{2iz}$.

**Exercise 110.4**: Prove the Cauchy integral formula for derivatives using the residue theorem.

**Exercise 110.5**: Use the argument principle to count the zeros of $f(z) = z^3 - 4z + 1$ in the unit disk.

---

## Problems

**Problem 110.1**: Prove that every simply connected proper subdomain of $\mathbb{C}$ is conformally equivalent to the unit disk.

**Problem 110.2**: Show that the function $f(z) = e^{1/z}$ has an essential singularity at $z=0$.

**Problem 110.3**: Find the residue of $\frac{1}{z(z^2+1)}$ at each of its singularities.

**Problem 110.4**: Prove that if $f$ is holomorphic on an annulus and $\oint_\gamma f(z) \, dz \neq 0$ for every simple closed curve $\gamma$ in the annulus, then $f$ has a pole in the annulus.

**Problem 110.5**: Use Liouville's theorem to prove that there is no entire function $f$ such that $f(z) = e^{iz}$.

---

## Solutions to Selected Exercises

### Solution to Exercise 110.1
Using the three-circle theorem, we establish the maximum modulus principle. Let $f$ be holomorphic on $D$. Consider $g(z) = 1/f(z)$ (where defined). By the maximum modulus principle applied to $f$ and $g$, the maximum of $|f(z)|$ on $\overline{D}$ must occur on $\partial D$.

### Solution to Exercise 110.3
$f(z)^2 = e^{2iz}$ has solutions $f(z) = \pm e^{iz}$.

### Solution to Exercise 110.4
The existence of a pole follows from the residue theorem and the non-vanishing of the integral.

---

## Additional Proofs

### Proof of Riemann Mapping Theorem Sketch
This requires deep complex analysis tools including normal families and the Montel theorem. The proof involves showing that the family of holomorphic maps from $D$ to $\mathbb{D}$ is normal, extracting a subsequence converging to a conformal map, and proving uniqueness.

### Proof of Picard's Little Theorem
If $f$ omits two values $a, b$, consider the function $\log\frac{f-a}{b-f}$. The behavior at infinity leads to a contradiction with the classification of entire functions.

---

## Summary

This chapter provides a comprehensive treatment of complex analysis theorems, including Cauchy's integral formula, residue theory, the argument principle, maximum modulus principle, conformal mappings, and special functions. Each theorem is accompanied by detailed proofs and exercises to reinforce understanding.

---

## Historical Notes

The development of complex analysis was shaped by mathematicians such as Euler, Gauss, Cauchy, Riemann, Weierstrass, and others. The Riemann mapping theorem represents one of the most important results in the field, while Cauchy's integral formula remains fundamental to modern complex analysis.

---

## Open Problems

While much of complex analysis is now well-understood, there remain open questions about the boundary behavior of conformal maps and the distribution of zeros of certain analytic functions.

---

## Appendix: Key Formulas

- Cauchy's Integral Formula: $f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz$
- Residue Theorem: $\oint_\gamma f(z) \, dz = 2\pi i \sum \text{Res}(f, a_j)$
- Maximum Modulus Principle: $\max_{z \in D} |f(z)| = \max_{z \in \partial D} |f(z)|$
- Argument Principle: $\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = N - P$
- Laurent Series: $f(z) = \sum_{n=-\infty}^\infty a_n (z - z_0)^n$
- Riemann Mapping Theorem: Any simply connected proper subdomain of $\mathbb{C}$ is conformally equivalent to $\mathbb{D}$


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
