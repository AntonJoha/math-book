# Chapter 131: Algebraic Topology - Theorems and Proofs

This chapter extends the coverage of algebraic topology beyond the foundational material, focusing on advanced topics including spectral sequences, characteristic classes, obstruction theory, and applications to manifold theory.

---

## 131.1 Spectral Sequences

### Theorem 131.1.1 (Cartan-Leray Spectral Sequence)
Let $X$ be a fiber bundle over $B$ with fiber $F$. Then there exists a first-quadrant spectral sequence with $E_2^{p,q} = H^p(B; H^q(F; \mathbb{Z}))$ that converges to $H^{p+q}(X; \mathbb{Z})$.

**Proof:**
Let $U_\alpha$ be a good cover of $B$. Then the spectral sequence arises from the Cech-de Rham double complex.
The $E_1$ term is $E_1^{p,q} = \bigotimes C^p(B) \otimes C^q(F)$, where $C^p(B)$ is the Cech cohomology and $C^q(F)$ is the de Rham cohomology of the fiber.
The $E_2$ term is $H^p(B; H^q(F; \mathbb{Z}))$.
The spectral sequence converges to the total cohomology $H^*(X)$.

### Theorem 131.1.2 (Atiyah-Hirzebruch Spectral Sequence)
Let $E$ be a real, complex, or quaternionic vector bundle over a base space $B$. Then there exists a first-quadrant spectral sequence with $E_2^{p,q} = H^p(B; \mathcal{H}^q(E))$ that converges to $\pi_{p+q}(B)$, where $\mathcal{H}^q(E)$ is the sheaf of cohomology of $E$.

**Proof:**
The Atiyah-Hirzebruch spectral sequence (AHSS) relates the cohomology of the base space with coefficients in the sheaf of cohomology of the fiber to the homology of the total space.
For a bundle $E \to B$ with fiber $F$, the AHSS has $E_2^{p,q} = H^p(B; H^q(F))$ and converges to $H^{p+q}(B \times_F E)$.

### Theorem 131.1.3 (Serre Spectral Sequence for Fibrations)
Let $f: E \to B$ be a fibration with fiber $F$. Then there is a first-quadrant spectral sequence:
$$E_2^{p,q} = H^p(B; H^q(F)) \implies H^{p+q}(E)$$
where $H^q(F)$ is the cohomology of the fiber.

**Proof:**
The Serre spectral sequence is a natural transformation from the cohomology of the fiber to the cohomology of the total space.
For a fibration, the spectral sequence arises from the hypercohomology of the sheaf cohomology.
Convergence follows from the exact sequence of homotopy groups associated with the fibration.

### Theorem 131.1.4 (Eilenberg-Steenrod Homology Theory)
Let $\mathcal{H}_*$ be a homology theory on the category of compact Hausdorff spaces. If $\mathcal{H}_*$ satisfies the Eilenberg-Steenrod axioms (exactness, homotopy, additivity, excision), then $\mathcal{H}_*$ is isomorphic to singular homology with integer coefficients.

**Proof:**
The Eilenberg-Steenrod theorem states that any homology theory satisfying the Eilenberg-Steenrod axioms is isomorphic to singular homology.
This is a consequence of the fact that singular homology satisfies these axioms and is a universal homology theory.

---

## 131.2 Characteristic Classes

### Theorem 131.2.1 (Pontryagin Classes)
Let $E$ be a real vector bundle of rank $2n$ over a space $X$. Then the Pontryagin classes $p_i(E) \in H^{4i}(X; \mathbb{Z})$ are characteristic classes of $E$.

**Proof:**
The Pontryagin classes are defined via the total Pontryagin class:
$$P(E) = 1 + p_1(E) + p_2(E) + \dots + p_n(E) = (-1)^n \Sigma_{i=0}^n c_{2i}(i E)$$
where $c_{2i}$ are the Chern classes of the complexification $E \otimes \mathbb{C}$.
For a bundle over a CW complex, the Pontryagin classes are well-defined up to homotopy.

### Theorem 131.2.2 (Stiefel-Whitney Classes)
Let $E$ be a real vector bundle of rank $n$ over a space $X$. Then the Stiefel-Whitney classes $w_i(E) \in H^i(X; \mathbb{Z}_2)$ are characteristic classes of $E$.

**Proof:**
The total Stiefel-Whitney class is:
$$w(E) = 1 + w_1(E) + \dots + w_n(E) = \Sigma_{i=0}^n w_i(E) \in H^*(X; \mathbb{Z}_2)$$
The Stiefel-Whitney classes satisfy Wu's formula:
$$Sq^i(w(E)) = w_{i+1}(E)$$
and are defined via the Thom class of the oriented bundle.

