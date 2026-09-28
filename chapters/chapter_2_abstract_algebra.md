# Chapter 2: Abstract Algebra - Group Theory and Ring Theory

## 2.1 Foundations of Abstract Algebra

Abstract algebra studies algebraic structures such as groups, rings, and fields. These structures provide the foundation for much of modern mathematics.

### Theorem 2.1: Definition of a Group

**Statement**: A set $G$ together with a binary operation $\cdot: G \times G \to G$ is a group if:

1. **Closure**: For all $a, b \in G$, $a \cdot b \in G$
2. **Associativity**: For all $a, b, c \in G$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
3. **Identity**: There exists an element $e \in G$ such that for all $a \in G$, $a \cdot e = e \cdot a = a$
4. **Inverse**: For every $a \in G$, there exists an element $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$

**Proof**: This is the definition itself. A group is the most fundamental algebraic structure in mathematics. ∎

### Theorem 2.2: Cancellation Laws in Groups

**Statement**: In a group $(G, \cdot)$:

1. Left cancellation: If $a \cdot b = a \cdot c$, then $b = c$
2. Right cancellation: If $b \cdot a = c \cdot a$, then $b = c$

**Proof**: 
For left cancellation, suppose $a \cdot b = a \cdot c$. Multiply both sides on the left by $a^{-1}$:

$a^{-1} \cdot (a \cdot b) = a^{-1} \cdot (a \cdot c)$

By associativity: $(a^{-1} \cdot a) \cdot b = (a^{-1} \cdot a) \cdot c$

By identity property: $e \cdot b = e \cdot c$

By identity property: $b = c$

Similarly for right cancellation. ∎

## 2.2 Subgroups and Cosets

### Theorem 2.3: Subgroup Criteria

**Statement**: Let $G$ be a group and $H \subseteq G$. The following are equivalent:

1. $H$ is a subgroup of $G$
2. $H$ is non-empty and closed under the group operation and inverses
3. $H$ is non-empty and closed under the group operation, and for all $a, b \in H$, $ab^{-1} \in H$
4. $H$ is non-empty and for all $a, b \in H$, $ab \in H$ and $a^{-1} \in H$

**Proof**: 
The equivalence between (2) and (3) is a standard exercise in group theory. If (3) holds, then for any $a \in H$, taking $b = e$ gives $ab^{-1} = aa^{-1} = e \in H$, so $H$ is non-empty. Then $e \in H$ and $e^{-1} = e \in H$. For any $a \in H$, $ab^{-1} \in H$ implies $a \cdot e \cdot a^{-1} \in H$, which shows inverses are in $H$. Closure under operation follows from $a \cdot b = a \cdot b \cdot e^{-1} \in H$.

The equivalence between (1) and (4) is immediate from the definition of a subgroup. ∎

### Theorem 2.4: Lagrange's Theorem

**Statement**: Let $G$ be a finite group and $H$ a subgroup of $G$. Then:

$$|H| \text{ divides } |G|$$

**Proof**: 
Consider the left cosets of $H$ in $G$: $gH = \{gh : h \in H\}$ for $g \in G$. The cosets partition $G$, and all cosets have the same size $|H|$ because the map $h \mapsto gh$ is a bijection from $H$ to $gH$.

Thus, $|G| = \sum_{i} |g_i H| = \sum_{i} |H| = [G:H] \cdot |H|$, where $[G:H]$ is the number of cosets (the index of $H$ in $G$). Therefore, $|H|$ divides $|G|$. ∎

### Theorem 2.5: Coset Representation

**Statement**: The left cosets of a subgroup $H$ in $G$ are the equivalence classes under the equivalence relation: $a \sim b \iff a b^{-1} \in H$.

Similarly, the right cosets $Ha = \{h a : h \in H\}$ form the equivalence classes under $a \sim' b \iff a^{-1} b \in H$.

**Proof**: 
We need to show that $a \sim b \iff a b^{-1} \in H$ defines an equivalence relation.

- **Reflexive**: $a a^{-1} = e \in H$, so $a \sim a$.
- **Symmetric**: If $a b^{-1} \in H$, then $(a b^{-1})^{-1} = b a^{-1} \in H$, so $b \sim a$.
- **Transitive**: If $a \sim b$ and $b \sim c$, then $a b^{-1} \in H$ and $b c^{-1} \in H$. Then $(a b^{-1})(b c^{-1}) = a c^{-1} \in H$, so $a \sim c$.

