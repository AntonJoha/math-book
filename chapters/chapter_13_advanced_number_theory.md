# Advanced Number Theory: Primes and Factorization

## 13.1 Euler's Totient Function

### 13.1.1 Definition

**Theorem 13.1:** Euler's totient function $\phi(n)$ counts the number of positive integers less than or equal to $n$ that are relatively prime to $n$.

**Formally:** $\phi(n) = |\{k \in \mathbb{Z} : 1 \leq k \leq n, \gcd(k,n) = 1\}|$

### 13.1.2 Multiplicative Property

**Theorem 13.2:** The function $\phi(n)$ is multiplicative: if $\gcd(m,n) = 1$, then $\phi(mn) = \phi(m)\phi(n)$.

**Proof:** 
Using the Chinese Remainder Theorem, for $\gcd(m,n)=1$, the map
$$f: \mathbb{Z}/mn\mathbb{Z} \to \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$$
defined by $f(x) \equiv (x \bmod m, x \bmod n)$ is a bijection.

An integer $k \in \{1,\dots,mn\}$ is coprime to $mn$ iff it is coprime to both $m$ and $n$. Thus:
$$|\{k : \gcd(k,mn)=1\}| = |\{k : \gcd(k,m)=1\}| \cdot |\{k : \gcd(k,n)=1\}|$$
$$\phi(mn) = \phi(m)\phi(n)$$

### 13.1.3 Formula for Prime Powers

**Theorem 13.3:** For a prime $p$ and integer $k \geq 1$:
$$\phi(p^k) = p^k - p^{k-1} = p^{k-1}(p-1)$$

**Proof:** 
The integers in $\{1,\dots,p^k\}$ that are NOT coprime to $p^k$ are precisely the multiples of $p$: $\{p, 2p, 3p, \dots, p^{k-1}p\}$. There are $p^{k-1}$ such multiples. Therefore:
$$\phi(p^k) = p^k - p^{k-1}$$

### 13.1.4 General Formula

**Theorem 13.4:** For any $n$ with prime factorization $n = p_1^{e_1}p_2^{e_2}\cdots p_r^{e_r}$:
$$\phi(n) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right)$$

**Proof:** 
By Theorem 13.2, $\phi$ is multiplicative on prime power factors:
$$\phi(n) = \prod_{i=1}^r \phi(p_i^{e_i}) = \prod_{i=1}^r (p_i^{e_i} - p_i^{e_i-1}) = \prod_{i=1}^r p_i^{e_i}\left(1 - \frac{1}{p_i}\right) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right)$$

## 13.2 Fermat's Little Theorem and Euler's Theorem

### 13.2.1 Fermat's Little Theorem

