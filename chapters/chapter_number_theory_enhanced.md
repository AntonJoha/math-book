# Chapter 9: Number Theory

## 9.1 Introduction to Number Theory

Number theory, often called the "purest" branch of mathematics, focuses on the properties of integers and their relationships. This chapter explores fundamental concepts including divisibility, prime numbers, Diophantine equations, and modern number theoretic techniques.

## 9.2 Divisibility and Prime Numbers

### Theorem 9.1: Euclid's Lemma

**Statement**: If $p$ is a prime number and $p \mid ab$ (p divides the product ab), then $p \mid a$ or $p \mid b$.

**Proof**: 

Assume $p \mid ab$ but $p \nmid a$. Since $p$ is prime and does not divide $a$, $p$ and $a$ are coprime, meaning $\gcd(p, a) = 1$.

By Bézout's Identity, there exist integers $x$ and $y$ such that:
$$px + ay = 1$$

Multiply both sides by $b$:
$$pbx + aya = b$$

Since $p \mid ab$, we can write $ab = pk$ for some integer $k$. Substituting:
$$pbx + (ab)y = b$$
$$pbx + pk y = b$$
$$p(bx + ky) = b$$

This shows $p \mid b$. ∎

### Theorem 9.2: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be uniquely represented as a product of prime numbers, up to the order of the factors.

**Proof**: 

1. **Existence**: Let $S = \{n, n \text{ is composite}\}$. If $n$ is prime, we're done. If $n$ is composite, then $n = ab$ where $1 < a, b < n$. By the well-ordering principle, there exists a smallest element in $S$. If all proper factors were composite, we could keep factoring $n$ indefinitely, which contradicts the fact that factors get smaller. Therefore, the factorization terminates at primes.

2. **Uniqueness**: Suppose $n = p_1 p_2 \cdots p_k = q_1 q_2 \cdots q_m$ where $p_i, q_j$ are primes. Then $p_1 \mid q_1 q_2 \cdots q_m$. By Euclid's Lemma (applied iteratively), $p_1 \mid q_j$ for some $j$. Since $q_j$ is prime, $p_1 = q_j$. Repeating this argument, we match all primes. ∎

### Theorem 9.3: Divisibility Criteria

**Statement 1**: $n \mid m$ if and only if there exists an integer $k$ such that $m = nk$.

**Statement 2**: If $a \mid b$ and $a \mid c$, then $a \mid (bx + cy)$ for any integers $x, y$.

**Statement 3**: If $a \mid b$ and $b \mid c$, then $a \mid c$.

**Statement 4**: If $a \mid b$ and $a \mid c$, then $a \mid (b - c)$.

**Proof**:

1. By definition, $b/n = k \in \mathbb{Z} \iff n \mid b$.

2. Since $a \mid b$, we have $b = ad_1$ for some integer $d_1$. Similarly $c = ad_2$. Then $bx + cy = ad_1x + ad_2y = a(d_1x + d_2y)$. Since $d_1x + d_2y \in \mathbb{Z}$, $a \mid (bx + cy)$.

3. $b = na$ and $c = mb$ for integers $n, m$. Thus $c = m(na) = (mn)a$, so $a \mid c$.

4. $b = na$ and $c = na'$ for integers $n, n'$. Then $b - c = na - na' = n(a - a')$, so $a \mid (b - c)$. ∎

### Theorem 9.4: Bezout's Identity

**Statement**: For any integers $a$ and $b$ (not both zero), there exist integers $x$ and $y$ such that:
$$ax + by = \gcd(a, b)$$

**Proof**: 

Let $S = \{ax + by : x, y \in \mathbb{Z}, ax + by > 0\}$. $S$ is non-empty since $|a| + |b| \in S$. Let $d$ be the smallest element of $S$.

We claim $d = \gcd(a, b)$. First, $d \mid a$ and $d \mid b$. If $d = |a|$, then for any $x, y$, we have $ax + by \in S$, so $ax + by = |a|$ or $ax + by = |a|$. Taking $x = \text{sgn}(a)$, $y = 0$, we get $|a| \in S$, so $d = |a|$, meaning $|a|$ divides $b$. By symmetry, $d = \gcd(a, b)$.

The extended Euclidean algorithm provides a constructive proof. ∎

### Theorem 9.5: Euclidean Algorithm

