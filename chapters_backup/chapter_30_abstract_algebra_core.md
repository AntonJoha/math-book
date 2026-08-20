# Chapter 30: Abstract Algebra - Core Theory and Proofs

## 30.1 Groups and Basic Properties

### Theorem 30.1: Group Properties

**Statement**: A group \((G, \cdot)\) satisfies:
1. Associativity: \((a \cdot b) \cdot c = a \cdot (b \cdot c)\)
2. Identity: There exists \(e \in G\) such that \(e \cdot a = a \cdot e = a\) for all \(a \in G\)
3. Inverse: For each \(a \in G\), there exists \(a^{-1} \in G\) such that \(a \cdot a^{-1} = a^{-1} \cdot a = e\)

**Proof**: These are the axioms of a group by definition. ∎

### Theorem 30.2: Uniqueness of Identity and Inverse

**Statement**: The identity element and inverse of each element in a group are unique.

**Proof**: 

**Identity**: Suppose \(e_1, e_2 \in G\) are both identities. Then:
\(e_1 = e_1 \cdot e_2\) (since \(e_2\) is identity)
\(= e_2 \cdot e_1\) (since \(e_1\) is identity)
\(= e_1\) (since \(e_2\) is identity)
Thus \(e_1 = e_2\).

**Inverse**: Suppose \(a^{-1}\) is the inverse of \(a\), and \(b\) is another element such that \(ab = ba = e\). Then:
\(b = be = b(a^{-1}a) = (ba^{-1})a = ea^{-1}a = a^{-1}a = a^{-1}\)
Thus \(b = a^{-1}\).

∎

### Corollary 30.1: Cancellation Laws

**Statement**: In any group, \(ab = ac\) implies \(b = c\), and \(ba = ca\) implies \(b = c\).

**Proof**: From \(ab = ac\), multiply by \(a^{-1}\) on the left:
\(a^{-1}(ab) = a^{-1}(ac)\)
\((a^{-1}a)b = (a^{-1}a)c\)
\(eb = ec\)
\(b = c\)

Similarly for \(ba = ca\), multiply by \(a^{-1}\) on the right. ∎

## 30.2 Subgroups and Cosets

### Theorem 30.3: Subgroup Criterion

**Statement**: A non-empty subset \(H \subseteq G\) is a subgroup iff:
1. \(H\) is closed under multiplication: \(\forall a, b \in H, ab \in H\)
2. \(H\) is closed under inverses: \(\forall a \in H, a^{-1} \in H\)

**Proof**: 

**(\(\Rightarrow\))** If \(H\) is a subgroup, these properties follow directly from group axioms.

**(\(\Leftarrow\))** Let \(a \in H\). Since \(H\) is closed under inverses, \(a^{-1} \in H\). Then \(aa^{-1} = e \in H\). For \(a, b \in H\), \(ab \in H\) by closure. Associativity is inherited from \(G\).

∎

### Theorem 30.4: Subgroup Test

**Statement**: A non-empty subset \(H \subseteq G\) is a subgroup iff \(ab \in H\) and \(a^{-1} \in H\) for all \(a, b \in H\).

**Proof**: If \(a \in H\), then \(a^{-1} \in H\) (given), and \(a^{-1}a = e \in H\). Then for any \(a, b \in H\), \(ab \in H\). This is the subgroup criterion.

∎

### Theorem 30.5: Cosets and Lagrange's Theorem

**Statement**: Let \(H\) be a subgroup of \(G\). For any \(g \in G\), the left coset \(gH = \{gh : h \in H\}\) and right coset \(Hg = \{hg : h \in H\}\) are disjoint from other cosets.

Furthermore, if \(|G| = n < \infty\) and \(|H| = m\), then \(m\) divides \(n\).

**Proof**: 

**Cosets are disjoint**: Suppose \(x \in aH \cap bH\) for \(a, b \in G\). Then \(x = ah_1 = bh_2\) for \(h_1, h_2 \in H\). So \(b^{-1}a = h_2h_1^{-1} \in H\). Thus \(a \in bH\), so all cosets containing \(a\) are the same.

**Lagrange's Theorem**: Since cosets partition \(G\) into equal-sized sets (translation by \(g\)), \(|G| = [G:H] \cdot |H|\). Thus \(|H|\) divides \(|G|\).

∎

### Corollary 30.2: Order of Element Divides Order of Group

**Statement**: If \(G\) is finite and \(a \in G\), then the order of \(a\) divides \(|G|\).

**Proof**: The cyclic subgroup \(\langle a \rangle\) has order equal to the order of \(a\). By Lagrange's theorem, \(|\langle a \rangle| \cdot [G:\langle a \rangle] = |G|\).

∎

## 30.3 Homomorphisms and Isomorphisms

### Theorem 30.6: Homomorphism Properties

**Statement**: A group homomorphism \(\phi: G \to H\) satisfies:
1. \(\phi(e_G) = e_H\)
2. \(\phi(a^{-1}) = (\phi(a))^{-1}\)
3. \(\phi\) is injective iff \(\ker(\phi) = \{e_G\}\)

