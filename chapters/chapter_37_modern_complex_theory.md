# Chapter 37: Modern Complex Analysis - Riemann Surfaces and Analytic Continuation

## 37.1 Introduction to Riemann Surfaces

**Definition 37.1.** A **Riemann surface** is a connected one-dimensional complex manifold. A function $f: U \to \mathbb{C}$ has a multivalued inverse that can be made single-valued by passing to a Riemann surface.

**Theorem 37.2 (Local Representation).** Every Riemann surface $M$ has an atlas of charts $(U_\alpha, \phi_\alpha)$ where $\phi_\alpha: U_\alpha \to \mathbb{C}$ are homeomorphisms onto open sets in $\mathbb{C}$, with transition maps $\phi_\beta \circ \phi_\alpha^{-1}$ being holomorphic.

**Theorem 37.3 (Classification of Compact Riemann Surfaces).** Every compact connected Riemann surface $M$ is conformally equivalent to either:
- $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ (sphere, genus 0), or
- A torus $\mathbb{C}/\Lambda$ (genus 1), or
- A higher-genus surface $\mathbb{C} \cup \dots$ (genus $g \geq 2$).

**Theorem 37.4 (Universal Covering).** Every compact Riemann surface $M$ of genus $g$ has:
- The Riemann sphere $\hat{\mathbb{C}}$ as its universal cover if $g=0$,
- The complex plane $\mathbb{C}$ as its universal cover if $g=1$,
- The unit disk $\mathbb{D}$ as its universal cover if $g \geq 2$.

**Theorem 37.5 (Uniformization Theorem).** Let $M$ be a compact Riemann surface of genus $g$. Then:
- If $g=0$, $M \cong \hat{\mathbb{C}}$,
- If $g=1$, $M \cong \mathbb{C}/\Lambda$ for some lattice $\Lambda \cong \mathbb{Z} \oplus \mathbb{Z}\tau$,
- If $g \geq 2$, there exists a holomorphic map $\pi: \mathbb{D} \to M$ which is a universal covering.

## 37.2 Analytic Continuation

**Definition 37.6.** An analytic continuation of $f: D \to \mathbb{C}$ to $D'$ (where $\overline{D} \cap \text{int}(D') \neq \emptyset$) is a holomorphic function $F: D' \to \mathbb{C}$ such that $F|_D = f$.

**Theorem 37.7 (Monodromy Theorem).** Let $D$ be a simply connected domain and $f$ be single-valued holomorphic on $D$. Then $f$ has a unique analytic continuation to any domain $D'$ obtainable by successive analytic continuation along paths in $D'$.

**Theorem 37.8 (Identity Theorem).** Let $f: D_1 \to \mathbb{C}$ and $g: D_2 \to \mathbb{C}$ be holomorphic on domains $D_1, D_2 \subseteq \mathbb{C}$ with $D_1 \cap D_2 \neq \emptyset$. If $f$ and $g$ agree on a set $S$ having an accumulation point in $D_1 \cap D_2$, then $f$ and $g$ agree on $D_1 \cap D_2$.

**Theorem 37.9 (Uniqueness of Analytic Continuation).** If $f$ is holomorphic on a domain $D$, then $f$ has at most one analytic continuation to any domain containing $D$.

**Theorem 37.10 (Principal Branch of Logarithm).** The principal branch $\text{Log}(z) = \ln|z| + i\text{Arg}(z)$ is holomorphic on $\mathbb{C} \setminus (-\infty, 0]$. Any other branch differs by $2\pi i n$.

**Theorem 37.11 (Branch Cuts).** For a multivalued function $f(z)$ with branch points, a branch cut is a curve joining branch points (or a branch point to $\infty$) along which $f$ cannot be made single-valued.

**Theorem 37.12 (Analytic Continuation along Paths).** The value of $f$ after analytic continuation along a path $\gamma$ depends only on the homotopy class of $\gamma$ relative to $\mathbb{C} \setminus S$, where $S$ is the set of branch points.

**Theorem 37.13 (Monodromy Representation).** The analytic continuation of $f$ around a loop $\gamma$ defines a monodromy map $m_\gamma: f \mapsto m_\gamma(f)$. These maps satisfy the monodromy group relations.

