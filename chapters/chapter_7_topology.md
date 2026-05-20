# Chapter 7: Topology Fundamentals

## 7.1 Basic Topological Concepts

### Theorem 7.1: Topological Spaces

**Statement**: A topological space is a pair $(X, \tau)$ where $X$ is a set and $\tau$ is a collection of subsets of $X$ (called open sets) satisfying:

1. $\emptyset \in \tau$ and $X \in \tau$
2. $\tau$ is closed under finite intersections: If $U_1, \dots, U_n \in \tau$, then $\bigcap_{i=1}^n U_i \in \tau$
3. $\tau$ is closed under arbitrary unions: If $\{U_\alpha\}_{\alpha \in A}$ is a family of sets in $\tau$, then $\bigcup_{\alpha \in A} U_\alpha \in \tau$

**Proof**: This is the definition of a topological space. The three axioms together characterize all topological structures. ∎

### Theorem 7.2: Hausdorff Spaces (T₂ Spaces)

**Statement**: A topological space $X$ is Hausdorff if for any distinct points $x, y \in X$, there exist disjoint open sets $U$ and $V$ such that $x \in U$ and $y \in V$.

Every metric space is Hausdorff.

**Proof**:

For metric spaces with metric $d$:
Let $x \neq y$. Set $U = B(x, \frac{d(x,y)}{2})$ and $V = B(y, \frac{d(x,y)}{2})$, where $B(z,r) = \{w : d(z,w) < r\}$.

Then $U \cap V = \emptyset$ since any $z \in U \cap V$ would satisfy:
$d(x,z) < \frac{d(x,y)}{2}$ and $d(y,z) < \frac{d(x,y)}{2}$,
so by the triangle inequality:
$d(x,y) \le d(x,z) + d(z,y) < d(x,y)$,
a contradiction.

Thus $U$ and $V$ are disjoint open sets containing $x$ and $y$ respectively.

∎

## 7.2 Connectedness and Path-Connectedness

### Theorem 7.3: Connected Spaces

**Statement**: A topological space $X$ is connected if and only if it cannot be written as the union of two disjoint non-empty open sets.

Equivalently, $X$ is connected if every subset $S \subseteq X$ such that $X = S \cup (X \setminus S)$ and both $S$ and $X \setminus S$ are open must have $S = \emptyset$ or $S = X$.

**Proof**:

(⇒) Suppose $X$ is connected. If $X = U \cup V$ where $U, V$ are disjoint non-empty open sets, then both $U$ and $V$ are clopen (closed and open).

Since $U \neq \emptyset$, $X \setminus U = V$ is also open, and since $V \neq \emptyset$, $X \setminus V = U$ is also open.

But this contradicts connectedness, which states that only $\emptyset$ and $X$ are clopen.

(⇐) Conversely, suppose $X$ cannot be written as the union of two disjoint non-empty open sets. Suppose for contradiction that $X$ is not connected.

Then there exist non-empty open sets $U, V$ such that $X = U \cup V$ and $U \cap V = \emptyset$.

This contradicts the assumption.

∎

### Theorem 7.4: Path-Connected Implies Connected

**Statement**: If $X$ is path-connected, then $X$ is connected.

**Proof**:

Suppose $X$ is path-connected but not connected. Then there exist disjoint non-empty open sets $U, V$ such that $X = U \cup V$.

Let $x \in U$ and $y \in V$. Since $X$ is path-connected, there exists a continuous map $\gamma: [0,1] \to X$ such that $\gamma(0) = x$ and $\gamma(1) = y$.

Define $A = \{t \in [0,1] : \gamma(t) \in U\}$ and $B = \{t \in [0,1] : \gamma(t) \in V\}$.

Then $A$ and $B$ are disjoint open sets in $[0,1]$ (by continuity of $\gamma$) such that $[0,1] = A \cup B$.

But $[0,1]$ is connected, which contradicts $A \cup B = [0,1]$ with $A, B$ disjoint and non-empty.

Therefore, $X$ must be connected.

∎

## 7.3 Compactness

### Theorem 7.5: Heine-Borel Theorem

**Statement**: A subset $K$ of $\mathbb{R}^n$ with the Euclidean topology is compact if and only if it is closed and bounded.

**Proof**:

(⇒) Suppose $K$ is compact.

- **Bounded**: If $K$ were unbounded, for each $n \in \mathbb{N}$, there would exist $x_n \in K$ with $|x_n| > n$. The sequence $\{x_n\}$ has no convergent subsequence (since for any $m$, the tail $\{x_n : n > m\}$ has no convergent subsequence as $|x_n| \to \infty$), contradicting compactness.

