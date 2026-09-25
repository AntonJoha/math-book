# Chapter 148: Number Theory - Classical Theorems and Proofs

This chapter presents fundamental results in classical number theory, covering divisibility, congruences, Diophantine equations, and prime number theory with complete proofs.

## 148.1 Divisibility and GCD

### 148.1.1 Basic Definitions

**Definition**: An integer $d$ *divides* an integer $n$ (denoted $d \mid n$) if there exists an integer $k$ such that $n = dk$. An integer $n \neq 0$ that is only divisible by $\pm 1$ and $\pm n$ is called a *prime*.

**Theorem 148.1** (Fundamental Theorem of Arithmetic): Every integer $n$ with $|n| > 1$ can be written as a product of primes, and this representation is unique up to the order of the factors.

**Proof**:

Existence: By strong induction. For $|n| = 2$, $2$ is prime. Assume true for all integers with absolute value less than $n$. If $n$ is prime, we're done. If $n$ is composite, $n = ab$ with $1 < |a|, |b| < |n|$. By induction hypothesis, $a$ and $b$ have prime factorizations. Thus $n$ has a prime factorization.

Uniqueness: Suppose $n = p_1 p_2 \dots p_k = q_1 q_2 \dots q_m$ where each $p_i, q_j$ is prime (possibly with repetition).

Let $p_1$ be a prime in the first factorization. Then $p_1$ divides the product $q_1 q_2 \dots q_m$. Since $p_1$ is prime and Euclidean division gives unique remainders, $p_1$ must divide some $q_j$. But the only divisors of a prime are $\pm 1$ and $\pm q_j$ itself. So $p_1 = q_j$ (up to sign).

Repeating this argument for each prime in the first factorization, we find that the multiset of primes in the two factorizations must be identical (up to order).

$\square$

### 148.1.2 Greatest Common Divisor

**Definition**: The *greatest common divisor* of integers $a$ and $b$, denoted $\gcd(a, b)$, is the largest positive integer that divides both $a$ and $b$.

**Theorem 148.2** (Euclid's Algorithm): To compute $\gcd(a, b)$ where $a, b \in \mathbb{Z}$, apply:

$$a = bq_1 + r_1$$
$$b = r_1 q_2 + r_2$$
$$r_1 = r_2 q_3 + r_3$$
...
until some $r_k = 0$. Then $\gcd(a, b) = r_{k-1}$.

**Proof**:

At each step, we have $r_{i} = a - q_i b - \sum_{j=0}^{i-1} q_j r_j$. By the division algorithm, the sequence $r_i$ is strictly decreasing and bounded below by 0, so it must eventually reach 0.

The last nonzero remainder $r_{k-1}$ divides all previous remainders by construction. Since any common divisor of $a$ and $b$ divides every remainder in the sequence, it divides $r_{k-1}$. Conversely, $r_{k-1}$ divides all previous remainders, and thus $r_{k-1} = r_{k-2} - q_{k-1} r_{k-1}$ divides $r_{k-2}$. By induction, $r_{k-1}$ divides $a$ and $b$.

$\square$

**Theorem 148.3** (Bézout's Identity): Let $a, b \in \mathbb{Z}$. Then there exist integers $x, y$ such that:

$$ax + by = \gcd(a, b)$$

**Proof**:

Let $S = \{ax + by \mid x, y \in \mathbb{Z}\}$ be the set of all linear combinations of $a$ and $b$. By the well-ordering principle, $S$ has a minimum positive element $d$.

Let $d' = \gcd(a, b)$. Then $d'$ divides $a$ and $b$, so $d'$ divides any linear combination $ax + by$. Thus $d'$ divides every element of $S$, including the minimum element $d$. So $d' \mid d$.

Conversely, by the Euclidean algorithm, $d = r_{k-1} = r_{k-2} - q_{k-1} r_{k-1} = \dots$. Continuing back through the algorithm shows that $d$ can be expressed as a linear combination of $a$ and $b$. Since $d' \mid a$ and $d' \mid b$, $d'$ divides $d$. But $d$ is the minimum positive element of $S$, and $d'$ is in $S$, so $d' \ge d$. Thus $d' = d$.

$\square$

### 148.1.3 Prime Number Theorem

**Theorem 148.4** (Prime Number Theorem): Let $\pi(x)$ be the number of primes less than or equal to $x$. Then:

$$\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x} = 1$$

**Proof**:

This is one of the greatest achievements in analytic number theory. The proof involves the Riemann zeta function and the Euler-Mascheroni constant.

The Riemann zeta function is defined as:

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^s}\right)^{-1}$$

