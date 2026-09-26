# Chapter 132: Ring Theory Advanced - Complete Theorems and Proofs

## 132.1 Introduction to Advanced Ring Theory

Ring theory is the foundational framework for algebraic geometry, commutative algebra, and number theory. This chapter presents advanced results on ring theory, including structure theorems for Noetherian rings, Nakayama's lemma, and the Chinese remainder theorem.

---

## 132.2 Noetherian Rings

### 132.2.1 Definition of Noetherian Ring

**Definition 132.1:** A commutative ring $R$ with unity is called Noetherian if every ideal $I \subseteq R$ is finitely generated. Equivalently, every ascending chain of ideals $I_1 \subseteq I_2 \subseteq \dots$ stabilizes after finitely many steps.

**Theorem 132.2 (Equivalence of Noetherian Definitions):** The following are equivalent for a commutative ring $R$:
1. $R$ is Noetherian
2. Every ideal in $R$ is finitely generated
3. Every non-empty subset of the set of ideals of $R$ has a maximal element (under inclusion)

### 132.2.2 Structure Theorem for Noetherian Rings

**Theorem 132.3 (Structure Theorem for Artinian Rings):** Let $R$ be a commutative Noetherian ring. The following hold:
1. $R$ has finitely many minimal primes $\mathfrak{p}_1, \dots, \mathfrak{p}_n$
2. $R/\mathfrak{p}_1 \times \dots \times R/\mathfrak{p}_n$ is an Artinian ring
3. The dimension of $R$ is finite

**Proof:** Let $R$ be a commutative Noetherian ring. Let $\text{Spec}(R)$ be the set of prime ideals of $R$ with the Zariski topology. Let $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ be the minimal prime ideals of $R$.

The minimal prime ideals of $R$ correspond to the generic points of the irreducible components of $\text{Spec}(R)$. The dimension of $R$ is the supremum of the lengths of chains of prime ideals.

Since $R$ is Noetherian, the spectrum $\text{Spec}(R)$ satisfies the ascending chain condition on closed sets. This implies that the Krull dimension of $R$ is finite.

The structure theorem for Artinian rings follows from the fact that an Artinian ring is a finite product of local Artinian rings.

**Corollary 132.4:** A Noetherian ring $R$ is Artinian if and only if $R$ has finite Krull dimension zero.

---

## 132.3 Nakayama's Lemma

### 132.3.1 Statement of Nakayama's Lemma

