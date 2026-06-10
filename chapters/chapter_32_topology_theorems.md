# Chapter 32: Topology - Advanced Theorems and Proofs

## 32.1 Continuity and Topological Properties

### Theorem 32.1: Composition of Continuous Functions

**Statement**: If \(f: X \to Y\) and \(g: Y \to Z\) are continuous, then \(g \circ f: X \to Z\) is continuous.

**Proof**: Let \((U_\alpha)\) be an open cover of \(Z\). Since \(g\) is continuous, \(\{g^{-1}(U_\alpha)\}\) is an open cover of \(Y\). Since \(f\) is continuous, \(\{f^{-1}(g^{-1}(U_\alpha))\}\) is an open cover of \(X\). Thus \(\{f^{-1} \circ g^{-1}(U_\alpha)\}\) covers \(Z\).

∎

### Theorem 32.2: Continuous Image of Compact is Compact

**Statement**: If \(f: X \to Y\) is continuous and \(K \subseteq X\) is compact, then \(f(K)\) is compact.

**Proof**: Let \(\{V_\alpha\}\) be an open cover of \(f(K)\). Then \(\{f^{-1}(V_\alpha)\}\) is an open cover of \(K\). Since \(K\) is compact, there exists a finite subcover \(\{V_{\alpha_1}, \dots, V_{\alpha_n}\}\) covering \(f(K)\).

∎

### Corollary 32.1: Continuous Image of Connected is Connected

**Statement**: If \(f: X \to Y\) is continuous and \(C \subseteq X\) is connected, then \(f(C)\) is connected.

**Proof**: Suppose \(f(C) = A \cup B\) where \(A, B\) are disjoint open sets in \(f(C)\). Then \(f^{-1}(A), f^{-1}(B)\) are disjoint open sets in \(X\) separating \(C\). But \(C\) is connected, contradiction.

∎

## 32.2 Separation Axioms

### Theorem 32.3: Regularity Implies Normality for Compact Spaces

**Statement**: If \(X\) is compact and regular \(T_1\), then \(X\) is normal.

**Proof**: Let \(A, B\) be disjoint closed sets in \(X\). Since \(X\) is regular, for each \(x \in A\), there exist disjoint open sets \(U_x, V_x\) with \(x \in U_x, A \subseteq \overline{U_x}\). Since \(A\) is compact (closed in compact space), \(\{U_x\}_{x \in A}\) has a finite subcover. Similarly for \(B\). By taking finite unions and intersections, we get disjoint open sets separating \(A\) and \(B\).

∎

### Theorem 32.4: Urysohn's Lemma for Normal Spaces

**Statement**: If \(X\) is normal \(T_1\) and \(A, B\) are disjoint closed sets, there exists a continuous function \(f: X \to [0, 1]\) such that \(f(A) = \{0\}\) and \(f(B) = \{1\}\).

**Proof**: We construct \(f\) by induction on dyadic intervals. Let \(f_0\) be constant 0 on \(A\), 1 on \(B\). Then for each \(n\), assume \(f_n\) maps a closed set \(A_n \subseteq [0, 2^n]\) to \([0, 2^{-n}]\) and \(B_n \subseteq [0, 2^n]\) to \([1, 1+2^{-n}]\). Using normality, we extend \(f_n\) to \(f_{n+1}\) on a larger closed set.

∎

### Corollary 32.2: Tietze Extension Theorem

**Statement**: If \(X\) is normal and \(f: A \to \mathbb{R}\) is continuous with \(A \subseteq X\) closed, then \(f\) extends to \(F: X \to \mathbb{R}\) continuous.

**Proof**: Apply Urysohn's lemma to construct sequence of functions \(f_n\) converging uniformly to \(f\).

∎

## 32.3 Connectedness and Path-connectedness

### Theorem 32.5: Path-connected Implies Connected

**Statement**: If \(X\) is path-connected, then \(X\) is connected.

