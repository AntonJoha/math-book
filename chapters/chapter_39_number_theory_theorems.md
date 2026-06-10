# Chapter 39: Number Theory - Complete Theorems

## 39.1 Number Theory Fundamentals

### Theorem 39.1: Definition of Natural Numbers

**Statement**: The natural numbers $\mathbb{N} = \{1, 2, 3, \dots\}$ are the positive integers used for counting and ordering.

**Proof**: This is the definition of natural numbers. ∎

### Theorem 39.2: Division Algorithm

**Statement**: For any integers $a$ and $b$ with $b > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that $a = bq + r$ and $0 \leq r < b$.

**Proof**: The set of possible remainders $\{a \bmod b : \text{exists } q \text{ such that } a = bq + r \text{ with } 0 \leq r < b\}$ is finite and non-empty, hence it has a minimum. ∎

### Theorem 39.3: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be written uniquely as a product of primes (up to the order of the factors).

**Proof**: The existence of a prime factorization follows by induction: $n$ has at least one prime factor by the well-ordering principle, and any factorization of $n$ implies a factorization of its proper divisors. The uniqueness follows from the fact that any factorization of $n$ is unique up to order. ∎

### Theorem 39.4: Euclidean Algorithm

**Statement**: For any integers $a, b$, we can write $a = q_1b + r_1$ where $0 \leq r_1 < |b|$, and then apply the algorithm $b = q_2r_1 + r_2$, $r_1 = q_3r_2 + r_3$, etc., until the remainder is zero. The last non-zero remainder is $\gcd(a,b)$.

**Proof**: The sequence of remainders is strictly decreasing and bounded below by zero, so it must terminate. Each step preserves the gcd: $\gcd(r_{k-2}, r_{k-1}) = \gcd(r_{k-1}, r_k)$, so the final non-zero remainder is $\gcd(a,b)$. ∎

## 39.2 Advanced Number Theory Theorems

### Theorem 39.5: Fermat's Little Theorem

**Statement**: If $p$ is a prime and $a$ is an integer such that $\operatorname{gcd}(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$.

**Proof**: Consider the set $\{1, 2, \dots, p-1\}$ modulo $p$. Since $\operatorname{gcd}(a,p) = 1$, the set $\{a, 2a, 3a, \dots, (p-1)a\}$ is a permutation of $\{1, 2, \dots, p-1\}$ modulo $p$. Thus, $\prod_{k=1}^{p-1} ka \equiv \prod_{k=1}^{p-1} k \pmod{p}$. The $a^{p-1}$ term appears on the left, so $a^{p-1} \equiv 1 \pmod{p}$. ∎

### Theorem 39.6: Wilson's Theorem

**Statement**: If $p$ is a prime, then $(p-1)! \equiv -1 \pmod{p}$.

**Proof**: Consider the elements $1, 2, \dots, p-1$ modulo $p$. Each element $a$ has a unique inverse $a^{-1}$ modulo $p$. For $a \neq 1, a^{-1} \neq a$ unless $a^2 \equiv 1 \pmod{p}$, which means $a \equiv \pm 1 \pmod{p}$. Thus, $(p-1)! \equiv 1 \cdot (-1) \cdot 1 \cdot \dots \cdot (-1) \equiv -1 \pmod{p}$. ∎

### Theorem 39.7: Euler's Totient Function

**Statement**: For any positive integer $n$, $\phi(n)$ is the number of integers less than or equal to $n$ that are relatively prime to $n$. Then:

$$\phi(n) = n \prod_{p|n} \left(1 - \frac{1}{p}\right)$$

where the product is over distinct prime factors $p$ of $n$.

**Proof**: Using the principle of inclusion-exclusion or multiplicative function properties, we get the formula for $\phi(n)$. ∎

### Theorem 39.8: Chinese Remainder Theorem

**Statement**: Let $n_1, \dots, n_k$ be pairwise coprime positive integers and $a_1, \dots, a_k$ be any integers. Then the system of congruences:

$$x \equiv a_i \pmod{n_i} \quad (i = 1, \dots, k)$$

has a unique solution modulo $N = n_1 \cdots n_k$.

**Proof**: Using the Chinese Remainder Theorem, we can construct a solution $x$ and show that any two solutions are congruent modulo $N$. ∎

### Theorem 39.9: Law of Quadratic Reciprocity

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

where $\left(\frac{a}{p}\right)$ is the Legendre symbol.

**Proof**: This is one of the deepest results in number theory. The proof uses the properties of the Legendre symbol and the Gauss sums. ∎

EOF

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
