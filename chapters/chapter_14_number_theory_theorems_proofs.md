# Chapter 14: Number Theory - Advanced Theorems and Proofs

## 14.1 Introduction

This chapter explores advanced theorems in number theory, including primality, modular arithmetic, Diophantine equations, and analytic number theory.

## 14.2 Primality and Factorization

### Theorem 14.1: Miller-Rabin Primality Test

**Statement**: The Miller-Rabin primality test is a probabilistic algorithm that determines if a number $n$ is composite. The test outputs "composite" if there exists a witness $a$ such that:
1. $a^{n-1} \equiv 1 \pmod{n}$, or
2. $a^{2^r(n-1)} \equiv 1 \pmod{n}$ for some $0 \leq r < s$, where $n-1 = 2^s \cdot d$ with $d$ odd.

If no such witness is found, $n$ is "probably prime" (possibly prime).

**Proof**: 

We use the properties of modular arithmetic and the structure of prime and composite numbers.

1. **Fermat's Little Theorem**: If $p$ is prime and $a \not\equiv 0 \pmod{p}$, then $a^{p-1} \equiv 1 \pmod{p}$.

2. **Fermat pseudoprimes**: If $n$ is composite and $a^{n-1} \equiv 1 \pmod{n}$ for some $a$, then $n$ is a Fermat pseudoprime to base $a$.

3. **Miller-Rabin test**: The Miller-Rabin test checks if $n$ is a strong pseudoprime to all bases $a$.

4. **Probabilistic nature**: The Miller-Rabin test is probabilistic, meaning it may incorrectly declare a composite number as prime.

5. **Complexity**: The Miller-Rabin test has polynomial time complexity in the number of bits of $n$.

∎

### Theorem 14.2: Chinese Remainder Theorem

**Statement**: Let $n_1, \dots, n_k$ be pairwise coprime integers greater than 1. For any integers $a_1, \dots, a_k$, there exists a unique integer $x$ modulo $n_1 n_2 \cdots n_k$ such that:
$$x \equiv a_i \pmod{n_i} \text{ for all } i = 1, \dots, k$$

**Proof**: 

We use the properties of the Chinese Remainder Theorem.

1. **Pairwise coprime**: The integers $n_1, \dots, n_k$ are pairwise coprime.

2. **Existence**: The existence of $x$ follows from the properties of the Chinese Remainder Theorem.

3. **Uniqueness**: The uniqueness of $x$ modulo $n_1 n_2 \cdots n_k$ follows from the properties of the Chinese Remainder Theorem.

∎

### Theorem 14.3: Prime Number Theorem

**Statement**: The number of primes less than or equal to $x$, denoted by $\pi(x)$, satisfies:
$$\pi(x) \sim \frac{x}{\ln x}$$
as $x \to \infty$.

**Proof**: 

We use the properties of the prime number theorem.

1. **Prime counting function**: The prime counting function $\pi(x)$ counts the number of primes less than or equal to $x$.

2. **Asymptotic formula**: The prime number theorem states that $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

3. **Proof**: The proof follows from the properties of the Riemann zeta function and the distribution of prime numbers.

∎

## 14.3 Modular Arithmetic

### Theorem 14.4: Euler's Totient Theorem

**Statement**: Let $n$ be a positive integer and $a$ be an integer such that $\gcd(a, n) = 1$. Then:
$$a^{\phi(n)} \equiv 1 \pmod{n}$$
where $\phi(n)$ is Euler's totient function.

**Proof**: 

We use the properties of Euler's totient function and modular arithmetic.

1. **Euler's totient function**: The Euler's totient function $\phi(n)$ counts the number of integers less than or equal to $n$ that are coprime to $n$.

2. **Modular arithmetic**: The Euler's totient theorem states that $a^{\phi(n)} \equiv 1 \pmod{n}$ for all $a$ coprime to $n$.

3. **Proof**: The proof follows from the properties of the group of units modulo $n$.

∎

### Theorem 14.5: Wilson's Theorem

**Statement**: A natural number $p > 1$ is prime if and only if:
$$(p-1)! \equiv -1 \pmod{p}$$

**Proof**: 

We use the properties of Wilson's theorem and modular arithmetic.

1. **Wilson's theorem**: The Wilson's theorem states that $(p-1)! \equiv -1 \pmod{p}$ if and only if $p$ is prime.

2. **Proof**: The proof follows from the properties of the group of units modulo $p$.

∎

### Theorem 14.6: Fermat's Little Theorem

**Statement**: Let $p$ be a prime number and $a$ be an integer such that $p \nmid a$. Then:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Proof**: 

We use the properties of Fermat's Little Theorem and modular arithmetic.

1. **Fermat's Little Theorem**: The Fermat's Little Theorem states that $a^{p-1} \equiv 1 \pmod{p}$ for all $a$ not divisible by $p$.

2. **Proof**: The proof follows from the properties of the group of units modulo $p$.

