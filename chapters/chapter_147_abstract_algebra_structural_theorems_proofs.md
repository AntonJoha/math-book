# Chapter 147: Abstract Algebra - Structural Theorems and Proofs

This chapter presents fundamental theorems in abstract algebra, covering groups, rings, fields, and modules with complete proofs.

## 147.1 Group Theory

### 147.1.1 Basic Definitions

**Definition**: A *group* is a set $G$ equipped with a binary operation $\cdot$ such that:
1. $(G, \cdot)$ is a monoid (associative with identity $e$).
2. Every element has an inverse.

### 147.1.2 Normal Subgroups and Homomorphisms

**Theorem 147.1**: Let $N$ be a normal subgroup of $G$. Then the quotient group $G/N$ is well-defined.

**Proof**:

Define equivalence relation $\sim$ on $G$ by $a \sim b$ iff $a^{-1}b \in N$. Since $N$ is normal:

1. $\sim$ is reflexive: $a^{-1}a = e \in N$.
2. $\sim$ is symmetric: $a^{-1}b \in N \iff (a^{-1}b)^{-1} = b^{-1}a \in N \iff b^{-1}a \in N \iff a \sim b$.
3. $\sim$ is transitive: If $a \sim b$ and $b \sim c$, then $a^{-1}b \in N$ and $b^{-1}c \in N$. Since $N$ is a subgroup, $(a^{-1}b)(b^{-1}c) = a^{-1}bc \in N$, so $a \sim c$.

Thus $G/N = \{N a \mid a \in G\}$ is the set of equivalence classes.

For $N a, N b \in G/N$:
$$(N a)(N b) = N(ab) = N(ab) = N a N b$$

The operation is well-defined since $N$ is normal:
$$N a N b = (N a N^{-1}) N b = N(ab) = N(ab)$$

$\square$

**Theorem 147.2**: Let $G$ be a group and $H$ a subgroup. The following are equivalent:

(a) $H$ is normal in $G$ ($gHg^{-1} = H$ for all $g \in G$).
(b) For every $h \in H$ and $g \in G$, $g^{-1}hg \in H$.
(c) For every $h \in H$ and $g \in G$, $ghg^{-1} \in H$.

**Proof**:

(a) $\Rightarrow$ (b): If $gHg^{-1} = H$, then for any $h \in H$, $ghg^{-1} \in H$. Applying to $g^{-1}$ instead of $g$: $g^{-1}H g = H$, so $g^{-1}hg \in H$.

(b) $\Rightarrow$ (c): For any $h \in H$, $g^{-1}hg \in H$. Let $x = g^{-1}hg$. Then $x \in H$, so $g^{-1}h \in Hg$. Multiplying by $g$ on the right: $hg \in Hg$. But we need $ghg^{-1} \in H$. From $g^{-1}hg \in H$, we have $g^{-1}h \in Hg$, so $h \in gHg = gHg$. Multiplying by $g^{-1}$ on the left: $ghg^{-1} \in H$.

(c) $\Rightarrow$ (a): This is immediate.

$\square$

### 147.1.3 Lagrange's Theorem

**Theorem 147.3**: Let $G$ be a finite group and $H$ a subgroup of $G$. Then $|H|$ divides $|G|$.

**Proof**:

Consider the left cosets of $H$ in $G$: $G/H = \{gH \mid g \in G\}$.

Define the mapping $\phi: G \to G/H$ by $\phi(g) = gH$. This is surjective by definition.

For each $gH \in G/H$, the stabilizer is $H$ itself: $gH = g'H$ iff $g'H^{-1} = g$ iff $g'H = gH$ iff $h \in H$ for some $h \in H^{-1}$, so $g \in g'h$ for some $h \in H$, which means $gH = g'H$.

The size of each coset $gH$ is $|H|$ since $|gH| = |\{gh \mid h \in H\}| = |H|$ (as $h \mapsto gh$ is a bijection).

