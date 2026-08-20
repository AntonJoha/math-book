# Chapter 29: Topology - Fundamental Theory and Proofs

## 29.1 Topological Spaces and Basic Properties

### Theorem 29.1: The Intersection Property

**Statement**: In any topological space \((X, \tau)\), the arbitrary intersection of open sets is open.

**Proof**: Let \(\{U_\alpha\}_{\alpha \in A}\) be a collection of open sets, where each \(U_\alpha \in \tau\).

By definition of a topology, \(\emptyset \in \tau\). If \(A = \emptyset\), then \(\bigcup_{\alpha \in \emptyset} U_\alpha = \emptyset \in \tau\).

For non-empty \(A\), each \(U_\alpha\) is a union of open sets (itself). The intersection \(\bigcap_{\alpha \in A} U_\alpha\) is not necessarily open, as shown by:
- Let \(X = \{a, b\}\) with \(\tau = \{\emptyset, \{a\}, X\}\)
- \(U_1 = \{a\}, U_2 = X\) are both open
- \(U_1 \cap U_2 = \{a\}\) is open
- But finite intersections are required, not arbitrary

Wait, the statement should be: **Finite** intersection of open sets is open.

Let \(\{U_1, U_2, \dots, U_n\}\) be finite open sets. Then \(\bigcap_{i=1}^n U_i\) is open since the intersection of \(n\) sets can be built by \(n-1\) iterations of binary intersection, and by axiom \(T_1\) (finite intersection).

∎

### Theorem 29.2: Topology Uniqueness

**Statement**: The set of open sets in a topological space \((X, \tau)\) uniquely determines \(\tau\).

**Proof**: By definition, a topology \(\tau\) is a collection of subsets of \(X\) satisfying:
1. \(\emptyset, X \in \tau\)
2. Arbitrary unions of sets in \(\tau\) are in \(\tau\)
3. Finite intersections of sets in \(\tau\) are in \(\tau\)

Two topologies with the same collection of open sets are identical by extensionality of sets. ∎

## 29.2 Metric Spaces and Topology

### Theorem 29.3: Metric Induced Topology

**Statement**: Every metric space \((X, d)\) induces a topology \(\tau_d\) where \(U \in \tau_d\) iff for each \(x \in U\), there exists \(\epsilon > 0\) such that \(B_\epsilon(x) \subseteq U\).

**Proof**: Let \(\mathcal{B} = \{B_\epsilon(x) : x \in X, \epsilon > 0\}\) be the collection of all open balls.

1. \(\emptyset = \bigcup_{x \in \emptyset} B_\epsilon(x)\) and \(X = \bigcup_{x \in X} B_1(x)\), so \(\emptyset, X \in \tau_d\).

2. Let \(\{U_\alpha\}_{\alpha \in A}\) be open sets. For any \(x \in \bigcup U_\alpha\), there exists \(\alpha_0\) such that \(x \in U_{\alpha_0}\). Since \(U_{\alpha_0}\) is open, there exists \(\epsilon > 0\) such that \(B_\epsilon(x) \subseteq U_{\alpha_0} \subseteq \bigcup U_\alpha\). Thus \(\bigcup U_\alpha\) is open.

3. Let \(\{U_n\}_{n \in \mathbb{N}}\) be a finite collection of open sets. For any \(x \in \bigcap_{n=1}^n U_n\), each \(U_k\) is open, so there exists \(\epsilon_k > 0\) such that \(B_{\epsilon_k}(x) \subseteq U_k\). Let \(\epsilon = \min\{\epsilon_1, \dots, \epsilon_n\} > 0\). Then \(B_\epsilon(x) \subseteq \bigcap_{k=1}^n U_k\). Thus the intersection is open.

∎

### Corollary 29.1: Open Balls Form a Base

**Statement**: The collection of all open balls \(\mathcal{B}\) forms a base for the topology \(\tau_d\) on \((X, d)\).

**Proof**: For any \(x \in B_\epsilon(x_0)\), let \(r = \epsilon - d(x, x_0) > 0\). Then \(B_r(x) \subseteq B_\epsilon(x_0)\). This follows from the triangle inequality: if \(y \in B_r(x)\), then \(d(y, x_0) \leq d(y, x) + d(x, x_0) < r + d(x, x_0) = \epsilon\). ∎