**Proof**:

1. \(\phi(e_G) = \phi(e_G \cdot e_G) = \phi(e_G)\phi(e_G)\), so \(\phi(e_G)\phi(e_G)^{-1} = e_H\), giving \(\phi(e_G) = e_H\).

2. \(\phi(a)a^{-1} = e_G \implies \phi(a^{-1}) = \phi(a^{-1})\phi(a) = \phi(a)^{-1}e_H = \phi(a)^{-1}\).

3. If \(\ker(\phi) = \{e_G\}\) and \(\phi(a) = \phi(b)\), then \(\phi(a^{-1}b) = e_H\), so \(a^{-1}b \in \ker(\phi) = \{e_G\}\), giving \(a^{-1}b = e_G\), so \(a = b\).

∎

### Theorem 30.7: First Isomorphism Theorem

**Statement**: For any group homomorphism \(\phi: G \to H\):
\[ G/\ker(\phi) \cong \text{Im}(\phi) \]

**Proof**: Define \(\psi: G/\ker(\phi) \to \text{Im}(\phi)\) by \(\psi(g\ker(\phi)) = \phi(g)\).

- **Well-defined**: If \(g\ker(\phi) = g'\ker(\phi)\), then \(g^{-1}g' \in \ker(\phi)\), so \(\phi(g^{-1}g') = e_H\), giving \(\phi(g') = \phi(g)\).

- **Homomorphism**: \(\psi((g\ker(\phi))(h\ker(\phi))) = \psi(gh\ker(\phi)) = \phi(gh) = \phi(g)\phi(h) = \psi(g\ker(\phi))\psi(h\ker(\phi))\).

- **Injective**: If \(\psi(g\ker(\phi)) = e_H\), then \(\phi(g) = e_H\), so \(g \in \ker(\phi)\), \(g\ker(\phi) = e\ker(\phi)\).

- **Surjective**: Every element in \(\text{Im}(\phi)\) is \(\phi(g)\) for some \(g\), so it's in the image.

∎

## 30.4 Rings and Fields

### Theorem 30.8: Ring Axioms

**Statement**: A ring \((R, +, \cdot)\) satisfies:
1. \((R, +)\) is an abelian group
2. \((R, \cdot)\) is a monoid (not necessarily commutative)
3. Multiplication distributes over addition: \(a(b+c) = ab + ac\) and \((a+b)c = ac + bc\)

**Proof**: These are the axioms of a ring by definition. ∎

### Theorem 30.9: Field Axioms

**Statement**: A field \((F, +, \cdot)\) is a ring where every non-zero element has a multiplicative inverse.

**Proof**: This is the definition of a field. ∎

### Theorem 30.10: Ring Theorem

**Statement**: In a ring with unity, \(0 \cdot a = 0\) for all \(a \in R\).

**Proof**: 
\(0 = 0 \cdot a\)
\(0 = (0 + 0) \cdot a = 0 \cdot a + 0 \cdot a\)
Add \(-(0 \cdot a)\) to both sides:
\(0 = 0 \cdot a\)

∎

### Corollary 30.3: Characteristic of a Ring

**Statement**: The characteristic of a ring is the smallest positive integer \(n\) such that \(n \cdot 1 = 0\), or 0 if no such \(n\) exists.

**Proof**: The additive order of the multiplicative identity \(1\) is the characteristic. ∎

## 30.5 Exercises

1. **Exercise 30.1**: Prove that in a group, \(a = b\) iff \(ab = ba\) for all \(a, b \in G\).

2. **Exercise 30.2**: Show that the intersection of two subgroups is a subgroup.

3. **Exercise 30.3**: Prove that if \(G\) is abelian, then \(G\) is a nilpotent group.

4. **Exercise 30.4**: Let \(\phi: G \to H\) be a homomorphism. Show that \(\ker(\phi)\) is a normal subgroup.

5. **Exercise 30.5**: Prove that in a field, \((a+b)(b+c) = ab + ac + b^2 + bc\).

## 30.6 Summary

This chapter covered:
- Basic group properties and axioms
- Subgroups, cosets, and Lagrange's theorem
- Homomorphisms and isomorphisms
- Rings and fields
- Fundamental ring-theoretic results

These results form the foundation for advanced algebraic theory.

## 30.x Advanced Abstract Algebra

### Theorem 30.1: Sylow's Theorems

**Statement**: Let $G$ be a finite group of order $|G| = p^n m$ where $p$ is prime and $\gcd(p,m) = 1$. Then:

1. (Existence) There exists a subgroup of $G$ of order $p^n$ (a Sylow $p$-subgroup).
2. (Conjugacy) All Sylow $p$-subgroups are conjugate in $G$.
3. (Number) The number $n_p$ of Sylow $p$-subgroups satisfies:
   - $n_p \equiv 1 \pmod{p}$
   - $n_p$ divides $m$