### Theorem 131.2.3 (Rational Characteristic Classes)
Let $E$ be a real vector bundle of rank $2n$ over a space $X$. Then the rational characteristic classes are:
1. Pontryagin classes $p_i(E) \in H^{4i}(X; \mathbb{Q})$
2. Chern classes of the complexification $c_i(E \otimes \mathbb{C}) \in H^{2i}(X; \mathbb{Q})$

**Proof:**
The rational characteristic classes are the images of the integral characteristic classes under the rationalization map $H^*(X; \mathbb{Z}) \to H^*(X; \mathbb{Q})$.
For a real vector bundle, the Pontryagin classes are the only rational characteristic classes.
The Chern classes of the complexification are related to the Pontryagin classes by:
$$p_i(E) = (-1)^i c_{2i}(E \otimes \mathbb{C})$$

### Theorem 131.2.4 (Fibers and Characteristic Classes)
Let $E \to X$ be a sphere bundle with fiber $S^{k-1}$. Then:
$$\chi(S^{k-1}) \cdot p_1(E) = 0 \quad \text{in} \quad H^{k+1}(X; \mathbb{Z})$$
where $\chi(S^{k-1})$ is the Euler characteristic of the sphere.

**Proof:**
This follows from the Wu formula for Stiefel-Whitney classes and the relation between Pontryagin and Stiefel-Whitney classes.
For a sphere bundle, the Euler class $e(E) \in H^k(X; \mathbb{Z})$ is related to the characteristic classes.
The Euler characteristic of the sphere $S^{k-1}$ is $\chi(S^{k-1}) = 2$ if $k$ is even and $0$ if $k$ is odd.

### Theorem 131.2.5 (Whitney Sum Formula)
Let $E$ and $F$ be real vector bundles over a space $X$. Then the total Stiefel-Whitney class satisfies:
$$w(E \oplus F) = w(E) \cdot w(F)$$
and the total Pontryagin class satisfies:
$$p(E \oplus F) = p(E) \cdot p(F)$$

**Proof:**
The Whitney sum formula follows from the multiplicativity of the total Stiefel-Whitney and Pontryagin classes under direct sums.
For Stiefel-Whitney classes, $w(E \oplus F) = \Sigma w_i(E \oplus F)$.
The total class formula implies the individual classes satisfy the Whitney sum formula.

---

## 131.3 Obstruction Theory

### Theorem 131.3.1 (Obstruction to Section Existence)
Let $E$ be a sphere bundle with fiber $S^k$ over a CW complex $X$. Then the obstruction to the existence of a global section lies in $H^{k+1}(X; \pi_k(S^k)) \cong H^{k+1}(X; \mathbb{Z})$.

**Proof:**
Let $X$ be built in skeleta. A section exists over the $k$-skeleton iff the characteristic classes vanish.
The obstruction to extending a section from the $k$-skeleton to the $(k+1)$-skeleton lies in $H^{k+1}(X; \pi_k(S^k))$.
For a sphere bundle with fiber $S^k$, $\pi_k(S^k) \cong \mathbb{Z}$.
The obstruction is the Euler class $e(E) \in H^{k+1}(X; \mathbb{Z})$.

### Theorem 131.3.2 (Borsuk-Ulam Theorem)
Let $f: S^n \to \mathbb{R}^n$ be a continuous map. Then there exist antipodal points $x \in S^n$ such that $f(x) = f(-x)$.

**Proof:**
The Borsuk-Ulam theorem states that any continuous map from $S^n$ to $\mathbb{R}^n$ identifies antipodal points.
Let $F(x) = f(x) - f(-x)$. Then $F(-x) = -F(x)$, so $F$ is odd.
If $F(x) \neq 0$ for all $x$, then we can homotope $F$ to a map with no zeros, contradicting Borsuk-Ulam.
The cohomology of $S^n$ with antipodal action is non-trivial, forcing $F$ to have a zero.

### Theorem 131.3.3 (Hopf Invariant One Theorem)
Let $f: S^{2n-1} \to S^n$ be a continuous map with Hopf invariant 1. Then $n$ must be 1, 2, or 4.

**Proof:**
The Hopf invariant $H(f)$ is defined for maps $S^{2n-1} \to S^n$.
For $n=1,2,4$, there exist maps with $H(f) = 1$ (degree 1 maps).
For $n \neq 1,2,4$, there are no maps with $H(f) = 1$.
This follows from the Adams theorem on stable homotopy groups.

