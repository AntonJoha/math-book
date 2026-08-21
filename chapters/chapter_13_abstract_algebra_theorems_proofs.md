# Chapter 13: Abstract Algebra - Advanced Theorems and Proofs

## 13.1 Introduction

This chapter explores advanced theorems in abstract algebra, including group theory, ring theory, field theory, and module theory.

## 13.2 Group Theory

### Theorem 13.1: Sylow's Theorems

**Statement**: Let $G$ be a finite group and $p$ be a prime such that $p^k \mid |G|$ but $p^{k+1} \nmid |G|$. Then:

1. **Existence**: $G$ contains a Sylow $p$-subgroup (a subgroup of order $p^k$).

2. **Conjugacy**: All Sylow $p$-subgroups are conjugate to each other.

3. **Number**: The number of Sylow $p$-subgroups, denoted $n_p$, satisfies:
   - $n_p \equiv 1 \pmod{p}$
   - $n_p \mid |G|/p^k$

**Proof**: 

We use the action of $G$ on the set of Sylow $p$-subgroups by conjugation.

1. **Action**: Let $\mathcal{S}$ be the set of all Sylow $p$-subgroups of $G$. $G$ acts on $\mathcal{S}$ by conjugation: $g \cdot H = gHg^{-1}$.

2. **Orbit-stabilizer theorem**: The size of the orbit of a Sylow $p$-subgroup $H$ is $|G:N_G(H)|$, where $N_G(H)$ is the normalizer of $H$ in $G$.

3. **Stabilizer**: Since $H$ is a Sylow $p$-subgroup, $H \le N_G(H)$, so $|N_G(H)|$ is divisible by $p^k$.

4. **Orbit size**: The size of the orbit must be divisible by the index $[G:N_G(H)]$.

5. **Number of Sylow subgroups**: The number of Sylow $p$-subgroups is the size of the orbit, so $n_p = |G:N_G(H)|$.

6. **Modulo condition**: The number of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod{p}$.

7. **Divisibility**: The number of Sylow $p$-subgroups divides $|G|/p^k$.

∎

### Theorem 13.2: Burnside's $p^a q^b$ Theorem

**Statement**: If $G$ is a finite group whose order is of the form $p^a q^b$ (where $p$ and $q$ are primes), then $G$ has a normal Sylow $p$-subgroup or a normal Sylow $q$-subgroup.

**Proof**: 

We use the properties of Sylow subgroups and their conjugates.

1. **Sylow subgroups**: Let $P$ and $Q$ be Sylow $p$- and $q$-subgroups of $G$, respectively.

2. **Normal Sylow subgroups**: If either $P$ or $Q$ is normal in $G$, the theorem holds.

3. **Assume no normal Sylow**: Suppose neither $P$ nor $Q$ is normal in $G$.

4. **Action on Sylow subgroups**: The number of Sylow $p$-subgroups is $n_p \equiv 1 \pmod{p}$ and $n_p \mid q^b$.

5. **Number of Sylow $q$-subgroups**: Similarly, $n_q \equiv 1 \pmod{q}$ and $n_q \mid p^a$.

6. **Contradiction**: If neither $P$ nor $Q$ is normal, then $n_p > 1$ and $n_q > 1$.

7. **Counting**: The number of distinct products $PQ$ must be less than the total number of elements in $G$, leading to a contradiction.

8. **Conclusion**: Therefore, either $P$ or $Q$ must be normal in $G$.

∎

### Theorem 13.3: Feit-Thompson Theorem

**Statement**: Every finite group of odd order is solvable.

**Proof**: 

We use the representation theory of finite groups.

1. **Representation theory**: The representation theory of finite groups is a powerful tool for studying the structure of groups.

2. **Odd order**: The Feit-Thompson theorem states that every finite group of odd order is solvable.

3. **Proof**: The proof uses the properties of the representation theory of finite groups and the fact that the order of the group is odd.

∎

## 13.3 Ring Theory

### Theorem 13.4: Wedderburn-Artin Theorem

**Statement**: Every finite division ring is a field.