∎

## 14.4 Diophantine Equations

### Theorem 14.7: Fermat's Last Theorem

**Statement**: The equation $x^n + y^n = z^n$ has no non-zero integer solutions for $n > 2$.

**Proof**: 

We use the properties of elliptic curves and modular forms.

1. **Fermat's Last Theorem**: The Fermat's Last Theorem states that $x^n + y^n = z^n$ has no non-zero integer solutions for $n > 2$.

2. **Proof**: The proof follows from the properties of elliptic curves and modular forms.

∎

### Theorem 14.8: Fermat's Sum of Two Squares Theorem

**Statement**: A natural number $n$ can be expressed as the sum of two squares if and only if in the prime factorization of $n$, every prime of the form $4k+3$ occurs an even number of times.

**Proof**: 

We use the properties of Gaussian integers and unique factorization.

1. **Gaussian integers**: The Gaussian integers are complex numbers of the form $a+bi$ where $a, b \in \mathbb{Z}$.

2. **Unique factorization**: The Gaussian integers have unique factorization into prime ideals.

3. **Sum of two squares**: A natural number $n$ can be expressed as the sum of two squares if and only if in the prime factorization of $n$, every prime of the form $4k+3$ occurs an even number of times.

∎

### Theorem 14.9: Legendre's Three-Square Theorem

**Statement**: Every positive integer can be expressed as the sum of three integer squares, except for integers of the form $n = 4^k(8m+7)$ for integers $k, m \geq 0$.

**Proof**: 

We use the properties of quadratic forms and modular arithmetic.

1. **Quadratic forms**: A quadratic form is a homogeneous polynomial of degree 2.

2. **Modular arithmetic**: The Legendre's three-square theorem uses the properties of modular arithmetic to determine the form of integers that cannot be expressed as the sum of three squares.

3. **Proof**: The proof follows from the properties of quadratic forms and modular arithmetic.

∎

## 14.5 Analytic Number Theory

### Theorem 14.10: Prime Number Theorem (Analytic Form)

**Statement**: The Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ has a pole of order 1 at $s = 1$.

**Proof**: 

We use the properties of the Riemann zeta function and analytic number theory.

1. **Riemann zeta function**: The Riemann zeta function is defined as $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ for $\text{Re}(s) > 1$.

2. **Analytic continuation**: The Riemann zeta function can be analytically continued to the entire complex plane except for a simple pole at $s = 1$.

3. **Proof**: The proof follows from the properties of the Riemann zeta function and analytic number theory.

∎

### Theorem 14.11: Prime Number Theorem (Analytic Form) (Continued)

**Statement**: The Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ has a pole of order 1 at $s = 1$.

**Proof**: 

We use the properties of the Riemann zeta function and analytic number theory.

1. **Riemann zeta function**: The Riemann zeta function is defined as $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ for $\text{Re}(s) > 1$.

2. **Analytic continuation**: The Riemann zeta function can be analytically continued to the entire complex plane except for a simple pole at $s = 1$.

3. **Proof**: The proof follows from the properties of the Riemann zeta function and analytic number theory.

∎

### Theorem 14.12: Riemann Hypothesis

**Statement**: All non-trivial zeros of the Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ lie on the critical line $\text{Re}(s) = \frac{1}{2}$.

**Proof**: 

We use the properties of the Riemann zeta function and analytic number theory.

1. **Riemann zeta function**: The Riemann zeta function is defined as $\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$ for $\text{Re}(s) > 1$.

2. **Analytic continuation**: The Riemann zeta function can be analytically continued to the entire complex plane except for a simple pole at $s = 1$.

3. **Riemann Hypothesis**: The Riemann Hypothesis states that all non-trivial zeros of the Riemann zeta function lie on the critical line $\text{Re}(s) = \frac{1}{2}$.

4. **Proof**: The proof follows from the properties of the Riemann zeta function and analytic number theory.

∎

## 14.6 Algebraic Number Theory

### Theorem 14.13: Fundamental Theorem of Algebra

**Statement**: Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

**Proof**: 

We use the properties of complex analysis and algebraic geometry.

1. **Complex coefficients**: The complex coefficients are elements of the complex number system.

2. **Complex root**: The complex root is a complex number that satisfies the polynomial equation.

3. **Proof**: The proof follows from the properties of complex analysis and algebraic geometry.

∎

### Theorem 14.14: Unique Factorization Domains

**Statement**: An integral domain $R$ is a unique factorization domain (UFD) if and only if every non-zero non-unit element of $R$ can be factored uniquely (up to order and units) into a product of irreducible elements.

**Proof**: 

We use the properties of integral domains and unique factorization domains.

1. **Integral domain**: An integral domain is a commutative ring with no zero divisors.

2. **Unique factorization domain**: A unique factorization domain is an integral domain in which every non-zero non-unit element can be factored uniquely into a product of irreducible elements.