Similarly for right cosets. ∎

## 2.3 Homomorphisms and Isomorphisms

### Theorem 2.6: Group Homomorphism Definition

**Statement**: A function $\phi: G \to H$ between two groups $(G, \cdot)$ and $(H, \cdot)$ is a homomorphism if for all $a, b \in G$:

$$\phi(a \cdot b) = \phi(a) \cdot \phi(b)$$

**Proof**: This is the definition of a group homomorphism. ∎

### Theorem 2.7: Kernel and Image of a Homomorphism

**Statement**: Let $\phi: G \to H$ be a group homomorphism. Then:

1. The kernel $\ker(\phi) = \{g \in G : \phi(g) = e_H\}$ is a normal subgroup of $G$
2. The image $\text{im}(\phi) = \phi(G)$ is a subgroup of $H$

**Proof**: 
For the kernel:
- $e_G \in \ker(\phi)$ since $\phi(e_G) = e_H$.
- If $a, b \in \ker(\phi)$, then $\phi(a b^{-1}) = \phi(a)\phi(b)^{-1} = e_H e_H^{-1} = e_H$, so $a b^{-1} \in \ker(\phi)$.
- If $a \in \ker(\phi)$, then $\phi(a^{-1}) = \phi(a)^{-1} = e_H^{-1} = e_H$, so $a^{-1} \in \ker(\phi)$.

For the image:
- $e_H \in \text{im}(\phi)$ since $\phi(e_G) = e_H$.
- If $a, b \in \text{im}(\phi)$, there exist $g_1, g_2 \in G$ such that $\phi(g_1) = a, \phi(g_2) = b$. Then $\phi(g_1 g_2) = \phi(g_1)\phi(g_2) = a b$, so $a b \in \text{im}(\phi)$.
- If $a \in \text{im}(\phi)$, there exists $g \in G$ such that $\phi(g) = a$. Then $\phi(g^{-1}) = \phi(g)^{-1} = a^{-1}$, so $a^{-1} \in \text{im}(\phi)$. ∎

### Theorem 2.8: First Isomorphism Theorem

**Statement**: Let $\phi: G \to H$ be a group homomorphism. Then:

$$G/\ker(\phi) \cong \text{im}(\phi)$$

**Proof**: 
Define $\bar{\phi}: G/\ker(\phi) \to H$ by $\bar{\phi}(g\ker(\phi)) = \phi(g)$. We need to show:

1. **Well-defined**: If $g\ker(\phi) = h\ker(\phi)$, then $g h^{-1} \in \ker(\phi)$, so $\phi(g h^{-1}) = e_H$, which means $\phi(g) = \phi(h)$.
2. **Homomorphism**: $\bar{\phi}((g\ker(\phi))(h\ker(\phi))) = \bar{\phi}(gh\ker(\phi)) = \phi(gh) = \phi(g)\phi(h) = \bar{\phi}(g\ker(\phi))\bar{\phi}(h\ker(\phi))$
3. **Injective**: $\ker(\bar{\phi}) = \{g\ker(\phi) : \phi(g) = e_H\} = \{g\ker(\phi) : g \in \ker(\phi)\} = \ker(\phi)/\ker(\phi) = \{e\}$
4. **Surjective onto $\text{im}(\phi)$**: By definition of the image.

Thus $\bar{\phi}$ is an isomorphism from $G/\ker(\phi)$ onto $\text{im}(\phi)$. ∎

## 2.4 Abelian Groups

### Theorem 2.9: Definition of Abelian Group

**Statement**: A group $G$ is abelian (commutative) if for all $a, b \in G$, $a \cdot b = b \cdot a$.

**Proof**: This is the definition of an abelian group. ∎

### Theorem 2.10: Cauchy's Theorem

**Statement**: If $G$ is a finite group and $p$ is a prime number such that $p \mid |G|$, then $G$ has a subgroup of order $p$.

**Proof**: 
Consider the action of $G$ on itself by left multiplication. The orbits of this action have size equal to the order of the elements. By the orbit-stabilizer theorem, for any $g \in G$, the size of the orbit of $g$ is $|G|/|Stab(g)|$.

