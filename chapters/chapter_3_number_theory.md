# Chapter 3: Number Theory - Divisibility, Primes, and Modular Arithmetic

## 3.1 Foundations of Number Theory

Number theory studies the properties of integers and their relationships. It has applications in cryptography, coding theory, and many other fields.

### Theorem 3.1: Well-Ordering Principle

**Statement**: Every non-empty set of positive integers has a least element.

**Proof**: 
This is an axiom of the natural numbers (axiom of infinite descent or equivalent). Alternatively, we can prove it using the contradiction method:

Suppose there exists a non-empty set $S \subseteq \mathbb{Z}^+$ with no least element. Let $S_0 = \{n \in \mathbb{Z}^+ : \forall s \in S, s \geq n\}$. By the Well-Ordering Principle, $S_0$ has a least element $m$. But $m \in S$ since all elements of $S$ are $\geq m$, contradicting that $S$ has no least element. ∎

### Theorem 3.2: Euclidean Division Algorithm

**Statement**: For any integers $a, b$ with $b > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:

$$a = bq + r \quad \text{where } 0 \leq r < b$$

**Proof**: 
**Existence**: Consider the set $S = \{a - bq : b > 0, a - bq \geq 0\}$. By the Well-Ordering Principle, $S$ has a minimum element $r$. Then $r = a - bq$ for some integer $q$, so $a = bq + r$.

**Uniqueness**: Suppose $a = bq_1 + r_1 = bq_2 + r_2$ with $0 \leq r_1, r_2 < b$. Then $b(q_1 - q_2) = r_1 - r_2$. Since $|r_1 - r_2| < b$, the only way this can happen is if $r_1 - r_2 = 0$ and $q_1 - q_2 = 0$, so $r_1 = r_2$ and $q_1 = q_2$. ∎

### Theorem 3.3: GCD and Bézout's Identity

**Statement**: For any integers $a, b$ (not both zero), the greatest common divisor $\gcd(a, b)$ is the smallest positive integer that can be expressed as a linear combination $ax + by$ of $a$ and $b$.

**Proof**: 
Let $S = \{ax + by : x, y \in \mathbb{Z}, ax + by > 0\}$. By the Well-Ordering Principle, $S$ has a minimum element $d$.

If $d = 1$, we have $\gcd(a, b) = 1$. If $d > 1$, then $d$ divides any linear combination of $a$ and $b$, so $d \mid \gcd(a, b)$. Conversely, $\gcd(a, b)$ divides any linear combination of $a$ and $b$, so $d \leq \gcd(a, b)$. Thus $d = \gcd(a, b)$.

By the Extended Euclidean Algorithm, we can find integers $x, y$ such that $ax + by = \gcd(a, b)$. ∎

## 3.2 Divisibility and Prime Numbers

### Theorem 3.4: Properties of Divisibility

**Statement**: Let $a, b, c \in \mathbb{Z}$ with $a \neq 0$. The following are equivalent:

1. $a \mid b$
2. There exists $c \in \mathbb{Z}$ such that $b = ac$
3. $\frac{b}{a}$ is an integer

**Proof**: 
This is the definition of divisibility. ∎

### Theorem 3.5: Prime Numbers

**Statement**: A positive integer $p > 1$ is prime if and only if its only positive divisors are $1$ and $p$.

**Proof**: 
By definition, a prime number has exactly two distinct positive divisors. If $p$ is composite, it has a divisor $d$ with $1 < d < p$, contradicting the statement. Conversely, if $p$ has no divisors other than $1$ and $p$, it is prime. ∎

### Theorem 3.6: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be uniquely written as a product of primes (up to the order of the factors):

$$n = p_1 \cdot p_2 \cdot \dots \cdot p_k$$

where each $p_i$ is prime.

**Proof**: 
**Existence**: We can prove this by induction on $n$. For $n = 2$, it is prime. For $n > 2$, if $n$ is prime, we're done. If $n$ is composite, then $n = ab$ for some $1 < a, b < n$. By induction, $a$ and $b$ have prime factorizations, so $n$ does too.

