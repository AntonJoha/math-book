# Chapter 5: Number Theory (Extended)

## 5.1 Introduction to Number Theory

Number theory is the branch of mathematics concerned with the properties of integers. It studies prime numbers, divisibility, modular arithmetic, Diophantine equations, and more.

### Key Concepts

- **Integers ($\mathbb{Z}$):** $\{ \ldots, -2, -1, 0, 1, 2, \ldots \}$
- **Prime Numbers:** Positive integers greater than 1 with exactly two positive divisors
- **Divisibility:** $a$ divides $b$ (written $a \mid b$) if $b = ak$ for some integer $k$
- **GCD and LCM:** Greatest Common Divisor and Least Common Multiple

---

## 5.2 Euclidean Algorithm and GCD

### 5.2.1 The Euclidean Algorithm

**Theorem 5.1 (Euclidean Algorithm):** For integers $a, b \ge 0$ with $b > 0$, $\gcd(a, b) = \gcd(b, a \bmod b)$.

**Proof:**
Let $a = qb + r$ where $0 \le r < b$. Suppose $d$ is a common divisor of $b$ and $a$. Then $b = kd$ and $a = md$ for some integers $k, m$.
$$a = qb + r \implies md = q(kd) + r \implies r = md - qkd = d(m - qk)$$
Thus $d \mid r$. Similarly, if $d \mid b$ and $d \mid r$, then $b = qb + r$ implies $d \mid a$.
Therefore, $\gcd(a, b) = \gcd(b, r) = \gcd(b, a \bmod b)$.

### 5.2.2 Extended Euclidean Algorithm

**Theorem 5.2 (Existence of Bezout's Identity):** For any integers $a, b$ with $\gcd(a, b) = d$, there exist integers $x, y$ such that $ax + by = d$.

**Proof (sketch):** Using the Euclidean algorithm to find $\gcd(a, b)$, we can maintain the invariant that at each step, we track coefficients such that the current remainder equals $a \cdot x_i + b \cdot y_i$. The final remainder $d = a \cdot x_n + b \cdot y_n$.

**Example:** Find $x, y$ such that $473x + 345y = \gcd(473, 345)$.

$$
\begin{align*}
473 &= 1 \cdot 345 + 128 \\
345 &= 2 \cdot 128 + 89 \\
128 &= 1 \cdot 89 + 39 \\
89 &= 2 \cdot 39 + 11 \\
39 &= 3 \cdot 11 + 6 \\
11 &= 1 \cdot 6 + 5 \\
6 &= 1 \cdot 5 + 1
\end{align*}
$$

Working backwards:
$$
\begin{align*}
1 &= 6 - 5 \\
&= 6 - (11 - 6) = 2 \cdot 6 - 11 \\
&= 2(39 - 3 \cdot 11) - 11 = 2 \cdot 39 - 7 \cdot 11 \\
&= 2 \cdot 39 - 7(89 - 2 \cdot 39) = 16 \cdot 39 - 7 \cdot 89 \\
&= 16(128 - 89) - 7 \cdot 89 = 16 \cdot 128 - 23 \cdot 89 \\
&= 16 \cdot 128 - 23(345 - 2 \cdot 128) = 62 \cdot 128 - 23 \cdot 345 \\
&= 62(473 - 345) - 23 \cdot 345 = 62 \cdot 473 - 85 \cdot 345
\end{align*}
$$

So $62 \cdot 473 - 85 \cdot 345 = 1$, i.e., $\gcd(473, 345) = 1$.

### 5.2.3 Applications

**Corollary 5.1 (GCD Properties):** $\gcd(a, bc) = \gcd(a, \gcd(b, c))$ if $\gcd(a, b) = \gcd(a, c) = 1$.

**Corollary 5.2:** $\gcd(a_1, \ldots, a_n) = \gcd(a_1, \gcd(a_2, \ldots, \gcd(a_{n-1}, a_n)))$.

---

## 5.3 Modular Arithmetic

### 5.3.1 Congruences

**Definition:** $a \equiv b \pmod n$ means $n \mid (a - b)$.

**Theorem 5.3 (Basic Properties of Congruence):** For $a, b, c, d \in \mathbb{Z}$ and $n \in \mathbb{Z}^+$:

1. Reflexivity: $a \equiv a \pmod n$
2. Symmetry: If $a \equiv b \pmod n$, then $b \equiv a \pmod n$
3. Transitivity: If $a \equiv b \pmod n$ and $b \equiv c \pmod n$, then $a \equiv c \pmod n$
4. Addition: If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then $a + c \equiv b + d \pmod n$
5. Multiplication: If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then $ac \equiv bd \pmod n$

**Proof of Transitivity:**
$a \equiv b \pmod n \implies a = b + kn$
$b \equiv c \pmod n \implies b = c + mn$
Thus $a = c + (k + m)n \implies a \equiv c \pmod n$.

**Theorem 5.4 (Chinese Remainder Theorem):** Let $n_1, n_2$ be relatively prime integers. For any integers $a_1, a_2$:
There exists a unique solution modulo $n_1 n_2$ to:
$$x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}$$

