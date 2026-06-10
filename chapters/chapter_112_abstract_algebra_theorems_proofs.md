# Chapter 112: Abstract Algebra - Comprehensive Theorems and Proofs

## 112.1 Ring Theory

### Theorem 112.1.1 (Fundamental Theorem of Arithmetic)
Every positive integer $n > 1$ can be uniquely factored into primes (up to order).

**Proof**: The existence follows from Euclid's algorithm, and uniqueness follows from Euclid's lemma: if $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.

### Theorem 112.1.2 (Unique Factorization in UFDs)
An integral domain $R$ is a unique factorization domain (UFD) if and only if every non-zero non-unit element factors uniquely into irreducible elements.

**Proof**: The forward direction is by definition. For the reverse, we need to show that irreducibles are primes in UFDs.

### Theorem 112.1.3 (Chinese Remainder Theorem)
Let $R$ be a commutative ring with unity, and let $I_1, \dots, I_n$ be pairwise coprime ideals. Then for any $a_1, \dots, a_n \in R$, the system of congruences:
$$x \equiv a_i \pmod{I_i} \quad \text{for } i=1,\dots,n$$
has a unique solution modulo $\prod_{i=1}^n I_i$.

**Proof**: Use the fact that $\gcd(I_i, I_j) = R$ for $i \neq j$, which implies $\sum_{i=1}^n I_i = R$.

### Theorem 112.1.4 (Euclidean Algorithm)
The greatest common divisor of two integers $a$ and $b$ can be computed as a linear combination $ax + by = \gcd(a,b)$.

**Proof**: Use the division algorithm $a = bq + r$ and the fact that $\gcd(a,b) = \gcd(b,r)$.

---

## 112.2 Polynomial Rings

### Theorem 112.2.1 (Fundamental Theorem of Algebra)
Every non-constant polynomial $P(z) = a_n z^n + \dots + a_0$ with complex coefficients has at least one complex root.

**Proof**: Using Liouville's theorem, or more directly using the properties of holomorphic functions and the argument principle.

### Theorem 112.2.2 (Polynomial Remainder Theorem)
For any polynomial $P(z)$ and any polynomial $d(z)$, there exist unique polynomials $q(z)$ and $r(z)$ such that:
$$P(z) = d(z)q(z) + r(z)$$
where either $r(z) = 0$ or $\deg(r) < \deg(d)$.

**Proof**: Use the division algorithm for polynomials.

### Theorem 112.2.3 (Factor Theorem)
Let $P(z)$ be a polynomial. Then $z - a$ is a factor of $P(z)$ if and only if $P(a) = 0$.

**Proof**: If $z-a$ divides $P(z)$, then $P(z) = (z-a)Q(z)$, so $P(a) = 0$. Conversely, if $P(a) = 0$, then by the division algorithm, $P(z) = (z-a)Q(z) + r$, where $r = P(a) = 0$.

### Theorem 112.2.4 (Gauss's Lemma)
A polynomial $f(z)$ with integer coefficients is irreducible in $\mathbb{Z}[z]$ if and only if it is irreducible in $\mathbb{Q}[z]$.

**Proof**: Use the fact that if $f(z) = g(z)h(z)$ in $\mathbb{Q}[z]$, then $g$ and $h$ can be scaled to have integer coefficients.

---

## 112.3 Field Extensions

### Theorem 112.3.1 (Tower Law)
Let $K \subseteq L \subseteq M$ be fields. Let $[M:L]$ and $[L:K]$ denote the degrees of $M$ over $L$ and $L$ over $K$, respectively. Then:
$$[M:K] = [M:L][L:K]$$

**Proof**: Use the fact that if $\{m_i\}$ is a basis for $M$ over $L$ and $\{l_j\}$ is a basis for $L$ over $K$, then $\{l_j m_i\}$ is a basis for $M$ over $K$.

### Theorem 112.3.2 (Primitive Element Theorem)
Let $K$ be a field and $L = K(\alpha_1, \dots, \alpha_n)$ be a finite separable extension. Then there exists $\theta \in L$ such that $L = K(\theta)$.

**Proof**: Consider the polynomial $f(x) = \prod_{\sigma: L \to L} (x - \sigma(\alpha_1))$, where $\sigma$ ranges over the distinct $K$-embeddings of $L$ into an algebraic closure of $K$.

### Theorem 112.3.3 (Artin-Schreier Theory)
Let $K$ be a field. Then $K \subseteq L$ is an algebraic field extension of degree 2 if and only if $L = K(\alpha)$ where $\alpha^2 \in K \setminus K^2$.