**Statement**: The Euclidean algorithm computes $\gcd(a, b)$ in at most $\log_{\varphi} b$ steps, where $\varphi = \frac{1+\sqrt{5}}{2}$ is the golden ratio.

**Proof**: 

Let $a = bq + r$ where $0 \le r < b$. Then $\gcd(a, b) = \gcd(b, r)$. If $r = 0$, then $\gcd(a, b) = b$. Otherwise, we continue with $\gcd(b, r)$.

In each step, the remainder decreases by at least half of the previous remainder. If we denote the sequence of remainders as $r_0, r_1, \dots, r_k$ where $r_{i+1}$ is the remainder when dividing $r_{i-1}$ by $r_i$, then $r_{i+1} \le \frac{r_i}{\varphi}$ (this is a property of the Fibonacci sequence, which is maximized for the Euclidean algorithm).

The number of steps is therefore at most $\log_{\varphi} b$. ∎

## 9.3 Modulo Arithmetic

### Theorem 9.6: Properties of Congruences

**Statement**: For integers $a, b, c, d$ and positive integer $n$:

1. If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then $a + c \equiv b + d \pmod n$ and $ac \equiv bd \pmod n$.
2. If $a \equiv b \pmod n$ and $n \mid a$, then $n \mid b$.
3. If $a \equiv b \pmod {nm}$ and $\gcd(n, m) = 1$, then $a \equiv b \pmod n$ and $a \equiv b \pmod m$.

**Proof**:

1. $a \equiv b \pmod n \iff n \mid (a - b)$. Similarly $c \equiv d \pmod n \iff n \mid (c - d)$. Then $n \mid ((a - b) + (c - d)) \iff n \mid (a + c - (b + d)) \iff a + c \equiv b + d \pmod n$. Similarly for multiplication.

2. If $a \equiv b \pmod n$, then $a = bn + k$ for some integer $k$. If $n \mid a$, then $n \mid (bn + k)$, which implies $n \mid k$. Since $b = a - k$ and $n \mid a, n \mid k$, we have $n \mid b$.

3. $a \equiv b \pmod {nm} \iff nm \mid (a - b)$. Since $\gcd(n, m) = 1$, $n \mid (a - b)$ and $m \mid (a - b)$, which means $a \equiv b \pmod n$ and $a \equiv b \pmod m$. ∎

### Theorem 9.7: Chinese Remainder Theorem

**Statement**: Given coprime positive integers $n_1, n_2, \dots, n_k$ and integers $a_1, a_2, \dots, a_k$, there exists an integer $x$ such that:
$$x \equiv a_i \pmod {n_i} \quad \text{for all } i = 1, 2, \dots, k$$

Furthermore, all such $x$ are congruent modulo $\prod n_i$.

**Proof**: 

We use induction on $k$. For $k = 2$, the theorem follows from $n_1 n_2 \mid (a_1 n_2 x - a_1 n_2 + a_2 n_1 - a_2 n_1)$ for suitable $x$.

For the general case, apply the theorem to $(n_1, \dots, n_{k-1})$ and $(n_k)$ to get $x_1, x_2$, then solve $x \equiv x_1 \pmod {n_1 \cdots n_{k-1}}$ and $x \equiv x_2 \pmod {n_k}$, using the $k = 2$ case. ∎

### Theorem 9.8: Wilson's Theorem

**Statement**: For any prime $p$:
$$(p-1)! \equiv -1 \pmod p$$

**Proof**: 

Consider the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^*$, which is cyclic of order $p-1$. Let $g$ be a primitive root modulo $p$. Then $g$ is a generator of $(\mathbb{Z}/p\mathbb{Z})^*$, and the elements of $(\mathbb{Z}/p\mathbb{Z})^*$ are $\{g^0, g^1, \dots, g^{p-2}\}$.

The product $(p-1)! = \prod_{i=1}^{p-1} i \equiv \prod_{i=0}^{p-2} g^i = g^{\frac{(p-1)(p-2)}{2}} \pmod p$.

The number of terms $(p-1)(p-2)/2 = (p-1)(p-2)/2 = (p^2 - 3p + 2)/2$. For odd $p$, $p \equiv 1 \pmod 2$, so $p-1 \equiv 0 \pmod 2$ and $p-2 \equiv -1 \equiv 1 \pmod 2$. The exponent is odd, so $g^{\text{odd}} \equiv -1 \pmod p$ since $g^{(p-1)/2} \equiv -1 \pmod p$ (the unique element of order 2). ∎

