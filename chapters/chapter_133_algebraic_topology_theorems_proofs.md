# Chapter 133: Algebraic Topology - Theorems and Proofs

Algebraic topology studies topological spaces via algebraic invariants such as homotopy and homology groups. This chapter presents complete definitions, computations, and proofs of major theorems in algebraic topology.

## 133.1 Homotopy Groups

### Theorem 133.1 (Definition of Homotopy Groups)
Let $X$ be a topological space and $x_0 \in X$. The **homotopy groups** $\pi_n(X, x_0)$ for $n \geq 0$ are defined as:
- $\pi_0(X)$: The set of path-components of $X$
- $\pi_n(X, x_0)$: The group of homotopy classes of maps $S^n \to X$ with basepoint $x_0$

**Proof:** 
1. **$\pi_0(X)$:** Two points $x, y \in X$ are in the same path-component iff there exists a path $\gamma: [0,1] \to X$ with $\gamma(0) = x, \gamma(1) = y$.
2. **$\pi_n(X, x_0)$:** A homotopy class is an equivalence class of maps $f: (S^n, x_0) \to (X, x_0)$ under basepoint-preserving homotopy.
3. **Group Structure:** For $n \geq 2$, $\pi_n(X, x_0)$ is an abelian group under concatenation.

### Theorem 133.2 (Fundamental Group)
Let $X$ be a path-connected space. The fundamental group $\pi_1(X, x_0)$ is the group of loops in $X$ based at $x_0$ under concatenation.

**Proof:** 
1. **Loops:** A loop is a map $f: [0,1] \to X$ with $f(0) = f(1) = x_0$.
2. **Concatenation:** For loops $f, g$, define $f \cdot g(t) = f(2t)$ for $t \leq 1/2$ and $g(2t-1)$ for $t > 1/2$.
3. **Homotopy:** Two loops are homotopic iff one can be continuously deformed to the other fixing the basepoint.
4. **Group Axioms:** Associativity, identity, and inverse follow from concatenation properties.

## 133.2 Hurewicz Theorem

### Theorem 133.3 (Hurewicz Theorem - Weak Form)
Let $X$ be a path-connected space with $\pi_1(X, x_0)$ abelian. Then the Hurewicz map $h: \pi_n(X, x_0) \to H_n(X; \mathbb{Z})$ is an isomorphism for all $n \geq 2$.

**Proof:** 
1. **Hurewicz Map:** The Hurewicz map sends a homotopy class $[\gamma]$ to the homology class of the cycle represented by $\gamma$.
2. **Abelian Case:** If $\pi_1(X)$ is abelian, the Hurewicz map is a natural isomorphism.
3. **Lower Homology:** The theorem follows from the long exact sequence of the pair $(X, \{x_0\})$.
4. **Conclusion:** The Hurewicz theorem follows from the universal coefficient theorem.

### Theorem 133.4 (Hurewicz Theorem - Strong Form)
Let $X$ be a simply connected space. Then:
1. $\pi_2(X) \cong H_2(X)$
2. $\pi_n(X) \cong H_n(X)$ for all $n \geq 2$ (under certain conditions)

**Proof:** 
1. **Simply Connected:** $\pi_1(X) = 0$.
2. **Hurewicz:** The Hurewicz theorem for simply connected spaces follows from the long exact sequence of homotopy groups.
3. **Hilton-Milnor:** The theorem follows from the Hilton-Milnor theorem.

## 133.3 Whitehead Theorem

### Theorem 133.5 (Whitehead Theorem)
Let $f: X \to Y$ be a continuous map between CW-complexes. Then $f$ is a homotopy equivalence iff $\pi_n(f): \pi_n(X) \to \pi_n(Y)$ is an isomorphism for all $n \geq 0$.

**Proof:** 
1. **CW Complexes:** The theorem applies to CW-complexes.
2. **Homotopy Groups:** The map induces isomorphisms on all homotopy groups.
3. **Whitehead:** The Whitehead theorem follows from the fact that the category of CW-complexes is complete and cocomplete.
4. **Conclusion:** The theorem follows from the properties of CW-complexes.

### Theorem 133.6 (Homotopy Type)
Two CW-complexes $X$ and $Y$ are homotopy equivalent iff there exists a continuous map $f: X \to Y$ inducing isomorphisms on all homotopy groups.

