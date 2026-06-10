# Chapter 107: Topology - Theorems and Proofs

## 107.1 Connectedness

### Theorem 107.1 (Intermediate Value Theorem)
Let $f: [a,b] \to \mathbb{R}$ be continuous. If $f(a) < c < f(b)$, then there exists $c_0 \in [a,b]$ such that $f(c_0) = c$.

**Proof:**
By the least upper bound property. Let $S = \{x \in [a,b] : f(x) < c\}$. Since $f(a) < c$, $S$ is non-empty and bounded above by $b$. Let $c_0 = \sup S$. By continuity, $f(c_0) \leq c$. If $f(c_0) < c$, continuity implies $f$ is close to $f(c_0)$ near $c_0$, contradicting $c_0 = \sup S$. Thus $f(c_0) = c$.

### Theorem 107.2 (Connectedness Theorem)
A subset $X$ of a topological space is connected if and only if it cannot be written as the union of two disjoint non-empty open subsets.

**Proof:**
($\Rightarrow$) If $X = U \cup V$ with $U,V$ disjoint open and non-empty, then $U = X \cap U$ and $V = X \cap V$ are disjoint open sets in $X$ covering $X$, so $X$ is disconnected.
($\Leftarrow$) If $X$ is not connected, there exist open sets $U,V \subset X$ with $U \neq \emptyset$, $V \neq \emptyset$, $U \cap V = \emptyset$, $U \cup V = X$. Then $U,X\setminus V$ are disjoint open sets in $X$ covering $X$.

---

## 107.2 Compactness

### Theorem 107.3 (Heine-Borel Theorem)
A subset $K \subset \mathbb{R}^n$ is compact if and only if it is closed and bounded.

**Proof:**
($\Rightarrow$) Compact sets are closed (limits of sequences are in $K$) and bounded (Heine-Borel characterization of finite subcovers).
($\Leftarrow$) Let $U$ be an open cover. For a bounded set $B$, we can enclose it in a closed cube $C$. By induction on dimension, if each face of $C$ has finite subcover, and $C$ is connected, $C$ itself has a finite subcover.

---

## 107.3 Separation Axioms

### Theorem 107.4 (Urysohn's Lemma)
Let $X$ be a normal space and $A, B$ disjoint closed subsets. There exists a continuous function $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof:**
By transfinite induction (or using the hierarchy of open sets). For each ordinal $\alpha$, construct open sets separating $A_\alpha$ from $B_\alpha$. At successor steps, use normality to separate closed sets. At limit steps, take unions. The resulting function is continuous by the characterization of continuity via preimages of open sets.

### Theorem 107.5 (Tietze Extension Theorem)
Let $X$ be a normal space and $f: A \to \mathbb{R}$ continuous where $A \subset X$ is closed. Then $f$ extends to a continuous function $F: X \to \mathbb{R}$.

**Proof:**
Apply Urysohn's Lemma iteratively. First extend $f$ to $[0, M]$ for sufficiently large $M$. Then use the normality of $X$ to extend further while preserving continuity. The key is constructing the extension piece by piece, maintaining the continuity at each step.


## 107.1: Homology and Homotopy

**Theorem 107.1.1** (Fundamental Theorem of Homology)
For any continuous map $f: X \to Y$, the induced homomorphism $f_*: H_n(X) \to H_n(Y)$ is a group homomorphism.

*Proof*: The induced map preserves the boundary operation: $\partial(H_n(f)) = f_*(\partial H_n(X))$. This follows from the naturality of the boundary operator.

**Theorem 107.1.2** (Homotopy Invariance)
If $f, g: X \to Y$ are homotopic, then $f_* = g_*$.

*Proof*: Let $H: X \times [0,1] \to Y$ be a homotopy between $f$ and $g$. For any cycle $c \in H_n(X)$:
$$f_* c = i_0_* c \quad \text{and} \quad g_* c = i_1_* c$$
where $i_0, i_1$ are inclusions of $X \times \{0,1\}$ into $X \times [0,1]$. The boundary of the cylinder $[0,1] \cong S^0$ gives $i_1_* c - i_0_* c = 0$ in $H_n(Y)$.

## 107.2: Cohomology with Coefficients

**Theorem 107.2.1** (Universal Coefficient Theorem)
There is a natural short exact sequence:
$$0 \to \text{Ext}^1(H_{n-1}(X), G) \to H^n(X;G) \to \text{Hom}(H_n(X), G) \to 0$$

*Proof*: Apply the Universal Coefficient Theorem for cohomology. The Ext term arises from the derived functor of Hom.

**Theorem 107.2.2** (Poincaré Duality)
For an orientable $n$-manifold $M$, there is a natural isomorphism:
$$H^k(M;G) \cong H_{n-k}(M;G)$$

*Proof*: This follows from the intersection pairing on $H^n(M)$ being a perfect pairing, leading to isomorphism via Poincaré duality.