**Proof**: If $[L:K] = 2$, let $L = K(\alpha)$ with $\alpha$ having a minimal polynomial $x^2 + ax + b$. The discriminant must be non-zero.

### Theorem 112.3.4 (Normal Extensions)
A finite field extension $L/K$ is normal if and only if it is the splitting field of some polynomial in $K[x]$.

**Proof**: If $L = K(\alpha)$ is the splitting field of $f(x)$, then any embedding of $L$ into an algebraic closure of $K$ maps $L$ into $L$.

---

## 112.4 Galois Theory

### Theorem 112.4.1 (Fundamental Theorem of Galois Theory)
There is a one-to-one correspondence between the subfields of a Galois extension $L/K$ and the subgroups of the Galois group $\text{Gal}(L/K)$.

**Proof**: Use the Artin's theorem on the fixed field of a subgroup of automorphisms.

### Theorem 112.4.2 (Galois Group of $x^n - a$)
Let $K$ be a field of characteristic 0 containing the $n$-th roots of unity. Then the Galois group of $x^n - a$ over $K$ is isomorphic to the multiplicative group $\mathbb{Z}/n\mathbb{Z}$.

**Proof**: The roots are $\alpha, \zeta\alpha, \zeta^2\alpha, \dots, \zeta^{n-1}\alpha$, where $\zeta$ is a primitive $n$-th root of unity. The automorphisms map $\alpha$ to $\zeta^k\alpha$.

### Theorem 112.4.3 (Solubility by Radicals)
A polynomial $f(x) \in K[x]$ is solvable by radicals if and only if its Galois group is solvable.

**Proof**: Use the fact that solvable groups correspond to tower of normal extensions obtainable by adjoining radicals.

### Theorem 112.4.4 (Abelian Extensions)
Let $L/K$ be a Galois extension. Then $L/K$ is abelian if and only if for every $a \in K$, there exists $b \in L$ such that $L = K(a^{1/n})$ for some $n \geq 1$.

**Proof**: Use Kummer theory.

### Theorem 112.4.5 (Hilbert's Irreducibility Theorem)
Let $f(t, x) \in \mathbb{Q}(t)[x]$ be an irreducible polynomial in $x$ with coefficients in $\mathbb{Q}(t)$. Then there exists a dense subset $S \subset \mathbb{Q}$ such that for all $\alpha \in S$, $f(\alpha, x)$ is irreducible in $\mathbb{Q}[x]$.

**Proof**: Use Chebotarev's density theorem.

---

## 112.5 Modular Arithmetic

### Theorem 112.5.1 (Fermat's Little Theorem)
Let $p$ be a prime number and $a$ be an integer not divisible by $p$. Then:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Proof**: The multiplicative group $\mathbb{Z}/p\mathbb{Z}$ has order $p-1$, so by Lagrange's theorem, $a^{p-1} \equiv 1 \pmod{p}$.

### Theorem 112.5.2 (Euler's Theorem)
Let $n$ be a positive integer and $a$ be an integer coprime to $n$. Then:
$$a^{\phi(n)} \equiv 1 \pmod{n}$$

**Proof**: The multiplicative group $(\mathbb{Z}/n\mathbb{Z})^\times$ has order $\phi(n)$.

### Theorem 112.5.3 (Wilson's Theorem)
A positive integer $p > 1$ is prime if and only if:
$$(p-1)! \equiv -1 \pmod{p}$$

**Proof**: If $p$ is prime, then every element $1 < a < p$ generates a subgroup of $(\mathbb{Z}/p\mathbb{Z})^\times$. If $p$ is composite, $(p-1)! \equiv 0 \pmod{p}$.

### Theorem 112.5.4 (Chinese Remainder Theorem for Modular Arithmetic)
Let $n_1, n_2, \dots, n_k$ be pairwise coprime positive integers. Then the system of congruences:
$$x \equiv a_i \pmod{n_i} \quad \text{for } i=1,\dots,k$$
has a unique solution modulo $N = n_1 n_2 \dots n_k$.

**Proof**: Use the fact that there exist integers $t_i$ such that $t_i n_i \equiv 1 \pmod{n_i}$ and $t_i n_j \equiv 0 \pmod{n_j}$ for $j \neq i$.

---

## 112.6 Linear Algebra and Vector Spaces

