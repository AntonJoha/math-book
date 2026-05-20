# Chapter 5: Number Theory Fundamentals

## 5.1 Divisibility

### Theorem 5.1: Basic Divisibility Properties

**Statement**: For integers $a, b$ with $b \neq 0$, the following are equivalent:
1. $b$ divides $a$ (denoted $b \mid a$)
2. There exists an integer $k$ such that $a = bk$
3. $a$ is a multiple of $b$

**Proof**:

(1 ⇔ 2) By definition, $b \mid a$ means there exists an integer $k$ such that $a = bk$.

(2 ⇔ 3) By definition, $a$ is a multiple of $b$ if $a = bk$ for some integer $k$.

∎

### Theorem 5.2: Properties of Divisibility

**Statement**: For integers $a, b, c$ with $b, c \neq 0$:

1. If $b \mid a$ and $b \mid c$, then $b \mid (ax + cy)$ for any integers $a, c, x, y$
2. If $b \mid a$ and $a \neq 0$, then $|b| \le |a|$
3. If $a \mid b$ and $b \mid a$, then $|a| = |b|$

**Proof**:

1. If $b \mid a$, then $a = bk$ for some integer $k$. Similarly, $c = bm$ for some integer $m$.
   Then $ax + cy = (bk)x + (bm)y = b(kx + my)$, so $b \mid (ax + cy)$.

2. If $b \mid a$ and $a \neq 0$, then $a = bk$ for some integer $k \neq 0$ (since $a \neq 0$).
   Thus $|a| = |b||k| \ge |b|$ since $|k| \ge 1$ for any non-zero integer.

3. If $a \mid b$ and $b \mid a$, then $a = bk$ and $b = am$ for some integers $k, m$.
   Substituting: $a = (am)k = amk$. Thus $a = a(mk)$.
   Since $a \neq 0$ (if $a = 0$, then $b = 0$ by definition), we have $mk = 1$.
   Since $m, k$ are integers, $mk = 1$ implies $m = k = 1$ or $m = k = -1$.
   Thus $|m| = 1$, so $|a| = |b|$. ∎

## 5.2 Greatest Common Divisor

### Theorem 5.3: Existence of GCD

**Statement**: For any integers $a, b$ (not both zero), there exists a greatest common divisor $d = \gcd(a, b)$ such that:
1. $d \mid a$ and $d \mid b$
2. If $c \mid a$ and $c \mid b$, then $c \mid d$

**Proof of existence**:
Consider the set $S = \{|xa + yb| : x, y \in \mathbb{Z}\} \cap \mathbb{N}_0$.
Since $a, b$ are not both zero, $S$ contains at least one positive integer.
Let $d$ be the smallest positive integer in $S$.

(1) We show $d = |a|a' + |b|b'$ for some integers $a', b'$.

Let $d = |xa + yb|$ for some integers $x, y$.
Clearly $d \mid (xa + yb)$, and $a = (1)a + (0)b$, $b = (0)a + (1)b$.
Thus $d$ is a linear combination of $a$ and $b$.

(2) If $c \mid a$ and $c \mid b$, then $c \mid (xa + yb)$, so $c \mid d$.

Since $d$ divides $a$ and $b$, and any common divisor of $a$ and $b$ divides $d$, $d$ is the greatest common divisor. ∎

## 5.3 Euclidean Algorithm

### Theorem 5.4: Euclidean Algorithm Correctness

**Statement**: For any positive integers $a, b$, the Euclidean algorithm computes $\gcd(a, b)$ as follows:

1. $a = bq_1 + r_1$ where $0 \le r_1 < b$
2. $b = r_1q_2 + r_2$ where $0 \le r_2 < r_1$
3. Continue until $r_n = 0$
4. Then $\gcd(a, b) = r_{n-1}$

**Proof**:

The algorithm terminates because the sequence of remainders is strictly decreasing:
$r_1 > r_2 > \dots > r_n = 0$.

The last non-zero remainder $r_{n-1}$ divides all previous remainders, and thus divides $a$ and $b$.

If $d$ is any common divisor of $a$ and $b$, it divides all remainders by the divisibility property.

Thus $d \mid r_{n-1}$, and since $r_{n-1}$ divides $a$ and $b$, $r_{n-1}$ is the GCD. ∎

## 5.4 Bezout's Identity

### Theorem 5.5: Bezout's Identity