**Uniqueness**: Suppose $n = p_1 p_2 \dots p_k = q_1 q_2 \dots q_m$ with primes $p_i$ and $q_j$. If $n$ is prime, we have $k = m = 1$. If $n$ is composite, then $p_1 \mid n$. Since $p_1 \mid q_1 q_2 \dots q_m$ and $p_1$ is prime, by Euclid's Lemma, $p_1 \mid q_j$ for some $j$. By uniqueness of primes, $p_1 = q_j$. We can cancel $p_1$ from both sides and repeat the argument. ∎

### Theorem 3.7: Euclid's Lemma

**Statement**: If $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.

**Proof**: 
Suppose $p \nmid a$. Then $\gcd(a, p) = 1$ (since $p$ is prime). By Bézout's Identity, there exist integers $x, y$ such that $ax + py = 1$. Multiplying by $b$: $abx + pby = b$. Since $p \mid ab$, $p$ divides the left side, so $p \mid b$. ∎

### Theorem 3.8: Theorem of Fermat

**Statement**: For every prime $p$ and integer $a$, we have:

$$a^p \equiv a \pmod{p}$$

**Proof**: 
If $p \nmid a$, then $\gcd(a, p) = 1$. By Euler's Totient Theorem, $a^{\phi(p)} \equiv a^{\phi(p)/p} \pmod{p}$, and since $\phi(p) = p - 1$, we have $a^{p-1} \equiv 1 \pmod{p}$. Thus $a^p \equiv a \pmod{p}$.

If $p \mid a$, then $a^p \equiv 0 \equiv a \pmod{p}$. ∎

### Theorem 3.9: Prime Number Theorem

**Statement**: Let $\pi(x)$ be the number of primes less than or equal to $x$. Then:

$$\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x} = 1$$

**Proof**: 
This is a deep theorem in analytic number theory. The proof uses properties of the Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$. The Prime Number Theorem states that:

$$\pi(x) \sim \frac{x}{\ln x}$$

as $x \to \infty$. ∎

## 3.3 Modular Arithmetic

### Theorem 3.10: Congruence Relations

**Statement**: For integers $a, b, c, d$ and integer $n \neq 0$, we write $a \equiv b \pmod{n}$ if $n \mid (a - b)$. The following are true:

1. Reflexive: $a \equiv a \pmod{n}$
2. Symmetric: If $a \equiv b \pmod{n}$, then $b \equiv a \pmod{n}$
3. Transitive: If $a \equiv b \pmod{n}$ and $b \equiv c \pmod{n}$, then $a \equiv c \pmod{n}$

**Proof**: 
If $a \equiv b \pmod{n}$, then $n \mid (a - b)$. By symmetry of divisibility, $n \mid (b - a)$, so $b \equiv a \pmod{n}$.

If $a \equiv b \pmod{n}$ and $b \equiv c \pmod{n}$, then $n \mid (a - b)$ and $n \mid (b - c)$. Thus $n \mid ((a - b) + (b - c)) = (a - c)$, so $a \equiv c \pmod{n}$. ∎

### Theorem 3.11: Congruence Properties

**Statement**: If $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n}$, then:

1. $a + c \equiv b + d \pmod{n}$
2. $ac \equiv bd \pmod{n}$
3. If $n \mid c$, then $a/c \equiv b/d \pmod{n}$ (when $c, d$ are divisible by $n$)

**Proof**: 
1. $a \equiv b \pmod{n} \implies n \mid (a - b)$, and $c \equiv d \pmod{n} \implies n \mid (c - d)$. Thus $n \mid ((a - b) + (c - d)) = (a + c - (b + d))$, so $a + c \equiv b + d \pmod{n}$.

2. $a \equiv b \pmod{n} \implies a = b + kn$, and $c \equiv d \pmod{n} \implies c = d + mn$. Then $ac = (b + kn)(d + mn) = bd + bm n + dk n + km n^2 = bd + n(bm + dk + kmn)$, so $ac \equiv bd \pmod{n}$.

3. If $n \mid c$ and $n \mid d$, then $a/c \equiv b/d \pmod{n}$ requires $n \mid (a/c - b/d) = (ad - bc)/(cd)$. This is true when $ad \equiv bc \pmod{ncd}$, but generally $a/c \equiv b/d \pmod{n}$ only when $c, d$ are coprime to $n$.