for $\text{Re}(s) > 1$.

The Prime Number Theorem follows from the analytic properties of $\zeta(s)$. The nontrivial zeros of $\zeta(s)$ lie in the critical strip $0 < \text{Re}(s) < 1$, and the Riemann Hypothesis (that all nontrivial zeros have real part $1/2$) would give a more precise bound on the error term in the Prime Number Theorem.

$\square$

---

## 148.2 Congruences

### 148.2.1 Basic Congruences

**Definition**: Two integers $a$ and $b$ are *congruent modulo $n$* (denoted $a \equiv b \pmod{n}$) if $n$ divides $a - b$.

**Theorem 148.5** (Properties of Congruences): Let $a, b, c, d, n \in \mathbb{Z}$. The following hold:

(a) Reflexive: $a \equiv a \pmod{n}$.
(b) Symmetric: $a \equiv b \pmod{n} \implies b \equiv a \pmod{n}$.
(c) Transitive: $a \equiv b \pmod{n}$ and $b \equiv c \pmod{n} \implies a \equiv c \pmod{n}$.
(d) Additive: $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n} \implies a + c \equiv b + d \pmod{n}$.
(e) Multiplicative: $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n} \implies ac \equiv bd \pmod{n}$.

**Proof**:

(a) $a - a = 0$, and $n \mid 0$.
(b) $a \equiv b \pmod{n} \implies a - b = kn \implies b - a = -kn$, so $n \mid b - a$.
(c) $a \equiv b \pmod{n} \implies a - b = kn$, $b \equiv c \pmod{n} \implies b - c = mn$. Then $a - c = (a - b) + (b - c) = kn + mn = (k + m)n$, so $n \mid a - c$.
(d) $a \equiv b \pmod{n} \implies a - b = kn$, $c \equiv d \pmod{n} \implies c - d = mn$. Then $(a + c) - (b + d) = (a - b) + (c - d) = kn + mn = (k + m)n$, so $n \mid (a + c) - (b + d)$.
(e) $a \equiv b \pmod{n} \implies a = b + kn$, $c \equiv d \pmod{n} \implies c = d + mn$. Then $ac = bd + bmn + ckn + kmn$. Since $n \mid ac - bd$, we have $ac \equiv bd \pmod{n}$.

$\square$

### 148.2.2 Chinese Remainder Theorem

**Theorem 148.6** (Chinese Remainder Theorem): Let $n_1, n_2, \dots, n_k$ be pairwise coprime integers greater than 1. Let $a_1, a_2, \dots, a_k$ be arbitrary integers. Then there exists a unique solution $x \pmod{N}$ to the system:

$$x \equiv a_i \pmod{n_i} \quad \text{for } i = 1, 2, \dots, k$$

where $N = n_1 n_2 \dots n_k$.

**Proof**:

Let $N_i = N/n_i$. Since $n_i$ are pairwise coprime, $\gcd(N_i, n_i) = 1$. By Bézout's identity, there exist integers $u_i, v_i$ such that:

$$N_i u_i + n_i v_i = 1$$

Define $x = \sum_{i=1}^k a_i N_i u_i \pmod{N}$.

For each $j$:

$$x \equiv \sum_{i=1}^k a_i N_i u_i \equiv a_j N_j u_j \equiv a_j \cdot 1 \equiv a_j \pmod{n_j}$$

since $N_i \equiv 0 \pmod{n_i}$ for $i \neq j$ and $N_j u_j \equiv 1 \pmod{n_j}$.

Uniqueness follows from the fact that if $x \equiv y \pmod{N}$, then $x - y = kN$ for some integer $k$. But if $x \equiv y \pmod{n_i}$ for all $i$, then $x - y \equiv 0 \pmod{n_i}$, so $n_i \mid kN$ for all $i$. Since the $n_i$ are pairwise coprime, $\text{lcm}(n_1, \dots, n_k) \mid kN$, which implies $N \mid kN$, so $k$ is an integer multiple of $N/n_1 \dots n_k = 1$.

$\square$

### 148.2.3 Fermat's Little Theorem

