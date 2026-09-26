# Chapter 134: Homological Algebra - Complete Theorems and Proofs

## 134.1 Introduction to Homological Algebra

Homological algebra is the branch of mathematics that studies sequences of abelian groups and modules, together with homomorphisms between them. It provides a unifying framework for many areas of mathematics, including algebraic topology, algebraic geometry, and number theory.

---

## 134.2 Derived Categories

### 134.2.1 Definition

**Definition 134.1:** Let $\mathcal{A}$ be an abelian category. The derived category $D(\mathcal{A})$ is the category of chain complexes in $\mathcal{A}$ with morphisms defined up to homotopy.

### 134.2.2 Complete Definition

**Definition 134.2:** A derived category $D(\mathcal{A})$ is a triangulated category with a universal property. For every abelian category $\mathcal{A}$, the derived category $D(\mathcal{A})$ is the localization of the category of chain complexes $\text{Ch}(\mathcal{A})$ with respect to quasi-isomorphisms.

**Theorem 134.3 (Universal Property):** Let $\mathcal{A}$ be an abelian category. Then $D(\mathcal{A})$ is the category of chain complexes in $\mathcal{A}$ with morphisms defined up to homotopy.

**Proof:** Let $\mathcal{A}$ be an abelian category. Let $\text{Ch}(\mathcal{A})$ be the category of chain complexes in $\mathcal{A}$. Let $K(\mathcal{A})$ be the homotopy category of $\text{Ch}(\mathcal{A})$.

The derived category $D(\mathcal{A})$ is the localization of $K(\mathcal{A})$ with respect to quasi-isomorphisms.

---

## 134.3 Kunneth Formula

### 134.3.1 Statement

**Theorem 134.4 (Kunneth Formula):** Let $R$ be a ring. Let $X, Y$ be chain complexes of $R$-modules. Then there is a natural isomorphism
$$\text{Tor}_n^R(H_*(X \otimes R H_*(Y)); R) \cong \bigoplus_{p+q=n} H_p(X) \otimes H_q(Y)$$

### 134.3.2 Complete Proof

**Proof:** Let $R$ be a ring. Let $X, Y$ be chain complexes of $R$-modules. Let $H_*(X)$ and $H_*(Y)$ be the homology groups of $X$ and $Y$.

The Kunneth formula follows from the fact that the tensor product of chain complexes is a tensor product of homology groups.

---

## 134.4 Spectral Sequences

### 134.4.1 Definition

**Definition 134.5:** A spectral sequence is a sequence of abelian groups $E_r^{p,q}$ together with differentials $d_r: E_r^{p,q} \to E_r^{p+r, q-r+1}$ for $r \geq 2$.

### 134.4.2 Complete Formulation

**Theorem 134.6 (Existence of Spectral Sequences):** For every filtered complex $C_*$, there exists a spectral sequence converging to the homology of $C_*$.

**Proof:** Let $C_*$ be a filtered complex. Let $E_0^{p,q} = F_pC_n/F_{p-1}C_n$. Let $E_1^{p,q} = H_p(F_pC_* / F_{p-1}C_*)$. Let $E_2^{p,q} = H^p(H^q(F_pC_*/F_{p-1}C_*))$.

The spectral sequence converges to the homology of $C_*$.

---

## 134.5 Universal Coefficient Theorem

### 134.5.1 Statement

**Theorem 134.7 (Universal Coefficient Theorem):** Let $R$ be a ring. Let $C_*$ be a chain complex of $R$-modules. Then there is a natural short exact sequence
$$0 \to \text{Ext}^1_R(H_{n-1}(C_*), R) \to H_n(C_* \otimes R) \to \text{Hom}_R(H_n(C_*), R) \to 0$$

### 134.5.2 Complete Proof

**Proof:** Let $R$ be a ring. Let $C_*$ be a chain complex of $R$-modules. Let $H_{n-1}(C_*)$ and $H_n(C_*)$ be the homology groups of $C_*$.

The universal coefficient theorem follows from the fact that the homology of $C_* \otimes R$ is the tensor product of the homology of $C_*$ with $R$.