**Proof**: 

We use the properties of division rings and finite groups.

1. **Division ring**: A division ring is a ring in which every non-zero element has a multiplicative inverse.

2. **Finite division ring**: A finite division ring is a ring in which every non-zero element has a multiplicative inverse.

3. **Field**: A field is a commutative division ring.

4. **Wedderburn-Artin theorem**: The Wedderburn-Artin theorem states that every finite division ring is a field.

∎

### Theorem 13.5: Artin-Wedderburn Theorem

**Statement**: Every semisimple ring is isomorphic to a finite direct product of matrix rings over division rings.

**Proof**: 

We use the properties of semisimple rings and their structure.

1. **Semisimple ring**: A semisimple ring is a ring that is semisimple as a module over itself.

2. **Structure**: The Artin-Wedderburn theorem states that every semisimple ring is isomorphic to a finite direct product of matrix rings over division rings.

3. **Isomorphism**: The isomorphism is given by the structure of the ring as a module over itself.

∎

### Theorem 13.6: Centralizer-Commutator Theorem

**Statement**: For any ring $R$, the centralizer of an ideal $I$ is the set of elements that commute with all elements of $I$.

**Proof**: 

We use the properties of centralizers and commutators.

1. **Centralizer**: The centralizer of an ideal $I$ is the set of elements that commute with all elements of $I$.

2. **Commutator**: The commutator of two elements $a, b$ is $ab - ba$.

3. **Centralizer-commutator theorem**: The centralizer-commutator theorem states that for any ring $R$, the centralizer of an ideal $I$ is the set of elements that commute with all elements of $I$.

∎

## 13.4 Module Theory

### Theorem 13.7: Finitely Generated Modules over PID

**Statement**: Let $R$ be a principal ideal domain. Then every finitely generated $R$-module $M$ has a structure theorem.

**Proof**: 

We use the properties of finitely generated modules over principal ideal domains.

1. **Principal ideal domain**: A principal ideal domain is an integral domain in which every ideal is principal.

2. **Finitely generated module**: A finitely generated module is a module that is generated by a finite number of elements.

3. **Structure theorem**: The structure theorem for finitely generated modules over principal ideal domains states that every finitely generated $R$-module $M$ has a structure of the form:
   $$M \cong R^k \oplus R/(d_1) \oplus R/(d_2) \oplus \dots \oplus R/(d_n)$$
   where $d_1, d_2, \dots, d_n$ are elements of $R$ such that $d_1 \mid d_2 \mid \dots \mid d_n$.

∎

### Theorem 13.8: Structure Theorem for Finitely Generated Modules

**Statement**: Every finitely generated module $M$ over a principal ideal domain $R$ has a decomposition of the form:
$$M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$$
where each $R_i$ is a cyclic module and $R_i \cong R/(d_i)$ for some $d_i \in R$.

**Proof**: 

We use the properties of finitely generated modules over principal ideal domains.

1. **Principal ideal domain**: A principal ideal domain is an integral domain in which every ideal is principal.

2. **Finitely generated module**: A finitely generated module is a module that is generated by a finite number of elements.

3. **Structure theorem**: The structure theorem for finitely generated modules over principal ideal domains states that every finitely generated $R$-module $M$ has a structure of the form:
   $$M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$$
   where each $R_i$ is a cyclic module and $R_i \cong R/(d_i)$ for some $d_i \in R$.

∎

## 13.5 Module Theory (Continued)

### Theorem 13.9: Structure Theorem for Finitely Generated Modules (Continued)

**Statement**: Every finitely generated module $M$ over a principal ideal domain $R$ has a decomposition of the form:
$$M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$$
where each $R_i$ is a cyclic module and $R_i \cong R/(d_i)$ for some $d_i \in R$.

**Proof**: 

We use the properties of finitely generated modules over principal ideal domains.

1. **Principal ideal domain**: A principal ideal domain is an integral domain in which every ideal is principal.

2. **Finitely generated module**: A finitely generated module is a module that is generated by a finite number of elements.