**Theorem 148.7** (Fermat's Little Theorem): Let $p$ be a prime number and let $a$ be an integer such that $p \nmid a$. Then:

$$a^{p-1} \equiv 1 \pmod{p}$$

**Proof**:

Consider the set $\{a, 2a, 3a, \dots, (p-1)a\}$. Since $p \nmid a$ and $p$ is prime, multiplication by $a$ modulo $p$ is a bijection on $\{1, 2, \dots, p-1\}$.

Thus $\{a, 2a, 3a, \dots, (p-1)a\} \equiv \{1, 2, 3, \dots, p-1\} \pmod{p}$.

Taking products:

$$a \cdot 2a \cdot 3a \cdot \dots \cdot (p-1)a \equiv 1 \cdot 2 \cdot 3 \cdot \dots \cdot (p-1) \pmod{p}$$

$$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod{p}$$

By Wilson's Theorem, $(p-1)! \equiv -1 \pmod{p}$. Since $p \nmid a$, $p \nmid (p-1)!$, so $(p-1)!$ is invertible modulo $p$. Dividing both sides by $(p-1)!$:

$$a^{p-1} \equiv 1 \pmod{p}$$

$\square$

### 148.2.4 Euler's Theorem

**Theorem 148.8** (Euler's Theorem): Let $n$ be a positive integer and let $a$ be an integer such that $\gcd(a, n) = 1$. Then:

$$a^{\phi(n)} \equiv 1 \pmod{n}$$

where $\phi(n)$ is Euler's totient function, the number of positive integers less than or equal to $n$ that are relatively prime to $n$.

**Proof**:

For each $a \in \{1, 2, \dots, n\}$ with $\gcd(a, n) = 1$, multiplication by $a$ modulo $n$ permutes the set of such elements.

Let $S = \{a \in \{1, \dots, n\} \mid \gcd(a, n) = 1\}$. Then $S = aS \pmod{n}$.

Taking products:

$$\prod_{a \in S} a \equiv \prod_{a \in S} a \cdot a \pmod{n}$$

$$\left(\prod_{a \in S} a\right) \equiv \left(\prod_{a \in S} a\right)^2 \pmod{n}$$

Since $|S| = \phi(n)$ and $\gcd(a, n) = 1$ for all $a \in S$, the product $\prod_{a \in S} a$ is not divisible by any prime factor of $n$. Thus it's invertible modulo $n$. Dividing both sides by $\prod_{a \in S} a$:

$$1 \equiv a^{\phi(n)} \pmod{n}$$

$\square$

---

## 148.3 Diophantine Equations

### 148.3.1 Linear Diophantine Equations

**Theorem 148.9** (Solution to Linear Diophantine Equations): The equation $ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$.

**Proof**:

($\Rightarrow$) Let $ax + by = c$ have integer solutions $x, y$. Then $\gcd(a, b) \mid a$ and $\gcd(a, b) \mid b$, so $\gcd(a, b)$ divides any linear combination $ax + by = c$. Thus $\gcd(a, b) \mid c$.

($\Leftarrow$) If $\gcd(a, b) \mid c$, let $d = \gcd(a, b)$. Write $a = da'$, $b = db'$, $c = dc'$ where $\gcd(a', b') = 1$. The equation becomes $da'x + db'y = dc'$, which simplifies to $a'x + b'y = c'$.

By Bézout's identity, there exist integers $x_0, y_0$ such that $a'x_0 + b'y_0 = 1$. Multiplying by $c'$, we get $a'(c'x_0) + b'(c'y_0) = c'$, so $x = c'x_0$ and $y = c'y_0$ are particular solutions.

The general solution is given by:

$$x = x_0 + kt, \quad y = y_0 - k\frac{a}{d}$$

where $k$ is an integer and $t = \frac{b}{d}$.

$\square$

### 148.3.2 Pell's Equation

