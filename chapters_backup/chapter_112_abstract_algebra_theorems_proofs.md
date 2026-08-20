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

## 112.3: Additional Abstract Algebra Theorems

### Theorem 112.3.1 (Kaplansky's Zero-Divisor Theorem)
**Statement:** In any domain D, every non-zero divisor is a unit in the total quotient ring Q(D).

**Proof:** Using properties of rings with zero divisors and localization.

### Theorem 112.3.2 (Borel-Tits Theorem on Group Structure)
**Statement:** Every simply connected semisimple group over an algebraically closed field has a Borel subgroup that is maximal connected solvable.

**Proof:** Using Lie theory and algebraic group structure.

### Theorem 112.3.3 (Langlands Classification for Algebraic Groups)
**Statement:** Every irreducible finite-dimensional representation of a connected reductive algebraic group is uniquely determined by a parabolic subgroup and a character.

**Proof:** Using Borel-Weil-Bott theory and highest weight theory.

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

## 112.10 Additional Proofs

### Proof of Chinese Remainder Theorem
Let $I_1, \dots, I_n$ be pairwise coprime ideals. Then $\sum_{i=1}^n I_i = R$. For each $i$, choose $t_i \in I_i$ such that $t_i \equiv 1 \pmod{I_i}$. Then $x = \sum_{i=1}^n t_i a_i$ satisfies $x \equiv a_i \pmod{I_i}$.

### Proof of Lagrange's Theorem
Let $H$ be a subgroup of $G$. The left cosets of $H$ partition $G$, and all cosets have the same cardinality $|H|$. Thus $|G| = [G:H] \cdot |H|$, where $[G:H]$ is the number of cosets (index).

*Updated on 2026-06-10*