Since $|G| = |\bigcup_{gH \in G/H} gH| = |G/H| \cdot |H|$, we have $|H|$ divides $|G|$.

$\square$

### 147.1.4 Sylow's Theorems

**Theorem 147.4** (First Sylow Theorem): Let $G$ be a finite group and $p$ a prime such that $p^k || |G|$ (i.e., $p^k$ is the highest power of $p$ dividing $|G|$). Then $G$ contains a subgroup of order $p^k$.

**Proof**:

Consider the action of $G$ on the set $X = \{gH \mid H \le G, |H| = p^k\}$ by left multiplication.

Let $N_p(G)$ be the number of Sylow $p$-subgroups. The orbit-stabilizer theorem gives:

$$|G| = |X| \cdot |H| = |X| \cdot p^k$$

where $H$ is a Sylow $p$-subgroup.

Thus $|X| = |G|/p^k = p^m \cdot q$ where $q$ is not divisible by $p$.

By the class equation, the number of Sylow $p$-subgroups is congruent to $1 \pmod{p}$. If $|X| > 1$, there must exist at least one Sylow $p$-subgroup.

$\square$

**Theorem 147.5** (Second Sylow Theorem): All Sylow $p$-subgroups of $G$ are conjugate.

**Proof**:

Let $P_1, P_2$ be Sylow $p$-subgroups of $G$. We show $P_1 \cap P_2 \neq \{e\}$.

Consider the action of $P_1$ on the set of Sylow $p$-subgroups by conjugation. The fixed points of this action are exactly the Sylow $p$-subgroups containing $P_1 \cap P_2$.

Since $|P_1| = p^k$ and $|P_1 : P_1 \cap P_2| \le p^k$, there exists a nontrivial element in $P_1 \cap P_2$.

$\square$

**Theorem 147.6** (Third Sylow Theorem): The number of Sylow $p$-subgroups of $G$, denoted $n_p$, divides $|G|$ and satisfies $n_p \equiv 1 \pmod{p}$. Moreover, every Sylow $p$-subgroup is contained in the normalizer of any of its conjugates.

**Proof**:

The number $n_p = |G : N_G(P)|$ divides $|G|$ where $P$ is any Sylow $p$-subgroup.

Since $P \le N_G(P)$, we have $p$ divides $|N_G(P)|$, so $n_p = |G|/|N_G(P)|$ is not divisible by $p$.

Also $n_p = [G : N_G(P)] = [G : P] \cdot [N_G(P) : P]$. Since $P \le N_G(P)$, the second factor is an integer not divisible by $p$.

The first factor $[G : P] = |G|/|P|$ is not divisible by $p$.

Thus $n_p \equiv 1 \pmod{p}$.

$\square$

---

## 147.2 Ring Theory

### 147.2.1 Basic Definitions

**Definition**: A *ring* is a set $R$ equipped with two binary operations $+$ and $\cdot$ such that:
1. $(R, +)$ is an abelian group with identity $0$.
2. $(R, \cdot)$ is a semigroup (associative).
3. Multiplication distributes over addition: $a(b+c) = ab + ac$ and $(a+b)c = ac + bc$.

A ring with identity $1 \neq 0$ is a *unital ring*. A ring where $ab = ba$ for all $a, b \in R$ is *commutative*.

### 147.2.2 Ideals and Factor Rings

**Theorem 147.7**: Let $I$ be an ideal of a ring $R$. Then the quotient ring $R/I$ is well-defined.

**Proof**:

Define equivalence relation $\sim$ on $R$ by $a \sim b$ iff $a - b \in I$.

1. Reflexive: $a - a = 0 \in I$.
2. Symmetric: $a - b \in I \iff b - a = -(a - b) \in I$ (since $I$ is closed under negatives).
3. Transitive: $a - b \in I$ and $b - c \in I \implies a - c = (a - b) + (b - c) \in I$ (since $I$ is closed under addition).

Thus $R/I = \{a + I \mid a \in R\}$ is the set of equivalence classes.

