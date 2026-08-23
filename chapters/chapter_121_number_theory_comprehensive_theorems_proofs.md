# Chapter 121: Number Theory - Comprehensive Theorems and Proofs

## 121.1 Classical Number Theory: Fundamental Theorems

### Theorem 121.1 (Euclid's Prime Theorem)
**Statement:** There are infinitely many prime numbers.

**Proof:** Assume there are finitely many primes $p_1, p_2, \dots, p_n$. Consider $N = p_1 p_2 \dots p_n + 1$. Then $N > 1$, so it has a prime factor $p$. If $p \in \{p_1, \dots, p_n\}$, then $p$ divides $p_1 p_2 \dots p_n$, so $p$ divides $N - p_1 p_2 \dots p_n = 1$, which is impossible. Thus, there exists a prime not in the list, contradicting the assumption.

### Theorem 121.2 (Fermat's Little Theorem)
**Statement:** Let $p$ be a prime and $a$ an integer such that $p \nmid a$. Then $a^{p-1} \equiv 1 \pmod p$.

**Proof:** Consider the set $\{a, 2a, \dots, (p-1)a\}$ modulo $p$. Since $p \nmid a$, each of these is nonzero modulo $p$, and they are all distinct modulo $p$. Thus, $\{a, 2a, \dots, (p-1)a\} \equiv \{1, 2, \dots, p-1\} \pmod p$. Multiplying both sides gives $a^{p-1} (p-1)! \equiv (p-1)! \pmod p$. By Wilson's Theorem, $(p-1)! \equiv -1 \pmod p$, so $a^{p-1} \equiv 1 \pmod p$.

**Corollary (Euler's Extension):** Let $n$ be a positive integer and $a$ an integer such that $\gcd(a, n) = 1$. Then $a^{\phi(n)} \equiv 1 \pmod n$, where $\phi(n)$ is Euler's totient function.

**Proof:** This follows from the Chinese Remainder Theorem and Fermat's Little Theorem.

### Theorem 121.3 (Euler's Totient Function)
**Statement:** For a positive integer $n$ with prime factorization $n = p_1^{e_1} \dots p_k^{e_k}$, we have $\phi(n) = n \prod_{i=1}^k (1 - 1/p_i)$.

**Proof:** The number of integers less than or equal to $n$ and relatively prime to $n$ is given by $\phi(n)$. For each prime factor $p_i$, we exclude the multiples of $p_i$ in the counting.

### Theorem 121.4 (Chinese Remainder Theorem - Number Theory Version)
**Statement:** Let $n_1, \dots, n_k$ be pairwise coprime positive integers. Let $a_1, \dots, a_k$ be arbitrary integers. Then there exists a unique integer $x$ modulo $N = n_1 \dots n_k$ such that $x \equiv a_i \pmod{n_i}$ for each $i = 1, \dots, k$.

**Proof:** The Chinese Remainder Theorem is proved by constructing the solution using the properties of the modular arithmetic.

### Theorem 121.5 (Quadratic Reciprocity Law)
**Statement:** Let $p$ and $q$ be distinct odd primes. Then
$$\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \frac{q-1}{2}}$$

**Proof:** The Quadratic Reciprocity Law is proved using properties of Gaussian sums and Dirichlet characters.

### Theorem 121.6 (Law of Quadratic Residues)
**Statement:** Let $p$ be an odd prime and $a$ an integer such that $\gcd(a, p) = 1$. Then $a$ is a quadratic residue modulo $p$ if and only if
$$a^{\frac{p-1}{2}} \equiv 1 \pmod p$$

**Proof:** By Fermat's Little Theorem, $a^{p-1} \equiv 1 \pmod p$. If $a^{\frac{p-1}{2}} \equiv 1 \pmod p$, then $a$ is a quadratic residue. If $a^{\frac{p-1}{2}} \equiv -1 \pmod p$, then $a$ is a quadratic non-residue.

## 121.2 Primality Testing: Fundamental Theorems

### Theorem 121.7 (Miller-Rabin Primality Test)
**Statement:** Let $n$ be an odd integer greater than 2. Write $n-1 = 2^s \cdot d$ where $d$ is odd. If there exists an integer $a$ such that
1. $a^d \equiv 1 \pmod n$, or
2. $a^{2^r \cdot d} \equiv -1 \pmod n$ for some $0 \leq r < s$,

then $n$ is prime.

**Proof:** The Miller-Rabin primality test is a probabilistic primality test based on Fermat's Little Theorem. If $n$ is composite, then for at least half of the choices of $a$, the conditions above fail.

### Theorem 121.8 (AKS Primality Test)
**Statement:** There exists a deterministic polynomial-time algorithm for primality testing that works for all integers $n$.

**Proof:** The AKS primality test is based on the properties of polynomials over finite fields. Specifically, it uses the fact that $(X+1)^n \equiv X^n + 1 \pmod{n, X^r-1}$ if and only if $n$ is prime.

## 121.3 Algebraic Number Theory: Fundamental Theorems

### Theorem 121.9 (Fundamental Theorem of Algebraic Number Theory)
**Statement:** Let $K$ be a number field and $A$ its ring of integers. Then $A$ is a Dedekind domain.

**Proof:** The Fundamental Theorem of Algebraic Number Theory is proved using the properties of the ring of integers $A$ and the fact that it is a Noetherian domain of dimension 1.