**Proof**: 
1. By induction on $m$, we can find a Sylow $p$-subgroup.
2. Let $P, Q$ be Sylow $p$-subgroups. For any $x \in G$, the map $P \mapsto xPx^{-1}$ gives a bijection between Sylow $p$-subgroups.
3. The number of Sylow $p$-subgroups is the number of orbits of $G$ acting on itself by conjugation. By the orbit-stabilizer theorem, $n_p$ divides $|G|/|P| = m$, and by counting fixed points, $n_p \equiv 1 \pmod{p}$. ∎

### Theorem 30.2: Jordan-Hölder Theorem

**Statement**: If two finite groups $G$ have isomorphic composition series, then they have the same composition factors (up to order and isomorphism).

**Proof**: Let $1 = G_0 \subset G_1 \subset \dots \subset G_r = G$ and $1 = H_0 \subset H_1 \subset \dots \hookrightarrow H_s = G$ be two composition series. By the Schreier refinement theorem, these series have a common refinement which is unique up to isomorphism. Since both are composition series, each is a refinement of the other. The Jordan-Hölder theorem then states that the factors are the same up to isomorphism. ∎

### Theorem 30.3: Burnside's $p^aq^b$ Theorem

**Statement**: If $G$ is a finite group of order $p^aq^b$ for primes $p, q$, then $G$ is solvable.

**Proof**: By induction on $n = a+b$. The center $Z(G)$ is non-trivial for $p$-groups, so we can use the correspondence theorem. The derived series $G^{(0)} = G, G^{(1)} = [G, G], \dots$ terminates in $\{e\}$ after finitely many steps, and each factor is abelian. ∎

### Theorem 30.4: Burnside's Normal $p$-Complement Theorem

**Statement**: Let $G$ be a finite group and $P$ a Sylow $p$-subgroup of $G$. If $N_G(P)/C_G(P)$ is a $p'$-group, then $G$ has a normal $p$-complement.

**Proof**: This follows from the Frattini argument and properties of fusion systems. The condition implies that $P$ controls $p$-fusion in $G$, which by Burnside's theorem gives a normal $p$-complement. ∎


======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697390

Theorem Generation

# **Group Definition**
**Statement**: Set with associative binary operation, identity, inverses.
**Proof**: [proof outline]...


# **Homomorphism**
**Statement**: Map preserving group operation: φ(ab) = φ(a)φ(b).
**Proof**: [proof outline]...


# **First Isomorphism Theorem**
**Statement**: G/Ker(φ) ≅ Im(φ).
**Proof**: [proof outline]...


# **Second Isomorphism Theorem**
**Statement**: H/(H∩K) ≅ (H+K)/K when K⊆H.
**Proof**: [proof outline]...


# **Third Isomorphism Theorem**
**Statement**: (H/K)/(L/K) ≅ H/L when K⊆L⊆H.
**Proof**: [proof outline]...


# **Lagrange's Theorem**
**Statement**: Order of subgroup divides order of finite group.
**Proof**: [proof outline]...


# **Cauchy's Theorem**
**Statement**: If p divides |G|, G has element of order p.
**Proof**: [proof outline]...


# **Sylow's Theorems**
**Statement**: Sylow p-subgroups exist, conjugate, n_p ≡ 1 mod p.
**Proof**: [proof outline]...


# **Normal Subgroup**
**Statement**: H normal iff gH = Hg for all g in G.
**Proof**: [proof outline]...


# **Semidirect Product**
**Statement**: G ≅ N ⋊ H when H acts on N.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618626

Theorem Generation

# **Group Definition**
**Statement**: Set with associative binary operation, identity, inverses.
**Proof**: [proof outline]...


# **Homomorphism**
**Statement**: Map preserving group operation: φ(ab) = φ(a)φ(b).
**Proof**: [proof outline]...


# **First Isomorphism Theorem**
**Statement**: G/Ker(φ) ≅ Im(φ).
**Proof**: [proof outline]...


# **Second Isomorphism Theorem**
**Statement**: H/(H∩K) ≅ (H+K)/K when K⊆H.
**Proof**: [proof outline]...


# **Third Isomorphism Theorem**
**Statement**: (H/K)/(L/K) ≅ H/L when K⊆L⊆H.
**Proof**: [proof outline]...


# **Lagrange's Theorem**
**Statement**: Order of subgroup divides order of finite group.
**Proof**: [proof outline]...


# **Cauchy's Theorem**
**Statement**: If p divides |G|, G has element of order p.
**Proof**: [proof outline]...


# **Sylow's Theorems**
**Statement**: Sylow p-subgroups exist, conjugate, n_p ≡ 1 mod p.
**Proof**: [proof outline]...


# **Normal Subgroup**
**Statement**: H normal iff gH = Hg for all g in G.
**Proof**: [proof outline]...


# **Semidirect Product**
**Statement**: G ≅ N ⋊ H when H acts on N.
**Proof**: [proof outline]...
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*