**Theorem 37.14 (Picard's Great Theorem).** Let $f$ be holomorphic at $\infty$. Then the image of any neighborhood of $\infty$ omits at most two points of $\mathbb{C}$.

**Theorem 37.15 (Picard's Little Theorem).** Let $f$ be entire and omit two values $a, b \in \mathbb{C}$. Then $f$ is constant.

**Theorem 37.16 (Weierstrass Elliptic Function).** The Weierstrass $\wp(z)$ is defined by
$$\wp(z) = \frac{1}{z^2} + \sum_{\omega \in \Lambda \setminus \{0\}} \left(\frac{1}{(z-\omega)^2} - \frac{1}{\omega^2}\right)$$
for a lattice $\Lambda \cong \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$.

**Theorem 37.17 (Differential Equation for $\wp$).** The Weierstrass elliptic function satisfies
$$\wp'(z)^2 = 4\wp(z)^3 - g_2 \wp(z) - g_3,$$
where $g_2, g_3$ are invariants of the lattice.

**Theorem 37.18 (J-Invariant).** The J-invariant of a lattice $\Lambda$ is
$$J(\Lambda) = g_2^3 / \Delta,$$
where $\Delta = g_2^3 - 27g_3^2$ is the discriminant.

**Theorem 37.19 (Modular Curve).** The map $J: \mathcal{H} \to \mathbb{C}$ from the upper half-plane $\mathcal{H}$ to $\mathbb{C}$ (where $\mathcal{H}/SL(2,\mathbb{Z}) \cong \mathbb{C}$) gives a bijective correspondence between elliptic curves and their $j$-invariants.

**Theorem 37.20 (Complex Multiplication).** A complex number $\alpha$ has **complex multiplication** by $\mathbb{Z}[\alpha]$ if $\mathbb{Z}[\alpha]$ is an imaginary quadratic order. The endomorphism ring of a CM elliptic curve is maximal among orders containing $\mathbb{Z}$.

**Theorem 37.21 (Shimura-Taniyama-Weierstrass Conjecture).** Every elliptic curve over $\mathbb{Q}$ is isomorphic to a modular curve $E \cong \mathbb{C}^*/q^{\mathbb{Z}}$.

**Theorem 37.22 (Siegel's Theorem on Integral Points).** If $C \subseteq \mathbb{C}^2$ is an algebraic curve of genus $\geq 2$, then $C(\mathbb{Z})$ is finite.

**Theorem 37.23 (Fermat's Last Theorem - Mod $p$).** For prime $p \geq 3$, the curve $x^p + y^p = z^p$ has no non-trivial solutions in $\mathbb{F}_p$.

## 37.3 Advanced Topics

**Theorem 37.24 (Hilbert's Irreducibility Theorem).** Let $f \in \mathbb{C}[t](X)$ be an irreducible polynomial. Then the set of $t_0 \in \mathbb{C}$ for which $f(t_0, X)$ is reducible over $\mathbb{C}$ is at most countable.

**Theorem 37.25 (Osgood's Theorem).** Let $D$ be a domain in $\mathbb{C}$. If $f_n \to f$ uniformly on compact subsets of $D$, then $f$ is holomorphic.

**Theorem 37.26 (Mergelyaں's Theorem).** If $E \subseteq \mathbb{C}$ is a compact set, there exists a function holomorphic on $\mathbb{C} \setminus E$ which takes a prescribed set of values on $E$.

**Theorem 37.27 (Runge's Theorem).** Let $K \subseteq \mathbb{C}$ be a compact set. Then there exists a rational function $R$ holomorphic on $\mathbb{C} \setminus K$ such that
$$\sup_{z \in K} |f(z) - R(z)| < \epsilon$$
for any $\epsilon > 0$.

**Theorem 37.28 (Runge's Approximation Theorem).** Let $K$ be a compact subset of $\mathbb{C}$. If $K$ is connected, then every holomorphic function on $\mathbb{C} \setminus K$ can be approximated uniformly on $K$ by entire functions.

**Theorem 37.29 (Weyl's Equidistribution Theorem).** Let $\alpha \in \mathbb{R}$ be irrational. Then $\{n\alpha \mod 1\}_{n \geq 1}$ is equidistributed in $[0,1)$.

**Theorem 37.30 (Kronecker's Approximation Theorem).** Let $\alpha_1, \dots, \alpha_k \in \mathbb{R}$ be linearly independent over $\mathbb{Q}$. Then the sequence $\{n\alpha_1, \dots, n\alpha_k \mod 1\}$ is dense in $[0,1]^k$.


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