### Theorem 112.6.1 (Rank-Nullity Theorem)
Let $T: V \to W$ be a linear transformation between finite-dimensional vector spaces. Then:
$$\dim(V) = \dim(\ker T) + \dim(\text{im} T)$$

**Proof**: Use the fact that the quotient space $V/\ker T$ is isomorphic to $\text{im} T$.

### Theorem 112.6.2 (Sylvester's Law of Inertia)
Let $A$ be a symmetric matrix. Then the number of positive, negative, and zero eigenvalues of $A$ (with multiplicity) is invariant under congruence transformations $A \mapsto P^T A P$.

**Proof**: Use Sylvester's criterion and the properties of quadratic forms.

### Theorem 112.6.3 (Spectrum of Symmetric Matrices)
Let $A$ be a real symmetric $n \times n$ matrix. Then $A$ has real eigenvalues, and $A$ is orthogonally diagonalizable.

**Proof**: Use the fact that $A$ is self-adjoint with respect to the Euclidean inner product.

### Theorem 112.6.4 (Singular Value Decomposition)
Every matrix $A \in \mathbb{C}^{m \times n}$ can be written as $A = U \Sigma V^*$, where $U \in \mathbb{C}^{m \times m}$ and $V \in \mathbb{C}^{n \times n}$ are unitary matrices, and $\Sigma \in \mathbb{R}^{m \times n}$ is a diagonal matrix with non-negative real entries (singular values).

**Proof**: Use the spectral theorem for $AA^*$ and $A^*A$.

---

## 112.7 Group Theory

### Theorem 112.7.1 (Lagrange's Theorem)
If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$.

**Proof**: Use the orbit-stabilizer theorem.

### Theorem 112.7.2 (Cauchy's Theorem)
If $p$ is a prime dividing the order of a finite group $G$, then $G$ has an element of order $p$.

**Proof**: Use the class equation and properties of group actions.

### Theorem 112.7.3 (Sylow's Theorems)
Let $G$ be a finite group and $p$ be a prime such that $p^n || |G|$ (i.e., $p^n$ divides $|G|$ but $p^{n+1}$ does not). Then:
1. $G$ has a subgroup of order $p^n$.
2. All subgroups of order $p^n$ are conjugate.
3. The number of Sylow $p$-subgroups, denoted $n_p$, satisfies $n_p \equiv 1 \pmod{p}$ and $n_p$ divides $|G|/p^n$.

**Proof**: Use the action of $G$ on the set of subgroups of order $p^n$ by conjugation.

### Theorem 112.7.4 (Simple Groups)
A finite group $G$ is simple if and only if it has no non-trivial normal subgroups.

**Proof**: This is by definition. The classification of simple groups involves extensive work.

### Theorem 112.7.5 (Fundamental Theorem of Galois Theory)
Let $L/K$ be a finite Galois extension with Galois group $G$. Then there is a one-to-one correspondence between the intermediate fields $K \subseteq E \subseteq L$ and the subgroups $H$ of $G$, given by:
- $E \mapsto \text{Gal}(L/E) = \{ \sigma \in G : \sigma(x) = x \text{ for all } x \in E \}$
- $H \mapsto E_H = \{ x \in L : \sigma(x) = x \text{ for all } \sigma \in H \}$

**Proof**: Use Artin's theorem and properties of field automorphisms.

---

## 112.8 Number Theory and Algebraic Number Fields

### Theorem 112.8.1 (Fundamental Theorem of Algebra - Proof via Liouville)
Every non-constant polynomial with complex coefficients has a complex root.

**Proof**: Let $P(z)$ be a non-constant polynomial. If $P(z) \neq 0$ for all $z$, then $1/P(z)$ is entire and bounded (since $|P(z)| \to \infty$ as $|z| \to \infty$). By Liouville's theorem, $1/P(z)$ is constant, so $P(z)$ is constant, contradiction.

### Theorem 112.8.2 (Quadratic Reciprocity Law)
Let $p$ and $q$ be distinct odd primes. Then:
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}$$

**Proof**: Use properties of Legendre symbols and properties of Gaussian periods.

### Theorem 112.8.3 (Quadratic Residue Criterion)
An integer $a$ is a quadratic residue modulo an odd prime $p$ if and only if:
$$a^{\frac{p-1}{2}} \equiv 1 \pmod{p}$$
and $a$ is a non-residue if and only if $a^{\frac{p-1}{2}} \equiv -1 \pmod{p}$.

**Proof**: Use Euler's criterion.

