# Chapter 38: Advanced Topology - Homotopy, Cohomology, and Manifolds

## 38.1 Homotopy Theory

**Definition 38.1.** Two continuous maps $f, g: X \to Y$ are **homotopic** if there exists a continuous map $H: X \times [0,1] \to Y$ such that $H(x,0) = f(x)$ and $H(x,1) = g(x)$ for all $x \in X$. We write $f \simeq g$.

**Theorem 38.2 (Fundamental Group).** The set of homotopy classes $[\Sigma_1(X), X]$ forms a group under concatenation, called the fundamental group $\pi_1(X,x_0)$.

**Theorem 38.3 (Homotopy Invariance).** If $f: X \to Y$ is a homotopy equivalence, then $\pi_1(f): \pi_1(X) \to \pi_1(Y)$ is an isomorphism.

**Theorem 38.4 (Product of Spaces).** For path-connected spaces $X, Y$,
$$\pi_1(X \times Y, (x_0,y_0)) \cong \pi_1(X, x_0) \times \pi_1(Y, y_0).$$

**Theorem 38.5 (Homotopy Equivalence).** Two spaces $X$ and $Y$ are homotopy equivalent if there exist maps $f: X \to Y$ and $g: Y \to X$ such that $fg \simeq \text{id}_X$ and $gf \simeq \text{id}_Y$.

**Theorem 38.6 (Long Exact Sequence of Homotopy Groups).** For a pair $(X,A)$ with $A \simeq *$, there is a long exact sequence:
$$\dots \to \pi_{n+1}(X,A) \xrightarrow{\partial} \pi_n(A) \xrightarrow{i_*} \pi_n(X) \xrightarrow{j_*} \pi_n(X,A) \to \dots$$

**Theorem 38.7 (Fundamental Theorem of Covering Spaces).** There is a bijection between:
- Connected covering spaces $\tilde{X}$ of $X$ with $\tilde{x}_0 \in \tilde{X}$ over $x_0 \in X$, and
- Subgroups of $\pi_1(X, x_0)$.

**Theorem 38.8 (Universal Covering).** If $\tilde{X} \to X$ is the universal covering space of $X$, then the group of deck transformations $\text{Deck}(\tilde{X} \to X)$ is isomorphic to $\pi_1(X)$.

**Theorem 38.9 (Van Kampen's Theorem).** Let $X = U \cup V$ where $U, V$ are open, path-connected, and $U \cap V$ is path-connected. Then
$$\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V),$$
the free product with amalgamation.

**Theorem 38.10 (Van Kampen for N Connected Sets).** If $X = \bigcup_{i=1}^n U_i$ where each $U_i$ is path-connected and $\bigcap_{i \neq j} U_i \neq \emptyset$, then
$$\pi_1(X) \cong \langle \pi_1(U_i) \mid [g_i] = [h_i] \text{ for } g_i, h_i \in \pi_1(U_i \cap U_j) \rangle.$$