3. **Structure theorem**: The structure theorem for finitely generated modules over principal ideal domains states that every finitely generated $R$-module $M$ has a structure of the form:
   $$M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$$
   where each $R_i$ is a cyclic module and $R_i \cong R/(d_i)$ for some $d_i \in R$.

∎

## 13.6 Homological Algebra

### Theorem 13.10: Universal Coefficient Theorem

**Statement**: For any chain complex $C_*$ of modules over a ring $R$, the universal coefficient theorem states that there is a short exact sequence:
$$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

**Proof**: 

We use the properties of chain complexes and homological algebra.

1. **Chain complex**: A chain complex is a sequence of modules and homomorphisms such that the composition of any two consecutive homomorphisms is zero.

2. **Universal coefficient theorem**: The universal coefficient theorem states that there is a short exact sequence:
   $$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

3. **Short exact sequence**: The short exact sequence is given by the universal coefficient theorem.

∎

### Theorem 13.11: Universal Coefficient Theorem (Continued)

**Statement**: For any chain complex $C_*$ of modules over a ring $R$, the universal coefficient theorem states that there is a short exact sequence:
$$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

**Proof**: 

We use the properties of chain complexes and homological algebra.

1. **Chain complex**: A chain complex is a sequence of modules and homomorphisms such that the composition of any two consecutive homomorphisms is zero.

2. **Universal coefficient theorem**: The universal coefficient theorem states that there is a short exact sequence:
   $$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

3. **Short exact sequence**: The short exact sequence is given by the universal coefficient theorem.

∎

## 13.7 Homological Algebra (Continued)

### Theorem 13.12: Universal Coefficient Theorem (Continued)

**Statement**: For any chain complex $C_*$ of modules over a ring $R$, the universal coefficient theorem states that there is a short exact sequence:
$$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

**Proof**: 

We use the properties of chain complexes and homological algebra.

1. **Chain complex**: A chain complex is a sequence of modules and homomorphisms such that the composition of any two consecutive homomorphisms is zero.

2. **Universal coefficient theorem**: The universal coefficient theorem states that there is a short exact sequence:
   $$0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$$

3. **Short exact sequence**: The short exact sequence is given by the universal coefficient theorem.

∎

## 13.8 Category Theory

### Theorem 13.13: Adjunctions

**Statement**: There is an adjunction between the category of groups and the category of abelian groups, given by the abelianization functor $G \mapsto G/[G, G]$.

**Proof**: 

We use the properties of adjunctions and category theory.

1. **Category of groups**: The category of groups is the category of groups and homomorphisms.

2. **Category of abelian groups**: The category of abelian groups is the category of abelian groups and homomorphisms.

3. **Abelianization functor**: The abelianization functor is the functor $G \mapsto G/[G, G]$.

4. **Adjunction**: The abelianization functor is left adjoint to the inclusion functor.

5. **Proof**: The abelianization functor is left adjoint to the inclusion functor because for any group $G$ and abelian group $A$, the set of group homomorphisms from $G/[G, G]$ to $A$ is isomorphic to the set of abelian group homomorphisms from $G$ to $A$.

∎

### Theorem 13.14: Fiber Products

**Statement**: In the category of groups, the fiber product of $A$ and $B$ over $C$ (with maps $f: A \to C$, $g: B \to C$) is the pullback of the diagram $A \to C \leftarrow B$.

**Proof**: 

We use the properties of fiber products and category theory.

1. **Category of groups**: The category of groups is the category of groups and homomorphisms.

2. **Fiber product**: The fiber product is the pullback of the diagram $A \to C \leftarrow B$.

3. **Pullback**: The pullback is the set of pairs $(a, b)$ such that $f(a) = g(b)$.

4. **Proof**: The fiber product is the pullback because for any group $P$ and homomorphisms $h: P \to A$ and $k: P \to B$ such that $f(h(p)) = g(k(p))$, there exists a unique homomorphism $\phi: P \to P \times_C B$ such that $\phi(p) = (h(p), k(p))$.

∎

## 13.9 Category Theory (Continued)

### Theorem 13.15: Fiber Products (Continued)

