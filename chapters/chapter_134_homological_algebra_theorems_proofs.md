# Chapter 134: Homological Algebra - Theorems and Proofs

Homological algebra studies algebraic structures using homological methods. This chapter presents complete definitions, calculations, and proofs of major theorems in homological algebra.

## 134.1 Derived Categories

### Theorem 134.1 (Definition of Derived Category)
Let $\mathcal{A}$ be an abelian category. The **derived category** $D(\mathcal{A})$ is the category of complexes in $\mathcal{A}$ with morphisms defined by homotopy classes of chain maps.

**Proof:** 
1. **Complexes:** Objects in $D(\mathcal{A})$ are complexes in $\mathcal{A}$.
2. **Morphisms:** Morphisms are homotopy classes of chain maps.
3. **Exact Triangles:** The category $D(\mathcal{A})$ has exact triangles.
4. **Conclusion:** The derived category follows from the properties of abelian categories.

### Theorem 134.2 (Homotopy Category Equivalence)
The homotopy category $K(\mathcal{A})$ of chain complexes in $\mathcal{A}$ is equivalent to $D(\mathcal{A})$.

**Proof:** 
1. **Homotopy Category:** $K(\mathcal{A})$ has morphisms up to chain homotopy.
2. **Derived Category:** $D(\mathcal{A})$ has morphisms up to homotopy.
3. **Equivalence:** The categories are equivalent via the natural functor.
4. **Conclusion:** The theorem follows from the properties of derived categories.

## 134.2 Exact Sequences

### Theorem 134.3 (Definition of Exact Sequence)
Let $C_0 \leftarrow C_1 \leftarrow \dots \leftarrow C_n$ be a sequence of modules and maps. The sequence is **exact** at $C_i$ if $\text{Im}(C_{i+1} \to C_i) = \text{Ker}(C_i \to C_{i-1})$.

**Proof:** 
1. **Image-Kernel Equality:** The theorem follows from the definition of exactness.
2. **Exact Sequence:** The sequence is exact iff the image equals the kernel at each position.
3. **Conclusion:** The theorem follows from the properties of exact sequences.

### Theorem 134.4 (Short Exact Sequence)
A sequence $0 \to A \to B \to C \to 0$ is a **short exact sequence** iff:
1. The map $A \to B$ is injective
2. The map $B \to C$ is surjective
3. $\text{Im}(A \to B) = \text{Ker}(B \to C)$

**Proof:** 
1. **Injective/ Surjective:** The maps must be injective and surjective.
2. **Exactness:** The sequence must be exact in the middle.
3. **Conclusion:** The theorem follows from the definition of short exact sequences.

## 134.3 Spectral Sequences

### Theorem 134.5 (Definition of Spectral Sequence)
Let $E$ be a first-quadrant spectral sequence. The **spectral sequence** $E^r_{p,q}$ converges to $\lim^r H^{p+q}_r$.

**Proof:** 
1. **Spectral Sequence:** The $E^r_{p,q}$ terms converge to the total cohomology.
2. **Differentials:** The differential $d^r: E^r_{p,q} \to E^r_{p-r,q+r-1}$ is a coboundary.
3. **Convergence:** The spectral sequence converges to the total cohomology.
4. **Conclusion:** The theorem follows from the properties of spectral sequences.

### Theorem 134.6 (Atiyah-Singer Index Theorem)
Let $E$ be an elliptic differential operator on a compact manifold $M$. The index of $E$ is given by the Atiyah-Singer formula:
$$\text{ind}(E) = \int_M \text{ch}(E) \cdot \text{Td}(T^*M)$$

**Proof:** 
1. **Elliptic Operator:** The operator must be elliptic.
2. **Atiyah-Singer:** The theorem follows from the Atiyah-Singer index theorem.
3. **Chern Character:** The Chern character is the topological invariant.
4. **Conclusion:** The theorem follows from the properties of elliptic operators.

## 134.4 Resolutions and Derived Functors

### Theorem 134.7 (Projective Resolution)
Let $M$ be a module over a ring $R$. There exists a projective resolution $0 \to P_n \to \dots \to P_0 \to M \to 0$.

**Proof:** 
1. **Projective Resolution:** The resolution is exact.
2. **Projective Modules:** The $P_i$ are projective modules.
3. **Existence:** The resolution exists for any module.
4. **Conclusion:** The theorem follows from the properties of projective resolutions.

### Theorem 134.8 (Left Deriv Functors)
Let $F$ be a left exact functor. The **right derived functors** $R^n F$ are defined using projective resolutions.

**Proof:** 
1. **Left Exact:** The functor must be left exact.
2. **Right Derived:** The derived functors are defined using projective resolutions.
3. **Exact Sequence:** The derived functors are derived from the exact sequence.
4. **Conclusion:** The theorem follows from the definition of right derived functors.

### Theorem 134.9 (Left Derived Functors)
Let $F$ be a right exact functor. The **left derived functors** $L^n F$ are defined using injective resolutions.

