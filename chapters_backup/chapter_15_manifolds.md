# Manifold Theory and Differential Geometry

## 15.1 Basic Manifold Theory

### 15.1.1 Definition

**Theorem 15.1:** A smooth manifold $M$ of dimension $n$ is a topological space that is:
1. Hausdorff (distinct points have disjoint neighborhoods)
2. Second-countable (has a countable basis for the topology)
3. Locally Euclidean (every point has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$)

**Smooth Structure:** $M$ also has an atlas of compatible smooth charts $(U_\alpha, \phi_\alpha)$ where $\phi_\alpha: U_\alpha \to \mathbb{R}^n$.

### 15.1.2 Example: Torus $T^2$

**Theorem 15.2:** The 2-torus $T^2 = S^1 \times S^1$ is a smooth manifold of dimension 2.

**Proof:** $S^1 \cong \{z \in \mathbb{C} : |z| = 1\}$ is a 1-manifold (union of two disjoint open arcs in $\mathbb{R}^2$). The product of 1-manifolds is a 2-manifold.

### 15.1.3 Connectedness

**Theorem 15.3:** A manifold is either connected or the disjoint union of connected components.

**Theorem 15.4:** If $M$ is a compact manifold, then $M$ is connected iff it is path-connected.

## 15.2 Tangent Spaces and Vector Fields

### 15.2.1 Tangent Space Definition

**Theorem 15.5:** For a manifold $M$ and point $p \in M$, the tangent space $T_pM$ is the vector space of equivalence classes of smooth curves $\gamma: (-\epsilon, \epsilon) \to M$ with $\gamma(0) = p$. Two curves are equivalent if their derivatives at 0 are the same.

**Equivalently:** If $(U,\phi)$ is a chart around $p$, $T_pM$ consists of formal linear combinations $\sum a_i \frac{\partial}{\partial x_i}|_p$.

### 15.2.2 Tangent Bundle

**Theorem 15.6:** The tangent bundle $TM = \bigcup_{p \in M} T_pM$ is a smooth manifold of dimension $2n$.

**Theorem 15.7:** The projection $\pi: TM \to M$ is a smooth surjective submersion with fibers $T_pM \cong \mathbb{R}^n$.

### 15.2.3 Vector Fields

**Theorem 15.8:** A vector field $X$ on $M$ is a smooth section of $TM$, i.e., a smooth map $X: M \to TM$ such that $\pi \circ X = \text{id}_M$.

**Theorem 15.9:** Vector fields form a module over $C^\infty(M)$, not a vector space over $\mathbb{R}$ (multiplying by functions is allowed).

### 15.2.4 Lie Derivative

**Theorem 15.10:** For vector fields $X,Y$ on $M$, the Lie bracket $[X,Y]$ is defined by:
$$[X,Y](f) = X(Y(f)) - Y(X(f))$$
for any smooth function $f \in C^\infty(M)$.

## 15.3 Differential Forms

### 15.3.1 k-Forms Definition

**Theorem 15.11:** A $k$-form $\omega$ on $M$ is a skew-symmetric multilinear map $T_pM \times \cdots \times T_pM \to \mathbb{R}$ (k times).

**In local coordinates:** If $\{dx^i\}$ is a basis for $T^*_p\mathbb{R}^n$, a $k$-form is $\sum c_{i_1\dots i_k} dx^{i_1} \wedge \cdots \wedge dx^{i_k}$.

### 15.3.2 Exterior Derivative

**Theorem 15.12:** For a differential form $\omega$, the exterior derivative $d\omega$ satisfies:
1. $d^2 = 0$ (apply twice to get 0)
2. $d(f\omega) = df \wedge \omega + f d\omega$ (Leibniz rule)
3. For functions $f$, $df(X_1,\dots,X_k) = \sum f(\partial_i) X_i$

### 15.3.3 Integration on Manifolds

**Theorem 15.13 (Integration on Manifolds):** Let $M$ be an oriented compact $n$-manifold and $\omega$ an $n$-form (volume form). Then $\int_M \omega$ is well-defined.

**Theorem 15.14:** Integration of a form $\omega$ over a manifold $M$ satisfies Stokes' Theorem:
$$\int_M d\omega = \int_{\partial M} \omega$$

## 15.4 Stokes' Theorem

### 15.4.1 Statement

**Theorem 15.15 (Stokes' Theorem):** Let $M$ be an oriented compact $n$-manifold with boundary $\partial M$. For any $(n-1)$-form $\omega$:
$$\int_M d\omega = \int_{\partial M} \omega$$

**Proof Sketch:** Using a partition of unity subordinate to a coordinate atlas, reduce to local computation.

### 15.4.2 Example: Green's Theorem

**Theorem 15.16:** Green's Theorem is the case of Stokes' Theorem for $n=2$, $M$ a region in $\mathbb{R}^2$, $\omega = P dx + Q dy$:
$$\oint_{\partial M} P dx + Q dy = \iint_M \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx \wedge dy$$

## 15.5 Gauss's Theorem

### 15.5.1 Statement

**Theorem 15.17 (Gauss's Theorem/Divergence Theorem):** Let $M$ be a compact oriented 3-manifold with boundary. For a 3-form $\omega$ representing a vector field divergence:
$$\int_M d\omega = \int_{\partial M} \omega$$

## 15.6 Poincaré Lemma

### 15.6.1 Statement

**Theorem 15.18 (Poincaré Lemma):** If $M$ is contractible (star-shaped), then every closed $k$-form is exact:
$$d\omega = 0 \implies \omega = d\eta \quad \text{for some } (k-1)\text{-form } \eta$$

**Proof:** Use the homotopy operator $H$ defined by contraction with radial vector field.

### 15.6.2 Cohomology

**Theorem 15.19 (de Rham Cohomology):** The cohomology groups $H^k_{dR}(M) = \ker(d^k)/\text{im}(d^{k-1})$ are invariants of the manifold.

**Theorem 15.20:** For $\mathbb{R}^n$, $H^k_{dR}(\mathbb{R}^n) = 0$ for $k>0$, and $H^0_{dR}(\mathbb{R}^n) \cong \mathbb{R}$.

## 15.7 Applications

### 15.7.1 General Relativity

**Theorem 15.21:** Spacetime is modeled as a 4-dimensional Lorentzian manifold. Geodesic equation describes particle motion.

### 15.7.2 Continuum Mechanics

**Theorem 15.22:** Material and spatial configurations are modeled by smooth manifolds. Conservation laws are expressed via Stokes' theorem on appropriate form fields.

**Solutions:** (End of section)

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*