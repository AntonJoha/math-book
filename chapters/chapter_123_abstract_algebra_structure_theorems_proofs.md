# Chapter 123: Abstract Algebra - Structure Theorems and Proofs

## 123.1 Introduction

This chapter explores the structural theory of rings, fields, and modules through fundamental structure theorems. We examine:
- The Artin-Wedderburn Theorem
- The Structure Theorem for Finitely Generated Modules
- The Jordan-Holder Theorem
- The Fundamental Theorem of Galois Theory
- Classification of finite groups

## 123.2 The Artin-Wedderburn Theorem

**Theorem 123.1 (Artin-Wedderburn)**  
A ring $R$ is a finite direct product of matrix rings over division rings if and only if $R$ is a semisimple ring.

*Proof:*  
Let $R$ be semisimple. Then $R$ has a minimal set of orthogonal idempotents $e_1, \dots, e_n$ such that $R = e_1 R \oplus \dots \oplus e_n R$. Each $e_i R e_i$ is a division ring. Let $D_i = e_i R e_i$. Then $R \cong M_{n_i}(D_i)$.

Conversely, if $R \cong \prod M_{n_i}(D_i)$, then $R$ is Artinian and Noetherian, hence semisimple.

**Corollary:**  
Every semisimple ring is Artinian and Noetherian.

*Proof:*  
A semisimple ring is a finite direct product of matrix rings over division rings. Matrix rings over division rings are both Artinian and Noetherian (finite length).

## 123.3 Structure Theorem for Finitely Generated Modules

**Theorem 123.2 (Structure Theorem for Finitely Generated Modules over PIDs)**  
Let $R$ be a principal ideal domain and $M$ a finitely generated $R$-module. Then $M$ is isomorphic to:
$$M \cong R^r \oplus \bigoplus_{i=1}^k R/(d_i)$$
where $r$ is the free rank, $d_1 | d_2 | \dots | d_k$ are non-zero elements of $R$, and $R/(d_i)$ are the torsion submodules.

*Proof:*  
Let $M$ be a finitely generated $R$-module. By the structure theorem for modules over PIDs, we decompose $M$ into free and torsion parts. The torsion part decomposes further into invariant factor decomposition.

**Corollary:**  
Over a field $F$, every finite-dimensional vector space $V$ is isomorphic to $F^n$ where $n = \dim_F(V)$.

*Proof:*  
A field is a PID. Taking $R = F$ (a field), all ideals are principal. The invariant factors $d_i$ must be units, so $R/(d_i) = 0$. Thus $M \cong F^r$.

## 123.4 The Jordan-Holder Theorem

**Theorem 123.3 (Jordan-Holder / Second Isomorphism Theorem)**  
Let $G$ be a group and $N, H$ normal subgroups of $G$ with $H \subseteq N$. Then:
$$N/(N \cap H) \cong NH/H$$

*Proof:*  
Consider the natural homomorphism:
$$\phi: N \to NH/H$$
defined by $\phi(n) = nH$. This is well-defined since $H$ is normal. The kernel is $N \cap H$. By the First Isomorphism Theorem:
$$N/(N \cap H) \cong NH/H$$

**Corollary (Uniqueness of Composition Series)**  
Any two composition series of a finite group $G$ have the same length, and the factors are isomorphic up to reordering.

*Proof:*  
This follows from the Jordan-Holder theorem, which states that any two composition series have isomorphic factor groups.

## 123.5 The Fundamental Theorem of Galois Theory

**Theorem 123.4 (Galois Theory)**  
Let $L/K$ be a Galois extension with Galois group $G = \text{Gal}(L/K)$. There is a one-to-one correspondence between:
1. Intermediate fields $K \subseteq M \subseteq L$
2. Subgroups $H \subseteq G$

Under this correspondence:
- $M \leftrightarrow \text{Gal}(L/M) = \{ \sigma \in G \mid \sigma|_M = \text{id} \}$
- $H \leftrightarrow L^H = \{ x \in L \mid \sigma(x) = x \text{ for all } \sigma \in H \}$

*Proof:*  
The correspondence is constructed as follows:

1. For a subgroup $H$, let $L^H = \{ x \in L \mid \sigma(x) = x \forall \sigma \in H \}$ by definition.

2. For a field $M$, let $\text{Gal}(L/M) = \{ \sigma \in G \mid \sigma|_M = \text{id} \}$.

The maps are inverse to each other, forming a bijection.

**Theorem 123.5 (Galois Correspondence Properties)**  
For subgroups $H_1, H_2 \subseteq G$:
1. $M_1 \subseteq M_2 \iff H_2 \subseteq H_1$
2. $\text{Gal}(L/M_1 \cap M_2) = \text{Gal}(L/M_1) \cdot \text{Gal}(L/M_2)$
3. $\text{Gal}(L/M_1 M_2) = \text{Gal}(L/M_1) \cap \text{Gal}(L/M_2)$
4. $\text{Gal}(L/M_1 \cdot \text{Gal}(L/M_2)) \cong \text{Gal}(L/M_1) + \text{Gal}(L/M_2)$ (sum of subgroups)

*Proof:*  
These properties follow from the definitions and the isomorphism theorems.

## 123.6 Classification of Finite Groups

**Theorem 123.6 (Sylow Theorems)**  
Let $G$ be a finite group of order $|G| = p^k m$ where $p$ is prime and $\gcd(p, m) = 1$. Then:
1. For each $k$, there exists a subgroup of order $p^k$.
2. All subgroups of order $p^k$ are conjugate.
3. The number $n_p$ of Sylow $p$-subgroups divides $m$ and satisfies $n_p \equiv 1 \pmod p$.

*Proof:*  
Let $G$ be a finite group of order $p^k m$ with $\gcd(p, m) = 1$.

1. By Cauchy's theorem, if $p$ divides $|G|$, then $G$ has an element of order $p$. By inductive arguments and the normalizer-core argument, we can show existence of subgroups of order $p^k$.

2. If $P_1, P_2$ are Sylow $p$-subgroups, then $P_1 \cap P_2$ is a normal subgroup of $P_1 P_2$. Using the orbit-stabilizer theorem, all Sylow $p$-subgroups are conjugate.

3. The number of Sylow $p$-subgroups $n_p$ satisfies $n_p \equiv 1 \pmod p$ and $n_p$ divides $|G|/p^k = m$.

**Corollary (Sylow p-subgroups of abelian groups):**  
If $G$ is abelian, all Sylow $p$-subgroups are normal.

*Proof:*  
If $G$ is abelian, all subgroups are normal, so all Sylow $p$-subgroups are normal.

**Theorem 123.7 (Fundamental Theorem of Finite Abelian Groups)**  
Every finite abelian group $G$ is isomorphic to a direct product of cyclic groups of prime power order:
$$G \cong \mathbb{Z}_{p_1^{e_1}} \times \mathbb{Z}_{p_2^{e_2}} \times \dots \times \mathbb{Z}_{p_r^{e_r}}$$

*Proof:*  
Use the structure theorem for finitely generated abelian groups, which states that any finitely generated abelian group is isomorphic to $R^n \oplus \bigoplus R/(d_i)$ where $R = \mathbb{Z}$. The invariant factors can be further decomposed into prime power factors.

---

*End of Chapter 123*