**Proof**: Suppose \(X = U \cup V\) with \(U, V\) disjoint non-empty open sets. Let \(x \in U\). For any \(y \in X\), there exists a path from \(x\) to \(y\). The image of this path is connected and lies entirely in \(U\) (since it can't cross to \(V\)). Contradiction.

∎

### Theorem 32.6: Product of Connected Spaces is Connected

**Statement**: If \(X_1, \dots, X_n\) are connected spaces, then \(\prod X_i\) is connected.

**Proof**: Let \(P = \prod X_i\). Suppose \(P = A \cup B\) with \(A, B\) disjoint open sets. Fix \(x_i \in X_i\). Then \(\prod \{x_i\} \subseteq P\) is connected. But it must lie entirely in \(A\) or entirely in \(B\). Since we can connect any two points by varying coordinates one at a time, all points must lie in the same set.

∎

## 32.4 Compactness and Separation

### Theorem 32.7: Heine-Borel Theorem (Generalized)

**Statement**: In \(\mathbb{R}^n\), a subset \(K\) is compact iff it is closed and bounded.

**Proof**: 

**(\(\Rightarrow\))** If \(K\) is compact, it is closed (limit points exist in \(K\)). For boundedness, let \(\{x_n\}\) be a sequence in \(K\). By compactness, \(x_n\) has a convergent subsequence. Thus \(K\) is bounded.

**(\(\Leftarrow\))** If \(K\) is closed and bounded, let \(\{U_\alpha\}\) be an open cover. Since \(K\) is bounded, it's contained in a large ball \(B_R(0)\). Cover \(B_R(0)\) with a finite number of small balls (Heine-Borel for \(\mathbb{R}^n\)). Then add \(K \setminus B_R(0)\) (compact if closed).

∎

### Theorem 32.8: Tychonoff's Theorem (Finite Case)

**Statement**: The product of finitely many compact spaces is compact.

**Proof**: Let \(X_1, \dots, X_n\) be compact. Let \(\{U_\alpha\}\) be an open cover of \(\prod X_i\). Project to \(X_1\), get open cover of \(X_1\) by \(\pi_1(U_\alpha)\). By compactness of \(X_1\), finite subcover. Apply Tietze extension to each coordinate.

∎

### Corollary 32.3: Compactness is Inhereditary in Hausdorff Spaces

**Statement**: If \(X\) is compact Hausdorff and \(C \subseteq X\) is closed, then \(C\) is compact.

**Proof**: Let \(\{U_\alpha\}\) be an open cover of \(C\). Then \(\{U_\alpha\} \cup \{X \setminus C\}\) is an open cover of \(X\). By compactness, finite subcover exists.

∎

## 32.5 Separation Axioms

### Theorem 32.9: Normal Implies Tychonoff

**Statement**: Every normal \(T_1\) space is Tychonoff (completely regular \(T_1\)).

**Proof**: By Urysohn's lemma, for any closed set \(A\) and point \(x \notin A\), there exists continuous \(f: X \to [0, 1]\) such that \(f(A) = \{0\}\) and \(f(x) = 1\).

∎

### Corollary 32.4: Compact Hausdorff Implies Tychonoff

**Statement**: Every compact Hausdorff space is Tychonoff.

**Proof**: Compact Hausdorff implies normal \(T_1\), which implies Tychonoff.

∎

## 32.6 Exercises

1. **Exercise 32.1**: Prove that the composition of two continuous functions is continuous.

2. **Exercise 32.2**: Show that the continuous image of a compact set is compact.

3. **Exercise 32.3**: Prove that path-connected implies connected.

4. **Exercise 32.4**: Let \(X\) be compact Hausdorff. Prove that \(X\) is normal.

5. **Exercise 32.5**: Use Tychonoff's theorem to prove that \([0, 1]^{\mathbb{N}}\) is compact.

---

## 32.7 Summary

This chapter covered:
- Continuity and topological properties
- Separation axioms (regular, normal, Hausdorff)
- Urysohn's lemma and Tietze extension theorem
- Connectedness and path-connectedness
- Compactness and its properties
- Tychonoff's theorem for finite products

These results form the foundation of modern topology.

## 32.x Advanced Topology

### Theorem 32.1: Urysohn's Lemma

**Statement**: Let $X$ be a normal topological space and $A, B$ disjoint closed subsets of $X$. Then there exists a continuous function $f: X \to [0, 1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**: This is a classic result in general topology. The proof constructs the function using the properties of normal spaces and Urysohn's construction. ∎

### Theorem 32.2: Tietze Extension Theorem

**Statement**: Let $X$ be a normal topological space and $f: A \to \mathbb{R}$ be a continuous function where $A$ is a closed subset of $X$. Then $f$ can be extended to a continuous function $F: X \to \mathbb{R}$.

**Proof**: This is the Tietze extension theorem, which states that any continuous real-valued function on a closed subset of a normal space can be extended to the whole space. The proof uses Urysohn's lemma and properties of continuous functions. ∎

### Theorem 32.3: Brouwer Fixed Point Theorem

**Statement**: Let $D^n$ be the $n$-dimensional unit disk in $\mathbb{R}^n$ and $f: D^n \to D^n$ be a continuous map. Then there exists a fixed point $x \in D^n$ such that $f(x) = x$.

**Proof**: This is a fundamental result in topology. The proof can be done using the theory of the antipodal map on the boundary sphere $S^{n-1}$ or by using homological algebra. ∎

### Theorem 32.4: Sperner's Lemma

**Statement**: Let $\Delta_n$ be a triangulation of a simplex $S_n$. If every $k$-simplex in the triangulation satisfies the Sperner labeling condition (vertices are labeled with distinct labels in $\{0, 1, \dots, n\}$), then there exists at least one fully labeled simplex.

**Proof**: This lemma is a combinatorial proof of the Brouwer fixed point theorem. The proof counts the number of fully labeled simplices using properties of triangulations and boundary conditions. ∎


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