Consider the set $X = \{g \in G : o(g) = p\}$. The group $G$ acts on $X$ by conjugation. For each orbit $O \subseteq X$, the size $|O|$ divides $|G|$ by the orbit-stabilizer theorem.

If $|G|$ is divisible by $p$, there must exist an orbit of size divisible by $p$. This orbit consists of elements of order $p$ that are conjugate to each other. The centralizer of any such element has order divisible by $p$, and by Cauchy's theorem for abelian groups (which we prove below), there exists a subgroup of order $p$.

For the abelian case, consider the set $S = \{g \in G : g^p = e\}$. Since $G$ is abelian, $S$ is a subgroup of $G$ (closed under multiplication and inverses). If $|S| > 1$, there exists $g \in S \setminus \{e\}$, and the subgroup $\langle g \rangle$ has order dividing $p$. Since $p$ is prime, $|\langle g \rangle| = p$. ∎

## 2.5 Ring Theory

### Theorem 2.11: Definition of a Ring

**Statement**: A set $R$ together with two binary operations $+$ and $\cdot: R \times R \to R$ is a ring if:

1. $(R, +)$ is an abelian group with identity element $0_R$
2. $(R, \cdot)$ is a semigroup (closed and associative)
3. Distributivity: $a \cdot (b + c) = a \cdot b + a \cdot c$ and $(a + b) \cdot c = a \cdot c + b \cdot c$

**Proof**: This is the definition of a ring. ∎

### Theorem 2.12: Ring Homomorphism Definition

**Statement**: A function $\phi: R \to S$ between two rings $(R, +_R, \cdot_R)$ and $(S, +_S, \cdot_S)$ is a ring homomorphism if for all $a, b \in R$:

1. $\phi(a +_R b) = \phi(a) +_S \phi(b)$
2. $\phi(a \cdot_R b) = \phi(a) \cdot_S \phi(b)$
3. $\phi(0_R) = 0_S$

**Proof**: This is the definition of a ring homomorphism. ∎

### Theorem 2.13: Ideal Definition

**Statement**: An ideal $I$ of a ring $R$ is a subset $I \subseteq R$ such that:

1. $I$ is an additive subgroup of $R$
2. For all $r \in R$ and $i \in I$, both $r \cdot i \in I$ and $i \cdot r \in I$

If $R$ is commutative, the second condition simplifies to: for all $r \in R$ and $i \in I$, $r \cdot i \in I$.

**Proof**: An ideal is a generalization of a subgroup where elements from the larger ring can multiply elements from the subgroup and stay in the subgroup. ∎

### Theorem 2.14: Ring Structure on Polynomials

**Statement**: The set of polynomials $R[x]$ with coefficients in a ring $R$ forms a ring under polynomial addition and multiplication.

**Proof**: 
We need to verify all the ring axioms:

1. **Additive group**: Polynomial addition is commutative and associative, and every polynomial has an additive inverse (negative of each coefficient). The zero polynomial is the additive identity.
2. **Associative multiplication**: Polynomial multiplication is associative.
3. **Distributivity**: $(A + B)C = AC + BC$ and $C(A + B) = CA + CB$ hold for polynomials.

Thus $R[x]$ is a ring. ∎

## 2.6 Field Theory

### Theorem 2.15: Definition of a Field

**Statement**: A ring $F$ is a field if:

1. $(F, +)$ is an abelian group
2. $(F \setminus \{0\}, \cdot)$ is an abelian group
3. Distributivity holds: $a \cdot (b + c) = a \cdot b + a \cdot c$

**Proof**: This is the definition of a field. A field is a commutative ring in which every non-zero element has a multiplicative inverse. ∎

### Theorem 2.16: Division Ring (Skew Field)

**Statement**: A division ring (or skew field) is a ring $D$ such that:

1. $(D, +)$ is an abelian group
2. $(D \setminus \{0\}, \cdot)$ is a group (not necessarily commutative)
3. Distributivity holds

**Proof**: In a division ring, not all elements necessarily commute under multiplication, so $a \cdot b \neq b \cdot a$ is possible. Examples include the quaternions. ∎