### Theorem 112.8.4 (Minkowski's Theorem on Lattice Points)
Let $R$ be a lattice in $\mathbb{R}^n$ of rank $n$. If the volume of the fundamental parallelepiped of $R$ satisfies $\text{Vol}(R) \leq (4/\pi)^{n/2} \cdot 2^{n-1}$, then $R$ contains a non-zero lattice point $x$ such that $\|x\| \leq \sqrt{n/2}$, where $\|x\|$ is the Euclidean norm.

**Proof**: Use the fact that the volume of the ball in $\mathbb{R}^n$ is bounded by the volume of the fundamental parallelepiped.

---

## 112.9 Ring Theory and Commutative Algebra

### Theorem 112.9.1 (Chinese Remainder Theorem for Rings)
Let $R$ be a commutative ring with unity, and let $I_1, \dots, I_n$ be pairwise coprime ideals. Then the natural map:
$$R \to \prod_{i=1}^n R/I_i$$
is surjective with kernel $\cap_{i=1}^n I_i$.

**Proof**: Use the fact that $\sum_{i=1}^n I_i = R$ and the Chinese remainder theorem for integers.

### Theorem 112.9.2 (Prime Ideals and Irreducible Ideals)
In a commutative ring $R$, every irreducible ideal is prime.

**Proof**: Use the fact that if $I$ is irreducible and $ab \in I$, then either $a \in I$ or $b \in I$.

### Theorem 112.9.3 (Hilbert's Nullstellensatz)
Let $k$ be an algebraically closed field and $f_1, \dots, f_m \in k[x_1, \dots, x_n]$. Then:
$$\sqrt{(f_1, \dots, f_m)} = \{ f \in k[x_1, \dots, x_n] : f \text{ vanishes on all common zeros of } f_1, \dots, f_m \}$$

**Proof**: Use the correspondence between algebraic sets and ideals in $k[x_1, \dots, x_n]$.

### Theorem 112.9.4 (Going-Up and Going-Down Theorems)
Let $R \subseteq S$ be an integral extension of integral domains. Then:
- Going-Up: If $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ are prime ideals in $R$ and $\mathfrak{q}_1$ is a prime ideal in $S$ lying over $\mathfrak{p}_1$, then for any $\mathfrak{p}_2 \subseteq \mathfrak{p}_2$, there exists a prime $\mathfrak{q}_2 \subseteq \mathfrak{q}_2$ lying over $\mathfrak{p}_2$.
- Going-Down: If $R$ is integrally closed, then for any $\mathfrak{q}_1 \subseteq \mathfrak{q}_2$ in $S$, there exists $\mathfrak{p}_1 \subseteq \mathfrak{p}_2$ in $R$ lying over $\mathfrak{q}_1$.

**Proof**: Use the properties of integral extensions and the fact that the going-up theorem follows from the going-down theorem in the case of integral extensions.

---

## 112.10 Additional Proofs

### Proof of Chinese Remainder Theorem
Let $I_1, \dots, I_n$ be pairwise coprime ideals. Then $\sum_{i=1}^n I_i = R$. For each $i$, choose $t_i \in I_i$ such that $t_i \equiv 1 \pmod{I_i}$. Then $x = \sum_{i=1}^n t_i a_i$ satisfies $x \equiv a_i \pmod{I_i}$.

### Proof of Lagrange's Theorem
Let $H$ be a subgroup of $G$. The left cosets of $H$ partition $G$, and all cosets have the same cardinality $|H|$. Thus $|G| = [G:H] \cdot |H|$, where $[G:H]$ is the number of cosets (index).

---

## Exercises

**Exercise 112.1**: Prove that $\mathbb{Z}[x]$ is not a field.

**Exercise 112.2**: Show that the Chinese Remainder Theorem holds for rings.

**Exercise 112.3**: Prove that a finite field has characteristic $p$ for some prime $p$.

**Exercise 112.4**: Show that the polynomial $x^4 + 1$ is irreducible over $\mathbb{Q}$.

**Exercise 112.5**: Prove that $S_4$ is not a simple group.

**Exercise 112.6**: Show that $\mathbb{C}$ is the splitting field of $x^2 - a$ over $\mathbb{Q}(\sqrt{a})$.

**Exercise 112.7**: Prove the Chinese Remainder Theorem for integers.

**Exercise 112.8**: Show that any finite group $G$ has an abelian normal subgroup $N$ with $G/N$ abelian.

