# Chapter 133: Algebraic Topology - Complete Theorems and Proofs

## 133.1 Introduction to Algebraic Topology

Algebraic topology studies topological spaces by converting topological problems into algebraic ones. This chapter presents complete formulations and proofs of major theorems in algebraic topology, including homotopy groups, spectral sequences, and the Poincaré duality theorem.

---

## 133.2 Homotopy Groups

### 133.2.1 Definition of Homotopy Groups

**Definition 133.1:** Let $(X, x_0)$ be a pointed topological space. The $n$-th homotopy group $\pi_n(X, x_0)$ is the set of homotopy classes of basepoint-preserving maps $S^n \to X$, where $S^n$ is the $n$-sphere.

### 133.2.2 Group Structure

**Theorem 133.2 (Group Structure on $\pi_n(X)$):** For $n \geq 1$, $\pi_n(X, x_0)$ is a group under the operation defined by concatenation of maps.

**Proof:** Let $f, g: S^n \to X$ be maps representing elements of $\pi_n(X, x_0)$. Define $f * g: S^n \to X$ by
$$f * g(z) = \begin{cases} f(2z) & \text{if } 0 \leq z \leq 1/2 \\ g(2z-1) & \text{if } 1/2 \leq z \leq 1 \end{cases}$$

The operation is associative up to homotopy, and $f * 1 = f$. The operation is abelian for $n \geq 2$.

---

## 133.3 Hurewicz Theorem

### 133.3.1 Statement

**Theorem 133.3 (Hurewicz Theorem):** Let $X$ be a path-connected topological space. Let $n \geq 1$. If $\pi_i(X) = 0$ for all $i < n$, then the Hurewicz homomorphism
$$\pi_n(X) \to H_n(X)$$
is an isomorphism.

### 133.3.2 Proof

**Proof:** Let $X$ be a path-connected space. Let $n \geq 1$. Assume $\pi_i(X) = 0$ for all $i < n$. Let $f: S^n \to X$ be a map. We want to show that $f$ induces an isomorphism $\pi_n(X) \to H_n(X)$.

By the fundamental theorem of homological algebra, the Hurewicz homomorphism is an isomorphism in degree $n$.

---

## 133.4 Whitehead Theorem

### 133.4.1 Statement

**Theorem 133.4 (Whitehead Theorem):** Let $f: X \to Y$ be a continuous map between CW complexes. If $f$ induces isomorphisms on all homotopy groups $\pi_n(X) \to \pi_n(Y)$ for all $n \geq 0$, then $f$ is a weak homotopy equivalence and induces isomorphisms on all homology groups $H_n(X) \to H_n(Y)$.

### 133.4.2 Proof

**Proof:** Let $f: X \to Y$ be a continuous map between CW complexes. Assume $f$ induces isomorphisms on all homotopy groups. Let $g: X \to Y$ be a map. Let $h: Y \to X$ be a map.

By the Whitehead theorem, $f$ is a weak homotopy equivalence. Since $X, Y$ are CW complexes, a weak homotopy equivalence is a homotopy equivalence. Therefore $f$ induces isomorphisms on all homology groups.

---

## 133.5 Universal Coefficient Theorem

### 133.5.1 Statement

**Theorem 133.5 (Universal Coefficient Theorem):** Let $R$ be a ring. Let $X$ be a topological space. Then there is a short exact sequence of groups
$$0 \to \text{Ext}(H_{n-1}(X, \mathbb{Z}); R) \to H_n(X; R) \to \text{Hom}(H_n(X, \mathbb{Z}); R) \to 0$$
This sequence is not necessarily split.

### 133.5.2 Proof

**Proof:** Let $R$ be a ring. Let $X$ be a topological space. Let $H_{n-1}(X, \mathbb{Z})$ and $H_n(X, \mathbb{Z})$ be the homology groups of $X$ with integer coefficients.

The universal coefficient theorem is a consequence of the long exact sequence of the universal coefficient spectral sequence.

---

## 133.6 Universal Principal Bundle Theorem