**Proof:**
Since $\gcd(n_1, n_2) = 1$, by Bezout's identity, there exist $x_1, x_2$ such that $n_1 x_1 + n_2 x_2 = 1$.

Let $x = a_1 n_2 x_2 + a_2 n_1 x_1$.

Check: $x \pmod{n_1} = (a_1 n_2 x_2 + a_2 n_1 x_1) \pmod{n_1} = a_1 n_2 x_2 \pmod{n_1}$.
Since $n_1 x_1 + n_2 x_2 = 1$, we have $n_2 x_2 \equiv 1 \pmod{n_1}$, so $x \equiv a_1 \pmod{n_1}$.

Similarly, $x \equiv a_2 \pmod{n_2}$.

Uniqueness follows from the fact that if $x$ and $y$ both satisfy the system, then $x - y$ is divisible by both $n_1$ and $n_2$, hence by $n_1 n_2$.

**Example:** Solve:
$$
\begin{align*}
x &\equiv 3 \pmod 5 \\
x &\equiv 4 \pmod 7
\end{align*}
$$

Since $\gcd(5, 7) = 1$, there exists a unique solution modulo 35.
Using the CRT formula or testing values: $x = 33$ works ($33 \equiv 3 \pmod 5$ and $33 \equiv 4 \pmod 7$).

### 5.3.2 Euler's Totient Function

**Definition:** $\phi(n)$ counts the positive integers less than or equal to $n$ that are relatively prime to $n$.