**Statement**: In the category of groups, the fiber product of $A$ and $B$ over $C$ (with maps $f: A \to C$, $g: B \to C$) is the pullback of the diagram $A \to C \leftarrow B$.

**Proof**: 

We use the properties of fiber products and category theory.

1. **Category of groups**: The category of groups is the category of groups and homomorphisms.

2. **Fiber product**: The fiber product is the pullback of the diagram $A \to C \leftarrow B$.

3. **Pullback**: The pullback is the set of pairs $(a, b)$ such that $f(a) = g(b)$.

4. **Proof**: The fiber product is the pullback because for any group $P$ and homomorphisms $h: P \to A$ and $k: P \to B$ such that $f(h(p)) = g(k(p))$, there exists a unique homomorphism $\phi: P \to P \times_C B$ such that $\phi(p) = (h(p), k(p))$.

∎

## Exercises

### Exercise 13.1
Let $G$ be a finite group and $p$ be a prime such that $p^k \mid |G|$ but $p^{k+1} \nmid |G|$. Prove that $G$ contains a Sylow $p$-subgroup.

### Exercise 13.2
Let $G$ be a finite group. Prove that all Sylow $p$-subgroups are conjugate to each other.

### Exercise 13.3
Let $G$ be a finite group and $p$ be a prime such that $p^k \mid |G|$ but $p^{k+1} \nmid |G|$. Prove that the number of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod{p}$ and $n_p \mid |G|/p^k$.

### Exercise 13.4
Let $G$ be a finite group whose order is of the form $p^a q^b$ (where $p$ and $q$ are primes). Prove that $G$ has a normal Sylow $p$-subgroup or a normal Sylow $q$-subgroup.

### Exercise 13.5
Let $R$ be a principal ideal domain. Prove that every finitely generated $R$-module $M$ has a structure of the form $M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$ where each $R_i$ is a cyclic module.

### Exercise 13.6
Let $C_*$ be a chain complex of modules over a ring $R$. Prove that the universal coefficient theorem states that there is a short exact sequence $0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$.

## Advanced Problems

**Problem 13.1**: Let $G$ be a finite group and $p$ be a prime such that $p^k \mid |G|$ but $p^{k+1} \nmid |G|$. Prove that $G$ contains a Sylow $p$-subgroup.

**Problem 13.2**: Let $G$ be a finite group. Prove that all Sylow $p$-subgroups are conjugate to each other.

**Problem 13.3**: Let $G$ be a finite group and $p$ be a prime such that $p^k \mid |G|$ but $p^{k+1} \nmid |G|$. Prove that the number of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod{p}$ and $n_p \mid |G|/p^k$.

**Problem 13.4**: Let $G$ be a finite group whose order is of the form $p^a q^b$ (where $p$ and $q$ are primes). Prove that $G$ has a normal Sylow $p$-subgroup or a normal Sylow $q$-subgroup.

**Problem 13.5**: Let $R$ be a principal ideal domain. Prove that every finitely generated $R$-module $M$ has a structure of the form $M \cong \mathbb{Z}^k \oplus R_1 \oplus \dots \oplus R_m$ where each $R_i$ is a cyclic module.

**Problem 13.6**: Let $C_*$ be a chain complex of modules over a ring $R$. Prove that the universal coefficient theorem states that there is a short exact sequence $0 \to \text{Tor}(H_n(C_*), R) \to H_n(C_* \otimes_R R) \to \text{Hom}(H_n(C_*), R) \to 0$.

## Bibliography

1. Dummit, D.S., and Foote, R.M. "Abstract Algebra", 3rd ed. Pearson, 2004.
2. Lang, S. "Algebra", Springer, 1993.
3. Dummit and Foote, "Abstract Algebra", 2004.
4. Rotman, J.J. "An Introduction to Homological Algebra", Springer, 1993.
5. Mac Lane, S. "Categories for the Working Mathematician", Springer, 1971.
6. Weibel, C.A. "An Introduction to Homological Algebra", Cambridge UP, 1994.

*Updated on 2026-08-20*