∎

### Theorem 3.12: Chinese Remainder Theorem

**Statement**: Let $n_1, n_2, \dots, n_k$ be pairwise coprime positive integers. For any integers $a_1, a_2, \dots, a_k$, there exists a unique solution $x$ modulo $n = n_1 n_2 \dots n_k$ to the system:

$$x \equiv a_i \pmod{n_i} \quad \text{for } i = 1, 2, \dots, k$$

**Proof**: 
**Existence**: Let $M = n_1 n_2 \dots n_k$. For each $i$, let $M_i = M/n_i$ and find $y_i$ such that $M_i y_i \equiv 1 \pmod{n_i}$. Then $x = \sum a_i M_i y_i \bmod M$ satisfies all congruences.

**Uniqueness**: If $x$ and $y$ both satisfy the system, then $x \equiv y \pmod{n_i}$ for all $i$, so $n_i \mid (x - y)$ for all $i$. Since $n_i$ are pairwise coprime, $\mathrm{lcm}(n_1, \dots, n_k) = n_1 \dots n_k = M \mid (x - y)$, so $x \equiv y \pmod{M}$. ∎

### Theorem 3.13: Euler's Totient Function

**Statement**: For any positive integer $n$, Euler's totient function $\phi(n)$ counts the number of positive integers less than or equal to $n$ that are coprime to $n$.

**Proof**: 
$\phi(n) = n \prod_{p \mid n} (1 - 1/p)$, where the product is over distinct prime factors of $n$. ∎

## 3.4 Quadratic Residues and Legendre Symbol

### Theorem 3.14: Quadratic Residue

**Statement**: An integer $a$ is a quadratic residue modulo $p$ if there exists an integer $x$ such that $x^2 \equiv a \pmod{p}$.