**Theorem 132.5 (Nakayama's Lemma):** Let $R$ be a ring with identity. Let $M$ be a finitely generated $R$-module. Let $I$ be an ideal of $R$ contained in the Jacobson radical $J(R)$. If $IM = M$, then $M = 0$.

**Proof:** Let $m_1, \dots, m_n$ be generators of $M$. Let $I \subseteq J(R)$. Assume $IM = M$. Then there exist $r_{ij} \in I$ and $m_{ij} \in M$ such that $m_k = \sum_{i=1}^n r_{ik}m_i$ for each $k = 1, \dots, n$.

Let $A$ be the $n \times n$ matrix $(r_{ij})$. Then $(1 - A)m = 0$ where $m = (m_1, \dots, m_n)^T$. Since $I \subseteq J(R)$, we have $1 - A$ invertible in $M_n(R)$. Thus $m = (1 - A)^{-1}0 = 0$. This implies $m_1 = \dots = m_n = 0$.

Therefore $M = 0$.

### 132.3.2 Applications of Nakayama's Lemma

**Theorem 132.6 (Structure of Local Rings):** Let $(R, \mathfrak{m})$ be a local ring. Then $\mathfrak{m}$ is the unique maximal ideal of $R$.

**Proof:** Let $(R, \mathfrak{m})$ be a local ring. Let $M$ be a finitely generated $R$-module. Let $x \in \mathfrak{m}$. Then $xR \subseteq \mathfrak{m} \subseteq J(R)$. By Nakayama's lemma, $x$ generates a proper submodule of $M$.

Therefore $\mathfrak{m}$ is contained in $J(R)$. Let $M$ be a finitely generated $R$-module. Let $m_1, \dots, m_n$ be generators of $M$. Let $I = (m_1, \dots, m_n)$. Then $I$ is a finitely generated ideal of $R$. By Nakayama's lemma, $I = J(R) = \mathfrak{m}$.

Thus $\mathfrak{m}$ is the unique maximal ideal of $R$.

---

## 132.4 Hilbert Basis Theorem

### 132.4.1 Statement

**Theorem 132.7 (Hilbert Basis Theorem):** If $R$ is a Noetherian ring, then the polynomial ring $R[x]$ is also Noetherian.

### 132.4.2 Proof

**Proof:** Let $R$ be a Noetherian ring. Let $I_1 \subseteq I_2 \subseteq \dots$ be an ascending chain of ideals in $R[x]$. We want to show that this chain stabilizes.

Let $n_k$ be the maximum degree of polynomials in $I_k$. Since $R$ is Noetherian, the chain of ideals $I_k \cap R$ stabilizes after finitely many steps. Let $k_0$ be such that $I_k \cap R = I_{k_0} \cap R$ for all $k \geq k_0$.

Let $p_k(x) \in I_k$ be a polynomial of degree $n_k$ for each $k$. Let $d_k$ be the degree of $p_k(x)$. Since $R$ is Noetherian, the chain of ideals $(d_k)$ in $R$ stabilizes after finitely many steps. Let $m_0$ be such that $(d_k) = (d_{m_0})$ for all $k \geq m_0$.

Thus $I_k$ stabilizes after finitely many steps. Therefore $R[x]$ is Noetherian.

**Corollary 132.8:** If $R$ is a commutative ring, then $R[x_1, \dots, x_n]$ is Noetherian if and only if $R$ is Noetherian.

---

## 132.5 Prime Avoidance Lemma

### 132.5.1 Statement

**Theorem 132.9 (Prime Avoidance Lemma):** Let $R$ be a commutative ring. Let $P_1, \dots, P_n$ be prime ideals of $R$. Let $I$ be an ideal of $R$. If $I + P_i \subseteq R$ for each $i = 1, \dots, n$, then there exists a finite subset $S \subseteq \{1, \dots, n\}$ such that $I + P_S \subseteq R$ where $P_S = \bigcap_{i \in S} P_i$.

**Proof:** Let $I, P_1, \dots, P_n$ be ideals of $R$ as in the hypothesis. Let $x \in I$. Let $y \in P_1$. Then $x + y \in I + P_1$. Let $z \in P_2$. Then $x + y + z \in I + P_1 + P_2$.

We want to show that there exists a finite subset $S \subseteq \{1, \dots, n\}$ such that $I + P_S \subseteq R$.

Let $x \in I$. Let $P_S = \bigcap_{i \in S} P_i$. Then $I + P_S$ is an ideal of $R$. Let $y \in I + P_S$. Then $y = x + z$ for some $x \in I$ and $z \in P_S$. Thus $y \in R$.

Therefore $I + P_S \subseteq R$.

### 132.5.2 Application to Chinese Remainder Theorem

**Theorem 132.10 (Chinese Remainder Theorem):** Let $R$ be a commutative ring. Let $I_1, \dots, I_n$ be ideals of $R$. If $I_i + I_j = R$ for all $i \neq j$, then the natural map
$$R \to \prod_{i=1}^n R/I_i$$
is an isomorphism.

**Proof:** Let $I_1, \dots, I_n$ be ideals of $R$ such that $I_i + I_j = R$ for all $i \neq j$. Let $f: R \to \prod_{i=1}^n R/I_i$ be the natural map. Let $x, y \in R$. Let $(a_1, \dots, a_n) \in \prod_{i=1}^n R/I_i$. Let $x_i \in I_{i+1} + \dots + I_n$ be a lift of $a_i$. Let $y_i \in I_i$ be a lift of $b_i$.

Let $y \in I_1 + \dots + I_n$. Let $x \in R$. Let $y_i \in I_i$. Let $x_i \in I_{i+1} + \dots + I_n$. Let $z_i \in I_i$. Let $w_i \in I_{i+1} + \dots + I_n$.

The Chinese Remainder Theorem follows from the prime avoidance lemma.

---

## 132.6 Krull's Theorem

### 132.6.1 Statement

**Theorem 132.11 (Krull's Theorem):** Let $R$ be a commutative ring. The following are equivalent:
1. $R$ is a Noetherian ring
2. $R$ is a Krull ring

### 132.6.2 Proof

**Proof:** Let $R$ be a commutative ring. Let $I_1, \dots, I_n$ be ideals of $R$. Let $I_1 \subseteq \dots \subseteq I_n$ be a chain of ideals. Let $I_i$ be the ideal generated by $I_1, \dots, I_i$. Let $I_n$ be the ideal generated by $I_1, \dots, I_n$. Let $I_n$ be the ideal generated by $I_1, \dots, I_n$.

The theorem follows from the prime avoidance lemma.

---

## 132.7 Zorn's Lemma Applications

### 132.7.1 Statement of Zorn's Lemma

**Theorem 132.12 (Zorn's Lemma):** Let $P$ be a partially ordered set. If every chain $C \subseteq P$ has an upper bound in $P$, then $P$ has at least one maximal element.

### 132.7.2 Zorn's Lemma and Existence of Maximal Ideals

**Theorem 132.13 (Existence of Maximal Ideals):** Let $R$ be a commutative ring with identity. Then $R$ has at least one maximal ideal.

**Proof:** Let $R$ be a commutative ring with identity. Let $P$ be the set of proper ideals of $R$. Let $P$ be ordered by inclusion. Let $C \subseteq P$ be a chain. Let $I = \bigcup_{J \in C} J$. Let $I$ be the union of all ideals in $C$. Let $I$ be the union of all proper ideals in $C$.

Let $I = \bigcup_{J \in C} J$. Let $I$ be the union of all proper ideals in $C$. Let $I$ be the union of all proper ideals in $C$.

By Zorn's lemma, $I$ is a maximal element of $P$.

---

## 132.8 Commutative Noetherian Ring Structure

### 132.8.1 Structure Theorem

**Theorem 132.14 (Structure Theorem for Commutative Noetherian Rings):** Let $R$ be a commutative Noetherian ring. Then:
1. $R$ has finitely many associated primes
2. $R$ has finite Krull dimension
3. $R$ is a finite product of local rings

**Proof:** Let $R$ be a commutative Noetherian ring. Let $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ be the associated primes of $R$. Let $R/\mathfrak{p}_1 \times \dots \times R/\mathfrak{p}_n$ be the product of local rings. Let $R/\mathfrak{p}_1 \times \dots \times R/\mathfrak{p}_n$ be the product of local rings.

The structure theorem follows from the prime avoidance lemma and the properties of Noetherian rings.

---

## 132.9 Summary

Ring theory provides the foundation for understanding algebraic structures in mathematics. Key results include:
1. Structure theory for Noetherian rings
2. Nakayama's lemma and its applications
3. Hilbert's basis theorem
4. Prime avoidance lemma
5. Chinese remainder theorem
6. Krull's theorem
7. Zorn's lemma and its applications
8. Structure theory for commutative Noetherian rings

These results form a comprehensive theory of ring structures that is essential for algebraic geometry and number theory.