### Theorem 2.17: Quaternions

**Statement**: The quaternions $H = \{a + bi + cj + dk : a, b, c, d \in \mathbb{R}\}$ form a division ring with multiplication defined by:

- $i^2 = j^2 = k^2 = -1$
- $ij = k, ji = -k$
- $jk = i, kj = -i$
- $ki = j, ik = -j$

**Proof**: 
Quaternion multiplication is associative but not commutative. Every non-zero quaternion has a multiplicative inverse:

If $q = a + bi + cj + dk$, then $q^{-1} = \frac{\bar{q}}{|q|^2} = \frac{a - bi - cj - dk}{a^2 + b^2 + c^2 + d^2}$

This shows $H$ is a division ring (skew field). ∎

### Theorem 2.18: Algebraic Closure of $\mathbb{C}$

**Statement**: The complex numbers $\mathbb{C}$ form an algebraically closed field, meaning every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof**: 
This is the Fundamental Theorem of Algebra, proven earlier in the Complex Numbers chapter using Liouville's Theorem. ∎

## Exercises

### Exercise 2.1
Prove that the set of even integers $2\mathbb{Z}$ is not a group under multiplication.

**Solution**: 
$2\mathbb{Z} = \{\dots, -4, -2, 0, 2, 4, \dots\}$. The element $2$ has no multiplicative inverse in $2\mathbb{Z}$ since $1/2 \notin 2\mathbb{Z}$. Thus $2\mathbb{Z}$ is not a group. ∎

### Exercise 2.2
Show that the symmetric group $S_3$ has order $6$ and is non-abelian.

**Solution**: 
$S_3 = \{e, (1 2), (1 3), (2 3), (1 2 3), (1 3 2)\}$ has $3! = 6$ elements. Since $(1 2)(1 3) = (1 3 2)$ but $(1 3)(1 2) = (1 2 3)$, $S_3$ is non-abelian. ∎

### Exercise 2.3
Prove that if $G$ is a finite group and $H \leq G$, then $|G| = |H| \cdot [G:H]$.

**Proof**: 
This is the statement of Lagrange's Theorem with the index $[G:H]$ being the number of cosets. Since cosets partition $G$ and all have size $|H|$, we have $|G| = [G:H] \cdot |H|$. ∎

### Exercise 2.4
Show that $\mathbb{Z}[2i] = \{a + bi : a, b \in \mathbb{Z}, b = 0 \text{ or } b = \pm 2\}$ is a ring but not a domain.

**Solution**: 
$\mathbb{Z}[2i]$ is closed under addition and multiplication. However, $(2i)(-2i) = -4i^2 = 4$, but $(2i) + (-2i) = 0$, so it's not a domain. ∎

### Exercise 2.5
Prove that the quotient ring $\mathbb{Z}/n\mathbb{Z}$ has $n$ elements and is a ring for every integer $n \geq 1$.

**Proof**: 
The cosets of $n\mathbb{Z}$ in $\mathbb{Z}$ are represented by $\{0, 1, 2, \dots, n-1\}$. Addition and multiplication are well-defined modulo $n$, making $\mathbb{Z}/n\mathbb{Z}$ a ring. ∎

### Exercise 2.6
Show that the set of real numbers $\mathbb{R}$ with operation $a \oplus b = a + b - 1$ and $a \otimes b = ab$ forms a group.

**Solution**: 
Identity is $e = 1$ (since $a \oplus 1 = a + 1 - 1 = a$). Inverse is $1 - a$. The operation is associative and commutative. ∎

### Exercise 2.7
Prove that if $G$ is a cyclic group of order $n$, then $G$ is abelian.

**Solution**: 
Let $G = \langle a \rangle = \{a^0, a^1, \dots, a^{n-1}\}$. Any two elements are powers of $a$, and powers of $a$ commute. ∎

### Exercise 2.8
Show that the matrix ring $M_2(\mathbb{R})$ is non-commutative.

**Solution**: 
Let $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$. Then $AB = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ but $BA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$. Thus $AB \neq BA$. ∎

## 2.7 Advanced Topics in Ring Theory

### Theorem 2.19: Noetherian Rings

**Statement**: A commutative ring $R$ is Noetherian if every ideal in $R$ is finitely generated.