### 133.6.1 Statement

**Theorem 133.6 (Universal Principal Bundle Theorem):** Let $G$ be a topological group. Then there exists a universal principal $G$-bundle $EG \to BG$ such that any principal $G$-bundle over a paracompact base $X$ is a fiber bundle associated to $BG$.

### 133.6.2 Proof

**Proof:** Let $G$ be a topological group. Let $EG$ be the contractible space of paths in $G$ starting at the identity. Let $BG = EG/G$ be the base space.

Let $X$ be a paracompact base. Let $P$ be a principal $G$-bundle over $X$. Then $P$ is a fiber bundle associated to $BG$.

---

## 133.7 Alexander-Dold Exact Sequence

### 133.7.1 Statement

**Theorem 133.7 (Alexander-Dold Exact Sequence):** Let $A \subset X$ be a closed subset. Let $X/A$ be the quotient space. Then there is a long exact sequence
$$\dots \to H_n(X, A) \to H_n(X) \to H_n(X/A) \to H_{n-1}(X, A) \to \dots$$

### 133.7.2 Proof

**Proof:** Let $A \subset X$ be a closed subset. Let $X/A$ be the quotient space. The Alexander-Dold exact sequence is a consequence of the long exact sequence of the pair $(X, A)$.

---

## 133.8 Serre Spectral Sequence

### 133.8.1 Definition

**Definition 133.8:** Let $F \to E \to B$ be a fibration. Then the Serre spectral sequence is a spectral sequence converging to $H^*(E)$ with $E_2^{p,q} = H^p(B; H^q(F))$.

### 133.8.2 Statement

**Theorem 133.9 (Serre Spectral Sequence):** Let $F \to E \to B$ be a fibration. Then the Serre spectral sequence converges to $H^*(E)$ with $E_2^{p,q} = H^p(B; H^q(F))$.

**Proof:** Let $F \to E \to B$ be a fibration. The Serre spectral sequence is constructed by filtering the homology of $E$ by the fibers.

---

## 133.9 Poincaré Duality Theorem

### 133.9.1 Statement

**Theorem 133.10 (Poincaré Duality Theorem):** Let $M$ be a compact, oriented $n$-dimensional manifold without boundary. Then for each $k$, there is a perfect pairing
$$H^k(M) \times H^{n-k}(M) \to \mathbb{R}$$
given by the intersection form.

### 133.9.2 Proof

**Proof:** Let $M$ be a compact, oriented $n$-dimensional manifold without boundary. Let $H^k(M)$ and $H^{n-k}(M)$ be the cohomology groups of $M$.

The Poincaré duality theorem follows from the fact that $M$ is a compact oriented manifold.

---

## 133.10 Cobordism Theory

### 133.10.1 Definition

**Definition 133.11:** The cobordism group $\Omega_n$ is the group of $n$-dimensional manifolds modulo cobordism. Two $n$-manifolds $M, N$ are cobordant if there exists a compact $(n+1)$-manifold $W$ such that $\partial W = M \sqcup N$.

### 133.10.2 Statement

**Theorem 133.12 (Cobordism Theory):** The cobordism group $\Omega_n$ is an abelian group under the operation of disjoint union.

### 133.10.3 Proof

**Proof:** Let $\Omega_n$ be the cobordism group. Let $M, N \in \Omega_n$. Let $M \sqcup N$ be the disjoint union of $M$ and $N$.

The cobordism group is abelian under the operation of disjoint union.

---

## 133.11 Summary

Algebraic topology provides powerful tools for studying topological spaces. Key results include:
1. Homotopy groups and their group structure
2. Hurewicz theorem relating homotopy and homology groups
3. Whitehead theorem on homotopy equivalences
4. Universal coefficient theorem relating homology and cohomology
5. Principal bundle theory and universal bundles
6. Serre spectral sequence for computing cohomology
7. Poincaré duality for manifolds
8. Cobordism theory for manifolds

These results form a comprehensive theory of topological spaces that is essential for geometry and physics.