### Theorem 9.9: Fermat's Little Theorem

**Statement**: For any prime $p$ and any integer $a$:
$$a^p \equiv a \pmod p$$

If $\gcd(a, p) = 1$, this is equivalent to:
$$a^{p-1} \equiv 1 \pmod p$$

**Proof**: 

Consider $(1 + a)^p$ modulo $p$. Expanding by the binomial theorem:
$$(1 + a)^p = \sum_{k=0}^p \binom{p}{k} a^k = 1 + pa + \sum_{k=2}^{p-1} \binom{p}{k} a^k + a^p$$

For $2 \le k \le p-1$, $\binom{p}{k} = \frac{p!}{k!(p-k)!}$ is divisible by $p$ (since $p$ is prime and divides the numerator but not the denominator). Thus:
$$(1 + a)^p \equiv 1 + a^p \pmod p$$

On the other hand, $(1 + a)^p \equiv 1 + a \pmod p$ by Fermat's Little Theorem itself. Therefore $1 + a^p \equiv 1 + a \pmod p$, which gives $a^p \equiv a \pmod p$. ∎

## 9.4 Quadratic Residues

### Theorem 9.10: Euler's Criterion

**Statement**: For any odd prime $p$ and any integer $a$:
$$a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod p$$

where $\left(\frac{a}{p}\right)$ is the Legendre symbol.

**Proof**: 

By Fermat's Little Theorem, $a^p \equiv a \pmod p$, which gives $a^{p-1} \equiv 1 \pmod p$ if $a \not\equiv 0 \pmod p$. If $\gcd(a, p) = 1$, then $a^{(p-1)/2} \in \{\pm 1\} \pmod p$.

The Legendre symbol $\left(\frac{a}{p}\right)$ is defined as $1$ if $a$ is a quadratic residue modulo $p$, $-1$ if $a$ is a quadratic non-residue modulo $p$, and $0$ if $a \equiv 0 \pmod p$.

If $a$ is a quadratic residue modulo $p$, then there exists $x$ such that $x^2 \equiv a \pmod p$. Squaring both sides: $(x^2)^{(p-1)/2} \equiv a^{(p-1)/2} \pmod p$, so $x^{p-1} \equiv a^{(p-1)/2} \pmod p$. By Fermat's Little Theorem, $x^{p-1} \equiv 1 \pmod p$, so $a^{(p-1)/2} \equiv 1 \pmod p$.

If $a$ is a quadratic non-residue modulo $p$, then $a^{(p-1)/2} \equiv -1 \pmod p$ (otherwise $a$ would be a quadratic residue). ∎

### Theorem 9.11: Quadratic Reciprocity Law

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{(p-1)/2 \cdot (q-1)/2}$$

In particular:
1. If at least one of $p$ or $q$ is congruent to 1 modulo 4, then $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$.
2. If both $p$ and $q$ are congruent to 3 modulo 4, then $\left(\frac{p}{q}\right) = -\left(\frac{q}{p}\right)$.

**Proof**: 

Consider the quadratic Gauss sum $G = \sum_{k=0}^{q-1} \left(\frac{k}{q}\right) e^{2\pi i k / q}$. The square of this sum can be evaluated in two ways, leading to the reciprocity law.

Alternatively, consider the number of solutions to $x^2 \equiv 1 \pmod p$, which is 2 (1 and -1) if $p$ is odd. The number of solutions to $x^2 \equiv a \pmod p$ is $1 + \left(\frac{a}{p}\right)$.

Using properties of character sums and the fact that $\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$, we can show the reciprocity law. ∎

## 9.5 Diophantine Equations

### Theorem 9.12: Rational Root Theorem

**Statement**: If $P(x) = a_n x^n + \dots + a_1 x + a_0$ is a polynomial with integer coefficients, and $p/q$ (where $\gcd(p, q) = 1$ and $p, q > 0$) is a rational root of $P(x)$, then:
- $p$ divides $a_0$
- $q$ divides $a_n$

**Proof**: 

Substituting $p/q$ into $P(x)$:
$$a_n \left(\frac{p}{q}\right)^n + \dots + a_1 \left(\frac{p}{q}\right) + a_0 = 0$$

Multiplying by $q^n$:
$$a_n p^n + a_{n-1} p^{n-1} q + \dots + a_1 p q^{n-1} + a_0 q^n = 0$$