**Statement**: For any integers $a, b$ (not both zero), the set of all common divisors of $a$ and $b$ is exactly the set of all divisors of $\gcd(a, b)$.

Equivalently, for any integers $a, b$ and any integers $x, y$:

$$\gcd(a, b) = ax + by$$

**Proof**:

Let $d = ax + by$. If $p \mid a$ and $p \mid b$, then $p \mid (ax + by)$, so $p \mid d$.

Thus $\gcd(a, b)$ divides any common divisor $d$.

Since $d = \gcd(a, b)$ divides $a$ and $b$, any common divisor $c$ of $a$ and $b$ must divide $d$.

Conversely, since $\gcd(a, b) \mid a$ and $\gcd(a, b) \mid b$, $\gcd(a, b)$ is a common divisor.

∎

## 5.5 Linear Diophantine Equations

### Theorem 5.6: Solvability of Linear Diophantine Equations

**Statement**: The linear Diophantine equation $ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$.

**Proof**:

(⇒) If $ax + by = c$ has integer solutions, let $d = \gcd(a, b)$.
Then $d \mid a$ and $d \mid b$, so $d \mid (ax + by) = c$.

(⇐) Suppose $d = \gcd(a, b) \mid c$. Let $a = da', b = db', c = dc'$ where $\gcd(a', b') = 1$.
By Bezout's Identity, there exist integers $x', y'$ such that $a'x' + b'y' = 1$.
Multiplying by $c'$: $a'(x'c') + b'(y'c') = c'$.
Multiply by $d$: $a(x'c') + b(y'c') = c$.

Thus $x = x'c'$ and $y = y'c'$ are integer solutions. ∎

## 5.6 Prime Numbers

### Theorem 5.7: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be uniquely represented as a product of prime numbers, up to the order of the factors.

Uniqueness is understood after factoring into primes.

**Proof**:

**Existence**: Every positive integer has a prime factor (by the well-ordering principle).
We can factor any $n > 1$ as $n = p_1p_2\dots p_k$ where each $p_i$ is prime.

**Uniqueness**: Suppose $n = p_1p_2\dots p_k = q_1q_2\dots q_m$ where $p_i, q_j$ are primes.
If $p_1 \mid q_1q_2\dots q_m$, then $p_1$ must divide some $q_j$ (by property of primes).
Since $p_1$ is prime, $p_1 \mid q_j$ implies $p_1 = q_j$.
Thus one prime from the left factors equals one prime from the right factors.

Removing equal factors and repeating this argument shows all factors match up.

∎

## 5.7 Congruences

### Theorem 5.8: Properties of Congruences

**Statement**: For integers $a, b, c, d$ and positive integers $m, n$:
1. $a \equiv b \pmod{m} \iff m \mid (a - b)$
2. $a \equiv b \pmod{m} \implies a + c \equiv b + c \pmod{m}$
3. $a \equiv b \pmod{m} \text{ and } c \equiv d \pmod{m} \implies ac \equiv bd \pmod{m}$
4. $a \equiv b \pmod{m} \implies a^k \equiv b^k \pmod{m}$ for $k \ge 1$
5. $a \equiv b \pmod{m} \text{ and } a \equiv b \pmod{n} \implies a \equiv b \pmod{\text{lcm}(m, n)}$

**Proof**:

1. By definition, $a \equiv b \pmod{m}$ means $a - b$ is a multiple of $m$.
2. $a \equiv b \pmod{m} \implies m \mid (a - b)$. Then $m \mid (a + c - (b + c)) = a - b$.
3. $a \equiv b \pmod{m} \implies a = b + km$.
   $ac = (b + km)c = bc + kmc = bc + m(kc)$.
   Similarly $bd + m(kd) = bd + m(kd)$.
   So $ac - bd = bc + m(kc) - bd - m(kd) = b(c - d) + m(kc - kd)$.
   Since $c \equiv d \pmod{m}$, $c - d = nm$, so $ac - bd = b(nm) + m(kc - kd) = m(bn + kc - kd)$.
   Thus $ac \equiv bd \pmod{m}$.
4. By induction, $a^k \equiv b^k \pmod{m}$.
5. $a \equiv b \pmod{m} \implies m \mid (a - b)$.
   $a \equiv b \pmod{n} \implies n \mid (a - b)$.
   Thus $\text{lcm}(m, n) \mid \gcd(m, n)(a - b)$, so $\text{lcm}(m, n) \mid (a - b)$.

∎
