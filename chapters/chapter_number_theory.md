# Chapter: Advanced Number Theory

## 5.1 Prime Numbers and Factorization

### Theorem 5.1: Unique Factorization in $\mathbb{Z}[i]$

**Statement**: Every non-zero Gaussian integer can be factored into Gaussian primes uniquely (up to units and ordering).

**Proof**: The Gaussian integers form a Euclidean domain with norm $N(a+bi) = a^2 + b^2$. In any Euclidean domain, unique factorization into irreducibles holds. ∎

### Theorem 5.2: Quadratic Reciprocity

**Statement**: For distinct odd primes $p$ and $q$:
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof**: 
This follows from Gauss' proof using the sum of primitive roots modulo $p$ and $q$. ∎

### Theorem 5.3: Law of Quadratic Reciprocity

**Statement**: For any odd prime $p$:
1. If $p \equiv 1 \pmod 4$, then $-1$ is a quadratic residue modulo $p$.
2. If $p \equiv 3 \pmod 4$, then $-1$ is a quadratic non-residue modulo $p$.

**Proof**: 
By quadratic reciprocity:
$$\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}}$$
If $p \equiv 1 \pmod 4$, the exponent is even, so $\left(\frac{-1}{p}\right) = 1$.
If $p \equiv 3 \pmod 4$, the exponent is odd, so $\left(\frac{-1}{p}\right) = -1$. ∎

### Theorem 5.4: Fermat's Little Theorem

**Statement**: If $p$ is prime and $a$ is not divisible by $p$, then:
$$a^{p-1} \equiv 1 \pmod p$$

**Proof**: 
Consider the set $\{a, 2a, 3a, \dots, (p-1)a\}$ modulo $p$. These are distinct and non-zero, so they must be a permutation of $\{1, 2, \dots, p-1\}$. Multiplying them gives:
$$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod p$$
By Wilson's Theorem, $(p-1)! \equiv -1 \pmod p$, so $a^{p-1} \equiv 1 \pmod p$. ∎

### Theorem 5.5: Euler's Criterion

**Statement**: For a prime $p$ and integer $a$ not divisible by $p$:
$$a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod p$$

**Proof**: 
This follows from Fermat's Little Theorem and properties of modular arithmetic. ∎

## 5.2 Congruences and Modular Arithmetic

### Theorem 5.6: Chinese Remainder Theorem

**Statement**: Given pairwise coprime moduli $m_1, \dots, m_k$ and residues $a_1, \dots, a_k$, there exists a unique solution modulo $M = m_1 \cdots m_k$ to the system:
$$x \equiv a_i \pmod{m_i} \quad (i = 1, \dots, k)$$

**Proof**: 
Construct $x = \sum_{i=1}^k a_i M_i y_i$ where $M_i = M/m_i$ and $y_i = M_i^{-1} \pmod{m_i}$. ∎

### Theorem 5.7: Wilson's Theorem

**Statement**: If $p$ is prime, then $(p-1)! \equiv -1 \pmod p$.

**Proof**: 
The product of all non-zero residues modulo $p$ is $\pm 1$. If $p > 2$, no element is its own inverse except $1$ and $-1$. Thus $(p-1)! \equiv -1 \pmod p$. ∎

### Theorem 5.8: Binomial Theorem (Lucas' Theorem)

**Statement**: If $n = p_1 p_2 \cdots p_k$ and $a, b \in \mathbb{Z}$, then:
$$\binom{a+b}{b} \equiv \prod_{i=1}^k \binom{a_i+b_i}{b_i} \pmod p$$
where $n = \sum a_i p^{n-i}$ and $b = \sum b_i p^{n-i}$ are the base-$p$ expansions.

**Proof**: 
This follows from the fact that $\binom{n}{k} \pmod p$ depends only on the base-$p$ digits. ∎

## 5.3 Quadratic Residues and Reciprocity

### Theorem 5.9: Quadratic Reciprocity Law (Generalized)

**Statement**: For distinct odd primes $p$ and $q$:
$$\left(\frac{p}{q}\right) = (-1)^{\frac{p-1}{2} \frac{q-1}{2}} \left(\frac{q}{p}\right)$$

**Proof**: 
This is the classical quadratic reciprocity law, proven using Gauss' sum and primitive roots. ∎

## 5.4 Historical Notes

The theory of number theory developed from ancient Egyptian and Babylonian mathematics, with major contributions from Diophantus, Euler, Gauss, Dirichlet, and modern mathematicians. The fundamental theorem of arithmetic (unique factorization) dates to Pythagoras. The theory of congruences was developed in the 19th century by Euler, Gauss, and Legendre.

## Exercises

### Exercise 5.1
Show that the Gaussian primes are exactly the integers $a + bi$ where either $a$ or $b$ (but not both) is zero and $|a| \equiv 1 \pmod 4$, or both $a$ and $b$ are odd primes congruent to $1 \pmod 4$.

### Exercise 5.2
Prove that $\pi$ is transcendental over $\mathbb{Q}$.

### Exercise 5.3
Show that if $p \equiv 1 \pmod 4$, then there exist integers $a, b$ such that $a^2 + b^2 = p$.

### Exercise 5.4
Use Wilson's Theorem to show that for any prime $p > 3$, $(p-1)/2 \in \{1, -1\} \pmod p$.

### Exercise 5.5
Show that the ring of Gaussian integers $\mathbb{Z}[i]$ is a Euclidean domain.

## Advanced Problems

**Problem 5.1**: Let $p$ be an odd prime. Show that there exists a primitive root modulo $p$ iff $p-1$ is the product of distinct primes.

**Problem 5.2**: Prove that the equation $x^2 \equiv -1 \pmod p$ has a solution iff $p \equiv 1 \pmod 4$.

**Problem 5.3**: Show that if $p \equiv 3 \pmod 4$, then $p$ is a Gaussian prime.

## Bibliography

1. Hardy, G.H., and Wright, E.M. "An Introduction to the Theory of Numbers", 5th ed. Oxford UP, 1979.
2. Ireland, K., and Rosen, M. "A Classical Introduction to Modern Number Theory", Springer, 1990.
3. Apostol, T.M. "Introduction to Analytic Number Theory", Springer, 1976.
4. Koblitz, N. "A Course in Computational Algebraic Number Theory", Cambridge UP, 1994.
5. Niven, I., Zuckerman, H., and Montgomery, H. "An Introduction to the Theory of Numbers", 4th ed. Wiley, 1991.

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