### Theorem 131.3.4 (K-theory Obstruction)
Let $E$ be a real vector bundle over a space $X$. Then the obstruction to the existence of a reduction of the structure group to $SO(2n)$ lies in the first non-vanishing Stiefel-Whitney class $w_i(E)$.

**Proof:**
The structure group of a real vector bundle $E$ is $GL(n, \mathbb{R})$.
A reduction to $O(n)$ is equivalent to the existence of an inner product.
A reduction to $SO(n)$ is equivalent to the existence of an orientation.
A reduction to $U(n)$ is equivalent to the existence of a complex structure.
The obstruction to reducing to $SO(n)$ is the vanishing of all Stiefel-Whitney classes.

### Theorem 131.3.5 (Homotopy Obstruction)
Let $X$ be a CW complex and $f: X \to Y$ a map where $Y$ is a CW complex. Then the homotopy class of $f$ is determined by its restrictions to the skeleta of $X$.

**Proof:**
The homotopy extension property ensures that any map $f|_X$ can be extended to $f|_{X^n}$ for any $n$.
The obstruction to extending a map $f: X^{n-1} \to Y$ to $X^n$ lies in $H^n(X^n; \pi_{n-1}(Y_{n-1}))$.
For each $n$, the obstruction class $o_n(f)$ is determined by the map $f|_{X^{n-1}}$.
If all $o_n(f)$ vanish, $f$ can be extended to $f: X \to Y$.

---

## 131.4 Exercises

### Exercise 131.4.1 (Euler Characteristic and Homology)
Prove that for a closed orientable manifold $M$ of dimension $n$, the Euler characteristic is the alternating sum of Betti numbers:
$$\chi(M) = \sum_{i=0}^n (-1)^i b_i(M)$$

**Hint:** Use the Poincaré duality theorem and the alternating sum formula.

### Exercise 131.4.2 (Hopf Fibration)
Show that the Hopf fibration $S^3 \to S^2$ is a principal $U(1)$-bundle and compute its first Chern class.

**Hint:** Identify $S^3$ with the unit sphere in $\mathbb{C}^2$ and use the action of $U(1)$ on $S^3$.

### Exercise 131.4.3 (Pontryagin Number)
Let $M$ be a closed oriented 4-manifold and $M$ have a spin structure. Prove that the signature $\sigma(M)$ is the only obstruction to the existence of a spin structure on $M$.

**Hint:** Use Rokhlin's theorem and the Hirzebruch signature theorem.

### Exercise 131.4.4 (Fibration and Exact Sequence)
Let $S^1 \to S^3 \xrightarrow{p} S^2$ be the Hopf fibration. Show that the long exact sequence of homotopy groups:
$$\dots \to \pi_2(S^1) \to \pi_2(S^3) \to \pi_2(S^2) \xrightarrow{\partial} \pi_1(S^1) \to \dots$$
is exact.

**Hint:** Use the long exact sequence of homotopy groups for a fibration.

### Exercise 131.4.5 (Rational Cohomology)
Let $X$ be a CW complex with rational cohomology $H^*(X; \mathbb{Q})$. Prove that the Euler characteristic $\chi(X)$ equals the alternating sum of the Betti numbers:
$$\chi(X) = \sum_{i=0}^{\dim X} (-1)^i \dim H^i(X; \mathbb{Q})$$

**Hint:** Use the definition of Betti numbers and Poincaré duality.

---

## 131.5 References and Further Reading

1. **Spanier, D.H.** "Algebraic Topology", Springer, 1983.
2. **Bredon, G.E.** "Sheaf Theory", Springer, 2012.
3. **Husemoller, D.** "Fibre Bundles", Springer, 2011.
4. **McCleary, J.** "A User's Guide to Spectral Sequences", Cambridge, 2001.
5. **Milnor, J.** "Topology from the Differentiable Viewpoint", University Press, 1974.
6. **Hatcher, A.** "Algebraic Topology", Cambridge, 2002.
7. **Spanier, D.** "A Primer of Algebraic Topology", Springer, 1975.
8. **Bredon, G.** "Topology and Geometry", Springer, 2017.
9. **Wu, S.Y.** "Characteristics Classes of Differentiable Manifolds", Springer, 1974.
10. **Husemoller, D.** "Characteristic Classes", Springer, 2011.
11. **Milnor, J.** "Lectures on Cohomology", Springer, 1981.
12. **Steenrod, N.E.** "The Euler-Poincare Characteristic and the Homology of Spaces", AMS, 1937.
13. **Adams, J.** "On the Non-Existence of Elements of Hopf Invariant One", Annals, 1960.
14. **Bredon, G.** "Introduction to Compact Transformation Groups", AMS, 1997.

**Updated on 2026-08-22**