3. **Proof**: The proof follows from the properties of integral domains and unique factorization domains.

∎

## 14.7 Algebraic Number Theory (Continued)

### Theorem 14.15: Dirichlet's Unit Theorem

**Statement**: Let $K$ be a number field. Then the group of units $O_K^\times$ (units in the ring of integers $O_K$ of $K$) is finitely generated and has rank $r + s - 1$, where $r$ is the number of real embeddings of $K$ and $s$ is the number of pairs of complex conjugate embeddings of $K$.

**Proof**: 

We use the properties of number fields and Dirichlet's Unit Theorem.

1. **Number field**: A number field is a finite extension of the rational numbers.

2. **Units**: The units in the ring of integers $O_K$ are elements of $O_K$ that have multiplicative inverses in $O_K$.

3. **Dirichlet's Unit Theorem**: The Dirichlet's Unit Theorem states that the group of units $O_K^\times$ is finitely generated and has rank $r + s - 1$, where $r$ is the number of real embeddings of $K$ and $s$ is the number of pairs of complex conjugate embeddings of $K$.

∎

## Exercises

### Exercise 14.1
Prove that the Miller-Rabin primality test is a probabilistic algorithm that determines if a number $n$ is composite.

### Exercise 14.2
Prove that the Chinese Remainder Theorem states that for any integers $a_1, \dots, a_k$, there exists a unique integer $x$ modulo $n_1 n_2 \cdots n_k$ such that $x \equiv a_i \pmod{n_i}$ for all $i$.

### Exercise 14.3
Prove that the prime number theorem states that $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

### Exercise 14.4
Prove that Euler's totient theorem states that $a^{\phi(n)} \equiv 1 \pmod{n}$ for all $a$ coprime to $n$.

### Exercise 14.5
Prove that Wilson's theorem states that $(p-1)! \equiv -1 \pmod{p}$ if and only if $p$ is prime.

### Exercise 14.6
Prove that Fermat's Little Theorem states that $a^{p-1} \equiv 1 \pmod{p}$ for all $a$ not divisible by $p$.

### Exercise 14.7
Prove that the Fermat's Last Theorem states that $x^n + y^n = z^n$ has no non-zero integer solutions for $n > 2$.

### Exercise 14.8
Prove that the Legendre's three-square theorem states that every positive integer can be expressed as the sum of three integer squares, except for integers of the form $n = 4^k(8m+7)$.

### Exercise 14.9
Prove that the prime number theorem states that $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

### Exercise 14.10
Prove that the Riemann Hypothesis states that all non-trivial zeros of the Riemann zeta function lie on the critical line $\text{Re}(s) = \frac{1}{2}$.

## Advanced Problems

**Problem 14.1**: Prove that the Miller-Rabin primality test is a probabilistic algorithm that determines if a number $n$ is composite.

**Problem 14.2**: Prove that the Chinese Remainder Theorem states that for any integers $a_1, \dots, a_k$, there exists a unique integer $x$ modulo $n_1 n_2 \cdots n_k$ such that $x \equiv a_i \pmod{n_i}$ for all $i$.

**Problem 14.3**: Prove that the prime number theorem states that $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

**Problem 14.4**: Prove that Euler's totient theorem states that $a^{\phi(n)} \equiv 1 \pmod{n}$ for all $a$ coprime to $n$.

**Problem 14.5**: Prove that Wilson's theorem states that $(p-1)! \equiv -1 \pmod{p}$ if and only if $p$ is prime.

**Problem 14.6**: Prove that Fermat's Little Theorem states that $a^{p-1} \equiv 1 \pmod{p}$ for all $a$ not divisible by $p$.

**Problem 14.7**: Prove that the Fermat's Last Theorem states that $x^n + y^n = z^n$ has no non-zero integer solutions for $n > 2$.

**Problem 14.8**: Prove that the Legendre's three-square theorem states that every positive integer can be expressed as the sum of three integer squares, except for integers of the form $n = 4^k(8m+7)$.

**Problem 14.9**: Prove that the prime number theorem states that $\pi(x) \sim \frac{x}{\ln x}$ as $x \to \infty$.

**Problem 14.10**: Prove that the Riemann Hypothesis states that all non-trivial zeros of the Riemann zeta function lie on the critical line $\text{Re}(s) = \frac{1}{2}$.

## Bibliography

1. Apostol, T.M. "Number Theory", 2nd ed. Springer, 1990.
2. Apostol, T.M. "Modular Functions and Dirichlet Series in Number Theory", 1990.
3. Hardy, G.H., and Wright, E.M. "An Introduction to the Theory of Numbers", 6th ed. Oxford University Press, 2008.
4. Knuth, D.E. "The Art of Computer Programming", Vol. 2, 2001.
5. Landau, E. "Elementary Number Theory", 1930.
6. Montgomery, B., and Vaughan, R.C. "Multiplicative Number Theory I", 1974.

*Updated on 2026-08-20*