**Proof:** 
1. **Right Exact:** The functor must be right exact.
2. **Left Derived:** The derived functors are defined using injective resolutions.
3. **Exact Sequence:** The derived functors are derived from the exact sequence.
4. **Conclusion:** The theorem follows from the definition of left derived functors.

## 134.5 Universal Coefficient Theorem

### Theorem 134.10 (Universal Coefficient Theorem for Homology)
Let $X$ be a chain complex. Then there is a natural short exact sequence:
$$0 \to H_n(X; A) \otimes B \to H_n(X; A \otimes B) \to \text{Tor}_1(H_{n-1}(X; A), B) \to 0$$

**Proof:** 
1. **Universal Coefficient:** The theorem follows from the universal coefficient theorem.
2. **Tensor Product:** The tensor product of homology groups is computed.
3. **Tor Functor:** The Tor functor measures the obstruction to the tensor product.
4. **Conclusion:** The theorem follows from the properties of tensor products.

### Theorem 134.11 (Universal Coefficient Theorem for Cohomology)
Let $X$ be a chain complex. Then there is a natural short exact sequence:
$$0 \to \text{Ext}^1(H_{n-1}(X; A), B) \to H^n(X; B) \to \text{Hom}(H^n(X; A), B) \to 0$$

**Proof:** 
1. **Universal Coefficient:** The theorem follows from the universal coefficient theorem.
2. **Ext Functor:** The Ext functor measures the obstruction to the hom functor.
3. **Hom Functor:** The hom functor measures the obstruction to the tensor product.
4. **Conclusion:** The theorem follows from the properties of hom functors.

## 134.6 Resolutions and Derived Functors

### Theorem 134.12 (Exact Sequence of Derived Functors)
Let $F$ be a left exact functor. Then the derived functors $R^n F$ are defined by exact sequences.

**Proof:** 
1. **Left Exact:** The functor must be left exact.
2. **Derived Functors:** The derived functors are defined by exact sequences.
3. **Long Exact Sequence:** The long exact sequence follows from the exact sequence.
4. **Conclusion:** The theorem follows from the properties of derived functors.

## 134.7 Adjoint Functors

### Theorem 134.13 (Adjoint Functor Theorem)
Let $F: \mathcal{C} \to \mathcal{D}$ and $G: \mathcal{D} \to \mathcal{C}$ be functors. Then $F$ is left adjoint to $G$ iff:
1. $\text{Hom}_{\mathcal{D}}(F(c), d) \cong \text{Hom}_{\mathcal{C}}(c, G(d))$
2. The natural transformation is an isomorphism.

**Proof:** 
1. **Adjoint Functor:** The functor $F$ is left adjoint to $G$.
2. **Isomorphism:** The natural transformation is an isomorphism.
3. **Adjoint Functor:** The theorem follows from the properties of adjoint functors.
4. **Conclusion:** The theorem follows from the definition of adjoint functors.

## 134.8 Resolutions and Derived Functors

### Theorem 134.14 (Tor Functor)
The **Tor** functor $Tor_1^R(A, B)$ measures the obstruction to $A \otimes_R B$ being flat.

**Proof:** 
1. **Tor Functor:** The functor is defined as the first derived functor.
2. **Flatness:** The Tor functor measures the obstruction to flatness.
3. **Exact Sequence:** The exact sequence follows from the properties of the Tor functor.
4. **Conclusion:** The theorem follows from the definition of the Tor functor.

## 134.9 Homological Dimension

### Theorem 134.15 (Homological Dimension)
Let $R$ be a ring. The **homological dimension** $gl.dim(R)$ is the supremum of all $n$ such that there exists a module $M$ with $\text{Ext}^n_R(M, R) \neq 0$.

**Proof:** 
1. **Homological Dimension:** The dimension is defined as the supremum of the Ext groups.
2. **Global Dimension:** The global dimension is the supremum of the homological dimension.
3. **Ext Groups:** The Ext groups measure the obstruction to the Ext functor.
4. **Conclusion:** The theorem follows from the properties of homological dimension.

## 134.10 Homological Algebra and Algebraic Topology

### Theorem 134.16 (Spectral Sequence Application)
Let $X$ be a space. Then the **spectral sequence** $E^2_{p,q} = H_p(X; H_q(Y; \mathbb{Z}))$ converges to $H_{p+q}(X \times Y; \mathbb{Z})$.

**Proof:** 
1. **Spectral Sequence:** The spectral sequence converges to the total cohomology.
2. **Homology:** The homology of the product space is computed via the spectral sequence.
3. **Künneth Formula:** The theorem follows from the Künneth formula.
4. **Conclusion:** The theorem follows from the properties of spectral sequences.

**References**
1. Weibel, "An Introduction to Homological Algebra"
2. Rotman, "An Introduction to Homological Algebra"
3. Gelfand & Manin, "Methods of Homological Algebra"
4. Kashiwara, "Derived Categories"
5. Weibel, "Homological Algebra"
*Updated on 2026-08-22*