**Proof**: 
A ring is Noetherian if and only if it satisfies the ascending chain condition on ideals. ∎

### Theorem 2.20: Principal Ideal Domains

**Statement**: A ring $R$ is a Principal Ideal Domain (PID) if every ideal in $R$ is principal (generated by a single element).

**Proof**: 
Every PID is a unique factorization domain (UFD). $\mathbb{Z}$, $\mathbb{Q}[x]$, $\mathbb{Z}[x]$ (not a PID), $\mathbb{F}_p[x]$ are examples of PIDs. ∎

### Theorem 2.21: Unique Factorization Domain

**Statement**: An integral domain $R$ is a UFD if every non-zero, non-unit element can be written as a product of irreducible elements, and this factorization is unique up to order and units.

**Proof**: 
A UFD is not necessarily a PID (e.g., $\mathbb{Z}[x]$). However, every PID is a UFD. ∎

### Theorem 2.22: Euclidean Domain

**Statement**: A ring $R$ is a Euclidean domain if there exists a function $d: R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$ such that for all $a, b \in R$ with $b \neq 0$, there exist unique $q, r \in R$ such that $a = bq + r$ and either $r = 0$ or $d(r) < d(b)$.

**Proof**: 
Every Euclidean domain is a PID. Examples include $\mathbb{Z}$, $F[x]$, and Gaussian integers $\mathbb{Z}[i]$. ∎

## 2.9 Additional Theorems and Extensions

### Theorem 2.23: Group Theory in Cryptography

**Statement**: The Diffie-Hellman key exchange protocol relies on the discrete logarithm problem in finite cyclic groups.

**Proof**: 
Given a large prime $p$ and generator $g$ of $\mathbb{Z}_p^*$, two parties choose $a, b \in \mathbb{Z}_{p-1}$ and exchange $A = g^a \bmod p$ and $B = g^b \bmod p$. The shared key is $g^{ab} \bmod p$, computed as $A^b \bmod p$ or $B^a \bmod p$. The security relies on the difficulty of computing $a$ from $A$. ∎

### Theorem 2.24: Galois Theory

**Statement**: Galois theory establishes a correspondence between field extensions and subgroups of their Galois groups.

**Proof**: 
Let $E/F$ be a finite Galois extension. There is a bijection between:
- Intermediate fields $F \subseteq K \subseteq E$
- Subgroups $G \subseteq \text{Gal}(E/F)$

This correspondence reverses inclusion: larger fields correspond to smaller subgroups. ∎

## Conclusion

Abstract algebra provides the framework for understanding the structure of algebraic systems. Groups, rings, and fields form the bedrock of much of modern mathematics, with applications in cryptography, coding theory, and many other fields. The fundamental theorems of algebra, group theory, and ring theory provide deep insights into the structure of these systems and their relationships.

### Theorem 2.25: First Isomorphism Theorem for Groups

**Statement**: Let $G$ and $H$ be groups, and $\phi: G \to H$ be a group homomorphism. Then:

$$G / \ker(\phi) \cong \text{im}(\phi)$$

