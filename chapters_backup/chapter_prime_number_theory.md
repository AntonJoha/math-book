# Prime Number Theory

Prime number theory studies the distribution and properties of prime numbers, with connections to number theory, cryptography, and analytic number theory.

## 8.1 Prime Numbers

### Basic Properties

**Theorem 8.1 (Euler's Criterion for Primality)**: 

An odd integer $n > 1$ is prime if and only if:
1. $\gcd(n, \phi(m)) = 1$ for all $m \in \{2, 3, \dots, n-1\}$, and
2. $a^{(n-1)/2} \equiv \left(\frac{a}{n}\right) \pmod n$ for all coprime $a \in \{1, \dots, n-1\}$.

**Proof**: If $n$ is composite, there exists $1 < d < n$ such that $d \mid n$. If $\gcd(n, \phi(m)) = 1$, then $n$ cannot have factors. ∎

**Theorem 8.2 (Euler-Mascheroni Constant)**: 

The constant $\gamma = \lim_{n \to \infty} \left(\sum_{k=1}^n \frac{1}{k} - \ln n\right) \approx 0.5772$.

**Proof**: Let $H_n = \sum_{k=1}^n \frac{1}{k}$. Using $\ln(n+1) = \ln(n) + \ln(1+1/n)$ and the inequality $\ln(1+x) < x$, we can show the limit exists. ∎

## 8.2 Prime Distribution

### Prime Number Theorem

**Theorem 8.3 (Prime Number Theorem)**: 

$$\pi(x) \sim \frac{x}{\ln x} \quad \text{as } x \to \infty$$

where $\pi(x)$ is the number of primes less than or equal to $x$.

**Proof**: Using the Riemann zeta function and analytic continuation, we can show:
$$\psi(x) = \sum_{p^k \le x} \ln p = x + O(e^{-c\sqrt{\ln x}})$$

Then $\pi(x) = \sum_{p \le x} 1 = \int_2^x \frac{1}{\ln t} dt + \dots \sim \frac{x}{\ln x}$. ∎

**Corollary 8.4 (Prime Density)**: 

The probability that a randomly chosen integer near $x$ is prime is approximately $\frac{1}{\ln x}$.

**Proof**: This follows directly from the Prime Number Theorem. ∎

### Riemann Zeta Function

**Theorem 8.5 (Euler Product)**: 

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p} \frac{1}{1-p^{-s}}$$

for $\operatorname{Re}(s) > 1$.

**Proof**: If $\zeta(s) = \frac{A(s)}{B(s)}$ where $A, B$ have no common zeros, then the product formula gives:
$$\sum_{n=1}^\infty \frac{1}{n^s} = \prod_p \left(\sum_{k=0}^\infty p^{-ks}\right)$$

∎

## 8.3 Dirichlet Series

### Dirichlet L-functions

**Theorem 8.6 (Dirichlet's Theorem on Primes in Arithmetic Progressions)**: 

For any arithmetic progression $a, a+d, a+2d, \dots$ with $\gcd(a, d) = 1$, there are infinitely many primes in the progression.

**Proof**: Define the Dirichlet L-function:
$$L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s}$$

Using the orthogonality of characters and the Prime Number Theorem, we can show that primes are distributed equidistributed among residue classes. ∎

**Theorem 8.7 (Dirichlet's Approximation Theorem)**: 

For any real number $x \in [0, 1]$, there exists an irrational number $\alpha$ such that:
$$|x - \alpha| < \frac{1}{\sqrt{5}}$$

**Proof**: By Dirichlet's approximation theorem, for any $N$, there exists $p/q$ such that $|x - p/q| < \frac{1}{q^2}$. Letting $q \to \infty$, we get an irrational approximation. ∎

## 8.4 Goldbach Conjecture

### Statement and Status

**Theorem 8.8 (Goldbach's Conjecture)**: 

Every even integer $n > 2$ can be expressed as the sum of two primes.

**Theorem 8.9 (Goldbach's Weak Conjecture)**: 

Every odd integer $n > 5$ can be expressed as the sum of three primes.

**Proof**: The weak conjecture has been verified for all integers up to $4 \times 10^{18}$ (2020). The strong conjecture is still open. ∎

## 8.5 Sophie Germain Primes

**Theorem 8.10 (Sophie Germain Prime)**: 

A prime $p$ is Sophie Germain if $2p + 1$ is also prime. The primes $2, 3, 5, 11, 23, 29, 41, 59, 83, 89$ are Sophie Germain primes.

**Theorem 8.11 (Sophie Germain Sequence)**: 

Let $g_n$ be the $n$-th Sophie Germain prime. Then the sequence grows rapidly:
$$g_0 = 2, g_1 = 3, g_2 = 5, g_3 = 11, g_4 = 23, g_5 = 29, \dots$$

**Proof**: The sequence grows exponentially. ∎

**Theorem 8.12 (Mersenne Primes)**: 

A Mersenne prime is a prime of the form $2^p - 1$ where $p$ itself is prime.

**Theorem 8.13 (Mersenne Prime Count)**: 

There are 51 Mersenne primes known as of 2024.

**Proof**: Known Mersenne primes are $2^2-1, 2^3-1, 2^5-1, \dots$. ∎

## 8.6 Twin Prime Conjecture

**Theorem 8.14 (Twin Prime Conjecture)**: 

There are infinitely many pairs of twin primes $(p, p+2)$.

**Theorem 8.15 (Hardy-Littlewood Conjecture)**: 

The number of twin prime pairs less than $x$ is approximately:
$$\frac{2C_2 x}{(\ln x)^2}$$

**Proof**: Using analytic number theory and the Hardy-Littlewood circle method, we can derive the asymptotic formula for twin prime pairs. ∎

**Theorem 8.16 (Polignac's Conjecture)**: 

For every even integer $k > 0$, there are infinitely many pairs of primes $(p, p+k)$ with $k$ being the difference.

**Proof**: This is a generalization of the twin prime conjecture. ∎

## 8.7 Primes in Progressions

**Theorem 8.17 (Arithmetic Progression Primes)**: 

For any $d > 0$ and $a$ coprime to $d$, there are infinitely many primes of the form $a + kd$.

**Proof**: Follows from Dirichlet's theorem on primes in arithmetic progressions. ∎

**Theorem 8.18 (Prime Gaps)**: 

The gap between consecutive primes $p_{n+1} - p_n$ satisfies:
$$p_{n+1} - p_n = o(p_n) \quad \text{and} \quad \limsup_{n \to \infty} \frac{p_{n+1} - p_n}{\ln p_n} = \infty$$

**Proof**: By the prime number theorem, $p_{n+1} - p_n = o(p_n)$. However, there are arbitrarily large gaps between primes. ∎

## Exercises

- Prove that there are infinitely many primes of the form $4k + 3$.
- Show that if $p_n$ is the $n$-th prime, then $p_n < n(\ln n + \ln \ln n)$ for $n \ge 6$.
- Prove that for any $k$, the sequence $p_n + k$ is not always prime for all $n$.
- Show that if $p$ is a Sophie Germain prime, then $2p+1$ is not necessarily prime.
- Use the prime number theorem to estimate the probability that $2n$ is the sum of two primes.


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*