# Chapter 31: Topology - Key Theorems and Proofs

## 31.1 Open Sets and Topological Spaces

**Definition**: A collection $\tau$ of subsets of a set $X$ is a topology if:
1. $\emptyset, X \in \tau$.
2. Arbitrary unions of sets in $\tau$ are in $\tau$.
3. Finite intersections of sets in $\tau$ are in $\tau$.

A pair $(X, \tau)$ is a **topological space**.

**Theorem**: Every open set in a topological space is closed in its complement.

**Proof**: By definition, the complement of an open set is closed, and the complement of a closed set is open. ∎

## 31.2 Hausdorff (T2) Spaces

**Theorem**: A topological space $X$ is Hausdorff iff for any distinct $x,y \in X$, there exist disjoint open sets $U,V$ with $x \in U, y \in V$.

**Proof**:

*Forward direction*: Assume $X$ is Hausdorff. Let $x \neq y$. By definition, there exist disjoint open neighborhoods $U_x, U_y$.

*Reverse direction*: Assume every pair has disjoint neighborhoods. Let $U_x, U_y$ be neighborhoods. If $U_x \cap U_y \neq \emptyset$, pick $z \in U_x \cap U_y$. Then $z$ has open neighborhoods $U_z \cap U_x$ and $U_z \cap U_y$. But these are disjoint from $z$, contradiction. ∎

## 31.3 Connectedness

**Theorem**: A space $X$ is connected iff it contains no nonempty proper clopen subset.

**Proof**:

*Forward*: Suppose $U \subset X$ is nonempty, proper, clopen. Then $U^c$ is also open, so $X = U \cup U^c$ is a disconnection.

*Reverse*: Suppose $X = U \cup V$ with $U, V$ disjoint open sets. Then $U^c = V$ is closed. If $U$ is also open (clopen), we have a disconnection. ∎

## 31.4 Compactness

**Theorem**: A subset $K \subset X$ is compact iff every open cover has a finite subcover.

**Proof**: This is the definition of compactness in terms of open covers. ∎

**Theorem**: Heine-Borel Theorem. In $\mathbb{R}^n$ with the standard topology, a subset is compact iff it is closed and bounded.

**Proof**:

*Forward*: If $K$ is compact, it is closed (continuous image of compact is compact, and singletons are closed). By the open cover definition, boundedness follows.

*Reverse*: If $K$ is closed and bounded, it's a subset of a closed box. Any open cover restricts to a cover of the box. By construction, the box has a finite subcover. ∎

## 31.5 Separation Axioms

**Theorem (Urysohn's Lemma)**: Let $X$ be a normal topological space (T4: T1 and normal). If $A, B$ are disjoint closed sets, there exists a continuous function $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof Sketch**:

1. Build a sequence of open sets $U_n, V_n$ by iterating the normal property.
2. Define $f(x)$ as the supremum of all $m$ such that $x \in U_m$.
3. Continuity follows from the nested interval principle. ∎

## 31.6 The Stone-Čech Compactification

**Theorem**: Every completely regular Hausdorff space $X$ embeds into its Stone-Čech compactification $\beta X$, which is the largest compactification of $X$.

**Proof**:

1. Define $\beta X$ as the space of ultrafilters on $X$ containing all zero-sets.
2. The map $x \mapsto$ the principal ultrafilter at $x$ is an embedding.
3. $\beta X$ is compact and completely regular.
4. Any continuous map $f: X \to Y$ where $Y$ is compact extends uniquely to $\beta X$. ∎

## 31.7 Connected Components and Path Components

**Theorem**: In any topological space, the connected components are closed.

**Proof**: Let $C(x)$ be the connected component of $x$. Suppose $C(x)$ is not closed. Then there exists $y \notin C(x)$ in the closure of $C(x)$. But then any neighborhood of $y$ intersects $C(x)$, and since $C(x)$ is connected, $y \in C(x)$, contradiction. ∎

## 31.8 The Tychonoff Theorem

**Theorem**: The product of compact spaces is compact in the product topology.

**Proof**:

Use the finite intersection property: A family of closed sets in a product space has finite intersection property iff it has nonempty intersection.

For product of compact spaces $X_i$, any collection of closed sets with FIP has nonempty intersection by the compactness of each $X_i$. ∎

## 31.9 Baire Category Theorem

**Theorem**: A complete metric space cannot be written as a countable union of nowhere dense sets.

**Proof (Classic)**:

Assume $X = \bigcup_{n=1}^\infty F_n$ where each $F_n$ has empty interior.

1. Cover $X$ with balls $B_1, \dots, B_{2^k}$.
2. By pigeonhole, one ball $B_{k+1}$ has positive measure of $B_1$.
3. Continue inductively: $B_{k+1} = B \cap F_n$.
4. Since each $F_n$ has empty interior, diameters must shrink, but the intersection must be nonempty (completeness).
5. Contradiction, since $X$ cannot be covered by now dense sets. ∎

## 31.10 The Urysohn Metrization Theorem

**Theorem**: A topological space is metrizable iff it is regular and has a countable base.

**Proof Sketch**:

1. **Regularity + Countable Base implies Metrizable**: Use Urysohn's Lemma to construct a metric.
2. **Metrizable implies Regular + Countable Base**: Separation properties and a countable dense subset (if separable) can be constructed.

**Example**: $\mathbb{R}^n$ with Euclidean metric is metrizable. ∎

## 31.11 The Kuratowski-Morita Theorem

**Theorem**: A subset $K$ of a Hausdorff space is compact iff:
1. $K$ is closed.
2. Every collection of subsets with finite intersection property has nonempty intersection.

**Proof**: Use the finite intersection characterization of compactness. ∎

## 31.12 The Bolzano-Weierstrass Theorem

**Theorem**: Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence.

**Proof (Sequential Compactness)**:

1. Use the nested interval principle.
2. For each coordinate, apply Bolzano-Weierstrass in $\mathbb{R}$.
3. Construct a subsequence converging componentwise.
4. The limit exists and the sequence converges in $\mathbb{R}^n$. ∎

## 31.13 The Arzelà-Ascoli Theorem

**Theorem**: Let $X, Y$ be metric spaces, $C(X,Y)$ the space of continuous functions from $X$ to $Y$ with the uniform topology. A subset $\mathcal{F} \subset C(X,Y)$ is relatively compact iff:
1. $\mathcal{F}$ is pointwise bounded (for each $x \in X$, $\{f(x) : f \in \mathcal{F}\}$ is bounded).
2. $\mathcal{F}$ is equicontinuous.

**Proof**: Apply Banach-Alaoglu or use the Arzelà-Ascoli theorem directly. ∎

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*