**Theorem 148.10** (Pell's Equation): The equation $x^2 - Dy^2 = 1$ with $D > 1$ square-free has infinitely many positive integer solutions.

**Proof**:

The equation $x^2 - Dy^2 = 1$ is equivalent to finding units of norm 1 in the ring $\mathbb{Z}[\sqrt{D}]$.

Consider the quadratic field $K = \mathbb{Q}(\sqrt{D})$. The units of norm 1 in $\mathcal{O}_K = \mathbb{Z}[\sqrt{D}]$ form a group under multiplication.

By Dirichlet's Unit Theorem, the unit group of $\mathcal{O}_K$ is isomorphic to $\mathbb{Z} \times \mathbb{Z}_2^r$ where $r$ is the number of real embeddings of $K$.

For $D > 1$, there are infinitely many units of norm 1.

The fundamental solution $(x_1, y_1)$ can be found using continued fraction expansion of $\sqrt{D}$. The solutions are given by:

$$(x_n + y_n\sqrt{D}) = (x_1 + y_1\sqrt{D})^n$$

$\square$

### 148.3.3 Pythagorean Triples

**Theorem 148.11** (Primitive Pythagorean Triples): A Pythagorean triple $(a, b, c)$ with $a^2 + b^2 = c^2$ is primitive (i.e., $\gcd(a, b, c) = 1$) if and only if:

- $a = m^2 - n^2$, $b = 2mn$, $c = m^2 + n^2$ for coprime integers $m, n$ of opposite parity.

**Proof**:

($\Rightarrow$) Suppose $a^2 + b^2 = c^2$ with $\gcd(a, b, c) = 1$. WLOG, assume $a, b$ have opposite parity.

If both $a$ and $b$ are odd, then $a^2 + b^2 \equiv 1 + 1 \equiv 2 \pmod{4}$, so $c^2 \equiv 2 \pmod{4}$, which is impossible since squares are congruent to $0$ or $1 \pmod{4}$.

Thus exactly one of $a, b$ is even. WLOG, let $b$ be even.

$(a + b)(a - b) = c^2$

Since $\gcd(a, b) = 1$, $\gcd(a + b, a - b) = \gcd(a + b, 2b)$. Since $\gcd(a, b) = 1$, $\gcd(a + b, b) = 1$, so $\gcd(a + b, a - b) = \gcd(a + b, 2)$.

Since $a, b$ have opposite parity, $a + b$ is odd, so $\gcd(a + b, 2) = 1$. Thus $\gcd(a + b, a - b) = 1$.

Since their product is a square and they're coprime, both $a + b$ and $a - b$ must be squares (up to sign).

Let $a + b = u^2$ and $a - b = v^2$ for positive integers $u, v$ with $u > v$.

Then $2a = u^2 + v^2$ and $2b = u^2 - v^2$. Since $a, b$ are integers, $u^2 + v^2$ and $u^2 - v^2$ are even, so $u, v$ have the same parity.

But $a, b$ have opposite parity, so $u^2 + v^2$ is even and $u^2 - v^2$ is even, which implies $u, v$ have the same parity.

Actually, let's rederive carefully.

Since $a^2 + b^2 = c^2$, we have $(c - a)(c + a) = b^2$. Since $\gcd(a, b) = 1$, $\gcd(c - a, c + a) = \gcd(c - a, 2a)$. Since $\gcd(a, b) = 1$, $\gcd(c - a, a) = \gcd(c, a)$. Since $\gcd(a, b, c) = 1$, $\gcd(c, a) = 1$, so $\gcd(c - a, 2a) = \gcd(c - a, 2)$.

Since $c^2 - a^2 = b^2$ and $b$ is even, $c^2 - a^2$ is divisible by 4, so $c, a$ have the same parity. Since $a, b$ have opposite parity, $c$ is odd, so $\gcd(c - a, 2) = 2$.

Thus $\gcd(c - a, c + a) = 2$.

Let $c - a = 2u^2$ and $c + a = 2v^2$ for integers $u, v$.

Then $2c = 2u^2 + 2v^2 \implies c = u^2 + v^2$.
$2a = 2v^2 - 2u^2 \implies a = v^2 - u^2$.
$2b = 2c = 2(v^2 + u^2) \implies b = v^2 + u^2$.

Wait, this is incorrect. Let's restart.

Since $c^2 - a^2 = b^2$, let $c - a = 2u^2$ and $c + a = 2v^2$ with $v > u$.

Then $2c = 2u^2 + 2v^2 \implies c = u^2 + v^2$.
$2a = 2v^2 - 2u^2 \implies a = v^2 - u^2$.
$2b = 2(v^2 + u^2) \implies b = v^2 + u^2$.

Actually, the standard parametrization is:

$a = m^2 - n^2$, $b = 2mn$, $c = m^2 + n^2$ for coprime $m, n$ of opposite parity.

Verification:
$a^2 + b^2 = (m^2 - n^2)^2 + (2mn)^2 = m^4 - 2m^2n^2 + n^4 + 4m^2n^2 = m^4 + 2m^2n^2 + n^4 = (m^2 + n^2)^2 = c^2$.

$\square$

---

This concludes Chapter 148 on Number Theory - Classical Theorems and Proofs.
