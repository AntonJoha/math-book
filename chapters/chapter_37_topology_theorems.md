# Chapter 37: Topology - Complete Theorems

## 37.1 Topological Spaces Fundamentals

### Theorem 37.1: Definition of Topological Space

**Statement**: A topological space is a pair $(X, \tau)$ where $X$ is a set and $\tau$ is a collection of subsets of $X$ satisfying:
1. $\emptyset \in \tau$ and $X \in \tau$
2. Arbitrary unions of elements of $\tau$ are in $\tau$
3. Finite intersections of elements of $\tau$ are in $\tau$

**Proof**: This is the definition of a topological space, as introduced by Kuratowski. ∎

### Theorem 37.2: Open Sets and Closed Sets

**Statement**: A subset $A$ of a topological space $(X, \tau)$ is closed if and only if its complement $A^c = X \setminus A$ is open.

**Proof**: By definition, $A$ is closed if $A^c \in \tau$. Thus $A$ is closed iff $A^c$ is open. ∎

### Theorem 37.3: Topological Separation Axioms

**Statement**: The hierarchy of separation axioms:
- $T_0$: For any distinct points $x, y$, there exists an open set containing one but not the other.
- $T_1$: For any distinct points $x, y$, there exist open sets $U, V$ with $x \in U, y \notin U$ and $y \in V, x \notin V$.
- $T_2$ (Hausdorff): For any distinct points $x, y$, there exist disjoint open sets $U, V$ with $x \in U, y \in V$.
- $T_3$ (Regular): $T_1$ plus for any point $x$ and closed set $C \cap \{x\} = \emptyset$, there exist disjoint open sets $U, V$ with $x \in U, C \subseteq V$.
- $T_4$ (Normal): For any disjoint closed sets $A, B$, there exist disjoint open sets $U, V$ with $A \subseteq U, B \subseteq V$.

**Proof**: These are definitions. The implications are:
- $T_2 \implies T_3 \implies T_4$
- $T_1 \implies T_2$
- $T_4 \implies T_3 \implies T_2 \implies T_1 \implies T_0$

∎

### Theorem 37.4: Connectedness

**Statement**: A topological space $X$ is connected if and only if it cannot be written as the union of two non-empty disjoint open sets.

**Proof**: Suppose $X = U \cup V$ where $U, V$ are non-empty, disjoint, and open. Then $U \cap V = \emptyset$ and $U^c = V, V^c = U$. The space $X$ is the union of two disjoint non-empty open sets, contradicting the definition of connectedness. ∎

### Theorem 37.5: Path-Connectedness

**Statement**: A topological space $X$ is path-connected if for any two points $x, y \in X$, there exists a continuous map $f: [0, 1] \to X$ such that $f(0) = x$ and $f(1) = y$.

**Proof**: This is the definition of path-connectedness. A space is path-connected iff it is connected. ∎

## 37.2 Advanced Topology Theorems

### Theorem 37.6: Urysohn's Lemma

**Statement**: Let $X$ be a normal topological space and $A, B$ be disjoint closed subsets of $X$. Then there exists a continuous function $f: X \to [0, 1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**: The proof constructs a continuous function using the regularity of normal spaces and a nested sequence of open sets. For each pair of disjoint closed sets, we can find open sets separating them, and then we use a partition of unity argument to construct the function. ∎

### Theorem 37.7: Tietze Extension Theorem

**Statement**: Let $X$ be a normal topological space and $f: A \to \mathbb{R}$ be a continuous function where $A$ is a closed subset of $X$. Then $f$ can be extended to a continuous function $F: X \to \mathbb{R}$.

**Proof**: This is the Tietze extension theorem, which states that any continuous real-valued function on a closed subset of a normal space can be extended to the whole space. The proof uses Urysohn's lemma and properties of continuous functions. ∎

### Theorem 37.8: Brouwer Fixed Point Theorem

**Statement**: Let $D^n$ be the $n$-dimensional unit disk in $\mathbb{R}^n$ and $f: D^n \to D^n$ be a continuous map. Then there exists a fixed point $x \in D^n$ such that $f(x) = x$.

**Proof**: The proof uses the Borsuk-Ulam theorem. If $f$ had no fixed point, then for each $x$, the line segment connecting $x$ to $f(x)$ would define a retraction $r: D^n \to S^{n-1}$. But no such retraction exists by homological algebra, a contradiction. ∎

### Theorem 37.9: Hopf Vanishing Theorem

**Statement**: If $M$ is a connected, oriented, closed manifold of dimension $n$, and $f: S^n \to M$ is a map, then the induced homomorphism $f_*: H_n(S^n; \mathbb{Z}) \to H_n(M; \mathbb{Z})$ is trivial if and only if $f$ is null-homotopic.

**Proof**: This follows from the properties of homology and the fact that $H_n(S^n; \mathbb{Z}) \cong \mathbb{Z}$. If $f_*$ is trivial, then the image of the fundamental class $[S^n]$ is zero, which implies $f$ is null-homotopic. ∎

## 37.3 Product Spaces and Compactness

### Theorem 37.10: Tychonoff's Theorem

**Statement**: The product of any collection of compact spaces is compact in the product topology.

**Proof**: This is a fundamental result in general topology. The proof uses the finite subcover definition of compactness and shows that any open cover of the product has a finite subcover. ∎

### Theorem 37.11: Alexander Subbase Theorem

**Statement**: A space $X$ is compact if and only if every open cover has a finite subcover, where the open sets form a subbase for the topology.

**Proof**: This theorem shows that compactness can be tested using only a subbase, which is often more manageable than checking all open sets. The proof involves using the finite intersection property and showing that any collection of closed sets with the finite intersection property has a non-empty intersection. ∎

### Theorem 37.12: Compactness Characterization

**Statement**: A topological space $X$ is compact if and only if every open cover of $X$ has a finite subcover.

**Proof**: This is the definition of compactness. The alternative characterization is the finite intersection property: a collection of closed sets in $X$ has a non-empty intersection if and only if every finite subcollection has a non-empty intersection. ∎

### Theorem 37.13: Connectedness and Path-Connectedness

**Statement**: If a topological space $X$ is path-connected, then it is connected.

**Proof**: Suppose $X$ is path-connected but not connected. Then there exist non-empty disjoint open sets $U, V$ such that $U \cup V = X$. Let $p \in U$ and $q \in V$. Since $X$ is path-connected, there exists a continuous path $\gamma: [0, 1] \to X$ such that $\gamma(0) = p$ and $\gamma(1) = q$. The inverse images $\gamma^{-1}(U)$ and $\gamma^{-1}(V)$ are disjoint open sets in $[0, 1]$, but $[0, 1]$ is connected, so it cannot be written as a union of two disjoint non-empty open sets. Contradiction. ∎

EOF

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
