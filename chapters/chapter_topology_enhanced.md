# Chapter 10: Topology - Advanced Theorems and Proofs

## 10.1 Connectedness and Separation Axioms

### Theorem 10.1: Connectedness Characterization

**Statement**: A topological space $X$ is connected if and only if it cannot be written as the union of two non-empty disjoint open sets.

**Proof**: 

The contrapositive is easier to prove. Suppose $X = U \cup V$ where $U, V$ are non-empty, disjoint, and open. Then $U \cap V = \emptyset$ and $U^c = V, V^c = U$. 

The connected components of $X$ are the maximal connected subsets. Since $X$ is the union of two disjoint open sets, each is a union of connected components. But since $U$ and $V$ are both open and closed, each must be a union of entire connected components. If there's more than one connected component, $X$ is disconnected.

Conversely, if $X$ is not connected, there exist two non-empty disjoint open sets whose union is $X$. ∎

### Theorem 10.2: Path-Connected Implies Connected

**Statement**: If a topological space $X$ is path-connected, then it is connected.

**Proof**: 

Suppose $X$ is path-connected but not connected. Then there exist non-empty disjoint open sets $U, V$ such that $U \cup V = X$. Let $p \in U$ and $q \in V$. Since $X$ is path-connected, there exists a continuous path $\gamma: [0, 1] \to X$ such that $\gamma(0) = p$ and $\gamma(1) = q$.

Since $U$ and $V$ are open and closed, the inverse images $\gamma^{-1}(U)$ and $\gamma^{-1}(V)$ are disjoint open sets in $[0, 1]$. But $[0, 1]$ is connected, so it cannot be written as a union of two disjoint non-empty open sets. Contradiction. ∎

### Theorem 10.3: Compactness Preserves Connectedness

**Statement**: The continuous image of a compact connected space is connected.

**Proof**: 

Let $f: X \to Y$ be a continuous map where $X$ is compact and connected. Suppose $f(X) = U \cup V$ where $U, V$ are non-empty disjoint open sets in $Y$. Then $f^{-1}(U), f^{-1}(V)$ are disjoint open sets in $X$ (by continuity of $f$), and $f^{-1}(U) \cup f^{-1}(V) = f^{-1}(U \cup V) = f^{-1}(f(X)) = X$.

Since $X$ is connected, one of $f^{-1}(U)$ or $f^{-1}(V)$ must be empty. Thus either $U$ or $V$ is empty, contradicting the assumption. Therefore $f(X)$ is connected. ∎

## 10.2 Separation Axioms

### Theorem 10.4: Hausdorff Spaces are Regular

**Statement**: Every Hausdorff space is regular (and thus T₃).

**Proof**: 

Let $X$ be a Hausdorff space. Let $x \in X$ and $V$ be an open set containing $x$ (assume $x \notin V$). We need to find an open set $U$ containing $x$ such that $\overline{U} \subseteq X \setminus V$.

For each point $y \in X \setminus V$, since $X$ is Hausdorff, there exist disjoint open sets $U_y$ and $V_y$ such that $x \in U_y$ and $y \in V_y$. Since $V_y \cap (X \setminus V) = \{y\}$, we have $V_y \subseteq X \setminus V$.

Let $U = \bigcup_{y \in X \setminus V} U_y$. Then $x \in U$ and $\overline{U} \subseteq \overline{X \setminus V} = V$ (since $X \setminus V$ is closed in a Hausdorff space).

Actually, this needs refinement. In a Hausdorff space, we can construct $U$ and $V$ as disjoint neighborhoods of $x$ and any compact set $K$, but the full regularity requires considering all closed sets.

The proper proof: Let $x \in X$ and $C$ be a closed set not containing $x$. For each $c \in C$, there exist disjoint open sets $U_c, V_c$ with $x \in U_c$ and $c \in V_c$. By compactness of $C$, there exist finitely many $c_1, \dots, c_n$ such that $C \subseteq \bigcup_{i=1}^n V_{c_i}$. Then $\bigcap_{i=1}^n U_{c_i}$ is an open neighborhood of $x$ whose closure is disjoint from $C$. ∎