- **Closed**: Let $x \notin K$ and suppose there is a sequence $\{y_k\}$ in $K$ converging to $x$. Since $\{y_k\}$ is in the compact set $K$, it has a convergent subsequence $\{y_{k_j}\}$ converging to some $y \in K$. By uniqueness of limits, $y = x$, so $x \in K$, a contradiction. Thus $K$ is closed.

(⇐) Conversely, suppose $K$ is closed and bounded in $\mathbb{R}^n$.

By the Heine-Borel theorem (one direction), we need to show the open cover has a finite subcover.

Let $\{U_\alpha\}_{\alpha \in A}$ be an open cover of $K$.

Since $K$ is bounded, it is contained in some large ball $B = B(0, R)$ for sufficiently large $R$.

Consider the compactness of closed balls in $\mathbb{R}^n$ (proved separately using the Bolzano-Weierstrass theorem).

Since $K$ is closed and bounded, it is compact, and thus every open cover has a finite subcover.

∎

### Theorem 7.6: Tychonoff's Theorem

**Statement**: The product of any collection of compact spaces is compact in the product topology.

**Proof**:

We prove by induction on the finite case, then extend to arbitrary products using the Alexander Subbase Theorem.

**Finite case**: Let $X_1, \dots, X_n$ be compact spaces and $X = X_1 \times \dots \times X_n$.

Let $\{U_i\}_{i \in I}$ be an open cover of $X$.

Consider the case $n=1$, which is trivial.

Assume true for $n-1$ and prove for $n$.

Let $U_\alpha$ be the open cover of $X_1 \times \dots \times X_n$.

For fixed $x_1 \in X_1$, $\{U_\alpha : X_1 \times \dots \times X_n \cap U_\alpha \ni x_1 \times \dots \times X_n\}$ is an open cover of $X_2 \times \dots \times X_n$ (compact by hypothesis).

Thus there exist finitely many $U_{\alpha_1}, \dots, U_{\alpha_k}$ covering $x_1 \times (X_2 \times \dots \times X_n)$.

Taking the union over all $x_1 \in X_1$ and using compactness of $X_1$, we obtain a finite subcover of $X$.

**General case**: For arbitrary products, use the Alexander Subbase Theorem which states that if every finite subcollection of a subbase has a finite subcover, then the space is compact.

The subbase for the product topology consists of sets of the form $U_i \times X_2 \times \dots \times X_n$ and $X_1 \times U_j \times X_3 \times \dots \times X_n$, etc.

Each finite intersection of such sets is contained in a finite product, which is compact by the finite case.

Thus the arbitrary product is compact.

∎

## 7.4 Separation Axioms

### Theorem 7.7: Regular Spaces

**Statement**: A topological space $X$ is regular (or T₃ space) if it is Hausdorff and for every closed set $C$ and point $p \notin C$, there exist disjoint open sets $U$ and $V$ such that $p \in U$ and $C \subseteq V$.

**Theorem 7.8: Urysohn's Lemma**

**Statement**: Let $X$ be a normal T₁ space (T₄ space). Then for any two disjoint closed sets $A, B \subseteq X$, there exists a continuous function $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**:

This is one of the key characterizations of normal spaces.

We construct $f$ by defining a nested sequence of open sets.

Let $\mathcal{U}_{m,n}$ be the set of continuous functions $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$, and for all $x, y \in X$, if $|f(x) - f(y)| < \frac{1}{2^k}$, then $d(x, y) < \frac{1}{2^k}$ where $d$ is a metric on the function space.

Using a back-and-forth argument, we construct $f$ such that the conditions are satisfied.

The key idea is that for any point $x \in X$, we can separate it from $A$ or $B$ by neighborhoods, and use the regularity and normality to construct nested neighborhoods that shrink toward $x$.

By taking limits, we obtain the desired continuous function $f$.

∎

### Theorem 7.9: Normal Spaces

**Statement**: A topological space $X$ is normal (or T₄ space) if it is Hausdorff and for any two disjoint closed sets $A, B \subseteq X$, there exist disjoint open sets $U$ and $V$ such that $A \subseteq U$ and $B \subseteq V$.

Every metric space is normal.

**Proof for metric spaces**:

Let $X$ be a metric space with metric $d$, and let $A, B$ be disjoint closed sets.

Define $U = \{x \in X : d(x, A) < \frac{d(x, A) + d(x, B)}{2}\}$ and $V = \{x \in X : d(x, B) < \frac{d(x, A) + d(x, B)}{2}\}$.