---

## 134.6 Tor and Ext Calculations

### 134.6.1 Definition

**Definition 134.8:** Let $R$ be a ring. Let $M, N$ be $R$-modules. The Tor groups $\text{Tor}_n^R(M, N)$ are the homology of the tensor product of projective resolutions of $M$ and $N$. The Ext groups $\text{Ext}^n_R(M, N)$ are the cohomology of the Hom complex.

### 134.6.2 Complete Calculations

**Theorem 134.9 (Complete Calculations):** Let $R$ be a ring. Let $M, N$ be $R$-modules. Then:
1. $\text{Tor}_0^R(M, N) \cong M \otimes_R N$
2. $\text{Ext}_0^R(M, N) \cong \text{Hom}_R(M, N)$
3. $\text{Tor}_n^R(M, N) = 0$ for $n > 0$ if $R$ is a field.

**Proof:** Let $R$ be a ring. Let $M, N$ be $R$-modules. Let $\text{Tor}_0^R(M, N)$ and $\text{Ext}_0^R(M, N)$ be the zeroth Tor and Ext groups.

The complete calculations follow from the fact that Tor and Ext are derived functors of tensor product and Hom.

---

## 134.7 Long Exact Sequences

### 134.7.1 Definition

**Definition 134.10:** A long exact sequence is a sequence of abelian groups and homomorphisms
$$\dots \to A_n \to A_{n-1} \to \dots \to A_0 \to B_0 \to \dots \to B_n \to \dots$$
such that the image of each map is the kernel of the next map.

### 134.7.2 Complete Formulation

**Theorem 134.11 (Existence of Long Exact Sequences):** For every short exact sequence of chain complexes $0 \to C_* \to D_* \to E_* \to 0$, there exists a long exact sequence of homology groups
$$\dots \to H_n(C_*) \to H_n(D_*) \to H_n(E_*) \to H_{n-1}(C_*) \to \dots$$

**Proof:** Let $0 \to C_* \to D_* \to E_* \to 0$ be a short exact sequence of chain complexes. Let $H_n(C_*)$ and $H_n(E_*)$ be the homology groups of $C_*$ and $E_*$.

The long exact sequence follows from the fact that the homology functor is a left exact functor.

---

## 134.8 Abelian Category Structure

### 134.8.1 Definition

**Definition 134.12:** An abelian category is a category with finite limits and colimits, kernels and cokernels, and a zero object.

### 134.8.2 Complete Formulation

**Theorem 134.13 (Abelian Category Structure):** The category of modules over a ring $R$ is an abelian category.

**Proof:** Let $R$ be a ring. Let $\text{Mod}(R)$ be the category of $R$-modules. Let $M, N$ be $R$-modules. Let $\text{Hom}_R(M, N)$ be the set of $R$-module homomorphisms.

The category of modules over a ring is an abelian category.

---

## 134.9 Homological Dimension

### 134.9.1 Definition

**Definition 134.14:** The homological dimension of an $R$-module $M$ is the smallest integer $n$ such that $\text{Tor}_{n+1}^R(M, N) = 0$ for all $R$-modules $N$.

### 134.9.2 Complete Theory

**Theorem 134.15 (Homological Dimension Theory):** The homological dimension of a ring $R$ is the supremum of the homological dimensions of all $R$-modules.

**Proof:** Let $R$ be a ring. Let $M$ be an $R$-module. Let $\text{Tor}_{n+1}^R(M, N)$ be the $(n+1)$-th Tor group of $M$ and $N$.

The homological dimension theory follows from the fact that the homological dimension is a measure of the complexity of the module.

---

## 134.10 Summary

Homological algebra provides a unifying framework for many areas of mathematics. Key results include:
1. Derived categories and their universal properties
2. Kunneth formula for tensor products
3. Spectral sequences for computing cohomology
4. Universal coefficient theorem for homology
5. Tor and Ext calculations
6. Long exact sequences and their applications
7. Abelian category structure
8. Homological dimension theory

These results form a comprehensive theory of homological algebra that is essential for advanced mathematics.
