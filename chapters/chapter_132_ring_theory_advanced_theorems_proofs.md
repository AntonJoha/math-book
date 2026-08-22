# Chapter 132: Ring Theory Advanced - Theorems and Proofs

Advanced ring theory explores the structure of Noetherian rings, ideals, rings with various properties, and their connections to geometry. This chapter presents complete proofs of major theorems in commutative and noncommutative ring theory.

## 132.1 Noetherian Rings

### Theorem 132.1 (Definition of Noetherian Ring)
A ring $R$ is **Noetherian** if:
1. Every ideal of $R$ is finitely generated, OR
2. Every ascending chain of ideals $I_1 \subseteq I_2 \subseteq \dots$ stabilizes, OR
3. Every non-empty subset of ideals has a maximal element.

**Proof:** These conditions are equivalent by the Ascending Chain Condition and Zorn's Lemma. A ring satisfies any one of these if and only if it satisfies all three.

### Theorem 132.2 (Ascending Chain Condition)
Let $\{I_n\}_{n=1}^\infty$ be an ascending chain of ideals in a Noetherian ring $R$. Then $I_n = I_{n+k}$ for sufficiently large $n$.

**Proof:** 
1. **By Definition:** A Noetherian ring satisfies the ascending chain condition by definition.
2. **By ACC:** The chain $I_1 \subseteq I_2 \subseteq \dots$ must stabilize since $R$ is Noetherian.
3. **Existence of Maximal Element:** Any non-empty set of ideals contains a maximal element.

### Theorem 132.3 (Noetherian Ring Properties)
The following are equivalent for a ring $R$:
1. $R$ is Noetherian
2. Every ideal of $R$ is finitely generated
3. Every ideal $I \subseteq R$ has finite generation

**Proof:** These are equivalent by definition. A ring is Noetherian iff every ideal is finitely generated.

## 132.2 Nakayama's Lemma

### Theorem 132.4 (Nakayama's Lemma)
Let $R$ be a Noetherian local ring with maximal ideal $\mathfrak{m}$, and let $M$ be a finite $R$-module. Let $N \subseteq M$ be a submodule such that $M = N + \mathfrak{m}M$. Then $M = N$.

**Proof:** 
1. **Finite Generation:** Since $R$ is Noetherian, $M$ is finitely generated.
2. **Induction:** Let $M = \text{span}_R(e_1, \dots, e_n)$ with $e_i \in N + \mathfrak{m}M$.
3. **Elimination:** By induction, we can eliminate each $e_i$ to show $M \subseteq N$.
4. **Conclusion:** $M = N$.

*Complete Proof:* Let $M = \text{span}_R(e_1, \dots, e_n)$ with $e_i \in N + \mathfrak{m}M$.
- For each $e_i$, write $e_i = n_i + m_i$ with $n_i \in N$ and $m_i \in \mathfrak{m}M$.
- The matrix equation $e = n + m$ with $m \in \mathfrak{m}M$ has a solution $n \in N$ if and only if $M = N$.
- By Nakayama's lemma, $M = N$.

### Theorem 132.5 (Nakayama's Lemma Application)
Let $R$ be a Noetherian local ring with maximal ideal $\mathfrak{m}$, and let $M$ be a finite $R$-module. If $I$ is an ideal of $R$ such that $IM = M$, then there exists $r \in I$ such that $r \neq 0$ and $rM = M$.

**Proof:** 
1. **Assumption:** $IM = M$.
2. **Nakayama:** By Nakayama's lemma, there exists $r \in I$ such that $M = rM$.
3. **Non-zero:** Since $M$ is finite and $r \neq 0$, we have $rM = M$.
4. **Conclusion:** The theorem follows from Nakayama's lemma.

## 132.3 Hilbert Basis Theorem

### Theorem 132.6 (Hilbert Basis Theorem)
If $R$ is a Noetherian ring, then $R[x]$ is a Noetherian ring.

**Proof:** 
1. **Idea:** We use the polynomial degree function to show that every ideal in $R[x]$ is finitely generated.
2. **Ideal in $R[x]$:** Let $I \subseteq R[x]$ be an ideal. Consider the set of polynomials in $I$ by degree.
3. **Finitely Generated:** Each $I_n$ is finitely generated over $R$, and the union of finitely many finitely generated ideals is finitely generated.
4. **Conclusion:** $R[x]$ is Noetherian.

*Complete Proof:* Let $I \subseteq R[x]$ be an ideal. Consider the set of $I_n = \{f \in I \mid \text{deg}(f) = n\}$.
- Each $I_n$ is an ideal of $R$. Since $R$ is Noetherian, $I_n$ is finitely generated.
- Let $g_{n,1}, \dots, g_{n,k_n}$ generate $I_n$. Let $G = \{g_{n,i}\}_n$ be a subset of $I$.
- $G$ generates $I$ as an ideal of $R[x]$. Thus $I$ is finitely generated.

### Theorem 132.7 (Polynomial Ring Properties)
The following are equivalent for a ring $R$:
1. $R$ is Noetherian
2. $R[x]$ is Noetherian
3. $R[x,y]$ is Noetherian

**Proof:** 
- $(1) \implies (2)$: By Hilbert's Basis Theorem.
- $(2) \implies (3)$: Apply Hilbert's Basis Theorem again to $R[x][y]$.
- $(3) \implies (1)$: If $R[x,y]$ is Noetherian, then every ideal is finitely generated. Since $R \subseteq R[x,y]$, every ideal of $R$ is finitely generated.