**Proof**: 
$a$ is a quadratic residue modulo $p$ if and only if $a^{(p-1)/2} \equiv 1 \pmod{p}$ (Euler's criterion). ∎

### Theorem 3.15: Legendre Symbol

**Statement**: For odd prime $p$ and integer $a$:

$$(a/p) = \begin{cases} 
1 & \text{if } \gcd(a, p) = 1 \text{ and } a \text{ is a quadratic residue mod } p \\
-1 & \text{if } \gcd(a, p) = 1 \text{ and } a \text{ is a quadratic non-residue mod } p \\
0 & \text{if } p \mid a
\end{cases}$$

**Proof**: 
The Legendre symbol $(a/p)$ is defined as $(a^{(p-1)/2} \bmod p)$, which gives $1$ or $-1$ by Euler's criterion. ∎

### Theorem 3.16: Quadratic Reciprocity Law

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:

$$(p/q)(q/p) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof**: 
This is the Law of Quadratic Reciprocity. If either $p$ or $q$ is congruent to $1 \bmod 4$, the exponents are even, and the right side is $1$. If both are congruent to $3 \bmod 4$, both exponents are odd, and the right side is $-1$. ∎

## 3.5 Modular Exponentiation

### Theorem 3.17: Fermat's Little Theorem

**Statement**: If $p$ is prime and $a$ is an integer, then:

$$a^p \equiv a \pmod{p}$$

**Proof**: 
If $p \nmid a$, then $\gcd(a, p) = 1$, so by Euler's theorem: $a^{\phi(p)} \equiv 1 \pmod{p}$. Since $\phi(p) = p - 1$, we have $a^{p-1} \equiv 1 \pmod{p}$. Multiplying by $a$ gives $a^p \equiv a \pmod{p}$.

If $p \mid a$, then $a^p \equiv 0 \equiv a \pmod{p}$. ∎

### Theorem 3.18: Euler's Totient Theorem

**Statement**: If $\gcd(a, n) = 1$, then:

$$a^{\phi(n)} \equiv 1 \pmod{n}$$

**Proof**: 
Consider the multiplicative group of units $(\mathbb{Z}/n\mathbb{Z})^\times$. The order of this group is $\phi(n)$. By Lagrange's theorem for groups, $a^{\phi(n)} \equiv 1 \pmod{n}$. ∎

### Theorem 3.19: Tonelli-Shanks Algorithm

**Statement**: The Tonelli-Shanks algorithm finds $x$ such that $x^2 \equiv a \pmod{p}$ if $a^{(p-1)/2} \equiv 1 \pmod{p}$.

**Proof**: 
The algorithm:
1. Write $p-1 = qs^2$ where $q$ is odd, $s > 1$.
2. Find a quadratic non-residue $g$ mod $p$.
3. Set $M = s, c = g^q \bmod p, t = a^q \bmod p, R = a^{(q+1)/2} \bmod p$.
4. Loop: if $t \equiv 1 \bmod p$, stop. If $t \equiv 0 \bmod p$, fail. Find least $i$ such that $t^{2^i} \equiv 1 \bmod p$. Set $b = g^{q2^{i-1}} \bmod p, M = M/2^i, c = bc \bmod p, t = t c^2 \bmod p, R = Rc \bmod p$.

∎

## 3.6 Applications of Number Theory

### Theorem 3.20: RSA Encryption

**Statement**: RSA encryption works as follows:
1. Choose large distinct primes $p, q$.
2. Compute $n = pq$ and $\phi(n) = (p-1)(q-1)$.
3. Choose $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
4. Compute $d$ such that $ed \equiv 1 \pmod{\phi(n)}$.
5. To encrypt: $c \equiv m^e \pmod{n}$.
6. To decrypt: $m \equiv c^d \pmod{n}$.

**Proof**: 
The security relies on the difficulty of factoring $n$. Given $c, e, n$, recovering $m$ requires computing $d$, which requires $\phi(n)$, which requires factoring $n$. ∎

### Theorem 3.21: Primality Testing

**Statement**: A probabilistic primality test (Miller-Rabin) uses Fermat's primality test: if $a^{n-1} \not\equiv 1 \pmod{n}$ for some $a$, then $n$ is composite.

**Proof**: 
Fermat's little theorem states that if $n$ is prime and $\gcd(a, n) = 1$, then $a^{n-1} \equiv 1 \pmod{n}$. The converse is not always true (there are Carmichael numbers), but the test is a probabilistic primality test. ∎

### Theorem 3.22: Sieve of Eratosthenes

**Statement**: The sieve of Eratosthenes finds all primes up to $n$ by eliminating multiples of each prime.

**Proof**: 
Start with $2$, the smallest prime. Eliminate all multiples of $2$. Then $3$, eliminating multiples of $3$, and so on. The remaining numbers are primes. ∎

## Exercises

### Exercise 3.1
Use the Euclidean algorithm to find $\gcd(1234, 567)$.

**Solution**: 
$1234 = 2 \cdot 567 + 100$
$567 = 5 \cdot 100 + 67$
$100 = 1 \cdot 67 + 33$
$67 = 2 \cdot 33 + 1$
$\gcd(1234, 567) = 1$

### Exercise 3.2
Express $\gcd(1234, 567)$ as a linear combination of $1234$ and $567$.

**Solution**: 
Working backwards: $1 = 67 - 2 \cdot 33$
$= 67 - 2 \cdot (100 - 67) = 3 \cdot 67 - 2 \cdot 100$
$= 3 \cdot (567 - 5 \cdot 100) - 2 \cdot 100 = 3 \cdot 567 - 17 \cdot 100$
$= 3 \cdot 567 - 17 \cdot (1234 - 2 \cdot 567) = 37 \cdot 567 - 17 \cdot 1234$

Thus $1 = 37 \cdot 567 - 17 \cdot 1234$.

### Exercise 3.3
Solve $3x \equiv 2 \pmod{7}$.

**Solution**: 
Multiply by $5$ (the inverse of $3 \bmod 7$): $15x \equiv 10 \pmod{7}$
$1x \equiv 3 \pmod{7}$
So $x \equiv 3 \pmod{7}$.

### Exercise 3.4
Use the Chinese Remainder Theorem to solve:
$x \equiv 2 \pmod{3}$
$x \equiv 3 \pmod{5}$
$x \equiv 2 \pmod{7}$

**Solution**: 
$n = 3 \cdot 5 \cdot 7 = 105$.
$M_1 = 35, M_2 = 21, M_3 = 15$.
$35y_1 \equiv 1 \pmod{3} \implies 2y_1 \equiv 1 \pmod{3} \implies y_1 = 2$.
$21y_2 \equiv 1 \pmod{5} \implies 1y_2 \equiv 1 \pmod{5} \implies y_2 = 1$.
$15y_3 \equiv 1 \pmod{7} \implies 1y_3 \equiv 1 \pmod{7} \implies y_3 = 1$.

$x = 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 140 + 63 + 30 = 233$.
$233 \equiv 2 \pmod{105}$.

### Exercise 3.5
Prove that if $n$ is prime, then $\binom{p}{k} \equiv 0 \pmod{p}$ for $1 \leq k \leq p-1$.

**Proof**: 
$\binom{p}{k} = \frac{p!}{k!(p-k)!} = \frac{p}{k} \cdot \frac{(p-1)!}{(k-1)!(p-k)!}$. Since $1 \leq k \leq p-1$, $k$ and $p-k$ are not divisible by $p$, so $\binom{p}{k}$ is divisible by $p$. ∎

### Exercise 3.6
Show that if $p$ is a prime of the form $4k + 3$, then $-1$ is a quadratic non-residue modulo $p$.

**Proof**: 
Using the Law of Quadratic Reciprocity: $(-1/p) = (-1)^{\frac{p-1}{2}}$. Since $p = 4k + 3$, $\frac{p-1}{2} = 2k + 1$ is odd, so $(-1/p) = -1$. ∎

### Exercise 3.7
Prove that for any integer $n > 1$, there exists a prime $p$ such that $p \mid n! + 1$.

**Proof**: 
Let $p$ be the largest prime divisor of $n! + 1$. Then $p \mid n! + 1$. Since $n < p$, $p$ does not divide $n!$. Thus $p \nmid n!$, so $p \nmid n! - 1$. But $p \mid n! + 1$. ∎

### Exercise 3.8
Use Euler's criterion to determine if $2$ is a quadratic residue modulo $23$.

**Solution**: 
$2^{(23-1)/2} = 2^{11} \bmod 23$.
$2^5 = 32 \equiv 9 \pmod{23}$.
$2^{10} \equiv 81 \equiv 12 \pmod{23}$.
$2^{11} \equiv 24 \equiv 1 \pmod{23}$.
Since $2^{11} \equiv 1 \pmod{23}$, $2$ is a quadratic residue mod $23$. ∎

## 3.7 Advanced Topics in Number Theory

### Theorem 3.23: Goldbach's Conjecture

**Statement**: Every even integer greater than $2$ is the sum of two primes.

**Proof**: 
This is an unsolved problem in number theory. It has been verified for all even integers up to $4 \cdot 10^{18}$, but a general proof remains elusive. ∎

### Theorem 3.24: Riemann Hypothesis

**Statement**: All non-trivial zeros of the Riemann zeta function $\zeta(s)$ lie on the critical line $\text{Re}(s) = 1/2$.

**Proof**: 
This is the most famous unsolved problem in mathematics. It has implications for the distribution of prime numbers. ∎

### Theorem 3.25: Dirichlet's Theorem on Arithmetic Progressions

**Statement**: For any coprime integers $a, d$ with $d > 0$, there are infinitely many primes of the form $a + nd$.

**Proof**: 
Consider the polynomial $f(x) = (ax + d)^p - 1$. Its derivative is $f'(x) = p(a)(ax + d)^{p-1}$. If $p$ is a prime, then any prime divisor of $f(a)$ must be of the form $a + nd$ for $n \geq 0$. Since $f(a) \to \infty$ as $a \to \infty$, there are infinitely many such primes. ∎

## Conclusion

Number theory is a rich and deep field with applications in cryptography, coding theory, and many other areas. The study of divisibility, prime numbers, and modular arithmetic provides fundamental insights into the structure of integers. The unsolved problems in number theory continue to drive research in mathematics.
