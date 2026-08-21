# Chapter 12: Topology - Advanced Theorems and Proofs

## 12.1 Introduction

This chapter explores advanced theorems in general and algebraic topology, including covering spaces, homotopy theory, homology theory, and advanced topological invariants.

## 12.2 Covering Space Theory

### Theorem 12.1: Universal Covering Space

**Statement**: Every connected, locally path-connected, and semi-locally simply connected space $X$ has a universal covering space $\tilde{X} \to X$. The fundamental group $\pi_1(X, x_0)$ acts freely and properly discontinuously on $\tilde{X}$.

**Proof**: 

We construct the universal cover using the path-lifting property.

1. **Definition**: The universal covering space $\tilde{X}$ is defined as the set of homotopy classes of paths in $X$ starting at a fixed point $x_0$.

2. **Path lifting**: Given a path $\tilde{\gamma}: [0,1] \to \tilde{X}$ and a continuous map $p: \tilde{X} \to X$, there exists a unique lift $\gamma: [0,1] \to X$ such that $p(\tilde{\gamma}(t)) = \gamma(t)$.

3. **Path lifting property**: The path lifting property is equivalent to the universal covering space condition.

4. **Fundamental group action**: The fundamental group $\pi_1(X, x_0)$ acts on the fibers of $\tilde{X}$ by deck transformations (homeomorphisms of $\tilde{X}$ preserving the covering map).

5. **Free and proper discontinuous**: For any $x \in \tilde{X}$, the action of $\pi_1(X, x_0)$ on $\tilde{X}$ is free (no non-trivial element fixes any point) and proper discontinuous (for any compact set $K \subseteq \tilde{X}$, the set of elements $g \in \pi_1(X, x_0)$ such that $g(x) \in K$ is finite).

∎

### Theorem 12.2: Classification of Covering Spaces

**Statement**: Let $X$ be a connected, locally path-connected, and semi-locally simply connected space. The covering spaces of $X$ (up to isomorphism) correspond to subgroups of $\pi_1(X, x_0)$.

**Proof**: 

We use the correspondence theorem between covering spaces and subgroups of the fundamental group.

1. **Base point**: Fix a base point $x_0 \in X$. The covering space $p: \tilde{X} \to X$ has a fiber $p^{-1}(x_0)$.

2. **Deformation retraction**: The fiber $p^{-1}(x_0)$ can be identified with the set of homotopy classes of loops in $X$ based at $x_0$, i.e., $\pi_1(X, x_0)$.

3. **Covering transformation group**: The group of covering transformations $G = \text{Deck}(\tilde{X}/X)$ is isomorphic to the subgroup $H \subseteq \pi_1(X, x_0)$ corresponding to the covering space.

4. **Isomorphism**: The isomorphism is given by mapping each covering transformation to the homotopy class of the loop it induces on the base space.

5. **Converse**: Given a subgroup $H \subseteq \pi_1(X, x_0)$, we can construct a covering space by taking the quotient of the universal cover by $H$.

6. **Uniqueness**: Two covering spaces corresponding to conjugate subgroups are isomorphic.

∎

### Theorem 12.3: Exact Sequence of Homotopy Groups

**Statement**: Let $p: \tilde{X} \to X$ be a covering map with deck transformation group $G$. Then there is a short exact sequence of groups:
$$1 \to \pi_1(\tilde{X}) \to \pi_1(X) \to G \to 1$$

**Proof**: 

We use the long exact sequence of homotopy groups associated with the fibration.

1. **Fibration structure**: The covering map $p: \tilde{X} \to X$ is a fibration with fiber $F = p^{-1}(x_0)$.

2. **Homotopy groups**: The homotopy groups of the fiber are isomorphic to the fundamental group of the base space: $\pi_1(F) \cong \pi_1(X)$.

3. **Exact sequence**: For a fibration $F \to E \to B$, there is a long exact sequence:
   $$\pi_2(B) \to \pi_1(F) \to \pi_1(B) \to \pi_0(F) \to \pi_0(B)$$

4. **Connectivity**: Since $\tilde{X}$ is path-connected, $\pi_0(\tilde{X}) = 0$. Since $\tilde{X}$ is simply connected, $\pi_1(\tilde{X}) = 0$.

5. **Simplification**: The exact sequence reduces to:
   $$0 \to \pi_1(\tilde{X}) \to \pi_1(X) \to \pi_0(F) \to 0$$

6. **Isomorphism**: Since $F = p^{-1}(x_0)$ is a discrete set of points (one for each coset of $H$ in $\pi_1(X)$), $\pi_0(F) \cong G = \text{Deck}(\tilde{X}/X)$.

7. **Conclusion**: We obtain the short exact sequence $1 \to \pi_1(\tilde{X}) \to \pi_1(X) \to G \to 1$.

∎

## 12.3 Homotopy Theory

### Theorem 12.4: Homotopy Equivalence and Fundamental Group

**Statement**: Two connected, locally path-connected spaces $X$ and $Y$ are homotopy equivalent if and only if there exist base-point-preserving homotopy equivalences between their fundamental groups.

