# Number Theory

## 4.1 Integers and Division

### 4.1.1 The Set of Integers

The set of integers $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$ is the set of whole numbers and their negatives. Every integer $n$ can be written as $n = qk + r$ where $q$ is the quotient and $r$ is the remainder.

### 4.1.2 The Euclidean Algorithm

**Theorem 4.1 (GCD Algorithm):** For any integers $a, b$ (not both zero), there exist unique integers $x, y$ such that $ax + by = \gcd(a, b)$.

*Proof:* Consider the set $S = \{ax + by : x, y \in \mathbb{Z}, ax + by > 0\}$. This set is non-empty by the well-ordering principle. Let $d$ be the smallest element of $S$. We claim $d = \gcd(a, b)$.
- $d \mid a$: Write $a = qd + r$ with $0 \leq r < d$. Then $r = a - qd = a - q(ax + by)$ for some integers $x, y$. Thus $r$ is a linear combination of $a$ and $b$. Since $d$ is the smallest positive linear combination, $r = 0$, so $d \mid a$.
- $d \mid b$: Similarly, $b = q'd + r'$ with $0 \leq r' < d$. Thus $r' = b - q'd = b - q'(ax + by)$, so $r'$ is a linear combination. Again $r' = 0$, so $d \mid b$.
- If $g \mid a$ and $g \mid b$, then $g \mid (ax + by) = d$, so $g \mid d$. Since $d \mid a$ and $d \mid b$, we have $g = kd$, so $k = 1$ or $k = -1$. Thus $d = \pm g$. Since $d > 0$, $d = \gcd(a, b)$. ∎

### 4.1.3 The Euclidean Algorithm for Computation

The Euclidean Algorithm computes $\gcd(a, b)$ by repeated application of the division algorithm:

$$\begin{align*}
a &= qb_1 + r_1, \text{ where } 0 \leq r_1 < b \\
b &= r_1q_2 + r_2, \text{ where } 0 \leq r_2 < r_1 \\
r_1 &= r_2q_3 + r_3, \text{ where } 0 \leq r_3 < r_2 \\
&\vdots \\
r_{k-2} &= r_{k-1}q_k + r_k, \text{ where } 0 \leq r_k < r_{k-1} \\
r_{k-1} &= r_kq_{k+1} + 0
\end{align*}$$

The last non-zero remainder $r_k = \gcd(a, b)$.

**Back-Substitution:** We can also use the Euclidean Algorithm to find integers $x, y$ such that $ax + by = \gcd(a, b)$ by back-substitution.

## 4.2 Primes and Prime Factorization

### 4.2.1 Prime Numbers

**Definition:** A natural number $p > 1$ is **prime** if its only positive divisors are $1$ and $p$. Otherwise, it is **composite**.

**Theorem 4.2 (Uniqueness of Prime Factorization):** Every integer $n > 1$ can be uniquely written as a product of prime numbers, up to the order of the factors:
$$n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$$
where $p_1 < p_2 < \dots < p_k$ are primes and $e_i \geq 1$.

*Proof:* 
- **Existence:** By induction on $n$. For $n = 2$, the statement is true. Assume true for all $m < n$. If $n$ is prime, the statement holds. If $n$ is composite, write $n = ab$ with $1 < a, b < n$. By induction, $a = p_1^{e_1} \dots p_m^{e_m}$ and $b = q_1^{f_1} \dots q_k^{f_k}$, so $n = p_1^{e_1} \dots p_m^{e_m} q_1^{f_1} \dots q_k^{f_k}$.
- **Uniqueness:** Suppose $n = p_1^{e_1} \dots p_k^{e_k} = q_1^{f_1} \dots q_m^{f_m}$. Then $n \mid q_1^{f_1} \dots q_m^{f_m}$. Since $n > 1$, we must have $q_1^{f_1} \neq 1$, so there exists some prime factor $q_j$ of $n$. By the definition of divisibility, $q_j$ must be equal to some $p_i$. Repeating this argument, we show the sets $\{p_1, \dots, p_k\}$ and $\{q_1, \dots, q_m\}$ are equal, and the exponents must also be equal.

## 4.3 Congruences and Modular Arithmetic

### 4.3.1 Congruences

**Definition:** For integers $a, b$ and positive integer $n$, we say $a \equiv b \pmod{n}$ if $n \mid (a - b)$.

**Properties of Congruences:**
1. $a \equiv b \pmod{n} \iff a = b + kn$ for some integer $k$.
2. If $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n}$, then:
   - $a + c \equiv b + d \pmod{n}$ (addition)
   - $ac \equiv bd \pmod{n}$ (multiplication)