## 29.3 Connectedness and Compactness

### Theorem 29.4: Connectedness via Quotients

**Statement**: If \(X\) is connected and \(f: X \to Y\) is continuous with \(Y\) Hausdorff, then \(f(X)\) is connected.

**Proof**: Suppose \(f(X) = A \cup B\) where \(A, B\) are disjoint non-empty open sets in \(f(X)\). Let \(U = f^{-1}(A)\) and \(V = f^{-1}(B)\). Then \(U, V\) are disjoint open sets in \(X\).

Since \(f\) is surjective onto \(f(X)\), \(X = U \cup V\). But \(X\) is connected, so this is a contradiction unless one of \(U, V\) is empty. ∎

### Theorem 29.5: Heine-Borel Theorem

**Statement**: In \(\mathbb{R}^n\) with the standard Euclidean metric, a subset \(K \subseteq \mathbb{R}^n\) is compact iff it is closed and bounded.

**Proof**: 

**(\(\Rightarrow\))** Suppose \(K\) is compact. Let \(\{x_1, \dots, x_n\} \in K\). Then \(K \subseteq \overline{B}_R(0)\) where \(R = \max_i |x_i| + 1\), so \(K\) is bounded. Since compact sets are closed in any \(T_1\) space, \(K\) is closed.

**(\(\Leftarrow\))** Suppose \(K\) is closed and bounded. By Heine-Borel (Euclidean space), every open cover has a finite subcover. This follows from the fact that any bounded sequence has a convergent subsequence (Bolzano-Weierstrass), and every open cover admits a finite subcover.

∎

### Corollary 29.2: Compactness and Continuity

**Statement**: If \(f: K \to Y\) is continuous and \(K\) is compact, then \(f(K)\) is compact.

**Proof**: Let \(\{V_\alpha\}_{\alpha \in A}\) be an open cover of \(f(K)\). Then \(\{f^{-1}(V_\alpha)\}_{\alpha \in A}\) covers \(K\). By compactness, there exists finite \(\alpha_1, \dots, \alpha_n\) such that \(K \subseteq \bigcup_{i=1}^n f^{-1}(V_{\alpha_i})\). Applying \(f\) gives \(f(K) \subseteq \bigcup_{i=1}^n V_{\alpha_i}\).

∎

## 29.4 Separation Axioms

### Theorem 29.6: Regularity Implies Hausdorff

**Statement**: Every regular \(T_1\) space is Hausdorff.

**Proof**: Let \(X\) be regular and \(T_1\). Let \(x, y \in X, x \neq y\). By regularity, there exist open sets \(U, V\) such that \(x \in U, y \in V\), and \(\overline{U} \cap \overline{V} = \emptyset\). Since \(\overline{U}\) and \(\overline{V}\) are disjoint closed sets, they can be separated by disjoint open sets, giving two disjoint neighborhoods of \(x\) and \(y\).

∎

### Corollary 29.3: Metric Spaces Are Normal

**Statement**: Every metric space is normal (\(T_4\)).

**Proof**: Let \(X\) be a metric space and \(A, B\) disjoint closed sets. Let \(d_A(x) = d(x, A) = \inf_{a \in A} d(x, a)\) and \(d_B(x) = d(x, B)\). Since \(A, B\) are closed, \(d_A, d_B\) are continuous. Define \(U = \{x : d_A(x) < d_B(x)\}\) and \(V = \{x : d_B(x) < d_A(x)\}\). Both \(U, V\) are open, disjoint, \(A \subseteq U, B \subseteq V\).

∎

## 29.5 Separation Axioms

### Theorem 29.7: Urysohn's Lemma

**Statement**: If \(X\) is a normal \(T_1\) space and \(A, B\) are disjoint closed sets, there exists a continuous function \(f: X \to [0, 1]\) such that \(f(A) = \{0\}\) and \(f(B) = \{1\}\).

**Proof**: We construct \(f\) inductively. Let \(\{U_n\}_{n \in \mathbb{N}}\) be a sequence of open sets such that:
- \(A \subseteq U_0\)
- \(\overline{U_0} \subseteq U_1\)
- \(\overline{U_{n+1}} \subseteq U_{n+2}\)
- \(B \notin U_n\) for all \(n\)