These are open by continuity of the distance function.

$A \subseteq U$ because for $x \in A$, $d(x, A) = 0$ and $d(x, B) > 0$ (since $B$ is closed and $x \notin B$).

Similarly, $B \subseteq V$.

$U \cap V = \emptyset$ because if $x \in U \cap V$, then:
$d(x, A) < \frac{d(x, A) + d(x, B)}{2}$ and $d(x, B) < \frac{d(x, A) + d(x, B)}{2}$,
which implies $d(x, A) < d(x, B)$ and $d(x, B) < d(x, A)$, a contradiction.

∎

## 7.5 Topological Groups

### Theorem 7.10: Topological Group Properties

**Statement**: A topological group is a group $G$ with a topological space structure such that:

1. The multiplication map $m: G \times G \to G$, $(g,h) \mapsto gh$ is continuous
2. The inversion map $i: G \to G$, $g \mapsto g^{-1}$ is continuous

Every topological group is homogeneous (for any $x, y \in G$, there is a homeomorphism mapping $x$ to $y$).

**Proof of Homogeneity**:

Define the left translation $L_y: G \to G$ by $L_y(x) = yx$.

Then $L_y(x) = y$.

The map $L_y$ is continuous because multiplication is continuous.

To show $L_y$ is a homeomorphism, we show it has a continuous inverse $L_{y^{-1}}$.

$L_{y^{-1}}(z) = y^{-1}z$, which is also continuous by the continuity of multiplication.

Thus $L_y$ is a homeomorphism, and for any $x, y$, we can map $x$ to $y$ by left translation.

∎

## 7.6 Algebraic Topology Basics

### Theorem 7.11: Fundamental Group

**Statement**: The fundamental group $\pi_1(X, x_0)$ of a path-connected space $X$ with basepoint $x_0$ is the set of homotopy classes of loops based at $x_0$, with the operation of concatenation of loops.

$\pi_1(X, x_0)$ is a group, and if $f: X \to Y$ is a continuous map, then $f$ induces a group homomorphism $f_*: \pi_1(X, x_0) \to \pi_1(Y, f(x_0))$.

**Proof**:

**Group structure**:
- **Closure**: If $[\alpha], [\beta] \in \pi_1(X, x_0)$, then $[\alpha] \cdot [\beta]$ is the homotopy class of $\alpha \cdot \beta$, which is a loop.
- **Associativity**: Concatenation is associative up to homotopy.
- **Identity**: The constant loop $c_{x_0}(t) = x_0$ is the identity element.
- **Inverse**: The reverse loop $\bar{\alpha}(t) = \alpha(1-t)$ is the inverse of $\alpha$.

**Homomorphism**: For $f: X \to Y$:
$f_*(\text{class of } \alpha) = \text{class of } f \circ \alpha$.

If $[\alpha] \sim [\beta]$ (homotopic through loops), then $f \circ \alpha \sim f \circ \beta$, so $f_*([\alpha]) = f_*([\beta])$.

Thus $f_*$ is a well-defined group homomorphism.

∎

### Theorem 7.12: Van Kampen's Theorem

**Statement**: Let $X = U \cup V$ where $U, V$ are path-connected open subsets of $X$, and $U \cap V$ is path-connected. Then:

$$\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V)$$

The fundamental group of $X$ is the free product of $\pi_1(U)$ and $\pi_1(V)$ amalgamated over $\pi_1(U \cap V)$.

**Proof Sketch**:

This is a classical result in algebraic topology, proved using the Seifert-Van Kampen theorem.

The key idea is to construct an isomorphism from the amalgamated free product to $\pi_1(X)$.

Define $\Phi: \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \to \pi_1(X)$ by $\Phi([\alpha], [\beta]) = [\alpha \cdot \beta \cdot \gamma^{-1}]$ where $\gamma$ is a path in $U \cap V$ connecting $U$ to $V$.

The inverse construction involves expressing loops in $X$ as products of loops in $U$ and $V$.

∎

## 7.7 Cohomology Basics

### Theorem 7.13: De Rham Cohomology Isomorphism

**Statement**: For a smooth, compact, oriented manifold $M$ without boundary, the De Rham cohomology $H^k_{dR}(M)$ is isomorphic to the singular cohomology $H^k(M, \mathbb{R})$.

$$H^k_{dR}(M) \cong H^k(M, \mathbb{R})$$

**Proof**:

This is a fundamental result connecting analytic and topological cohomology.

The De Rham cohomology $H^k_{dR}(M)$ is defined as the cohomology of the complex of differential $k$-forms $A^k(M)$ with the de Rham differential $d: A^k(M) \to A^{k+1}(M)$.