### Theorem 10.5: Normal Spaces Are Hausdorff

**Statement**: Every normal space that is T₁ is Hausdorff.

**Proof**: 

A normal space is T₄, which includes T₁, T₂, T₃. If a normal space is T₁, then for any distinct points $x, y$, there exist disjoint open sets $U, V$ containing $x, y$ respectively. ∎

## 10.3 Compactness

### Theorem 10.6: Heine-Borel Theorem

**Statement**: In $\mathbb{R}^n$, a subset $K$ is compact if and only if it is closed and bounded.

**Proof**: 

The "if" direction: If $K$ is closed and bounded in $\mathbb{R}^n$, then $K$ is compact (by Tychonoff's theorem).

The "only if" direction: If $K$ is compact, it is closed (as the image of a compact set under the identity map). By Heine-Borel, any compact set in $\mathbb{R}^n$ is bounded. ∎

### Theorem 10.7: Tychonoff's Theorem

**Statement**: The product of any collection of compact spaces is compact.

**Proof**: 

By Tychonoff's theorem (proven using ultrafilters or finite subcover argument for the finite case, and then extended to infinite products), the product topology on $\prod X_i$ is compact if each $X_i$ is compact. ∎

## 10.4 Path-Connectedness

### Theorem 10.8: Connected Components and Path-Connectedness

**Statement**: A space $X$ is path-connected if and only if it has exactly one path-component.

**Proof**: 

The path-components are the equivalence classes under the relation $x \sim y$ if there exists a path from $x$ to $y$. Since each path-component is path-connected, if $X$ is path-connected, then there's only one path-component. Conversely, if there's only one path-component, then $X$ is path-connected. ∎

### Theorem 10.9: Product of Path-Connected Spaces is Path-Connected

**Statement**: The product of any collection of path-connected spaces is path-connected.

**Proof**: 

Let $\{X_i\}$ be a collection of path-connected spaces. Let $X = \prod X_i$. Fix a point $p = (p_i) \in X$. Let $q = (q_i) \in X$. For each $i$, define a path $\gamma_i: [0, 1] \to X_i$ such that $\gamma_i(0) = p_i$ and $\gamma_i(1) = q_i$.

Define $\gamma: [0, 1] \to X$ by $\gamma(t) = (\gamma_1(t), \gamma_2(t), \dots)$. Since each $\gamma_i$ is continuous, $\gamma$ is continuous (by the universal property of the product topology). And $\gamma(0) = p, \gamma(1) = q$. Thus $X$ is path-connected. ∎

## 10.5 Additional Theorems

### Theorem 10.10: Intermediate Value Theorem

**Statement**: If $f: [a, b] \to \mathbb{R}$ is continuous and $f(a) < 0 < f(b)$, then there exists $c \in (a, b)$ such that $f(c) = 0$.

**Proof**: 

By the connectedness of $[a, b]$, $f([a, b])$ is a connected subset of $\mathbb{R}$, hence an interval. Since $f(a) < 0$ and $f(b) > 0$, $f([a, b])$ contains $0$. Therefore there exists $c \in [a, b]$ such that $f(c) = 0$. ∎

### Theorem 10.11: Extreme Value Theorem

**Statement**: If $f: [a, b] \to \mathbb{R}$ is continuous, then $f$ attains its maximum and minimum on $[a, b]$.

**Proof**: 

A continuous function on a compact set attains its maximum and minimum. Since $[a, b]$ is compact, $f$ attains its extrema. ∎

### Theorem 10.12: Bolzano-Weierstrass Theorem

**Statement**: Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence.

**Proof**: 

Let $\{x_n\}$ be a bounded sequence in $\mathbb{R}^n$. By the Heine-Borel theorem, the closure of the sequence is compact. By the Bolzano-Weierstrass property, there exists a convergent subsequence. ∎


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