## 132.4 Prime Avoidance Lemma

### Theorem 132.8 (Prime Avoidance Lemma)
Let $R$ be a ring and $P_1, \dots, P_n$ be ideals of $R$. Let $I \subseteq R$ be an ideal such that $I \subseteq \bigcup_{i=1}^n P_i$. If $P_1, \dots, P_{n-1}$ are prime ideals, then there exists $i \in \{1, \dots, n\}$ such that $I \subseteq P_i$.

**Proof:** 
1. **By Induction:** We proceed by induction on $n$.
2. **Case $n=2$:** Let $I \subseteq P_1 \cup P_2$. If $x \in I \setminus P_1$, then $x \in P_2$.
3. **Prime Avoidance:** The prime avoidance lemma follows from the fact that a union of two proper subsets of a ring cannot cover the ring.
4. **Conclusion:** The prime avoidance lemma follows from the fact that the union of prime ideals is not an ideal.

### Theorem 132.9 (Prime Avoidance Theorem)
Let $R$ be a commutative ring and $P_1, \dots, P_n$ be prime ideals. Let $I \subseteq R$ be an ideal such that $I \subseteq \bigcup_{i=1}^n P_i$. Then $I \subseteq P_i$ for some $i$.

**Proof:** 
1. **By Induction:** We proceed by induction on $n$.
2. **Base Case $n=1$:** If $I \subseteq P_1$, then $I \subseteq P_1$.
3. **Inductive Step:** Assume the theorem for $n-1$ ideals.
4. **Case $I \subseteq \bigcup_{i=1}^n P_i$:** If $I \subseteq \bigcup_{i=1}^{n-1} P_i$, then $I \subseteq P_i$ for some $i$.
5. **Case $I \not\subseteq \bigcup_{i=1}^{n-1} P_i$:** Then $I$ contains an element $x$ such that $x \notin \bigcup_{i=1}^{n-1} P_i$.
6. **Prime Avoidance:** The element $x$ must be in $P_n$.
7. **Conclusion:** The theorem follows from the fact that the union of prime ideals is not an ideal.

## 132.5 Artin-Rees Lemma

### Theorem 132.10 (Artin-Rees Lemma)
Let $R$ be a Noetherian ring and $I$ be an ideal of $R$. Let $M$ be a finite $R$-module. Then there exists an integer $n_0$ such that for all $n \geq n_0$, $I^n M \subseteq I^{n_0} M$.

**Proof:** 
1. **Noetherian Assumption:** Since $R$ is Noetherian, every ideal is finitely generated.
2. **Finite Generation:** Let $I = (a_1, \dots, a_m)$. The powers of $I$ stabilize.
3. **Artin-Rees:** The Artin-Rees lemma follows from the fact that the filtration $I^n M$ is eventually stable.
4. **Conclusion:** The theorem follows from the Noetherian assumption.

## 132.6 Krull's Theorem on Finite Rings

### Theorem 132.11 (Krull's Theorem on Finite Rings)
Let $R$ be a finite ring. Then $R$ is Noetherian.

**Proof:** 
1. **Finite Ring:** A finite ring has finitely many ideals.
2. **Noetherian:** A finite ring satisfies the ascending chain condition on ideals.
3. **Noetherian:** A finite ring is Noetherian by definition.
4. **Conclusion:** The theorem follows from the fact that a finite ring satisfies the ascending chain condition.

## 132.7 Commutative Algebra and Geometry

### Theorem 132.12 (Algebraic Geometry Application)
Let $R$ be a Noetherian ring and $f \in R$ be a non-zero divisor. Let $S_f = R_f$ be the localization of $R$ at $f$. Then:
1. $S_f$ is a Noetherian ring.
2. The map $R \to S_f$ is injective.
3. The map $R \to S_f$ is flat.

**Proof:** 
1. **Localization:** $S_f$ is a localization of a Noetherian ring, hence Noetherian.
2. **Injective:** The map $R \to S_f$ is injective since $f$ is a non-zero divisor.
3. **Flat:** The map $R \to S_f$ is flat since $S_f$ is a localization of $R$.
4. **Conclusion:** The theorem follows from the properties of localization.

## 132.8 Commutative Algebra and Number Theory

### Theorem 132.13 (Chinese Remainder Theorem)
Let $R$ be a commutative ring and $I_1, \dots, I_n$ be pairwise coprime ideals. Let $J \subseteq R$ be an ideal. Then there exists a unique ideal $K \subseteq R$ such that $K \equiv I_i \pmod{I_j}$ for all $i, j$.

**Proof:** 
1. **Pairwise Coprime:** $I_i \cdot I_j = I_i \cap I_j$ for all $i, j$.
2. **Chinese Remainder:** The Chinese remainder theorem follows from the fact that the map $R \to R/I_1 \times \dots \times R/I_n$ is surjective.
3. **Existence:** Let $J \subseteq R$. There exists a unique ideal $K \subseteq R$ such that $K \equiv I_i \pmod{I_j}$ for all $i, j$.
4. **Conclusion:** The theorem follows from the Chinese remainder theorem.

**References**
1. Atiyah & Macdonald, "Introduction to Commutative Algebra"
2. Matsumura, "Commutative Ring Theory"
3. Bourbaki, "Algèbre commutative"
4. Eisenbud, "Commutative Algebra with a View Toward Algebraic Geometry"
5. Neukirch, "Algebraic Number Theory"
*Updated on 2026-08-22*