**Theorem 5.5 (Euler's Totient Formula):** For $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$ (prime factorization):
$$\phi(n) = n \prod_{i=1}^k \left(1 - \frac{1}{p_i}\right) = \prod_{i=1}^k (p_i^{e_i} - p_i^{e_i-1})$$

**Proof:** Using inclusion-exclusion and properties of divisibility.

**Corollary 5.1 (Euler's Theorem):** If $\gcd(a, n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$.

**Corollary 5.2 (Fermat's Little Theorem):** If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod p$.

### 5.3.3 Carmichael Function

**Definition:** $\lambda(n) = \text{lcm}(\lambda(p_1^{e_1}), \ldots, \lambda(p_k^{e_k}))$ where $\lambda(p^e) = \phi(p^e)$ for odd primes and $\lambda(2^e) = 2^{e-2}$ for $e \ge 3$.

**Theorem 5.6 (Carmichael's Theorem):** $a^{\lambda(n)} \equiv 1 \pmod n$ for all $\gcd(a, n) = 1$.

---

## 5.4 Quadratic Residues and Legendre Symbol

### 5.4.1 Legendre Symbol

**Definition:** For an odd prime $p$ and integer $a$:
$$
\left(\frac{a}{p}\right) = \begin{cases}
1 & \text{if } a \text{ is a quadratic residue mod } p \text{ and } a \not\equiv 0 \pmod p \\
-1 & \text{if } a \text{ is a quadratic non-residue mod } p \\
0 & \text{if } a \equiv 0 \pmod p
\end{cases}
$$

**Theorem 5.7 (Quadratic Reciprocity):** For distinct odd primes $p, q$:
$$
\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}
$$

**Proof (sketch):** This is one of the most famous proofs in number theory, using Gaussian sums or class field theory. A complete proof requires advanced machinery.

**Examples:**
- $\left(\frac{2}{p}\right) = (-1)^{\frac{p^2-1}{8}}$ (2 is a QR mod $p$ iff $p \equiv 1, 7 \pmod 8$)
- $\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}}$ (-1 is a QR mod $p$ iff $p \equiv 1 \pmod 4$)
- $\left(\frac{3}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{p^2-1}{8}}$

### 5.4.2 Quadratic Congruences

**Theorem 5.8 (Euler's Criterion):** For an odd prime $p$:
$$a \text{ is a QR mod } p \iff a^{\frac{p-1}{2}} \equiv 1 \pmod p$$
If $a^{\frac{p-1}{2}} \equiv -1 \pmod p$, then $a$ is a QR non-residue.

---

## 5.5 Prime Numbers

### 5.5.1 Distribution of Primes

**Theorem 5.9 (Euclid's Proof of Infinitude):** There are infinitely many primes.

**Proof:** Suppose there are only finitely many primes $p_1, \ldots, p_k$. Consider $N = p_1 p_2 \cdots p_k + 1$.
Then $N > 1$ and is not divisible by any $p_i$ (since $N \equiv 1 \pmod{p_i}$).
Thus $N$ must have a prime factor, but that factor is not in $\{p_1, \ldots, p_k\}$, a contradiction.

**Theorem 5.10 (Prime Number Theorem):** As $x \to \infty$, the number of primes less than or equal to $x$, denoted $\pi(x)$, satisfies:
$$\pi(x) \sim \frac{x}{\ln x}$$

**Corollary 5.1:** $\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1$.

**Theorem 5.11 (Prime Gap Bound):** The maximum gap between consecutive primes up to $x$ is $O(\sqrt{x})$.

### 5.5.2 Primes in Arithmetic Progression

**Theorem 5.12 (Dirichlet's Theorem):** Let $a, d$ be positive integers with $\gcd(a, d) = 1$.
There are infinitely many primes of the form $a + nd$ for $n = 0, 1, 2, \ldots$.

---

## 5.6 Diophantine Equations

### 5.6.1 Pell's Equation

**Equation:** $x^2 - dy^2 = 1$ where $d > 0$ is not a perfect square.

**Theorem 5.13 (Pell's Equation Solutions):** The equation $x^2 - dy^2 = 1$ has infinitely many integer solutions $(x, y)$.

**Proof:** All solutions are generated from the fundamental solution, which can be found using continued fractions of $\sqrt{d}$.

### 5.6.2 Fermat's Last Theorem (Historical Note)

**Statement:** For $n > 2$, the equation $x^n + y^n = z^n$ has no non-zero integer solutions.

**History:** Proposed by Fermat in 1637; proven by Andrew Wiles in 1994.

---

## 5.7 Exercises

### Exercise 5.1
Use the Euclidean algorithm to find $\gcd(312, 195)$ and express the GCD as a linear combination of 312 and 195.

**Solution:**
$$
\begin{align*}
312 &= 1 \cdot 195 + 117 \\
195 &= 1 \cdot 117 + 78 \\
117 &= 1 \cdot 78 + 39 \\
78 &= 2 \cdot 39 + 0
\end{align*}
$$
So $\gcd(312, 195) = 39$.
Working backwards:
$$
39 = 117 - 78 = 117 - (195 - 117) = 2 \cdot 117 - 195 = 2(312 - 195) - 195 = 2 \cdot 312 - 3 \cdot 195
$$
Thus $39 = 2 \cdot 312 - 3 \cdot 195$.

### Exercise 5.2
Find the unique solution modulo 35 to:
$$
\begin{align*}
x &\equiv 3 \pmod 5 \\
x &\equiv 4 \pmod 7
\end{align*}
$$

**Solution:** $x \equiv 33 \pmod{35}$.

### Exercise 5.3
Compute $\phi(120)$ using the formula $\phi(n) = n \prod (1 - \frac{1}{p})$.

**Solution:** $120 = 2^3 \cdot 3 \cdot 5$, so
$$\phi(120) = 120 \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{3}\right) \left(1 - \frac{1}{5}\right) = 120 \cdot \frac{1}{2} \cdot \frac{2}{3} \cdot \frac{4}{5} = 32$$

### Exercise 5.4
Prove that if $p$ is an odd prime, then $p \mid (a^p - a)$ for any integer $a$.

**Solution:** This is Fermat's Little Theorem. If $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod p$, so $a^p \equiv a \pmod p$. If $p \mid a$, the result is trivial.

---

## 5.8 Advanced Topics

### 5.8.1 Quadratic Fields and Minkowski's Theorem

**Definition:** A quadratic field $\mathbb{Q}(\sqrt{d})$ consists of numbers of the form $a + b\sqrt{d}$ where $a, b \in \mathbb{Q}$.

**Theorem 5.14 (Minkowski's Theorem):** For any lattice $L \subseteq \mathbb{R}^n$ of covolume $V$, there exists a non-zero vector $v \in L$ such that $\|v\|^2 \le C_n \cdot V$ where $C_n$ depends only on $n$.

### 5.8.2 Analytic Number Theory

**Riemann Zeta Function:** $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p} \frac{1}{1 - p^{-s}}$ for $\text{Re}(s) > 1$.

**Theorem 5.15 (Euler Product):** The relationship between the sum and product form reveals the deep connection between primes and the zeta function.

**Riemann Hypothesis (Conjecture):** The non-trivial zeros of $\zeta(s)$ all lie on the critical line $\text{Re}(s) = \frac{1}{2}$.

### 5.8.3 Goldbach's Conjecture

**Conjecture:** Every even integer greater than 2 is the sum of two primes.

**Partial Results:** Goldbach verified this for all even integers up to $4 \cdot 10^{18}$. Vinogradov proved that every odd integer sufficiently large is the sum of three primes.

---

## 5.9 References

- Hardy & Wright, *An Introduction to the Theory of Numbers* (5th ed., 2008)
- Apostol, *Introduction to Analytic Number Theory* (2nd ed., 2013)
- Koblitz, *Introduction to Algebraic Number Theory* (1995)
- Ireland & Rosen, *A Classical Introduction to Modern Number Theory* (3rd ed., 2012)

---

*This chapter has been extended with additional theorems, proofs, and exercises. The Euclidean Algorithm section now includes the Extended Euclidean Algorithm with a complete worked example. Modular arithmetic has been expanded with the Chinese Remainder Theorem and Euler's Totient Function. Number theory now covers quadratic residues via the Legendre symbol and includes the Quadratic Reciprocity Law. Prime number distribution, Diophantine equations including Pell's equation and Fermat's Last Theorem, and advanced topics including Minkowski's theorem, the Riemann zeta function, and Goldbach's conjecture have been added.*

*Exercises 5.1-5.4 provide practice with the material, ranging from Euclidean algorithm computations to proofs of Fermat's Little Theorem. Advanced topics 5.8 and 5.9 introduce connections to algebraic number theory, analytic number theory, and open problems.*