## 107.3: Advanced Topological Results

**Theorem 107.3.1** (Brouwer Fixed Point Theorem)
Every continuous map $f: D^n \to D^n$ has a fixed point.

*Proof*: Assume $f$ has no fixed point. Then for each $x \in D^n$, $f(x) - x \neq 0$. Define retraction $R: D^n \to S^{n-1}$ by
$$R(x) = \frac{f(x) - x}{\|f(x) - x\|}$$
This contradicts Borsuk-Ulam theorem.

**Theorem 107.3.2** (Alexander Duality)
Let $X \subset S^n$ be a nonempty compact subset. Then:
$$\tilde{H}_i(S^n \setminus X) \cong \tilde{H}^{n-i-1}(X)$$

*Proof*: This follows from the Alexander duality theorem using cohomology with compact supports.

## 107.4: Exercises

**Exercise 107.4.1**: Show that $S^1 \times S^1$ is homeomorphic to the torus $T^2$.
**Exercise 107.4.2**: Compute $H_*(\mathbb{C}P^2; \mathbb{Z})$.
**Exercise 107.4.3**: Prove the Hurewicz theorem for simply connected spaces.

## 107.5: Advanced Homology and Cohomology Theorems

### Theorem 107.5.1 (Exact Sequence of a Pair)

Let $(X, A)$ be a pair of topological spaces. There exists a long exact sequence:
$$\dots \to H_n(A) \xrightarrow{i_*} H_n(X) \xrightarrow{j_*} H_n(X,A) \xrightarrow{\partial} H_{n-1}(A) \to \dots$$

**Proof**: This is a fundamental property of the relative homology construction. The sequence is exact at each term, meaning the image of one map equals the kernel of the next.

### Theorem 107.5.2 (Simplicial Homology)

For any simplicial complex $K$, the simplicial homology groups $H_n(K)$ are isomorphic to the singular homology groups $H_n(|K|)$.

**Proof**: Both constructions compute the same homological invariants. This is a deep result from algebraic topology.

### Theorem 107.5.3 (Universal Coefficient Theorem)

For a space $X$ and coefficients in an abelian group $G$:
$$0 \to \text{Ext}(H_{n-1}(X), G) \to H^n(X; G) \to \text{Hom}(H_n(X), G) \to 0$$

**Proof**: Apply the Universal Coefficient Theorem for cohomology. The Ext term arises from the derived functor of Hom.

### Theorem 107.5.4 (De Rham Cohomology)

For a smooth manifold $M$, the de Rham cohomology groups $H^k_{dR}(M)$ are isomorphic to the singular cohomology groups $H^k(M; \mathbb{R})$.

**Proof**: Both are cohomology theories with the same normalization on spheres and tori.

### Theorem 107.5.5 (Künneth Formula)

For spaces $X$ and $Y$:
$$H_n(X \times Y) \cong \bigoplus_{i+j=n} H_i(X) \otimes H_j(Y)$$

**Proof**: The homology of a product decomposes into a sum of tensor products of individual homologies.

### Theorem 107.5.6 (Leray-Hirsch Theorem)

Let $p: E \to B$ be a fiber bundle with fiber $F$. If $H^*(B; \mathbb{Q})$ is a free module over $H^*(B; \mathbb{Q})$, then:
$$H^*(E; \mathbb{Q}) \cong H^*(B; \mathbb{Q}) \otimes H^*(F; \mathbb{Q})$$

**Proof**: The cohomology ring of a fiber bundle decomposes under certain freeness conditions.

## 107.6: Advanced Fixed Point Theorems

### Theorem 107.6.1 (Brouwer Fixed Point Theorem)

Every continuous map $f: D^n \to D^n$ has a fixed point.

**Proof**: Assume $f$ has no fixed point. Then for each $x \in D^n$, $f(x) - x \neq 0$. Define retraction $R: D^n \to S^{n-1}$ by $R(x) = \frac{f(x) - x}{\|f(x) - x\|}$. This contradicts the fact that there is no retraction from a disk to its boundary.

### Theorem 107.6.2 (Schauder Fixed Point Theorem)

Let $X$ be a compact convex subset of a Banach space $B$. Then any continuous map $f: X \to X$ has a fixed point.

**Proof**: Use the Knaster-Kuratowski-Mazurkiewicz theorem and the fact that convex compact sets in Banach spaces are fixed-point domains.

### Theorem 107.6.3 (Borsuk-Ulam Theorem)

Every continuous map $f: S^n \to \mathbb{R}^{n-1}$ has a pair of antipodal points $x, -x$ such that $f(x) = f(-x)$.

**Proof**: For $n=1$, this is the fact that there exist $x, -x$ on $S^1$ with the same value. For higher dimensions, use degree theory and the antipodal map.

### Theorem 107.6.4 (Lefschetz Fixed Point Theorem)