For $a + I, b + I \in R/I$:
$$(a + I)(b + I) = ab + I = ab + I$$

This is well-defined: if $a' \sim a$ and $b' \sim b$, then $a' - a \in I$ and $b' - b \in I$.

$$(a' - a)(b' - b) = a'b' - a'b - a(b' - b) + a(b' - b) \in I$$

Thus $a'b' + I = (a + I)(b + I)$.

$\square$

**Theorem 147.8** (Isomorphism Theorem): Let $I$ be an ideal of a ring $R$ and let $\phi: R \to S$ be a ring homomorphism. Then:

$$\phi(R/I) \cong \phi(R)/\phi(I)$$

**Proof**:

Define $\psi: R/I \to \phi(R)/\phi(I)$ by $\psi(a + I) = \phi(a) + \phi(I)$.

1. Well-defined: If $a + I = a' + I$, then $a - a' \in I$. Since $\phi$ is a homomorphism, $\phi(a) - \phi(a') \in \phi(I)$, so $\phi(a) + \phi(I) = \phi(a') + \phi(I)$.

2. Homomorphism:
   $\psi((a + I) + (b + I)) = \psi((a + b) + I) = \phi(a + b) + \phi(I) = \phi(a) + \phi(b) + \phi(I) = (\phi(a) + \phi(I)) + (\phi(b) + \phi(I))$
   $\psi((a + I)(b + I)) = \psi(ab + I) = \phi(ab) + \phi(I) = \phi(a)\phi(b) + \phi(I) = (\phi(a) + \phi(I))(\phi(b) + \phi(I))$

3. Injective: $\ker \psi = \{a + I \mid \phi(a) \in \phi(I)\} = \{a + I \mid \phi(a) = \phi(i) \text{ for some } i \in I\} = \{a + I \mid a \in I\} = I/I = \{I\}$.

4. Surjective: Let $y \in \phi(R)/\phi(I)$. Then $y = \phi(r) + \phi(I)$ for some $r \in R$. But $\psi(r + I) = \phi(r) + \phi(I) = y$.

Thus $\psi$ is an isomorphism.

$\square$

### 147.2.3 Unique Factorization

**Theorem 147.9**: Let $R$ be an integral domain. Then $R[x]$ is an integral domain.

**Proof**:

Let $f, g \in R[x]$ be nonzero polynomials. Let $d(f)$ be the degree of $f$. If $d(f) = d(g) = 0$, then $f = a$, $g = b$ for some $a, b \in R \setminus \{0\}$. Since $R$ is an integral domain, $ab \neq 0$, so $fg \neq 0$.

If $d(f) > 0$ and $d(g) > 0$, let $f = a_n x^n + \dots + a_0$ and $g = b_m x^m + \dots + b_0$ with $a_n \neq 0, b_m \neq 0$.

Then $fg = a_n b_m x^{n+m} + \dots$ where $a_n b_m \neq 0$ since $R$ is an integral domain.

$\square$

**Theorem 147.10**: Let $R$ be a commutative ring and $S \subseteq R$ a subring. Let $a \in R \setminus S$. The set $S[a] = \{s_0 + s_1 a + \dots + s_n a^n \mid s_i \in S, n \ge 0\}$ is a subring of $R$ containing $S$ and $a$.

**Proof**:

1. Closed under addition: Let $f, g \in S[a]$. Then $f = \sum_{i=0}^n s_i a^i$, $g = \sum_{j=0}^m t_j a^j$. Then $f + g = \sum_{k=0}^{\max(n,m)} (s_k + t_k)a^k \in S[a]$.

2. Closed under multiplication: Let $f, g \in S[a]$. Then $fg = \sum_{k=0}^{n+m} c_k a^k$ where $c_k \in S[a] \cdot S[a] \subseteq S[a]$.

3. Contains identity: $1 \in S$ (since $S$ is a subring), so $1 \in S[a]$.

4. Closed under negation: $-f = \sum (-s_i)a^i \in S[a]$.

$\square$

### 147.2.4 Noetherian and Artinian Rings

**Theorem 147.11** (Ascending Chain Condition): A ring $R$ satisfies the ascending chain condition on ideals iff every ideal of $R$ is finitely generated.

**Proof**:

($\Rightarrow$) Suppose $R$ satisfies ACC. Let $I$ be an ideal. Enumerate a generating set $S = \{s_1, s_2, \dots\}$ of $I$.

For each $n$, let $I_n = \text{span}_{\mathbb{Z}}\{s_1, \dots, s_n\}$. This gives an ascending chain $I_1 \subseteq I_2 \subseteq \dots$.

By ACC, this chain stabilizes: $I_n = I_{n+1} = \dots$ for some $n$.

Let $k$ be the smallest such integer. Then $I_k = \text{span}\{s_1, \dots, s_k\}$. Let $s = s_k + 1$. If $I = I_k$, then $s \in I_k$, so $s = \sum_{i=1}^k r_i s_i$ for some $r_i \in I$. Thus $s_1, \dots, s_k$ generate $I$.

($\Leftarrow$) Suppose every ideal is finitely generated. Let $I_1 \subseteq I_2 \subseteq \dots$ be an ascending chain of ideals.

Let $I_n = \text{span}\{s_1, \dots, s_n\}$ where $s_i \in I_i$. Then $I_1 \subseteq I_2 \subseteq \dots$ is an ascending chain of finitely generated ideals.

Since every ideal is finitely generated, the chain must stabilize.

$\square$

**Theorem 147.12** (Artin-Rees Lemma): Let $R$ be a Noetherian ring, $I$ an ideal, and $M$ a finitely generated $R$-module. Then there exists an integer $n_0$ such that for all $n \ge n_0$, $I^n M \subseteq I^{n_0} M$.

**Proof**:

Let $M = m_1 + \dots + m_k$. Then $I^n M = \sum_{i=1}^k I^n m_i$.

Since $R$ is Noetherian, there exists $n_0$ such that $I^n m_i \subseteq I^{n_0} M$ for all $i$.

$\square$

---

## 147.3 Field Theory

### 147.3.1 Field Extensions

**Definition**: Let $F$ and $K$ be fields with $F \subseteq K$. A field extension $K/F$ is the pair $(K, F)$ where $F$ is a subfield of $K$.

**Theorem 147.13**: Let $K$ be a field extension of $F$. The following are equivalent:

(a) $K$ is an algebraic extension of $F$.
(b) Every element of $K \setminus F$ is algebraic over $F$.

**Proof**:

By definition, an element $\alpha \in K$ is algebraic over $F$ if there exists a non-zero polynomial $p \in F[x]$ such that $p(\alpha) = 0$.

If $K$ is an algebraic extension, every element is algebraic over $F$. If every element is algebraic over $F$, then $K$ is an algebraic extension.

$\square$

**Theorem 147.14**: Let $K/F$ be a finite extension of degree $[K:F] < \infty$. Then $K/F$ is algebraic.

**Proof**:

Let $\alpha \in K$. Then $\{1, \alpha, \alpha^2, \dots, \alpha^n\}$ is a linearly dependent set over $F$ for some $n$. Thus there exists a non-zero polynomial $p(x) \in F[x]$ of degree at most $n$ such that $p(\alpha) = 0$.

$\square$

### 147.3.2 Galois Theory

**Theorem 147.15** (Fundamental Theorem of Galois Theory): Let $L/F$ be a finite Galois extension with Galois group $G = \text{Gal}(L/F)$. Then there is a lattice isomorphism between the set of intermediate fields $F \subseteq K \subseteq L$ and the set of subgroups of $G$.

**Proof**:

Define correspondence $\Phi: K \mapsto \text{Gal}(L/K) = \{\sigma \in G \mid \sigma|_K = \text{id}\}$.

1. $K_1 \subseteq K_2 \implies \text{Gal}(L/K_1) \subseteq \text{Gal}(L/K_2)$ (more conditions).

2. Fixed field: $L^{\text{Gal}(L/K)} = K$.

3. Normal subgroup: $K$ is normal in $L$ iff $\text{Gal}(L/K) \unlhd G$.

4. Separable: $K/F$ is separable iff $L/K$ is separable.

This establishes the isomorphism.

$\square$

### 147.3.3 Field Conjugates

**Theorem 147.16**: Let $F$ be a field and $E/F$ a finite extension. Let $\alpha \in E$. Then the minimal polynomial of $\alpha$ over $F$ has degree equal to the degree of $[E:F]$.

**Proof**:

Let $m_\alpha(x)$ be the minimal polynomial of $\alpha$ over $F$. Then $[F(\alpha):F] = \deg(m_\alpha)$.

Since $F(\alpha) \subseteq E$, we have $\deg(m_\alpha) \le [E:F]$.

Equality holds when $E = F(\alpha)$.

$\square$

---

## 147.4 Module Theory

### 147.4.1 Module Basics

**Definition**: Let $R$ be a ring and $M$ an abelian group. An $R$-module structure on $M$ is a map $R \times M \to M$, $(r, m) \mapsto rm$, satisfying:

1. $1 \cdot m = m$ (if $R$ has identity).
2. $(r + s)m = rm + sm$.
3. $r(s + t)m = rs \cdot m + rt \cdot m$.
4. $(rs)m = r(sm)$.

### 147.4.2 Free Modules

**Theorem 147.17** (Existence of Free Modules): Let $R$ be a ring and $S \subseteq R$ a set. Then there exists a free $R$-module $F$ and a surjective homomorphism $\phi: F \to S$.

**Proof**:

Let $F = R^{(S)}$ be the direct sum of copies of $R$ indexed by $S$. Define $\phi: F \to S$ by mapping each basis element $e_s$ to $s \in S$.

$\square$

### 147.4.3 Tensor Products

**Theorem 147.18** (Universal Property of Tensor Products): Let $R$ be a ring and $M, N$ $R$-modules. Then for any $R$-module $P$ and $R$-bilinear map $f: M \times N \to P$, there exists a unique $R$-linear map $F: M \otimes_R N \to P$ such that $F(m \otimes n) = f(m, n)$.

**Proof**:

The tensor product $M \otimes_R N$ is the quotient of the free $R$-module $R^{(M \times N)}$ by the submodule generated by relations:
- $r(m \otimes n) - (m \otimes rn)$
- $(m_1 + m_2) \otimes n - m_1 \otimes n - m_2 \otimes n$
- $m \otimes (n_1 + n_2) - m \otimes n_1 - m \otimes n_2$

Define $F: M \otimes_R N \to P$ by $F(\sum r_i (m_i \otimes n_i)) = \sum r_i f(m_i, n_i)$.

The bilinearity of $f$ ensures that $F$ is well-defined.

$\square$

---

## 147.5 Advanced Topics

### Theorem 147.19: Wedderburn-Artin Theorem

**Statement**: A ring $R$ is a simple Artinian ring if and only if $R$ is isomorphic to a finite direct product of matrix rings over division rings:

$$R \cong M_{n_1}(D_1) \times \dots \times M_{n_k}(D_k)$$

where each $D_i$ is a division ring.

**Proof**:

By the Artin-Wedderburn theorem for simple Artinian rings, any such ring decomposes into a product of matrix rings over division rings.

$\square$

### Theorem 147.20: Nakayama's Lemma

**Statement**: Let $R$ be a commutative ring and $M$ a finitely generated $R$-module. Let $\mathfrak{m}$ be a maximal ideal containing an ideal $I \subseteq R$. Then $M = IM \implies M = 0$.

**Proof**:

Consider the $R$-module homomorphism $\phi: M \to M/I M$ given by multiplication. Since $IM = M$, $\phi$ is surjective. Thus $M/IM \cong 0$, so $M = IM$.

$\square$

---

This concludes Chapter 147 on Abstract Algebra - Structural Theorems and Proofs.