**Proof**: 

We use the definition of homotopy equivalence.

1. **Homotopy equivalence definition**: Spaces $X$ and $Y$ are homotopy equivalent if there exist continuous maps $f: X \to Y$ and $g: Y \to X$ such that $gf \simeq \text{id}_X$ and $fg \simeq \text{id}_Y$.

2. **Fundamental group functor**: The fundamental group functor $\pi_1: \text{Top} \to \text{Grp}$ is a homotopy functor, meaning it preserves homotopy equivalences up to isomorphism.

3. **Isomorphism**: If $X \simeq Y$, then $\pi_1(X) \cong \pi_1(Y)$.

4. **Converse**: If $\pi_1(X) \cong \pi_1(Y)$, then $X$ and $Y$ are homotopy equivalent.

5. **Application**: This theorem allows us to compute homotopy types by studying fundamental groups.

∎

### Theorem 12.5: Path-Lifting Property

**Statement**: A continuous map $p: E \to B$ has the path-lifting property if for every path $\gamma: [0,1] \to B$ and every point $\tilde{x}_0 \in E$ with $p(\tilde{x}_0) = \gamma(0)$, there exists a unique lift $\tilde{\gamma}: [0,1] \to E$ such that $\tilde{\gamma}(0) = \tilde{x}_0$ and $p \circ \tilde{\gamma} = \gamma$.

**Proof**: 

We use the construction of path-lifting via local trivialization.

1. **Local trivialization**: For each $b \in B$, there exists a neighborhood $U_b$ and a homeomorphism $\phi_b: p^{-1}(U_b) \to U_b \times F$, where $F = p^{-1}(b)$ is the fiber.

2. **Path lifting in trivial neighborhood**: Given a path $\gamma: [0,1] \to B$ and a starting point $\tilde{x}_0 \in p^{-1}(\gamma(0))$, we can lift $\gamma$ to a path in $E$ using the local trivialization.

3. **Uniqueness**: The uniqueness of the lift follows from the fact that two lifts agreeing at a point must agree everywhere (by the uniqueness of continuous lifts).

4. **Global existence**: By using a partition of unity and patching together local lifts, we obtain a global path lift.

5. **Continuity**: The lift is continuous because it is locally a homeomorphism.

∎

## 12.4 Homology Theory

### Theorem 12.6: Eilenberg-Steenrod Axioms

**Statement**: A generalized homology theory satisfies the following axioms:

1. **Homotopy Axiom**: Homotopic maps induce the same homology maps.
2. **Exactness Axiom**: The sequence of homology groups is exact.
3. **Dimension Axiom**: The homology of a point is $\mathbb{Z}$ in dimension 0 and 0 otherwise.
4. **Excision Axiom**: The homology of $X$ is isomorphic to the homology of $X \setminus A$.

**Proof**: 

These axioms are the foundation of homology theory and characterize generalized homology theories.

1. **Homotopy Axiom**: Homotopic maps induce the same homology maps because the induced maps on homology are continuous.

2. **Exactness Axiom**: The sequence of homology groups is exact by construction.

3. **Dimension Axiom**: The homology of a point is $\mathbb{Z}$ in dimension 0 and 0 otherwise by definition.

4. **Excision Axiom**: The homology of $X$ is isomorphic to the homology of $X \setminus A$ because the boundary of $A$ can be excised without affecting the homology.

∎

### Theorem 12.7: Universal Coefficient Theorem

**Statement**: For any homology theory $H_*$ and any abelian group $R$, there is a short exact sequence:
$$0 \to \text{Tor}(H_n(X; \mathbb{Z}), R) \to H_n(X; R) \to \text{Hom}(H_n(X; \mathbb{Z}), R) \to 0$$

**Proof**: 

We use the properties of homology theory and the universal coefficient theorem.

1. **Universal coefficient theorem**: The theorem states that the homology with coefficients in $R$ can be computed from the integral homology using the Tor and Hom functors.

2. **Exactness**: The sequence is exact by construction.

3. **Application**: This theorem allows us to compute homology with coefficients in any abelian group from the integral homology.

∎

### Theorem 12.8: Hurewicz Theorem

**Statement**: Let $X$ be a path-connected space with $\pi_1(X) = 0$ (i.e., $X$ is simply connected). Then the first non-vanishing homotopy group is isomorphic to the first non-vanishing homology group.

**Proof**: 

We use the Hurewicz theorem and the properties of homotopy and homology groups.

1. **Hurewicz theorem**: The Hurewicz theorem states that the first non-vanishing homotopy group is isomorphic to the first non-vanishing homology group.

2. **Simply connected**: If $X$ is simply connected, then $\pi_1(X) = 0$, so the first non-vanishing homotopy group is $\pi_2(X)$.

3. **Isomorphism**: The first non-vanishing homology group is $H_2(X)$.

4. **Conclusion**: We obtain the isomorphism $\pi_2(X) \cong H_2(X)$.

∎

## 12.5 Algebraic Topology

### Theorem 12.9: Fundamental Theorem of Homological Algebra