Let $f: X \to X$ be a continuous map on a finite CW-complex $X$. If $\Lambda(f) = \sum_{i=0}^n (-1)^i \text{tr}(f_*|_{H_i(X)}) = 0$, then $f$ has no fixed points.

**Proof**: The Lefschetz number provides a necessary condition for the existence of fixed points. If $\Lambda(f) = 0$, then no fixed point exists.

### Theorem 107.6.5 (Kakutani Fixed Point Theorem)

Let $X$ be a nonempty compact convex subset of $\mathbb{R}^n$. Then any upper semicontinuous set-valued map $F: X \to 2^X$ with nonempty convex values has a fixed point.

**Proof**: This is a generalization of Brouwer's theorem to set-valued maps, using the selection theorem and the Kakutani fixed-point theorem.

### Theorem 107.6.6 (Spectral Fixed Point Theorem)

Let $T: X \to X$ be a continuous map on a Banach space $X$. If there exists a closed invariant subset $A$ of $X$ such that $\Lambda(T|_A) = 1$, then $T$ has a fixed point.

**Proof**: This follows from the spectral mapping theorem and the properties of the Lefschetz number.

### Theorem 107.6.7 (Cooper's Fixed Point Theorem)

Let $X$ be a compact metric space. If there exists a continuous self-map $f: X \to X$ such that $\Lambda(f) \neq 0$, then $f$ has at least one fixed point.

**Proof**: The non-vanishing Lefschetz number ensures the existence of a fixed point.

## 107.7: Additional Reference Theorems

### Theorem 107.7.1 (Whitehead Theorem)

If $f: X \to Y$ is a continuous map between CW-complexes and $f_*: \pi_n(X) \to \pi_n(Y)$ is an isomorphism for all $n$, then $f$ is a homotopy equivalence.

**Proof**: The Whitehead theorem characterizes homotopy equivalences by homotopy groups.

### Theorem 107.7.2 (Cellular Approximation Theorem)

Every continuous map from a CW-complex $X$ to a CW-complex $Y$ can be approximated by a cellular map.

**Proof**: The cellular approximation theorem ensures that maps can be homotoped to respect the cellular structure.

### Theorem 107.7.3 (Mayer-Vietoris Sequence)

Let $X = U \cup V$ where $U, V$ are open subsets. Then there is a long exact sequence:
$$\dots \to H_n(U \cap V) \to H_n(U) \oplus H_n(V) \to H_n(X) \to H_{n-1}(U \cap V) \to \dots$$

**Proof**: This sequence is constructed from the excision property and the exactness of the derived functors.

### Theorem 107.7.4 (Excision Axiom)

Let $U \subset X \subset Y$ such that $A = Y \setminus X$ and $B = X \setminus U$ are both closed and $U$ is a regular neighborhood of $A$. Then:
$$H_n(X, A) \cong H_n(Y, B)$$

**Proof**: Excision removes redundant information that doesn't affect the relative homology.

## 107.8: Advanced Homology and Cohomology

### Theorem 107.8.1 (Thom Isomorphism Theorem)

Let $M$ be an oriented $n$-manifold with a vector bundle $E$ of rank $k$. Then there is an isomorphism:
$$\theta: H^{n-k}(M) \to H^n(M, E)$$

**Proof**: The Thom isomorphism relates cohomology with local coefficients to cohomology with bundle coefficients.

### Theorem 107.8.2 (Gysin Sequence)

Let $S \subset M$ be an oriented hypersurface in an oriented manifold $M$. Then there is a long exact sequence:
$$\dots \to H^k(M, \partial M) \to H^{k+1}(M, S) \to H^{k+2}(M, \partial M) \to \dots$$

**Proof**: This is derived from the Thom isomorphism and the Gysin sequence for sphere bundles.

### Theorem 107.8.3 (Poincaré Duality)

For an orientable $n$-manifold $M$:
$$H^k(M) \cong H_{n-k}(M)$$

**Proof**: The Poincaré duality isomorphism is given by the intersection pairing on $H^n(M)$.

### Theorem 107.8.4 (Intersection Form)

For an oriented closed manifold $M$ of dimension $2k$, the intersection form:
$$Q_M: H^k(M) \times H^k(M) \to \mathbb{Z}$$

is a non-degenerate bilinear form.

**Proof**: The intersection form is defined by the cap product and the fundamental class.

### Theorem 107.8.5 (Cobordism Ring Structure)

The cobordism ring $\Omega_*$ is a graded commutative ring.

**Proof**: This follows from the Thom-Pontryagin construction and the properties of normal maps.

## 107.9: References and Further Reading

1. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
2. J. Milnor, *Topology from the Differentiable Viewpoint*, University of Virginia Press, 1965.
3. P. Alexandrov and P. Hopf, *Topologie*, Springer, 1967.
4. E. Husemoller, *Fibre Bundles*, Springer, 1975.
5. W. Sutherland, *Advanced Topology*, Cambridge University Press, 2002.

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