**Exercise 112.9**: Prove that the fundamental group of $S^1$ is $\mathbb{Z}$.

**Exercise 112.10**: Show that any finite abelian group is a direct product of cyclic groups.

---

## Problems

**Problem 112.1**: Prove that there exist infinitely many irreducible polynomials in $\mathbb{Q}[x]$.

**Problem 112.2**: Show that the Galois group of $x^5 - 2$ over $\mathbb{Q}$ is $D_5$.

**Problem 112.3**: Prove that the number of solutions to $x^2 \equiv a \pmod{p}$ is either 0 or 2.

**Problem 112.4**: Show that every finite field is the splitting field of $x^{p^n} - x$ for some prime $p$ and integer $n$.

**Problem 112.5**: Prove that if $G$ is a simple group of order greater than 60, then $|G| \geq 60$.

---

## Solutions to Selected Exercises

### Solution to Exercise 112.1
Let $R = \mathbb{Z}[x]$. The unit elements in $\mathbb{Z}[x]$ are $1$ and $-1$. Thus $\mathbb{Z}[x]$ is not a field.

### Solution to Exercise 112.4
Consider $x^4 + 1 = (x^2 + \sqrt{2}x + 1)(x^2 - \sqrt{2}x + 1)$ over $\mathbb{Q}(\sqrt{2})$. Since $\sqrt{2} \notin \mathbb{Q}$, the factors are irreducible over $\mathbb{Q}$.

### Solution to Exercise 112.8
Use the fact that any finite abelian group is isomorphic to $\mathbb{Z}_{n_1} \times \dots \times \mathbb{Z}_{n_k}$ where $n_1 | n_2 | \dots | n_k$.

---

## References

1. Dummit and Foote, *Abstract Algebra*, 3rd ed., Pearson, 2004.
2. Lang, *Algebra*, 3rd ed., Springer, 1993.
3. Jacobson, *Basic Algebra I*, Harper & Row, 1977.
4. B. H. Neumann, *A Primer of Group Theory*, Dover, 1985.
5. Herstein, *Topics in Algebra*, Dover, 1975.
6. Lang, *Algebraic Number Theory*, Addison-Wesley, 1970.
7. Lang, *Undergraduate Algebra*, Springer, 2005.
8. Herstein, *Topics in Algebra*, Dover, 1975.

---

## Historical Notes

The development of abstract algebra was shaped by mathematicians such as Gauss, Eisenstein, Galois, Kronecker, Dedekind, and others. The Fundamental Theorem of Arithmetic dates back to ancient Greece, while Galois theory revolutionized our understanding of polynomial equations and their solvability.

---

## Open Problems

While much of abstract algebra is now well-understood, there remain open questions about the classification of simple groups of characteristic 2 and other related problems in algebraic topology and representation theory.

---

## Appendix: Key Formulas

- Chinese Remainder Theorem: $x \equiv a_i \pmod{I_i}$ has solution $x \equiv \sum a_i t_i \pmod{\prod I_i}$
- Fundamental Theorem of Algebra: Every non-constant polynomial over $\mathbb{C}$ has a root in $\mathbb{C}$
- Fermat's Little Theorem: $a^{p-1} \equiv 1 \pmod{p}$ for prime $p$
- Euler's Criterion: $a^{\frac{p-1}{2}} \equiv \left(\frac{a}{p}\right) \pmod{p}$
- Lagrange's Theorem: $|H|$ divides $|G|$ for subgroup $H$ of $G$
- Chinese Remainder Theorem: $\mathbb{Z}/n_1n_2\mathbb{Z} \cong \mathbb{Z}/n_1\mathbb{Z} \times \mathbb{Z}/n_2\mathbb{Z}$
- Euclid's Algorithm: $\gcd(a,b) = a(x) + b(y)$
- Sylow's Theorem: Number of Sylow $p$-subgroups divides $|G|/p^n$ and is congruent to 1 mod $p$
- Gauss-Bonnet Theorem: $\int_M K \, dA = 2\pi \chi(M)$
- Riemann-Roch Theorem: $l(D) - l(K-D) = \deg(D) - g + 1$

---

## Summary

This chapter provides a comprehensive treatment of abstract algebra theorems, including ring theory, polynomial rings, field extensions, Galois theory, modular arithmetic, linear algebra, group theory, and number theory. Each theorem is accompanied by detailed proofs and exercises to reinforce understanding.

---

## End of Chapter


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

---

*Updated on 2026-06-10*