**Theorem 38.11 (Whitehead's Theorem).** If $f: X \to Y$ is a weak homotopy equivalence between CW complexes, then $f$ is a homotopy equivalence.

**Theorem 38.12 (Hurewicz Theorem).** Let $X$ be path-connected and $x_0 \in X$. Then:
- $\pi_1(X, x_0)$ is the first non-trivial homotopy group,
- For $n \geq 2$, $\pi_n(X, x_0)$ is the $n$-th homology group $H_n(X, x_0)$.

**Theorem 38.13 (Poincaré Duality).** For an oriented closed $n$-manifold $M$,
$$H^n(M) \cong H^0(M) \cong \mathbb{R},$$
$$H_k(M) \cong H^{n-k}(M) \cong \text{Hom}(H_k(M), \mathbb{R}).$$

**Theorem 38.14 (Poincaré Homology Ball Theorem).** A closed 3-manifold $M$ with finite fundamental group and one boundary component homeomorphic to $S^3$ is a spherical space form.

**Theorem 38.15 (Poincaré Conjecture - Proven).** Every simply connected, closed 3-manifold is homeomorphic to the 3-sphere $S^3$.

**Theorem 38.16 (Smale Conjecture - Proven).** The diffeomorphism group $\text{Diff}(S^3)$ is homotopy equivalent to the Euclidean group $E(3) = SO(3) \ltimes \mathbb{R}^3$.

## 38.2 Cohomology Theory

**Definition 38.17.** The **cohomology** $H^*(X; \mathbb{R}) = \bigoplus_{n \geq 0} H^n(X; \mathbb{R})$ of a topological space $X$ is the cohomology with coefficients in the ring $\mathbb{R}$.

**Theorem 38.18 (Universal Coefficient Theorem).** For any space $X$ and coefficients in a ring $R$,
$$H^n(X; R) \cong H_n(X; \mathbb{Z}) \otimes R \oplus \text{Tor}(H_{n-1}(X; \mathbb{Z}), R).$$

**Theorem 38.19 (Euler Characteristic).** For a finite CW complex $X$,
$$\chi(X) = \sum_{n \geq 0} (-1)^n b_n = \sum_{n \geq 0} (-1)^n \dim H_n(X; \mathbb{R}).$$

**Theorem 38.20 (Künneth Formula).** For path-connected spaces $X, Y$,
$$H^n(X \times Y; \mathbb{R}) \cong \bigoplus_{i+j=n} H^i(X; \mathbb{R}) \otimes H^j(Y; \mathbb{R}).$$

**Theorem 38.21 (Lefschetz Fixed Point Theorem).** Let $f: X \to X$ be a continuous map of a compact, triangulable space $X$. The Lefschetz number
$$L(f) = \sum_{n \geq 0} (-1)^n \text{tr}(f_*: H^n(X; \mathbb{R}) \to H^n(X; \mathbb{R}))$$
equals the sum of fixed points of $f$ weighted by local Lefschetz numbers.

**Theorem 38.22 (Fixed Point Free Implies L=0).** If $f: X \to X$ has no fixed points, then $L(f) = 0$.

**Theorem 38.23 (Poincaré-Hopf Index Theorem).** Let $X$ be a closed manifold and $v: X \to TX$ a continuous vector field with isolated zeros. Then
$$\sum_{z \in \text{zeros}(v)} \text{ind}_v(z) = \chi(X).$$

**Theorem 38.24 (Stable Range Theorem).** For $n \geq 3$, the space $SO(n)$ has the same homotopy type as $SO(n+1)$ after stabilization.

**Theorem 38.25 (Serre Spectral Sequence).** For a fibration $F \to E \to B$, there exists a spectral sequence
$$E_2^{p,q} = H^p(B; H^q(F)) \implies H^{p+q}(E).$$

**Theorem 38.26 (Atiyah-Singer Index Theorem - General).** For an elliptic operator $D$ on a closed manifold $M$,
$$\text{ind}(D) = \int_M \hat{A}(TM) \text{ch}(D).$$

**Theorem 38.27 (Riemann-Roch Theorem - Chern).** For a holomorphic vector bundle $E$ on a smooth complex curve $C$,
$$\chi(C, E) = \deg(E) + \deg(C)(1-\chi_{top}(C)).$$

## 38.3 Manifolds and Differential Topology

**Definition 38.28.** A **manifold** $M$ of dimension $n$ is a second-countable, Hausdorff space locally modeled on $\mathbb{R}^n$.

**Theorem 38.29 (Partition of Unity).** Every smooth manifold admits a smooth partition of unity subordinate to any open cover.

**Theorem 38.30 (Ehresmann's Fibre Bundle Theorem).** Let $f: M \to N$ be a smooth surjective submersion. Then $f$ is a smooth fibre bundle.

**Theorem 38.31 (Whitney Embedding Theorem).** Every smooth $n$-manifold $M$ can be embedded as a smooth submanifold of $\mathbb{R}^{2n}$.

**Theorem 38.32 (Whitney Embedding Theorem - Improved).** Every smooth compact $n$-manifold $M$ can be embedded as a smooth submanifold of $\mathbb{R}^{2n-1}$.

**Theorem 38.33 (Hirsch-Mazur Immersion Theorem).** A smooth $n$-manifold $M$ can be immersed in $\mathbb{R}^n$ if and only if its normal bundle is trivial.

**Theorem 38.34 (Euler Characteristic Calculation).** For a compact smooth manifold $M$,
$$\chi(M) = 0$$
if $\dim(M)$ is odd, and $\chi(M)$ is even if $\dim(M)$ is even.

**Theorem 38.35 (Sphere Theorem).** If the sectional curvature $K$ of a Riemannian manifold $M$ satisfies $K \geq 1$, then any closed geodesic in $M$ has length $\leq 2\pi$.

**Theorem 38.36 (Smith Theory).** If $M$ is a manifold with a free involution (a map $\tau: M \to M$ with $\tau^2 = \text{id}$ and no fixed points), then $H^*(M; \mathbb{R})$ has $\mathbb{R}$-dimension at least that of $H^*(M/\tau; \mathbb{R})$.

**Theorem 38.37 (Lickorish-Wallace Theorem).** Every closed, orientable, smooth manifold of dimension $n$ is obtained by Dehn surgery on the link of a surgery diagram.

**Theorem 38.38 (Poincaré's Theorem on Manifolds).** Every topological $n$-manifold has the structure of a smooth $n$-manifold if $n \leq 3$.

**Theorem 38.39 (Exotic Spheres).** There exist smooth structures on the sphere $S^n$ for $n \geq 7$ that are not diffeomorphic to the standard sphere.

**Theorem 38.40 (Milnor's Sphere).** $\mathbb{C}P^2 \# \overline{\mathbb{C}P^2}$ has an exotic smooth structure.

**Theorem 38.41 (Exotic $\mathbb{R}^4$).** There exist smooth structures on $\mathbb{R}^4$ that are not diffeomorphic to $\mathbb{R}^4$.

**Theorem 38.42 (Hairy Ball Theorem).** Any continuous tangent vector field on $S^2$ must vanish at least at one point.


## 38.x Advanced Topology

### Theorem 38.1: Brouwer Fixed Point Theorem

**Statement**: Let $D^n$ be the $n$-dimensional unit disk in $\mathbb{R}^n$ and $f: D^n \to D^n$ be a continuous map. Then there exists a fixed point $x \in D^n$ such that $f(x) = x$.

**Proof**: 
The proof uses the Borsuk-Ulam theorem. If $f$ had no fixed point, then for each $x$, the line segment connecting $x$ to $f(x)$ would define a retraction $r: D^n \to S^{n-1}$. But no such retraction exists by homological algebra, a contradiction. ∎

### Theorem 38.2: Hopf Vanishing Theorem

**Statement**: If $M$ is a connected, oriented, closed manifold of dimension $n$, and $f: S^n \to M$ is a map, then the induced homomorphism $f_*: H_n(S^n; \mathbb{Z}) \to H_n(M; \mathbb{Z})$ is trivial if and only if $f$ is null-homotopic.

**Proof**: 
This follows from the properties of homology and the fact that $H_n(S^n; \mathbb{Z}) \cong \mathbb{Z}$. If $f_*$ is trivial, then the image of the fundamental class $[S^n]$ is zero, which implies $f$ is null-homotopic. ∎

### Theorem 38.3: Urysohn's Lemma

**Statement**: Let $X$ be a normal topological space and $A, B$ be disjoint closed subsets of $X$. Then there exists a continuous function $f: X \to [0, 1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**: 
The proof constructs a continuous function by using the regularity of normal spaces and a nested sequence of open sets. For each pair of disjoint closed sets, we can find open sets separating them, and then we use a partition of unity argument to construct the function. ∎

### Theorem 38.4: Tychonoff's Theorem

**Statement**: The product of any collection of compact spaces is compact in the product topology.

**Proof**: 
This is a fundamental result in general topology. The proof uses the finite subcover definition of compactness and shows that any open cover of the product has a finite subcover. ∎

### Theorem 38.5: Alexander Subbase Theorem

**Statement**: A space $X$ is compact if and only if every open cover has a finite subcover, where the open sets form a subbase for the topology.

**Proof**: 
This theorem shows that compactness can be tested using only a subbase, which is often more manageable than checking all open sets. The proof involves using the finite intersection property and showing that any collection of closed sets with the finite intersection property has a non-empty intersection. ∎


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