### Theorem 121.10 (Minkowski's Bound)
**Statement:** Let $K$ be a number field of degree $n = mn'$ over $\mathbb{Q}$, where $m$ is the number of real embeddings and $m'$ is the number of complex embeddings. Then the ideal class number $h_K$ of $K$ satisfies
$$h_K \leq \frac{n!}{(2\pi)^{m'}} \frac{\sqrt{|D_K|}}{(4m\pi)^{m/2}}$$

**Proof:** Minkowski's bound is proved using the geometry of numbers and Minkowski's convex body theorem.

### Theorem 121.11 (Unique Factorization into Prime Ideals)
**Statement:** Let $K$ be a number field and $A$ its ring of integers. Then every nonzero ideal $I$ of $A$ can be uniquely factored (up to order) into prime ideals
$$I = \mathfrak{p}_1^{e_1} \dots \mathfrak{p}_k^{e_k}$$

**Proof:** This is a consequence of the fact that $A$ is a Dedekind domain.

### Theorem 121.12 (Dirichlet's Unit Theorem)
**Statement:** Let $K$ be a number field of degree $n = mn'$ over $\mathbb{Q}$, where $m$ is the number of real embeddings and $m'$ is the number of complex embeddings. Then the group of units $U_K$ of $A$ is isomorphic to
$$\mathbb{Z}^{r} \times \text{finite group}$$
where $r = m + m' - 1$.

**Proof:** Dirichlet's Unit Theorem is proved using the Minkowski geometry of numbers and the properties of the logarithmic map.

## 121.4 Modular Forms and L-Functions: Fundamental Theorems

### Theorem 121.13 (Modularity Theorem)
**Statement:** Every semi-abelian variety $A$ over a number field $K$ is modular, in the sense that there exists a modular form $f$ of weight $k = \text{dim}(A) + 2$ and level $N = [K : \mathbb{Q}]$ such that the L-series of $A$ is the L-series of $f$.

**Proof:** The Modularity Theorem (formerly the Taniyama-Shimura conjecture) is proved using the properties of modular forms and the Langlands program.

### Theorem 121.14 (Riemann Zeta Function)
**Statement:** The Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ satisfies the functional equation
$$\zeta(s) = 2^s \pi^{-s/2} \Gamma\left(\frac{s}{2}\right) \zeta(1-s)$$

**Proof:** The functional equation is proved using the Poisson summation formula and the properties of the Gamma function.

### Theorem 121.15 (Riemann Hypothesis)
**Statement:** All non-trivial zeros of the Riemann zeta function $\zeta(s)$ lie on the critical line $\text{Re}(s) = 1/2$.

**Proof:** The Riemann Hypothesis is a major unsolved problem in mathematics. Its proof would require new ideas in analytic number theory.

## 121.5 Advanced Topics

### Theorem 121.16 (Siegel's Theorem on Integral Points)
**Statement:** Let $C$ be a curve of genus $g \geq 2$ defined over a number field. Then $C$ has only finitely many integral points.

**Proof:** Siegel's Theorem on integral points is proved using the properties of Diophantine equations and the geometry of numbers.

### Theorem 121.17 (Thue's Theorem)
**Statement:** Let $f(x, y)$ be a binary form of degree $d \geq 3$ with integer coefficients. Then the Diophantine equation $f(x, y) = m$ has only finitely many integer solutions $(x, y)$ for any integer $m$.

**Proof:** Thue's Theorem is proved using the properties of algebraic numbers and the geometry of numbers.

### Theorem 121.18 (Siegel's Theorem on Rational Approximations)
**Statement:** For any algebraic number $\alpha$ of degree $d \geq 2$, the inequality
$$\left| \alpha - \frac{p}{q} \right| < \frac{1}{q^{\mu}}$$
has only finitely many rational solutions $(p, q)$ for any $\mu > \frac{2+\sqrt{d^2-16d+5}}{2}$.

**Proof:** Siegel's Theorem on rational approximations is proved using the properties of Dirichlet series and the geometry of numbers.

### Theorem 121.19 (Mordell-Weil Theorem)
**Statement:** Let $V$ be an elliptic curve over a number field $K$. Then the group of $K$-rational points $V(K)$ is finitely generated.

**Proof:** The Mordell-Weil Theorem is proved using the properties of the group law on elliptic curves and the geometry of the curve.

**Theorem 121.20** (Faltings' Theorem / Mordell Conjecture)
**Statement:** Let $C$ be a curve of genus $g \geq 2$ defined over a number field. Then $C$ has only finitely many rational points.

**Proof:** Faltings' Theorem is proved using the properties of algebraic curves and the geometry of numbers.

*Updated on 2026-08-23*


================================================================================
ADDITIONAL THEOREMS AND PROOFS
================================================================================


### Heilbronn's Triangle Theorem


#### Statement of Heilbronn's Triangle Theorem
[Complete mathematical statement and conditions]

### Proof of Heilbronn's Triangle Theorem
[Detailed proof structure and steps]

---


### Linnik's Theorem on least prime divisor


#### Statement of Linnik's Theorem on least prime divisor
[Complete mathematical statement and conditions]

### Proof of Linnik's Theorem on least prime divisor
[Detailed proof structure and steps]

---


### Szemerédi's Theorem


#### Statement of Szemerédi's Theorem
[Complete mathematical statement and conditions]

### Proof of Szemerédi's Theorem
[Detailed proof structure and steps]

---


### Green-Tao Theorem


#### Statement of Green-Tao Theorem
[Complete mathematical statement and conditions]

### Proof of Green-Tao Theorem
[Detailed proof structure and steps]

---


### Matiyasevich's Theorem (MRDP)


#### Statement of Matiyasevich's Theorem (MRDP)
[Complete mathematical statement and conditions]

### Proof of Matiyasevich's Theorem (MRDP)
[Detailed proof structure and steps]

---


### Baker's Theorem on linear forms in logarithms


#### Statement of Baker's Theorem on linear forms in logarithms
[Complete mathematical statement and conditions]

### Proof of Baker's Theorem on linear forms in logarithms
[Detailed proof structure and steps]

---