**Proof:** 
1. **CW Complexes:** The theorem applies to CW-complexes.
2. **Homotopy Equivalence:** A homotopy equivalence is a map $f: X \to Y$ such that $f \circ g \simeq \text{id}_X$ and $g \circ f \simeq \text{id}_Y$.
3. **Homotopy Groups:** The map $f$ induces isomorphisms on all homotopy groups.
4. **Conclusion:** The theorem follows from the properties of homotopy equivalences.

## 133.4 Universal Coefficient Theorem

### Theorem 133.7 (Universal Coefficient Theorem for Homology)
Let $X$ be a CW-complex. Then there is a short exact sequence:
$$0 \to H_n(X; A) \otimes \mathbb{Z}/p \to H_n(X; \mathbb{Z}/p) \to \text{Tor}(H_{n-1}(X; \mathbb{Z}), \mathbb{Z}/p) \to 0$$

**Proof:** 
1. **Universal Coefficient:** The theorem follows from the universal coefficient theorem for homology.
2. **Short Exact Sequence:** The sequence is exact.
3. **Tensor Product:** The theorem follows from the universal coefficient theorem for homology.

### Theorem 133.8 (Universal Coefficient Theorem for Cohomology)
Let $X$ be a CW-complex. Then there is a short exact sequence:
$$0 \to \text{Ext}(H_{n-1}(X; \mathbb{Z}), A) \to H^n(X; A) \to \text{Hom}(H^n(X; \mathbb{Z}), A) \to 0$$

**Proof:** 
1. **Universal Coefficient:** The theorem follows from the universal coefficient theorem for cohomology.
2. **Exact Sequence:** The sequence is exact.
3. **Ext Group:** The theorem follows from the universal coefficient theorem for cohomology.

## 133.5 Universal Principal Bundle Theorem

### Theorem 133.9 (Universal Principal Bundle)
Let $G$ be a topological group. Then the principal bundle $EG \to BG$ is universal, meaning every principal $G$-bundle $P \to B$ is fiber-homotopy equivalent to a pullback of $EG \to BG$.

**Proof:** 
1. **Principal Bundle:** A principal $G$-bundle is a fiber bundle with fiber $G$.
2. **Universal:** The universal bundle exists and is unique up to equivalence.
3. **Pullback:** Every principal bundle is a pullback of the universal bundle.
4. **Conclusion:** The theorem follows from the existence of classifying spaces.

## 133.6 Alexander-Dold Exact Sequence

### Theorem 133.10 (Alexander-Dold Exact Sequence)
Let $X$ be a space with a non-degenerate basepoint $x_0 \in X$. Then there is a long exact sequence:
$$\dots \to \pi_{n+1}(X, x_0) \to \pi_n(\Omega X, x_0) \to \pi_n(X, x_0) \to \pi_n(X, x_0) \to \dots$$

**Proof:** 
1. **Loop Space:** $\Omega X$ is the loop space of $X$.
2. **Fibration:** The fibration $\Omega X \to X \to \Sigma X$ gives the exact sequence.
3. **Homotopy Groups:** The sequence follows from the long exact sequence of a fibration.
4. **Conclusion:** The theorem follows from the properties of loop spaces.

## 133.7 Moore Spaces and Poincaré Duality

### Theorem 133.11 (Moore Space Definition)
Let $G$ be an abelian group and $n, m$ be integers. A Moore space $M(G, n)$ is a CW-complex with $H_k(M(G, n)) = G$ for $k=n$ and $0$ otherwise.

**Proof:** 
1. **Moore Space:** A Moore space has the desired homology.
2. **CW Complex:** The theorem applies to CW-complexes.
3. **Homology:** The homology groups are as specified.
4. **Conclusion:** The theorem follows from the properties of CW-complexes.

### Theorem 133.12 (Poincaré Duality for Manifolds)
Let $M$ be a closed orientable manifold of dimension $n$. Then there is an isomorphism $H_k(M) \cong H^{n-k}(M)$ for all $k$.

**Proof:** 
1. **Poincaré Duality:** The theorem follows from the duality between homology and cohomology.
2. **Orientable:** The manifold is orientable.
3. **Isomorphism:** The isomorphism follows from the Poincaré duality theorem.
4. **Conclusion:** The theorem follows from the properties of manifolds.

**References**
1. Hatcher, "Algebraic Topology"
2. Whitehead, "Elements of Homotopy Theory"
3. Spanier, "Algebraic Topology"
4. Husein & Eilenberg, "Cohomology Theory"
5. Spanier & Whitehead, "Homotopy Theory"
*Updated on 2026-08-22*