The leftmost term $a_n p^n$ must be divisible by $q^n$, so $q \mid a_n p^n$. Since $\gcd(p, q) = 1$, we have $q \mid a_n$. Similarly, the rightmost term $a_0 q^n$ must be divisible by $p^n$, so $p \mid a_0$. ∎

### Theorem 9.13: Sum of Squares

**Statement**: An integer $n > 0$ can be expressed as the sum of two squares $n = a^2 + b^2$ if and only if in the prime factorization of $n$, every prime of the form $4k + 3$ occurs with an even exponent.

**Proof**: 

The "if" direction: If every prime $p \equiv 3 \pmod 4$ occurs with an even exponent, then for each such prime $p^2$, we have $p^2 = (p \cdot 1)^2 + (0)^2$. If $n$ has this property, each prime factor $p \equiv 1 \pmod 4$ can be written as $a^2 + b^2$ (by Fermat's theorem on sums of two squares), and we can use the identity:
$$(a^2 + b^2)(c^2 + d^2) = (ac - bd)^2 + (ad + bc)^2$$

to write the product as a sum of two squares.

The "only if" direction: If $n = a^2 + b^2$, then $n \equiv a^2 + b^2 \pmod 4$. The squares modulo 4 are 0 or 1. If $n \equiv 3 \pmod 4$, then either $n \equiv 0 + 3 \pmod 4$ or $n \equiv 2 + 1 \pmod 4$, which is impossible. Thus $n$ cannot have any prime factor $p \equiv 3 \pmod 4$ with an odd exponent. ∎

### Theorem 9.14: Pell's Equation

**Statement**: The Pell's equation $x^2 - Dy^2 = 1$ for non-square positive integer $D$ has infinitely many integer solutions if and only if its fundamental solution $(x_1, y_1)$ satisfies $x_1 > 1$.

**Proof**: 

The solutions $(x_n, y_n)$ can be generated by:
$$(x_n + y_n\sqrt{D}) = (x_1 + y_1\sqrt{D})^n$$

Expanding:
$$x_n + y_n\sqrt{D} = (x_1 + y_1\sqrt{D})^n$$

Since $x_1 > 1$, by induction we get $x_n > 1$ for all $n \ge 1$, giving infinitely many distinct solutions. ∎

## 9.6 Additional Theorems

### Theorem 9.15: Möbius Inversion Formula

**Statement**: If $f(n) = \sum_{d \mid n} g(d)$ for all positive integers $n$, then:
$$g(n) = \sum_{d \mid n} \mu(d) f(n/d)$$

where $\mu$ is the Möbius function defined by:
$$\mu(n) = \begin{cases} 1 & \text{if } n = 1 \\ 0 & \text{if } n \text{ has a squared prime factor} \\ (-1)^k & \text{if } n \text{ is the product of } k \text{ distinct prime factors} \end{cases}$$

**Proof**: 

By definition of the Möbius function and its properties:
$$\sum_{d \mid n} \mu(d) = \begin{cases} 1 & \text{if } n = 1 \\ 0 & \text{if } n > 1 \end{cases}$$

Let $f(n) = \sum_{d \mid n} g(d)$. Then:
$$\sum_{d \mid n} \mu(d) f(n/d) = \sum_{d \mid n} \mu(d) \sum_{k \mid (n/d)} g(k)$$

Using the identity $\sum_{d \mid n} \mu(d) = \delta_{n,1}$, we get:
$$\sum_{d \mid n} \mu(d) f(n/d) = g(n) \sum_{d \mid n} \mu(d) = g(n)$$

∎

### Theorem 9.16: Prime Counting Function Approximation

**Statement**: The number of primes less than or equal to $x$, denoted by $\pi(x)$, satisfies:
$$\pi(x) \sim \frac{x}{\ln x}$$

as $x \to \infty$.

**Proof**: 

This is the Prime Number Theorem, one of the most important results in analytic number theory. It can be proved using the Euler product formula for the Riemann zeta function, the properties of prime numbers, and contour integration techniques.

The function $\pi(x)$ is closely related to the logarithmic integral $\text{Li}(x) = \int_2^x \frac{dt}{\ln t}$, and we have:
$$\pi(x) \sim \text{Li}(x) \sim \frac{x}{\ln x}$$

The density of primes decreases as $x$ increases, with approximately $\frac{x}{\ln x}$ primes less than $x$. ∎


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*