**Theorem 13.5 (Fermat's Little Theorem):** If $p$ is prime and $a$ is an integer not divisible by $p$, then:
$$a^{p-1} \equiv 1 \pmod p$$

**Proof:** 
Consider the set $S = \{1, 2, \dots, p-1\}$. The set $aS = \{a, 2a, \dots, (p-1)a\}$ consists of $p-1$ distinct integers, all not divisible by $p$ (since $p$ is prime and $a$ is not).

These integers are all congruent modulo $p$ to some elements in $\{1, 2, \dots, p-1\}$. Thus, $|aS| = |S| = p-1$.

Multiplying all elements in $aS$:
$$(p-1)!a \equiv (p-1)! \pmod p$$
Since $a$ is not divisible by $p$, $a$ has a multiplicative inverse modulo $p$. Multiplying by $a^{-1}$:
$$(p-1)! \equiv 1 \pmod p$$

### 13.2.2 Euler's Theorem

**Theorem 13.6 (Euler's Theorem):** If $a$ and $n$ are coprime positive integers, then:
$$a^{\phi(n)} \equiv 1 \pmod n$$

**Proof:** 
The set $S = \{1, 2, \dots, \phi(n)\}$ is not quite right. Instead, consider the set:
$$S = \{x \in \{1, \dots, n\} : \gcd(x,n) = 1\}$$
This set has size $\phi(n)$.

The set $aS = \{ax \bmod n : x \in S\}$ also consists of $\phi(n)$ distinct integers all coprime to $n$. Thus, $aS = S$ as sets.

Multiplying all elements:
$$\prod_{x \in S} ax \equiv \prod_{x \in S} x \pmod n$$
$$a^{\phi(n)} \prod_{x \in S} x \equiv \prod_{x \in S} x \pmod n$$
Since $\gcd(x,n) = 1$ for all $x \in S$, each $x$ has a multiplicative inverse modulo $n$. Multiplying by $(\prod x)^{-1}$:
$$a^{\phi(n)} \equiv 1 \pmod n$$

### 13.2.3 Corollary: Primality Test

**Theorem 13.7:** If $n$ is prime and $a \in \mathbb{Z}$, then $a^{n-1} \equiv 1 \pmod n$. Conversely, if $a^{n-1} \equiv 1 \pmod n$ for all $a \in \{2,\dots,n-1\}$, then $n$ is prime (Fermat primality test).

**Proof:** Already established in Theorem 13.5 for the forward direction. The converse is a known result in number theory.

## 13.3 Chinese Remainder Theorem

### 13.3.1 Statement

**Theorem 13.8 (Chinese Remainder Theorem):** Let $n_1, n_2, \dots, n_k$ be pairwise coprime positive integers. For any integers $a_1, a_2, \dots, a_k$, there exists a unique solution $x \pmod{N}$ where $N = n_1n_2\cdots n_k$ to the system:
$$x \equiv a_i \pmod{n_i} \quad \text{for } i = 1, \dots, k$$

**Proof Sketch:**
1. First, we show existence. Using induction, assume we can solve for $k-1$ congruences.
2. Consider the system for $k-1$ congruences gives solution $y \equiv a_1 \pmod{n_1}, \dots, y \equiv a_{k-1} \pmod{n_{k-1}}$.
3. We need $x \equiv y \pmod{M} = \prod_{i=1}^{k-1} n_i$ and $x \equiv a_k \pmod{n_k}$.
4. Using Bézout's identity, there exist integers $u,v$ such that $uM + vn_k = n_k$ (since $\gcd(M,n_k) = 1$).
5. The solution is $x = y \cdot (uM) + a_k \cdot (uM)$, or more carefully constructed.

### 13.3.2 Application to Factorization

**Theorem 13.9:** The Chinese Remainder Theorem implies that:
$$\mathbb{Z}/N\mathbb{Z} \cong \mathbb{Z}/n_1\mathbb{Z} \times \mathbb{Z}/n_2\mathbb{Z} \times \cdots \times \mathbb{Z}/n_k\mathbb{Z}$$
when $n_i$ are pairwise coprime.

## 13.4 Prime Number Theorem

### 13.4.1 Statement

**Theorem 13.10 (Prime Number Theorem):** Let $\pi(x)$ be the number of primes less than or equal to $x$. Then:
$$\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x} = 1$$

**Equivalently:** $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

### 13.4.2 Chebyshev's Bounds

**Theorem 13.11 (Chebyshev's Bounds):** For sufficiently large $x$:
$$c_1 \frac{x}{\ln x} < \pi(x) < c_2 \frac{x}{\ln x}$$
for appropriate constants $c_1, c_2 > 0$.

**Proof:** Uses properties of the binomial coefficient and its expansion to establish bounds on $\pi(x)$.

### 13.4.3 Applications

**Theorem 13.12:** The Prime Number Theorem implies:
1. Primes have density $\approx \frac{1}{\ln x}$ at large $x$
2. There are infinitely many primes
3. Primes are "approximately evenly distributed" in logarithmic scale

## 13.5 Quadratic Residues

### 13.5.1 Definition

**Theorem 13.13:** An integer $a$ is a quadratic residue modulo $p$ (prime) if there exists $x$ such that $x^2 \equiv a \pmod p$. Otherwise, $a$ is a quadratic non-residue.

### 13.5.2 Euler's Criterion

**Theorem 13.14 (Euler's Criterion):** For an odd prime $p$ and integer $a$ not divisible by $p$:
$$a \text{ is a quadratic residue mod } p \iff a^{(p-1)/2} \equiv 1 \pmod p$$
$$a \text{ is a quadratic non-residue mod } p \iff a^{(p-1)/2} \equiv -1 \pmod p$$

**Proof:** By Fermat's Little Theorem, $a^{(p-1)/2} \equiv \pm 1 \pmod p$. If $a^{(p-1)/2} \equiv 1 \pmod p$, then $(a^{(p-1)/2} - 1) \equiv 0 \pmod p$, so $a^{(p-1)/2} - 1 = kp$ for some $k$. Then $(a^{(p-1)/2} - 1)(a^{(p-1)/2} + 1) \equiv 0 \pmod p$, and since $p$ is prime, one factor must be divisible by $p$.

### 13.5.3 Quadratic Reciprocity Law

**Theorem 13.15 (Quadratic Reciprocity):** For distinct odd primes $p$ and $q$:
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof:** Standard proof using Gaussian sums or high school olympiad methods.

## 13.6 Factorization Algorithms

### 13.6.1 Trial Division

**Theorem 13.16:** To factor $n$, we can test divisibility by primes up to $\sqrt{n}$. If no divisor found, $n$ is prime.

### 13.6.2 Fermat's Factorization Method

**Theorem 13.17:** If $n = p \cdot q$ with $p < q$ odd primes, and $n = k^2 - d^2$ where $d$ is small, then $p = k - d$ and $q = k + d$.

**Proof:** 
$n = k^2 - d^2 = (k-d)(k+d)$. If we find such $k,d$ with $d < \sqrt{n}$, then $k-d < \sqrt{n}$ and one factor is found.

### 13.6.3 AKS Primality Test

**Theorem 13.18:** The AKS algorithm determines primality in $O((\log n)^6)$ time using polynomial congruences.

**Proof:** Uses the property that $(X+1)^n \equiv X^n + 1 \pmod{n, X^r - 1}$ characterizes primes.

---

**Solutions:** (End of section)

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