3. If $a \equiv b \pmod{n}$ and $n \mid c$, then $ac \equiv bc \pmod{n}$.

### 4.3.2 Fermat's Little Theorem

**Theorem 4.3 (Fermat's Little Theorem):** If $p$ is prime and $a$ is any integer, then:
$$a^p \equiv a \pmod{p}$$

Equivalently, if $p \nmid a$, then:
$$a^{p-1} \equiv 1 \pmod{p}$$

*Proof:* Consider the set $S = \{a, 2a, 3a, \dots, (p-1)a\}$. Since $p$ is prime and $a \not\equiv 0 \pmod{p}$, the integers $1, 2, \dots, p-1$ are all incongruent modulo $p$. Thus $a, 2a, \dots, (p-1)a$ are all incongruent modulo $p$. If $ka \equiv la \pmod{p}$ with $1 \leq k, l \leq p-1$, then $p \mid (k-l)a$. Since $p$ is prime and $p \nmid a$, we must have $p \mid (k-l)$, which implies $k = l$. Thus $S$ is a permutation of $\{1, 2, \dots, p-1\}$ modulo $p$. Multiplying all elements:
$$\prod_{i=1}^{p-1} ia \equiv \prod_{i=1}^{p-1} i \pmod{p}$$
$$a^{p-1}(p-1)! \equiv (p-1)! \pmod{p}$$
Since $p$ is prime, $(p-1)! \not\equiv 0 \pmod{p}$, so we can cancel $(p-1)!$:
$$a^{p-1} \equiv 1 \pmod{p}$$
Multiplying by $a$ gives $a^p \equiv a \pmod{p}$. ∎

### 4.3.3 Euler's Totient Function

**Definition:** Euler's totient function $\phi(n)$ counts the positive integers less than or equal to $n$ that are relatively prime to $n$.

**Theorem 4.4 (Euler's Generalization of Fermat's Little Theorem):** If $\gcd(a, n) = 1$, then:
$$a^{\phi(n)} \equiv 1 \pmod{n}$$

## 4.4 Quadratic Residues

### 4.4.1 Quadratic Residues

**Definition:** An integer $a$ is a **quadratic residue** modulo $n$ if there exists an integer $x$ such that $x^2 \equiv a \pmod{n}$. Otherwise, $a$ is a **quadratic non-residue** modulo $n$.

### 4.4.2 Euler's Criterion

**Theorem 4.5 (Euler's Criterion):** Let $p$ be an odd prime and $a$ an integer such that $p \nmid a$. Then:
$$a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod{p}$$
where $\left(\frac{a}{p}\right)$ is the Legendre symbol:
$$\left(\frac{a}{p}\right) = \begin{cases} 1 & \text{if } a \text{ is a quadratic residue mod } p \text{ and } p \nmid a \\ -1 & \text{if } a \text{ is a quadratic non-residue mod } p \end{cases}$$

## 4.5 The Chinese Remainder Theorem

### 4.5.1 Statement

**Theorem 4.6 (Chinese Remainder Theorem):** Let $n_1, \dots, n_k$ be pairwise coprime positive integers and let $r_1, \dots, r_k$ be arbitrary integers. The system of congruences:
$$\begin{align*}
x &\equiv r_1 \pmod{n_1} \\
x &\equiv r_2 \pmod{n_2} \\
&\vdots \\
x &\equiv r_k \pmod{n_k}
\end{align*}$$
has a unique solution modulo $n = n_1n_2\cdots n_k$.

*Proof Sketch:* Construct the solution using the Chinese Remainder Theorem construction: Let $N = n_1n_2\cdots n_k$ and $N_i = N/n_i$. Since $\gcd(N_i, n_i) = 1$, there exist integers $y_i$ such that $N_iy_i \equiv 1 \pmod{n_i}$. Let $x = \sum_{i=1}^k r_iN_iy_i$. Then $x \equiv r_iN_iy_i \equiv r_i \pmod{n_i}$ and $x \equiv 0 \pmod{n_j}$ for $j \neq i$. Thus $x \equiv r_i \pmod{n_i}$ for all $i$. The solution is unique modulo $N$. ∎

## Exercises

1. Use the Euclidean Algorithm to compute $\gcd(1234, 567)$.
2. Prove that every prime number greater than 2 is of the form $4k + 1$ or $4k + 3$.
3. Show that $n \mid (2^n - 2)$ if and only if $n$ is prime (Fermat's primality test).
4. Prove that there are infinitely many primes.
5. Use the Chinese Remainder Theorem to solve the system:
   $$x \equiv 2 \pmod{3}, \quad x \equiv 3 \pmod{5}, \quad x \equiv 2 \pmod{7}$$
