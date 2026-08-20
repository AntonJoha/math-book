# Chapter 7: Ring Theory - Foundations and Structure

## 7.1 Rings and Ring Homomorphisms

### Theorem 7.1: Ring Axioms

**Statement**: A ring $R$ is a set equipped with two binary operations, addition $(+,)$ and multiplication $(\cdot)$, satisfying:

1. $(R, +)$ is an abelian group
   - Closure: $\forall a,b \in R, a+b \in R$
   - Associativity: $(a+b)+c = a+(b+c)$
   - Identity: $\exists 0 \in R, a+0 = 0+a = a$
   - Inverses: $\forall a \in R, \exists -a \in R, a+(-a) = (-a)+a = 0$
   - Commutativity: $a+b = b+a$

2. Multiplication is associative: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$

3. Multiplication distributes over addition:
   - Left distributivity: $a \cdot (b+c) = (a \cdot b) + (a \cdot c)$
   - Right distributivity: $(b+c) \cdot a = (b \cdot a) + (c \cdot a)$

**Proof**: This is a definition. ∎

### Theorem 7.2: Uniqueness of Zero Element

**Statement**: If $(R,+, \cdot)$ satisfies the ring axioms, then the additive identity is unique.

**Proof**: Suppose $0, 0' \in R$ both satisfy the identity property. Then:
$0 = 0 + 0' = 0'$ (by identity property).

Thus $0 = 0'$. ∎

### Theorem 7.3: Uniqueness of Additive Inverses

**Statement**: If $(R,+, \cdot)$ satisfies the ring axioms, then for each $a \in R$, the additive inverse $-a$ is unique.