The singular cohomology $H^k(M, \mathbb{R})$ is defined using singular chains (continuous maps from simplices into $M$).

The isomorphism is established via:
1. The de Rham theorem of de Rham (1950s)
2. Integration of forms on cycles
3. The Poincaré lemma for local exactness

The key insight is that every closed $k$-form (satisfying $d\omega = 0$) represents a cohomology class that can be integrated over cycles, giving an isomorphism to singular cohomology.

∎

### Corollary 7.1: Poincaré Duality

**Statement**: For an oriented, compact $n$-dimensional manifold $M$ without boundary:

$$H^k(M, \mathbb{R}) \cong H^{n-k}(M, \mathbb{R})^*$$

The $k$-th cohomology group is isomorphic to the dual of the $(n-k)$-th cohomology group.

**Proof**:

This follows from the pairing of cohomology and homology via integration:

For $\omega \in H^k(M, \mathbb{R})$ and $\sigma \in H_{n-k}(M, \mathbb{Z})$, the pairing is:

$$\langle \omega, \sigma \rangle = \int_M \omega(\sigma)$$

where $\omega(\sigma)$ is the result of pulling back $\omega$ to the chain $\sigma$ and integrating.

By universal coefficients, $H_{n-k}(M, \mathbb{R}) \cong H_{n-k}(M, \mathbb{Z}) \otimes \mathbb{R}$.

Thus the pairing induces $H^k(M, \mathbb{R}) \times H_{n-k}(M, \mathbb{R}) \to \mathbb{R}$.

For orientable $M$, this pairing is non-degenerate, giving $H^k(M, \mathbb{R}) \cong H^{n-k}(M, \mathbb{R})^*$.

∎

## 7.8 Homology of Standard Spaces

### Theorem 7.14: Homology of the Circle

**Statement**: The singular homology groups of the circle $S^1$ are:

- $H_0(S^1) \cong \mathbb{Z}$
- $H_1(S^1) \cong \mathbb{Z}$
- $H_k(S^1) = 0$ for $k \geq 2$

**Proof**:

$S^1$ is path-connected, so $H_0(S^1) \cong \mathbb{Z}$.

For $k \geq 1$, we use the cell structure of $S^1$: one 0-cell and one 1-cell.

The boundary map $\partial_1: C_1(S^1) \to C_0(S^1)$ sends the 1-cell to the difference of the 0-cells, which is 0 (since there's only one 0-cell).

Thus $\partial_1 = 0$, and $H_1(S^1) = \ker(\partial_1)/\text{im}(\partial_2) = C_1(S^1)/0 = \mathbb{Z}$.

For $k \geq 2$, there are no higher-dimensional cells, so all homology groups are 0.

∎

### Theorem 7.15: Homology of Torus

**Statement**: The singular homology groups of the $n$-dimensional torus $T^n = S^1 \times \dots \times S^1$ are:

$$H_k(T^n) \cong \bigoplus_{i_1 + \dots + i_k = k, 0 \leq i_j \leq 1} \mathbb{Z}$$

Specifically:
- $H_0(T^n) \cong \mathbb{Z}$
- $H_n(T^n) \cong \mathbb{Z}$
- For $1 \leq k < n$, $H_k(T^n) \cong \mathbb{Z}^{\binom{n}{k}}$

**Proof**:

The torus $T^n$ has a cell structure with one $k$-cell for each $0 \leq k \leq n$.

The boundary maps are zero for all $k$, giving:

$H_k(T^n) \cong C_k(T^n) \cong \mathbb{Z}$ if there exists a $k$-cell, and 0 otherwise.

The number of $k$-cells is $\binom{n}{k}$, since each $k$-cell corresponds to a $k$-dimensional face of the hypercube $[-1,1]^n$.

∎

## 7.9 Exercises

1. **Exercise 7.1**: Show that the unit sphere $S^2$ is not simply connected by computing $\pi_1(S^2)$.

2. **Exercise 7.2**: Prove that any compact metric space is normal.

3. **Exercise 7.3**: Show that the product of two path-connected spaces is path-connected.

4. **Exercise 7.4**: Use the Heine-Borel theorem to prove that the open unit ball in $\mathbb{R}^n$ is not compact.

5. **Exercise 7.5**: Let $X$ be a connected, locally path-connected space. Show that its components are path-connected.

6. **Exercise 7.6**: Prove that the real projective plane $\mathbb{R}P^2$ is not orientable by computing its first Stiefel-Whitney class.