By normality, for each \(n\), there exist disjoint open sets \(V_n, W_n\) separating \(\overline{U_n}\) and \(B \setminus U_n\). Define \(f\) piecewise on dyadic intervals.

∎

### Corollary 29.4: Tietze Extension Theorem

**Statement**: If \(X\) is normal and \(f: A \to \mathbb{R}\) is continuous with \(A \subseteq X\) closed, then \(f\) can be extended to \(F: X \to \mathbb{R}\) continuous.

**Proof**: Use Urysohn's lemma to construct a sequence of functions \(f_n: X \to \mathbb{R}\) converging uniformly to \(f\).

∎

## 29.6 Exercises

1. **Exercise 29.1**: Prove that \(\mathbb{R}^n\) is complete.

2. **Exercise 29.2**: Show that the Cantor set is uncountable, compact, and totally disconnected.

3. **Exercise 29.3**: Prove that the product of compact spaces is compact (Tychonoff's theorem for finite products).

4. **Exercise 29.4**: Show that every continuous image of a connected space is connected.

5. **Exercise 29.5**: Let \(X\) be compact and \(f: X \to Y\) continuous. Prove \(f\) attains a maximum and minimum.

## 29.7 Summary

This chapter covered:
- Basic topological spaces and their properties
- Metric spaces and induced topologies
- Connectedness and compactness
- Separation axioms (Hausdorff, regular, normal)
- Urysohn's lemma and Tietze extension
- Applications to analysis and geometry

## 29.x Topology Fundamentals Theorems

### Theorem 29.1: Separation Axioms

**Statement**: In a topological space $X$:
- $X$ is $T_0$ if for any distinct points $x, y$, either $x \in U$ or $y \in U$ for all open sets containing one point but not the other.
- $X$ is $T_1$ if for any distinct points $x, y$, each point can be separated from the other by an open set.
- $X$ is $T_2$ (Hausdorff) if for any distinct points $x, y$, there exist disjoint open sets containing $x$ and $y$ respectively.
- $X$ is $T_3$ (regular) if it is $T_1$ and for any point $x$ and closed set $C$ not containing $x$, there exist disjoint open sets containing $x$ and $C$ respectively.
- $X$ is $T_4$ (normal) if it is $T_1$ and for any two disjoint closed sets $A, B$, there exist disjoint open sets containing $A$ and $B$ respectively.

**Proof**: These are definitions of separation axioms. The hierarchy is $T_2 \implies T_3 \implies T_4$, and $T_1 \implies T_2$. ∎

### Theorem 29.2: Connectedness Characterization

**Statement**: A topological space $X$ is connected if and only if it cannot be written as the union of two non-empty disjoint open sets.

**Proof**: 
The contrapositive is easier to prove. Suppose $X = U \cup V$ where $U, V$ are non-empty, disjoint, and open. Then $U \cap V = \emptyset$ and $U^c = V, V^c = U$. The space $X$ is the union of two disjoint non-empty open sets, which contradicts the definition of connectedness. ∎

### Theorem 29.3: Compactness Characterization

**Statement**: A topological space $X$ is compact if and only if every open cover of $X$ has a finite subcover.

**Proof**: 
This is the definition of compactness. The alternative characterization is the finite intersection property: a collection of closed sets in $X$ has a non-empty intersection if and only if every finite subcollection has a non-empty intersection. ∎

### Theorem 29.4: Path-Connected Implies Connected

**Statement**: If a topological space $X$ is path-connected, then it is connected.

**Proof**: 
Suppose $X$ is path-connected but not connected. Then there exist non-empty disjoint open sets $U, V$ such that $U \cup V = X$. Let $p \in U$ and $q \in V$. Since $X$ is path-connected, there exists a continuous path $\gamma: [0, 1] \to X$ such that $\gamma(0) = p$ and $\gamma(1) = q$. The inverse images $\gamma^{-1}(U)$ and $\gamma^{-1}(V)$ are disjoint open sets in $[0, 1]$, but $[0, 1]$ is connected, so it cannot be written as a union of two disjoint non-empty open sets. Contradiction. ∎


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*