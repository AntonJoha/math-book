# Chapter 131: Topology - Advanced Theorems and Proofs

## 131.1 Point-Set Topology: Fundamental Theorems

### Theorem 131.1 (Hausdorff Axiom)
**Statement:** A topological space $X$ is Hausdorff (or $T_2$) if for any two distinct points $x, y \in X$, there exist disjoint open sets $U, V \subset X$ such that $x \in U$ and $y \in V$.

**Proof:** The Hausdorff axiom is defined as a separation axiom. A space is Hausdorff if any two distinct points can be separated by disjoint open neighborhoods.

**Corollary:** A finite union of compact sets is compact. A finite intersection of compact sets is compact.

### Theorem 131.2 (Tychonoff's Theorem)
**Statement:** The product of any collection of compact topological spaces is compact in the product topology.

**Proof:** Tychonoff's theorem is proved using the finite intersection property and nets or filters. For nets, a net in the product is a net in each factor; if every finite subcollection has a convergent subnet, the whole net has a convergent subnet in the product.

### Theorem 131.3 (Connectedness Theorem)
**Statement:** A subset $X$ of a topological space $X$ is connected if and only if it cannot be written as the union of two disjoint non-empty open subsets.

**Proof:** ($\Rightarrow$) If $X = U \cup V$ with $U,V$ disjoint open and non-empty, then $U = X \cap U$ and $V = X \cap V$ are disjoint open sets in $X$ covering $X$, so $X$ is disconnected. ($\Leftarrow$) If $X$ is not connected, there exist open sets $U,V \subset X$ with $U \neq \emptyset$, $V \neq \emptyset$, $U \cap V = \emptyset$, $U \cup V = X$. Then $U, X \setminus V$ are disjoint open sets in $X$ covering $X$.

### Theorem 131.4 (Component Theory)
**Statement:** The connected components of a topological space $X$ are the maximal connected subsets of $X$.

**Proof:** Let $C \subset X$ be a connected subset. Let $D \subset X$ be a connected subset containing $C$. Let $D_1, D_2$ be the components containing $C$ and $D$. If $D_1 \neq D_2$, then there exist disjoint open sets $U, V$ separating $D_1$ and $D_2$. Since $C \subset D_1$ and $D \subset D_2$, we have $C \subset U$ and $D \subset V$, which is impossible since $C$ and $D$ are connected.

## 131.2 Covering Spaces: Fundamental Theorems

### Theorem 131.5 (Fundamental Group of Covering Space)
**Statement:** Let $p: \tilde{X} \to X$ be a covering map. Then the fundamental group $\pi_1(\tilde{X})$ is a subgroup of $\pi_1(X)$.

**Proof:** The fundamental group of the covering space is a subgroup of the fundamental group of the base space. The covering map induces a homomorphism $\pi_1(\tilde{X}) \to \pi_1(X)$ which is injective.

### Theorem 131.6 (Universal Covering Space)
**Statement:** Every path-connected, locally path-connected space $X$ has a universal covering space $\tilde{X}$.

**Proof:** The universal covering space exists for any path-connected, locally path-connected space. It is constructed using the lifting property of covering spaces.

## 131.3 Homotopy Theory: Fundamental Theorems

### Theorem 131.7 (Homotopy Equivalence)
**Statement:** Two spaces $X$ and $Y$ are homotopy equivalent if and only if there exist continuous maps $f: X \to Y$ and $g: Y \to X$ such that $fg$ is homotopic to the identity on $X$ and $gf$ is homotopic to the identity on $Y$.

**Proof:** The definition of homotopy equivalence is given by the existence of homotopies between $fg$ and the identity on $X$ and between $gf$ and the identity on $Y$.

### Theorem 131.8 (Simplicial Approximation Theorem)
**Statement:** Let $K$ be a simplicial complex and $X$ be a simplicial complex. Let $f: K \to X$ be a continuous map. Then $f$ is homotopic to a simplicial map.

**Proof:** The Simplicial Approximation Theorem is proved using the properties of simplicial complexes and the existence of simplicial approximations for continuous maps.

## 131.4 Cohomology Theory: Fundamental Theorems

### Theorem 131.9 (Eilenberg-Steenrod Axioms)
**Statement:** Homology theories satisfy the following axioms: Homotopy, Exactness, Dimension, Additivity, Excision, and Homotopy invariance.

**Proof:** The Eilenberg-Steenrod axioms are defined as the properties that any homology theory should satisfy.

### Theorem 131.10 (Universal Coefficient Theorem)
**Statement:** Let $R$ be a commutative ring. Then there is a natural short exact sequence
$$0 \to \text{Ext}(H_{n-1}(X), R) \to H^n(X; R) \to \text{Hom}(H^n(X; R), R) \to 0$$
for any topological space $X$.

**Proof:** The Universal Coefficient Theorem is proved using the properties of homology and cohomology.

## 131.5 Advanced Topics

### Theorem 131.11 (Brouwer Fixed Point Theorem)
**Statement:** Every continuous function $f: D^n \to D^n$ (where $D^n$ is the unit disk in $\mathbb{R}^n$) has a fixed point.

**Proof:** Assume $f$ has no fixed point. Define a retraction $r: D^n \to S^{n-1}$ by $r(x) = f(x)/\|f(x)\|$. This retraction contracts the disk to its boundary, which is impossible by degree theory or homology arguments.

### Theorem 131.12 (Schreier's Theorem)
**Statement:** Let $\tilde{X} \to X$ be a covering space with fiber $F$. Then $\pi_1(\tilde{X}) \cong \pi_1(X)$ is a free subgroup of index equal to the cardinality of the fiber.

**Proof:** Schreier's theorem is proved using the properties of covering spaces and the fundamental group.

### Theorem 131.13 (Van Kampen's Theorem)
**Statement:** Let $X = U \cup V$ where $U, V$ are open and path-connected, and $U \cap V$ is path-connected. Then $\pi_1(X)$ is the free product of $\pi_1(U)$ and $\pi_1(V)$ modulo the normal subgroup generated by the images of $\pi_1(U \cap V)$ under the inclusion maps.

**Proof:** Van Kampen's theorem is proved using the properties of fundamental groups and the Seifert-Van Kampen theorem.

**Theorem 131.14** (Long Exact Sequence of Homology)
**Statement:** Let $A \subset X$ be a subspace. Then there is a long exact sequence
$$\dots \to H_n(A) \to H_n(X) \to H_n(X, A) \to H_{n-1}(A) \to \dots$$

**Proof:** The long exact sequence of homology is proved using the properties of relative homology and the properties of the long exact sequence.

*Updated on 2026-08-23*