**Proof**: 
Define $\psi: G / \ker(\phi) \to \text{im}(\phi)$ by $\psi(g\ker(\phi)) = \phi(g)$. This is well-defined since if $g\ker(\phi) = g'\ker(\phi)$, then $g^{-1}g' \in \ker(\phi)$, so $\phi(g^{-1}g') = e_H$, which means $\phi(g)^{-1}\phi(g') = e_H$, so $\phi(g) = \phi(g')$.

$\psi$ is a homomorphism: $\psi(g\ker(\phi) \cdot g'\ker(\phi)) = \psi(gg'\ker(\phi)) = \phi(gg') = \phi(g)\phi(g') = \psi(g\ker(\phi))\psi(g'\ker(\phi))$.

$\psi$ is surjective onto $\text{im}(\phi)$ by definition.

$\ker(\psi) = \{g\ker(\phi) : \phi(g) = e_H\} = \{g\ker(\phi) : g \in \ker(\phi)\} = \ker(\phi)\ker(\phi) = \ker(\phi)$.

Thus by the First Isomorphism Theorem, $G / \ker(\phi) \cong \text{im}(\phi)$. ∎

### Theorem 2.26: Fundamental Theorem of Homomorphisms

**Statement**: Let $\phi: G \to H$ be a surjective homomorphism. Let $K$ be a subgroup of $H$. Then:

$$\phi^{-1}(K) / \ker(\phi) \cong K$$

**Proof**: 
Define $\psi: \phi^{-1}(K) / \ker(\phi) \to K$ by $\psi(g\ker(\phi)) = \phi(g)$. This is well-defined since if $g \in \phi^{-1}(K)$, then $\phi(g) \in K$. If $g'\ker(\phi) = g\ker(\phi)$, then $g^{-1}g' \in \ker(\phi)$, so $\phi(g^{-1}g') = e_H$, which means $\phi(g') = \phi(g) \in K$.

$\psi$ is a homomorphism and bijective onto $K$. ∎

### Theorem 2.27: Homomorphisms from Cyclic Groups

**Statement**: Let $G = \langle g \rangle$ be a cyclic group. For any subgroup $H \subseteq G$, there exists a unique homomorphism $\phi: G \to \mathbb{Z}$ such that $\phi(g) = 1$.

**Proof**: 
For any homomorphism $\phi: G \to \mathbb{Z}$, $\phi(g^n) = \phi(g)^n = 1^n = 1$. Since $G$ is generated by $g$, this uniquely determines $\phi$ on all elements. ∎

### Theorem 2.28: Product of Cyclic Groups

**Statement**: Let $n_1, \dots, n_k \in \mathbb{N}$. Then:

$$\mathbb{Z}/n_1\mathbb{Z} \times \cdots \times \mathbb{Z}/n_k\mathbb{Z} \cong \mathbb{Z}/(n_1 \times \cdots \times n_k)\mathbb{Z}$$

**Proof**: 
The isomorphism follows from the Chinese Remainder Theorem when $n_1, \dots, n_k$ are pairwise coprime. In general, the structure depends on the prime factorization of the $n_i$. ∎

### Theorem 2.29: Structure of Finite Abelian Groups

**Statement**: Every finite abelian group $G$ is isomorphic to a direct sum of cyclic groups:

$$G \cong \mathbb{Z}/n_1\mathbb{Z} \times \cdots \times \mathbb{Z}/n_k\mathbb{Z} \quad \text{or} \quad G \cong \mathbb{Z}/p_1^{e_1}\mathbb{Z} \times \cdots \times \mathbb{Z}/p_m^{e_m}\mathbb{Z}$$

**Proof**: 
The Fundamental Theorem of Finite Abelian Groups states this result, proved using the structure of finitely generated modules over a PID. ∎

### Theorem 2.30: Sylow's Theorems (Statement)

**Statement**: Let $G$ be a finite group of order $|G| = p^n \cdot m$ where $p$ is prime, $p \nmid m$. Then:

1. $G$ has at least one subgroup of order $p^n$ (a Sylow $p$-subgroup).
2. All Sylow $p$-subgroups are conjugate.
3. The number $n_p$ of Sylow $p$-subgroups satisfies:
   - $n_p$ divides $m$.
   - $n_p \equiv 1 \pmod{p}$.

**Proof**: 
The proof involves constructing Sylow $p$-subgroups via transitive actions on sets of $p$-subgroups and applying the orbit-stabilizer theorem. ∎

## 2.10 Ring Theory Extensions

### Theorem 2.31: Ring Definition

**Statement**: A ring $R$ is a set equipped with two binary operations $+$ and $\cdot$ such that:
1. $(R, +)$ is an abelian group.
2. $(R, \cdot)$ is a semigroup (associative operation).
3. $\cdot$ distributes over $+$: $a(b+c) = ab+ac$ and $(b+c)a = ba+ca$.

**Proof**: This is the definition of a ring. ∎

### Theorem 2.32: Subring Criteria

**Statement**: Let $R$ be a ring and $S \subseteq R$. Then $S$ is a subring of $R$ if and only if:
1. $0_R \in S$.
2. For all $a, b \in S$, $a-b \in S$.
3. For all $a, b \in S$, $a \cdot b \in S$.

**Proof**: If these conditions hold, $(S, +)$ is a subgroup of $(R, +)$ by conditions 1 and 2. Condition 3 ensures $S$ is closed under ring multiplication. ∎

### Theorem 2.33: Ideal Definitions

**Statement**: Let $R$ be a ring and $I \subseteq R$. Then $I$ is a left ideal of $R$ if:
1. $I$ is a subring of $R$ (contains 0, closed under subtraction and multiplication).
2. For all $r \in R$ and $i \in I$, $ri \in I$.

**Statement**: $I$ is a two-sided ideal if $I$ is both a left and right ideal.

**Statement**: $I$ is a proper ideal if $I \neq R$.

**Proof**: These are the standard definitions in ring theory. ∎

### Theorem 2.34: Maximal Ideals and Fields

**Statement**: Let $R$ be a commutative ring with unity. The following are equivalent:
1. $R$ is a field.
2. Every ideal $I$ of $R$ is either $\{0\}$ or $R$.
3. $R$ has no proper non-zero ideals.

**Proof**: 
- (1) ⇒ (2): Let $I$ be an ideal. If $I \neq \{0\}$, let $0 \neq a \in I$. Since $R$ is a field, $a$ has an inverse $a^{-1} \in R$, so $a^{-1}a = 1 \in I$. Thus $1 \in I$, so $R \subseteq I$, i.e., $I = R$.
- (2) ⇒ (3): Trivial implication.
- (3) ⇒ (1): Let $a \in R$ with $a \neq 0$. Consider the ideal $I = \langle a \rangle$. If $I \neq R$, then $I = \{0\}$, so $a = 0$, a contradiction. Thus $I = R$, so $1 \in \langle a \rangle$, i.e., there exist $r_1, \dots, r_n \in R$ such that $ar_1 + \cdots + ar_n = 1$. Taking $n = 1$, $a \cdot 1 = a$ gives $a = 0$, a contradiction. Thus $R$ is a field. ∎

### Theorem 2.35: Noetherian Rings

**Statement**: A ring $R$ is Noetherian if and only if:
1. Every ideal of $R$ is finitely generated.
2. Every ascending chain of ideals $I_1 \subseteq I_2 \subseteq \cdots$ stabilizes.
3. Every non-empty subset of the set of ideals of $R$ has a maximal element.

**Proof**: 
This is the ascending chain condition (ACC) equivalent to the definition of a Noetherian ring. ∎

### Theorem 2.36: Principal Ideal Domains

**Statement**: An integral domain $R$ is a principal ideal domain (PID) if and only if every ideal of $R$ is generated by a single element.

**Proof**: 
By definition, a PID is an integral domain in which every ideal is principal. ∎

### Theorem 2.37: Euclidean Domains

**Statement**: Every Euclidean domain is a PID. A Euclidean domain is an integral domain $R$ equipped with a Euclidean function $d: R \setminus \{0\} \to \mathbb{N}$ such that for any $a, b \in R$ with $b \neq 0$, there exist $q, r \in R$ such that:

$$a = bq + r \quad \text{where } r = 0 \text{ or } d(r) < d(b)$$

**Proof**: 
Given $a, b \in R$ with $b \neq 0$, the division algorithm yields a remainder $r$. If $R$ has the Euclidean function $d$, then every ideal $I$ has a minimal element with respect to $d$. Let $d$ be a principal ideal $I$. If $I$ is minimal, then $I = \langle d \rangle$. ∎

### Theorem 2.38: Polynomial Rings

**Statement**: Let $R$ be a commutative ring with unity. Then:
1. If $R$ is an integral domain, then $R[x]$ is an integral domain.
2. If $R$ is a field, then $R[x]$ is not a field (unless $x$ is a unit).
3. If $R$ is a PID, then $R[x]$ is not necessarily a PID.

**Proof**: 
- (1): Let $f, g \in R[x]$ with $f \neq 0$ and $g \neq 0$. Let $f$ have leading coefficient $a_n \neq 0$ and $g$ have leading coefficient $b_m \neq 0$. Then $fg$ has leading term $a_n b_m x^{n+m}$, and $a_n b_m \neq 0$ since $R$ is an integral domain.
- (2): The element $x$ has no multiplicative inverse in $R[x]$ since any product of polynomials has degree at least the sum of their degrees.
- (3): The ring $\mathbb{Z}[x]$ is not a PID. ∎

### Theorem 2.39: Noetherian Rings and Polynomial Rings

**Statement**: If $R$ is a Noetherian ring, then $R[x]$ is a Noetherian ring.

**Proof**: 
This is the Hilbert Basis Theorem. If $R$ is Noetherian, then every ideal in $R[x]$ has a finite set of generators. ∎

### Theorem 2.40: Quotient Rings

**Statement**: Let $R$ be a ring and $I$ an ideal of $R$. Then the quotient ring $R/I$ is a ring with operations:

$$(a + I) + (b + I) = (a + b) + I$$
$$(a + I) \cdot (b + I) = (a \cdot b) + I$$

**Proof**: 
These operations are well-defined because $I$ is an ideal: for any $i, j \in I$, $(a + i) + (b + j) = (a + b) + (i + j) \in (a + b) + I$, and $(a + i)(b + j) = ab + (aj + ib + ij) \in (ab) + I$ because $aj, ib, ij \in I$. ∎

### Theorem 2.41: Homomorphism of Quotient Rings

**Statement**: Let $R$ be a ring, $I$ an ideal of $R$, and $S$ a ring. Let $\phi: R \to S$ be a ring homomorphism such that $\phi(I) = \{0_S\}$. Then there exists a unique ring homomorphism $\bar{\phi}: R/I \to S$ such that the following diagram commutes:

$$\begin{array}{ccc}
&R/I & \ \\
&\downarrow{\bar{\phi}} & \ \\
&S & \ \\
&R & \ \\
&\downarrow{\pi} & \ \\
&S & \end{array}$$

**Proof**: 
Define $\bar{\phi}(a + I) = \phi(a)$. This is well-defined: if $a + I = b + I$, then $a - b \in I$, so $\phi(a - b) = \phi(a) - \phi(b) = 0$, so $\phi(a) = \phi(b)$.

$\bar{\phi}$ is a ring homomorphism: $\bar{\phi}((a + I) + (b + I)) = \bar{\phi}((a + b) + I) = \phi(a + b) = \phi(a) + \phi(b) = \bar{\phi}(a + I) + \bar{\phi}(b + I)$, and $\bar{\phi}((a + I) \cdot (b + I)) = \bar{\phi}(ab + I) = \phi(ab) = \phi(a)\phi(b) = \bar{\phi}(a + I)\bar{\phi}(b + I)$.

Uniqueness follows from the requirement that $\bar{\phi} \circ \pi = \phi$. ∎

### Theorem 2.42: First Isomorphism Theorem for Rings

**Statement**: Let $R$ and $S$ be rings, and $\phi: R \to S$ be a ring homomorphism. Then:

$$R / \ker(\phi) \cong \text{im}(\phi)$$

**Proof**: 
This follows from the First Isomorphism Theorem for groups, noting that a ring homomorphism is also a group homomorphism. ∎

### Theorem 2.43: Applications of Abstract Algebra

**Statement**: The Diffie-Hellman key exchange protocol relies on the discrete logarithm problem in finite cyclic groups.

**Proof**: 
Given a large prime $p$ and generator $g$ of $\mathbb{Z}_p^*$, two parties choose $a, b \in \mathbb{Z}_{p-1}$ and exchange $A = g^a \bmod p$ and $B = g^b \bmod p$. The shared key is $g^{ab} \bmod p$, computed as $A^b \bmod p$ or $B^a \bmod p$. The security relies on the difficulty of computing $a$ from $A$. ∎

### Theorem 2.44: Galois Theory

**Statement**: Galois theory establishes a correspondence between field extensions and subgroups of their Galois groups.

**Proof**: 
Let $E/F$ be a finite Galois extension. There is a bijection between:
- Intermediate fields $F \subseteq K \subseteq E$
- Subgroups $G \subseteq \text{Gal}(E/F)$

This correspondence reverses inclusion: larger fields correspond to smaller subgroups. ∎

## Conclusion

Abstract algebra provides the framework for understanding the structure of algebraic systems. Groups, rings, and fields form the bedrock of much of modern mathematics, with applications in cryptography, coding theory, and many other fields. The fundamental theorems of algebra, group theory, and ring theory provide deep insights into the structure of these systems and their relationships.