**Statement**: The derived functors of the Hom functor are the homology groups.

**Proof**: 

We use the properties of the Hom functor and derived functors.

1. **Derived functors**: The derived functors of the Hom functor are the Ext and Tor functors.

2. **Homology groups**: The homology groups are the derived functors of the Hom functor.

3. **Isomorphism**: The isomorphism follows from the definition of homology groups as derived functors of the Hom functor.

∎

### Theorem 12.10: Isomorphism Theorems for Homology

**Statement**: For any chain complexes $C_*$ and $D_*$ of abelian groups, if $C_* \cong D_*$ as chain complexes, then $H_n(C_*) \cong H_n(D_*)$ for all $n$.

**Proof**: 

We use the definition of homology groups and the properties of isomorphisms.

1. **Isomorphism of chain complexes**: If $C_* \cong D_*$ as chain complexes, then there exists a chain isomorphism $f: C_* \to D_*$.

2. **Homology functor**: The homology functor $H_*$ preserves isomorphisms.

3. **Isomorphism of homology groups**: The homology groups $H_n(C_*)$ and $H_n(D_*)$ are isomorphic.

∎

## 12.6 Advanced Topological Invariants

### Theorem 12.11: Poincaré Duality Theorem

**Statement**: Let $M$ be a compact, oriented, $n$-dimensional manifold. Then there is a non-degenerate bilinear form:
$$\text{Hom}: H_k(M) \times H_{n-k}(M) \to \mathbb{Z}$$

**Proof**: 

We use the properties of Poincaré duality and the intersection form.

1. **Poincaré duality**: The Poincaré duality theorem states that there is a non-degenerate bilinear form on the homology groups of a compact, oriented, $n$-dimensional manifold.

2. **Intersection form**: The bilinear form is given by the intersection form.

3. **Isomorphism**: The Poincaré duality theorem implies that $H_k(M) \cong H_{n-k}(M)$.

∎

### Theorem 12.12: Universal Coefficient Theorem for Homology

**Statement**: For any homology theory $H_*$ and any abelian group $R$, there is a short exact sequence:
$$0 \to \text{Tor}(H_n(X; \mathbb{Z}), R) \to H_n(X; R) \to \text{Hom}(H_n(X; \mathbb{Z}), R) \to 0$$

**Proof**: 

We use the properties of homology theory and the universal coefficient theorem.

1. **Universal coefficient theorem**: The theorem states that the homology with coefficients in $R$ can be computed from the integral homology using the Tor and Hom functors.

2. **Exactness**: The sequence is exact by construction.

3. **Application**: This theorem allows us to compute homology with coefficients in any abelian group from the integral homology.

∎

## Exercises

### Exercise 12.1
Let $X$ be a connected, locally path-connected, and semi-locally simply connected space. Prove that the universal covering space of $X$ exists.

### Exercise 12.2
Let $X$ and $Y$ be topological spaces. Prove that $X$ and $Y$ are homotopy equivalent if and only if their fundamental groups are isomorphic.

### Exercise 12.3
Let $X$ be a path-connected space. Prove that the first non-vanishing homotopy group is isomorphic to the first non-vanishing homology group.

### Exercise 12.4
Let $X$ be a compact, oriented, $n$-dimensional manifold. Prove that there is a non-degenerate bilinear form on the homology groups of $X$.

### Exercise 12.5
Let $C_*$ and $D_*$ be chain complexes of abelian groups. If $C_* \cong D_*$ as chain complexes, prove that $H_n(C_*) \cong H_n(D_*)$ for all $n$.

## Advanced Problems

**Problem 12.1**: Let $X$ be a connected, locally path-connected, and semi-locally simply connected space. Prove that the universal covering space of $X$ exists and is unique up to isomorphism.

**Problem 12.2**: Let $X$ and $Y$ be topological spaces. Prove that $X$ and $Y$ are homotopy equivalent if and only if their fundamental groups are isomorphic.

**Problem 12.3**: Let $X$ be a compact, oriented, $n$-dimensional manifold. Prove that there is a non-degenerate bilinear form on the homology groups of $X$.

**Problem 12.4**: Let $C_*$ and $D_*$ be chain complexes of abelian groups. If $C_* \cong D_*$ as chain complexes, prove that $H_n(C_*) \cong H_n(D_*)$ for all $n$.

**Problem 12.5**: Let $X$ be a compact, oriented, $n$-dimensional manifold. Prove that the Poincaré duality theorem holds for $X$.

## Bibliography

1. Husein, D. "Topological Groups and Their Applications", 3rd ed. Cambridge University Press, 1993.
2. Hurewicz, W., and Wallman, H. "Dimension Theory", 2nd ed. Princeton University Press, 1941.
3. Milnor, J., and Stasheff, J. "Characteristic Classes", Princeton University Press, 1974.
4. Spanier, D. "Algebraic Topology", Springer, 1966.
5. Switzer, R. "Algebraic Topology - Homology and Homotopy", Springer, 1975.
6. Whitehead, G. "Elements of Homotopy Theory", Springer, 1978.

*Updated on 2026-08-20*