**Proof**: Suppose $-a, -a' \in R$ are both inverses of $a$. Then:
$-a = -a + 0 = -a + (a + (-a')) = (-a + a) + (-a') = 0 + (-a') = -a'$.

Thus $-a = -a'$. ∎

### Theorem 7.4: Characteristic of a Ring

**Statement**: The characteristic of a ring $R$ is the smallest positive integer $n$ such that $n \cdot 1_R = 0$, where $1_R$ is the multiplicative identity (if it exists), or the smallest positive integer $n$ such that $n \cdot a = 0$ for all $a \in R$. If no such $n$ exists, the characteristic is 0.

**Theorem 7.4**: Let $R$ be a ring with unity $1_R$. Define $n_k = k \cdot 1_R$ (sum of $1_R$ added $k$ times). The characteristic of $R$ is:
- $\text{char}(R) = n$ if $n_k = 0$ for some positive integer $n$
- $\text{char}(R) = 0$ if $n_k \neq 0$ for all $k \in \mathbb{Z}^+$

**Proof**: Consider the sequence $1_R, 1_R + 1_R, 2 \cdot 1_R, 3 \cdot 1_R, \dots$ in $R$.

If $n_k = 0$ for some positive $k$, then by the pigeonhole principle (or basic group theory), there exists a smallest such $k$. This $k$ is the characteristic.

Conversely, if $n_k \neq 0$ for all $k$, then the sequence has no repeating element, and the characteristic is 0.

### Theorem 7.5: Integer Ring is a Domain

**Statement**: $\mathbb{Z}$ is an integral domain.

**Proof**: $\mathbb{Z}$ satisfies all ring axioms, and:
1. Multiplication is associative (inherited from definition of integers)
2. For $a, b \in \mathbb{Z}, a \neq 0, b \neq 0$, we have $a \cdot b \neq 0$.

This follows from the properties of integers. If $a \cdot b = 0$ and $a \neq 0$, then $b = 0$. ∎

### Theorem 7.6: Field Characterization

**Statement**: A commutative ring $F$ with unity $1_F \neq 0$ is a field if and only if every nonzero element has a multiplicative inverse.

**Proof**: 
($\Rightarrow$) By definition, in a field every nonzero element has a multiplicative inverse.

($\Leftarrow$) If every nonzero element has an inverse, then every nonzero element is cancellable. For $a, b \in F, a \neq 0, a \cdot b = a \cdot c$, we have $b = a^{-1} \cdot (a \cdot b) = a^{-1} \cdot (a \cdot c) = (a^{-1} \cdot a) \cdot c = 1_F \cdot c = c$.

Since every nonzero element is cancellable, $F$ is an integral domain. Since $F$ is commutative and every nonzero element is invertible, $F$ is a field. ∎

### Theorem 7.7: Ring Substructure

**Statement**: A subset $S$ of a ring $R$ is a subring if:
1. $S$ is nonempty
2. $S$ is closed under subtraction: $\forall a,b \in S, a-b \in S$
3. $S$ is closed under multiplication: $\forall a,b \in S, ab \in S$

**Proof**: Theorem 7.7 follows from Theorem 7.1. If $S$ satisfies these conditions:
1. Since $S$ is closed under subtraction, $\forall a \in S, a-a = 0 \in S$, so $0 \in S$.
2. Since $S$ is closed under subtraction, $\forall a \in S, a-0 = a \in S$. Also $\forall a \in S, 0-a = -a \in S$. So $S$ is closed under additive inverses.
3. Since $0 \in S$ and $S$ is closed under subtraction, $\forall a,b \in S, a+b = a - (-b) \in S$. So $S$ is closed under addition.
4. $(S, +)$ is an abelian group (as a subgroup of $(R, +)$).
5. $S$ is closed under multiplication (condition 3).
6. Multiplication in $S$ is associative (inherited from $R$).
7. Distributivity in $S$ holds (inherited from $R$).

Thus $S$ is a ring (and a subring of $R$). ∎

### Theorem 7.8: Polynomial Ring Construction

**Statement**: The ring of polynomials $R[x]$ with coefficients in a ring $R$ is a ring under polynomial addition and multiplication.

**Theorem 7.8**: For each $a \in R$, define $P_a(x) = a$. Then the constant polynomial ring $\mathbb{C}[x]$ is a ring under polynomial addition and multiplication.

**Proof**:
1. Polynomial addition is associative: $(A+B)+C = A+(B+C)$.
2. Polynomial addition is commutative: $A+B = B+A$.
3. The zero polynomial $P_0(x) = 0$ is the additive identity.
4. The additive inverse of $P_n(x)$ is $P_n(-x)$ where coefficients are negated.
5. Polynomial multiplication is associative: $(AB)C = A(BC)$.
6. Distributivity holds: $A(B+C) = AB+AC$.
7. If $R$ has a multiplicative identity $1_R$, then the constant polynomial $1_R$ is a multiplicative identity for $R[x]$.

Thus $R[x]$ is a ring. ∎

## 7.2 Ideals and Factor Rings

### Theorem 7.9: Ideal Definition

**Statement**: An ideal $I$ of a ring $R$ is a subset of $R$ such that:
1. $I$ is an additive subgroup of $R$
2. For all $a \in I$ and $r \in R$, $ar \in I$ and $ra \in I$ (if $R$ is commutative, $ar \in I$ suffices)

**Proof**: This is a definition. ∎

### Theorem 7.10: Principal Ideal Generation

**Statement**: For any $a \in R$, the set $\{an \mid n \in \mathbb{Z}\}$ generates the principal ideal $\langle a \rangle$ of $R$.

**Proof**: Let $\langle a \rangle = \{an \mid n \in \mathbb{Z}\}$. We need to show:
1. $\langle a \rangle$ is an additive subgroup: 
   - $0 = a \cdot 0 \in \langle a \rangle$
   - $a, b \in \langle a \rangle \implies a = am, b = bn \implies a-b = am-bn = a(m-bn) \in \langle a \rangle$
2. For all $r \in R$, $ar \in \langle a \rangle$: $ar = a(r) \in \langle a \rangle$.

Thus $\langle a \rangle$ is an ideal. ∎

### Theorem 7.11: Ideal Product

**Statement**: If $I, J$ are ideals of a ring $R$, then the set $IJ = \{\sum_{i} a_i b_i \mid a_i \in I, b_i \in J\}$ is an ideal of $R$.

**Proof**:
1. $IJ$ is an additive subgroup: 
   - $0 = 0 \cdot 0 \in IJ$
   - $a, b \in IJ \implies a = \sum a_i b_i, b = \sum c_i d_i \implies a-b = \sum a_i b_i - \sum c_i d_i \in IJ$
2. For all $r \in R$, $ar \in IJ$: Let $a = \sum a_i b_i \in IJ$. Then $ar = \sum (a_i b_i) r = \sum a_i (b_i r)$. Since $I$ is an ideal, $b_i r \in I$, so $\sum a_i (b_i r) \in IJ$.

Thus $IJ$ is an ideal. ∎

### Theorem 7.12: Factor Ring Construction

**Statement**: If $I$ is an ideal of a ring $R$, then the factor ring $R/I$ is a ring.

**Proof**: Elements of $R/I$ are cosets $r+I = \{r+i \mid i \in I\}$. Define:
1. $(r+I) + (s+I) = (r+s) + I$
2. $(r+I)(s+I) = (rs) + I$

We need to verify:
1. Addition is well-defined: If $r+I = r'+I$ and $s+I = s'+I$, then $r-r' \in I$ and $s-s' \in I$. Then $(r+s)-(r'+s') = (r-r')+(s-s') \in I$ (since $I$ is an additive subgroup), so $(r+s)+I = (r'+s')+I$. Similarly for multiplication.
2. $(R/I, +)$ is a group: 
   - Associativity: $((r+I)+(s+I))+(t+I) = (r+s+t)+I = (r+I)+((s+I)+(t+I))$
   - Identity: $0+I$ is the additive identity
   - Inverse: $-r+I$ is the additive inverse of $r+I$
   - Commutativity: $r+I+s+I = (r+s)+I = s+I+r+I$
3. Multiplication is associative: $(r+I)(s+I)(t+I) = (rs)t+I = r(st)+I$
4. Distributivity: $(r+I)((s+I)+(t+I)) = (r+I)(s+t+I) = r(s+t)+I = (rs+rt)+I = (r+I)(s+I)+(r+I)(t+I)$

Thus $R/I$ is a ring. ∎

## 7.3 Homomorphisms and Isomorphisms

### Theorem 7.13: Ring Homomorphism Definition

**Statement**: A ring homomorphism $\phi: R \to S$ is a function such that:
1. $\phi(a+b) = \phi(a) + \phi(b)$
2. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$
3. $\phi(1_R) = 1_S$ (if $R$ and $S$ have unity)

**Proof**: This is a definition. ∎

### Theorem 7.14: Kernel of Homomorphism

**Statement**: The kernel of a ring homomorphism $\phi: R \to S$ is an ideal of $R$, defined as $\ker(\phi) = \{a \in R \mid \phi(a) = 0_S\}$.

**Proof**:
1. $0 \in \ker(\phi)$ since $\phi(0_R) = 0_S$.
2. If $a, b \in \ker(\phi)$, then $\phi(a-b) = \phi(a)-\phi(b) = 0-0 = 0$, so $a-b \in \ker(\phi)$.
3. If $a \in \ker(\phi)$ and $r \in R$, then $\phi(ra) = \phi(r)\phi(a) = \phi(r) \cdot 0_S = 0_S$, so $ra \in \ker(\phi)$. Similarly $\phi(ar) = \phi(a)\phi(r) = 0$.

Thus $\ker(\phi)$ is an ideal. ∎

### Theorem 7.15: Image of Homomorphism

**Statement**: The image of a ring homomorphism $\phi: R \to S$ is a subring of $S$.

**Proof**: Let $\text{Im}(\phi) = \{\phi(a) \mid a \in R\}$. 
1. $\text{Im}(\phi)$ is closed under subtraction: If $\phi(a), \phi(b) \in \text{Im}(\phi)$, then $\phi(a)-\phi(b) = \phi(a-b) \in \text{Im}(\phi)$.
2. $\text{Im}(\phi)$ is closed under multiplication: If $\phi(a), \phi(b) \in \text{Im}(\phi)$, then $\phi(a)\phi(b) = \phi(ab) \in \text{Im}(\phi)$.

Thus $\text{Im}(\phi)$ is a subring of $S$. ∎

### Theorem 7.16: First Isomorphism Theorem

**Statement**: If $\phi: R \to S$ is a ring homomorphism, then $R/\ker(\phi) \cong \text{Im}(\phi)$.

**Theorem 7.16**: The First Isomorphism Theorem for rings states: $R/\ker(\phi) \cong \text{Im}(\phi)$.

**Proof**: 
Define $\psi: R/\ker(\phi) \to \text{Im}(\phi)$ by $\psi(r+\ker(\phi)) = \phi(r)$.

1. Well-defined: If $r+\ker(\phi) = r'+\ker(\phi)$, then $r-r' \in \ker(\phi)$, so $\phi(r-r') = 0_S$, so $\phi(r) = \phi(r')$.
2. Injective: If $\psi(r+\ker(\phi)) = 0_{\text{Im}(\phi)}$, then $\phi(r) = 0_S$, so $r \in \ker(\phi)$, so $r+\ker(\phi) = \ker(\phi)$.
3. Surjective: For any $y \in \text{Im}(\phi)$, there exists $r \in R$ such that $\phi(r) = y$, so $y = \psi(r+\ker(\phi))$.
4. Ring homomorphism: $\psi((r_1+\ker(\phi))+(r_2+\ker(\phi))) = \psi((r_1+r_2)+\ker(\phi)) = \phi(r_1+r_2) = \phi(r_1)+\phi(r_2) = \psi(r_1+\ker(\phi))+\psi(r_2+\ker(\phi))$, and similarly for multiplication.

Thus $\psi$ is an isomorphism. ∎

## 7.4 Subrings and Inclusions

### Theorem 7.17: Intersection of Ideals

**Statement**: The intersection of any collection of ideals of a ring $R$ is an ideal of $R$.

**Proof**: Let $\{I_\alpha\}_{\alpha \in A}$ be a collection of ideals of $R$, and let $I = \bigcap_{\alpha \in A} I_\alpha$.
1. $I$ is nonempty: $0 \in I_\alpha$ for all $\alpha$, so $0 \in I$.
2. $I$ is closed under subtraction: If $a, b \in I$, then $a, b \in I_\alpha$ for all $\alpha$, so $a-b \in I_\alpha$ for all $\alpha$, so $a-b \in I$.
3. $I$ is closed under multiplication by elements of $R$: If $a \in I$ and $r \in R$, then $a \in I_\alpha$ and $r \in R$, so $ar \in I_\alpha$ for all $\alpha$, so $ar \in I$.

Thus $I$ is an ideal. ∎

### Theorem 7.18: Union of Ideals (Comma Ideal)

**Statement**: The union of two ideals $I$ and $J$ of a ring $R$ is an ideal of $R$ if and only if $I \subseteq J$ or $J \subseteq I$.

**Proof**:
($\Rightarrow$) Suppose $I \cup J$ is an ideal but $I \not\subseteq J$ and $J \not\subseteq I$. Then there exists $a \in I \setminus J$ and $b \in J \setminus I$. Since $I \cup J$ is an ideal, $a+b \in I \cup J$. But $a+b \notin J$ (since $a \notin J$) and $a+b \notin I$ (since $b \notin I$), a contradiction. Thus $I \subseteq J$ or $J \subseteq I$.

($\Leftarrow$) If $I \subseteq J$, then $I \cup J = J$, which is an ideal. Similarly if $J \subseteq I$.

## 7.5 Integral Domains and Fields

### Theorem 7.19: Zero Divisors in Integral Domains

**Statement**: If $R$ is an integral domain and $ab = 0$, then $a = 0$ or $b = 0$.

**Proof**: Suppose $ab = 0$ and $a \neq 0$. Since $R$ is a domain, $a$ has no zero divisors, so $b = 0$. Similarly if $b \neq 0$, then $a = 0$.

### Theorem 7.20: Polynomial Rings over Fields

**Statement**: If $F$ is a field, then $F[x]$ is an integral domain.

**Proof**: Let $P, Q \in F[x]$ with leading coefficients $a_n, b_m \neq 0$. Then $PQ$ has leading coefficient $a_n b_m \neq 0$ (since $F$ is a field, it has no zero divisors). Thus $F[x]$ has no zero divisors and is an integral domain. ∎

### Theorem 7.21: Field Extensions

**Statement**: If $F$ is a field and $S$ is a ring containing $F$ such that $S$ is closed under addition, multiplication, and additive inverses, then $S$ is a ring extension of $F$ and $S$ is a field if and only if every nonzero element of $S$ is invertible in $S$.

**Proof**: The ring axioms for $S$ follow from the fact that $S$ contains $F$. For $S$ to be a field, we need $S$ to be commutative (which follows from $F$) and every nonzero element to be invertible. ∎

### Theorem 7.22: Gaussian Integers Form a UFD

**Statement**: The ring $\mathbb{Z}[i]$ of Gaussian integers is a unique factorization domain (UFD).

**Proof**: $\mathbb{Z}[i] \subset \mathbb{C}$. The norm $N(a+bi) = a^2+b^2$ is a multiplicative function into $\mathbb{Z}_{\geq 0}$. If $\alpha, \beta \in \mathbb{Z}[i]$ have no common factor (in the sense that no Gaussian integer divides both except units), then $N(\alpha)$ and $N(\beta)$ are coprime in $\mathbb{Z}$ (as $a^2+b^2$ is coprime to $c^2+d^2$). By the unique factorization of integers, $\mathbb{Z}[i]$ has unique factorization. ∎

### Theorem 7.23: Euler's Product Formula

**Statement**: The ring of Gaussian integers $\mathbb{Z}[i]$ is isomorphic to the quotient of $\mathbb{Z}[x]$ by the ideal generated by $x^2+1$.

**Proof**: Define $\phi: \mathbb{Z}[x] \to \mathbb{Z}[i]$ by $\phi(x^k) = i^k$. Then $\phi$ is a ring homomorphism with $\ker(\phi) = \langle x^2+1 \rangle$. The First Isomorphism Theorem gives $\mathbb{Z}[x]/\langle x^2+1 \rangle \cong \text{Im}(\phi) = \mathbb{Z}[i]$. ∎

## 7.6 Advanced Topics

### Theorem 7.24: Artin-Wedderburn Theorem

**Statement**: A ring $R$ is a finite-dimensional algebra over a field $F$ is semisimple if and only if $R \cong F_1 \times \dots \times F_n$ where each $F_i$ is a simple Artinian ring.

**Proof**: (Sketch) The proof uses representation theory and module theory. A ring $R$ is semisimple if the regular representation decomposes into a direct sum of irreducible representations. This is equivalent to $R \cong M_{n_1}(D_1) \times \dots \times M_{n_k}(D_k)$ where $D_i$ are division rings. For commutative $R$, this is just $F_1 \times \dots \times F_n$.

### Theorem 7.25: Noetherian Rings

**Statement**: A ring $R$ is Noetherian if every ideal of $R$ is finitely generated, or equivalently, if every ascending chain of ideals $I_1 \subseteq I_2 \subseteq \dots$ stabilizes.

**Proof**: These are equivalent by the Ascending Chain Condition. ∎

## 7.x Advanced Ring Theory

### Theorem 7.1: Artin-Wedderburn Theorem

**Statement**: Every finite-dimensional division algebra over a field is a field (and thus commutative).

**Proof**: Let $D$ be a finite-dimensional division algebra over a field $F$. Let $\alpha \in D$ be not in $F$. The powers $1, \alpha, \alpha^2, \dots, \alpha^n$ are linearly dependent over $F$ where $n = \dim_F(D)$. Thus there exist coefficients $c_0, \dots, c_n$ not all zero such that $\sum c_i \alpha^i = 0$. Since $D$ is a division algebra, $\alpha$ is invertible, and we can rearrange this equation to show that $\alpha$ satisfies a polynomial equation of degree $\le n$ with coefficients in $F$. This implies that $\alpha$ is algebraic over $F$, and by the primitive element theorem, $F(\alpha)$ is a finite extension of $F$. The center of $D$ is a field, and $D$ is commutative by the properties of finite extensions. ∎

### Theorem 7.2: Noetherian Rings

**Statement**: A commutative ring $R$ is Noetherian if and only if every ascending chain of ideals $I_1 \subseteq I_2 \subseteq \dots$ stabilizes.

**Proof**: This is the definition of a Noetherian ring (ascending chain condition). If the condition holds, then every ideal is finitely generated (by induction on the length of the chain). Conversely, if every ideal is finitely generated, then any ascending chain must stabilize, otherwise one would construct an infinite strictly ascending chain of finitely generated ideals, which is impossible by the properties of rings. ∎

### Theorem 7.3: Chinese Remainder Theorem

**Statement**: Let $I_1, \dots, I_n$ be ideals of a ring $R$ such that $I_i + I_j = R$ for all $i \neq j$. Then the natural map

$$R \to \prod_{i=1}^n R/I_i$$

is a ring isomorphism.

**Proof**: The map is clearly a ring homomorphism. Surjectivity follows from the fact that for each pair $i,j$, there exist $e_i \in I_i$ and $f_j \in I_j$ such that $e_i + f_j = 1$, and we can construct elements in the product that map to any given tuple. The kernel consists of elements that are in all $I_i$, which must be zero since the $I_i$ are comaximal. ∎

### Theorem 7.4: Krull's Theorem

**Statement**: Every proper ideal in a ring $R$ is contained in a maximal ideal.

**Proof**: Suppose $I$ is a proper ideal not contained in any maximal ideal. Then for every maximal ideal $M$, there exists $x \in I \setminus M$. Consider the ideal generated by $I \cup \{x\}$. By assumption, this ideal is proper, so it is contained in a maximal ideal $M'$. But $x \in M'$, contradicting that $M$ is maximal and $x \notin M$. Therefore, $I$ must be contained in a maximal ideal. ∎


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*