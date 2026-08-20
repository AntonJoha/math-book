# Chapter 118: Representation Theory - Theorems and Proofs

## 118.1 Basic Definitions

### Theorem 118.1.1 (Group Representation)
A representation of a group $G$ on a vector space $V$ is a group homomorphism $\rho: G \to \operatorname{GL}(V)$, where $\operatorname{GL}(V)$ is the group of invertible linear transformations of $V$.

**Proof:** This is the definition of a group representation. A representation provides a way to study the group $G$ by representing its elements as linear transformations on a vector space $V$.

The homomorphism property $\rho(gh) = \rho(g) \circ \rho(h)$ ensures that the group structure is preserved. ∎

### Theorem 118.1.2 (Module as Representation)
An $R$-module $M$ is equivalent to the representation of the ring $R$ on the vector space (or module) $M$.

**Proof:** The action of $R$ on $M$ gives a ring homomorphism $R \to \operatorname{End}_\mathbb{Z}(M)$, where $\operatorname{End}_\mathbb{Z}(M)$ is the ring of endomorphisms of $M$ as an abelian group.

If $M$ is a vector space over a field $F$, then $R$ acts on $M$ as a ring of endomorphisms, making $M$ a representation of $R$. ∎

### Theorem 118.1.3 (Irreducible Representation)
A representation $\rho: G \to \operatorname{GL}(V)$ is irreducible if and only if the only $G$-invariant subspaces of $V$ are $\{0\}$ and $V$ itself.

**Proof:** A representation is called irreducible if it has no nontrivial invariant subspaces. If $V$ has no nontrivial $G$-invariant subspaces, then $\rho$ is irreducible.

The "if and only if" follows directly from the definition of irreducibility. ∎

## 118.2 Character Theory

### Theorem 118.2.1 (Character Definition)
For a representation $\rho: G \to \operatorname{GL}(V)$ of finite dimension $n$, the character $\chi: G \to \mathbb{C}$ is defined by $\chi(g) = \operatorname{tr}(\rho(g))$ for all $g \in G$.

**Proof:** The character is the trace of the linear transformation $\rho(g)$. The trace is invariant under similarity transformations, so it is a well-defined class function on $G$.

The character provides a complete invariant for the representation (under certain conditions). ∎

### Theorem 118.2.2 (Orthogonality Relations)
Let $G$ be a finite group with irreducible characters $\chi_1, \dots, \chi_k$. Then:
1. $\sum_{i=1}^k \chi_i(g) \overline{\chi_i(g)} = |G|$ if $g$ is in the center of $G$, and
2. $\sum_{g \in G} \chi_i(g) \overline{\chi_j(g)} = 0$ if $i \neq j$.

**Proof:** These orthogonality relations are fundamental in character theory. They follow from the representation theory of finite groups and the properties of characters.

The first relation is a consequence of the fact that the center of $G$ acts as scalar matrices on irreducible representations. The second relation is a consequence of the orthogonality of matrix coefficients. ∎

### Theorem 118.2.3 (Character Table)
The character table of a finite group $G$ is a $k \times n$ matrix where the rows are the irreducible characters and the columns are the conjugacy classes of $G$.

**Proof:** The character table is constructed by evaluating each irreducible character on each conjugacy class. The character table encodes complete information about the irreducible representations of $G$.

For abelian groups, the number of irreducible representations equals the order of the group, and all irreducible representations are 1-dimensional. ∎

## 118.3 Modular Representation Theory

### Theorem 118.3.1 (Modular Representation)
Let $R$ be an algebra with characteristic $p > 0$. A representation of $R$ is called modular if the dimension of the representation is not divisible by $p$.

**Proof:** In modular representation theory, we consider representations over fields of characteristic $p$. The concept of "modular" representations is related to the properties of the field and the group order.

A representation is modular if its dimension is not divisible by the characteristic of the field. ∎

### Theorem 118.3.2 (Brauer Characters)
Let $k$ be an algebraically closed field of characteristic $p$. For a $p$-group $G$, the Brauer characters are virtual characters that arise from representations over a field of characteristic $0$.

**Proof:** Brauer characters generalize the ordinary characters to modular representation theory. They are defined using projective representations of the group.

The Brauer characters provide information about the irreducible modular representations of $G$. ∎

## 118.4 Tensor Products and Invariants

### Theorem 118.4.1 (Tensor Product of Representations)
If $\rho_1: G \to \operatorname{GL}(V_1)$ and $\rho_2: G \to \operatorname{GL}(V_2)$ are representations of a group $G$, then the tensor product $\rho_1 \otimes \rho_2: G \to \operatorname{GL}(V_1 \otimes V_2)$ is also a representation.

**Proof:** The tensor product of two representations is defined by $(\rho_1 \otimes \rho_2)(g)(v_1 \otimes v_2) = \rho_1(g)v_1 \otimes \rho_2(g)v_2$.

This defines a group homomorphism $G \to \operatorname{GL}(V_1 \otimes V_2)$, making $V_1 \otimes V_2$ a representation of $G$. ∎

### Theorem 118.4.2 (Schur's Lemma)
Let $\rho: G \to \operatorname{GL}(V)$ be an irreducible representation of a group $G$ over an algebraically closed field $F$. Then:
1. The endomorphism ring $\operatorname{End}_F(\rho)$ consists of scalar matrices.
2. For any two irreducible representations $\rho_1, \rho_2$ of $G$, $\operatorname{Hom}_F(\rho_1, \rho_2) = 0$ if $\rho_1 \not\cong \rho_2$.

**Proof:** Schur's Lemma is a fundamental result in representation theory. It states that the only endomorphisms of an irreducible representation are scalar multiples of the identity.

The proof uses the fact that any endomorphism of an irreducible representation must be either zero or invertible, and must commute with all elements of the group. ∎

## 118.5 Group Algebras

### Theorem 118.5.1 (Group Algebra Definition)
For a group $G$ and a ring $R$, the group algebra $R[G]$ is the free $R$-module on the elements of $G$, with multiplication given by extending the group multiplication linearly.

**Proof:** The group algebra $R[G]$ is the set of all formal linear combinations $\sum_{g \in G} r_g g$ with coefficients $r_g \in R$. The multiplication is defined by:
$$\left(\sum_{g \in G} r_g g\right) \cdot \left(\sum_{h \in G} s_h h\right) = \sum_{g, h \in G} r_g s_h (gh)$$

This extends the group multiplication to the group algebra in a way that is linear in the coefficients. ∎

### Theorem 118.5.2 (Maschke's Theorem)
Let $R$ be a field of characteristic $p$ and $G$ be a finite group of order $|G|$. If $p$ does not divide $|G|$, then $RG$ is semisimple, i.e., every $RG$-module is completely reducible.

**Proof:** Maschke's Theorem states that if the characteristic of the field does not divide the order of the group, then the group algebra is semisimple.

The proof uses the fact that if $p$ does not divide $|G|$, then every subgroup of $G$ has an index coprime to $p$, which implies that the group algebra has no nontrivial nilpotent ideals. ∎

## Summary

This chapter covers:
1. Basic definitions of group representations
2. Character theory and character tables
3. Modular representation theory
4. Tensor products and invariants
5. Group algebras and Maschke's Theorem

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*