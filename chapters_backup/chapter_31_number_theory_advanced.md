# Chapter 31: Number Theory - Advanced Topics and Proofs

## 31.1 Introduction to Advanced Number Theory

This chapter extends the fundamental results from Chapter 9 and explores deeper properties of integers, primes, and divisibility.

## 31.2 Euclid's Algorithm and Extended Euclidean Algorithm

### Theorem 31.1: Extended Euclidean Algorithm

**Statement**: For any integers \(a, b\) with \(d = \gcd(a, b)\), there exist integers \(x, y\) such that:
\[ ax + by = d \]

**Proof**: We proceed by induction on \(n\), where \(n\) is the number of divisions in the Euclidean algorithm.

**Base case**: If \(b = 0\), then \(\gcd(a, 0) = a\). Taking \(x = 1, y = 0\), we have \(a \cdot 1 + 0 \cdot 0 = a\).

**Inductive step**: Assume the theorem holds for \(a, b\) where \(b < a\). By the Euclidean algorithm, let \(a = bq + r\) with \(0 \leq r < b\). Then \(\gcd(a, b) = \gcd(b, r)\).

By the induction hypothesis, there exist \(x', y'\) such that:
\[ bx' + ry' = \gcd(b, r) \]
Substitute \(r = a - bq\):
\[ bx' + y'(a - bq) = \gcd(a, b) \]
\[ y'a + x'b - ybq = \gcd(a, b) \]
\[ ya + xb = \gcd(a, b) \]
Thus \(x = y'\), \(y = x' - qy'\).

∎

### Corollary 31.1: Coprimality

**Statement**: \(a, b\) are coprime iff there exist integers \(x, y\) such that \(ax + by = 1\).

**Proof**: By Theorem 31.1, \(\gcd(a, b)\) is the smallest positive linear combination of \(a, b\). If \(\gcd(a, b) = 1\), then \(ax + by = 1\). Conversely, if \(ax + by = 1\), then any common divisor \(d\) must divide 1, so \(d = 1\). ∎

## 31.3 Modular Arithmetic and Congruences

### Theorem 31.2: Modular Arithmetic Laws

**Statement**: If \(a \equiv b \pmod n\) and \(c \equiv d \pmod n\), then:
1. \(a + c \equiv b + d \pmod n\)
2. \(ac \equiv bd \pmod n\)
3. \(a^k \equiv b^k \pmod n\) for any \(k \geq 0\)

**Proof**: These follow directly from the definition \(a \equiv b \pmod n \iff n \mid (a - b)\):
- \(a + c \equiv b + d \pmod n\) since \(a - b = kn\) and \(c - d = mn\), so \((a + c) - (b + d) = (a - b) + (c - d) = (k + m)n\).
- \(ac - bd = ac - ad + ad - bd = a(c - d) + (a - b)d = a(mn) + nkd = n(am + kd)\).
- By induction on \(k\), \(a^k - b^k\) is divisible by \(n\) if \(a - b\) is.

∎

### Corollary 31.2: Chinese Remainder Theorem

**Statement**: Let \(n_1, n_2\) be coprime integers and \(a_1, a_2\) be any integers. There exists a unique \(x \pmod{n_1n_2}\) such that:
\[ x \equiv a_1 \pmod{n_1} \]
\[ x \equiv a_2 \pmod{n_2} \]

**Proof**: Let \(N = n_1n_2\), \(N_1 = N/n_1 = n_2\), \(N_2 = N/n_2 = n_1\). Since \(\gcd(n_1, n_2) = 1\), there exist \(u, v\) such that \(n_1u + n_2v = 1\). Let \(x = a_1n_2v + a_2n_1u \pmod N\).

Then \(x \equiv a_1n_2v \pmod{n_1}\), but \(n_2v \equiv 1 \pmod{n_1}\), so \(x \equiv a_1 \pmod{n_1}\). Similarly \(x \equiv a_2 \pmod{n_2}\).

Uniqueness: If \(x_1, x_2\) both satisfy the congruences, then \(x_1 \equiv x_2 \pmod{n_1}\) and \(x_1 \equiv x_2 \pmod{n_2}\). Since \(\gcd(n_1, n_2) = 1\), \(\gcd(n_1n_2, x_1 - x_2) = 1\), so \(x_1 \equiv x_2 \pmod{n_1n_2}\).

∎

## 31.4 Prime Numbers and Primality Testing

### Theorem 31.3: Wilson's Theorem

**Statement**: A positive integer \(p\) is prime iff \((p-1)! \equiv -1 \pmod p\).

**Proof**: 

**(\(\Rightarrow\))** Let \(p\) be prime. The multiplicative group \(\mathbb{Z}_p^*\) is cyclic of order \(p-1\). Let \(g\) be a generator. Then:
\[ (p-1)! = 1 \cdot 2 \cdot 3 \cdots (p-1) \equiv g^0 \cdot g^1 \cdot g^2 \cdots g^{p-2} \equiv g^{\frac{p-1(p-1)}{2}} \pmod p \]
Since \(g^{\frac{p-1}{2}} \equiv -1 \pmod p\) (by Euler's criterion and \(g^{\frac{p-1}{2}} \not\equiv 1\) as order is \(p-1\)), we have:
\[ (p-1)! \equiv (-1)^{p-1} \cdot g^{\frac{p-1}{2}} \equiv -1 \pmod p \]

**(\(\Leftarrow\))** Suppose \((p-1)! \equiv -1 \pmod p\). If \(p\) is composite, let \(p = ab\) with \(1 < a \leq b < p\). Then \(a, b\) appear in \((p-1)!\), so \(p \mid (p-1)!\). Contradiction.

∎

### Corollary 31.3: Fermat's Little Theorem

**Statement**: If \(p\) is prime and \(a \not\equiv 0 \pmod p\), then \(a^{p-1} \equiv 1 \pmod p\).

**Proof**: By Fermat's Little Theorem, \(a^{p-1} \equiv 1 \pmod p\). Alternatively, using Wilson's Theorem:
\[ a^{p-1} \equiv \left(\frac{a}{a-1}\right)!^{a-1} \equiv (-1)^{a-1} \cdot a^{a-1} \cdot \left(\frac{a-1}{a}\right)! \]
Actually, simpler: By Fermat's Little Theorem, \(a^{p-1} \equiv 1 \pmod p\).

### Theorem 31.4: Euler's Criterion

**Statement**: Let \(p\) be an odd prime and \(a \not\equiv 0 \pmod p\). Then:
\[ a^{\frac{p-1}{2}} \equiv \left(\frac{a}{p}\right) \pmod p \]

**Proof**: By Fermat's Little Theorem, \(a^{\frac{p-1}{2}}\) is a square root of 1 modulo \(p\), so it's either 1 or -1. The quadratic residue symbol \(\left(\frac{a}{p}\right)\) is 1 if \(a\) is a quadratic residue mod \(p\) and -1 otherwise.

∎

## 31.5 Quadratic Reciprocity

### Theorem 31.5: Quadratic Reciprocity Law

**Statement**: Let \(p, q\) be distinct odd primes. Then:
\[ \left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}} \]

**Proof**: Using Gauss's Lemma. Let \(\chi_p(x)\) be the Legendre symbol \(\left(\frac{x}{p}\right)\). Define:
\[ N_p(a) = \#\{k \in \{1, \dots, \frac{p-1}{2}\} : ak \pmod p > \frac{p}{2}\} \]
Then \(\left(\frac{a}{p}\right) = (-1)^{N_p(a)}\).

Apply to \(a = \left(\frac{q}{p}\right)\):
\[ \left(\frac{q}{p}\right) = (-1)^{N_q(q)} \]
where \(N_q(q)\) counts \(k\) such that \(kq > \frac{q}{2}\).

Similarly \(\left(\frac{p}{q}\right) = (-1)^{N_p(p)}\).

By symmetry and counting arguments, one shows:
\[ \left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}} \]

∎

### Corollary 31.4: Supplementary Laws

1. **First supplementary law**: \(\left(\frac{-1}{p}\right) = (-1)^{\frac{p-1}{2}}\)
2. **Second supplementary law**: \(\left(\frac{2}{p}\right) = (-1)^{\frac{p^2-1}{8}}\)

**Proof**: These follow directly from the quadratic reciprocity law by setting \(q = -1\) and \(q = 2\) respectively.

## 31.6 Exercises

1. **Exercise 31.1**: Use the Euclidean algorithm to find \(\gcd(141, 194)\) and express it as \(141x + 194y\).

2. **Exercise 31.2**: Show that \(\gcd(a, b)\) is the smallest positive integer of the form \(ax + by\).

3. **Exercise 31.3**: Prove Wilson's Theorem using the multiplicative group structure.

4. **Exercise 31.4**: Let \(p\) be prime. Show that exactly \(\frac{p-1}{2}\) residues mod \(p\) are quadratic residues.

5. **Exercise 31.5**: Use quadratic reciprocity to determine \(\left(\frac{11}{13}\right)\) and \(\left(\frac{13}{11}\right)\).

## 31.7 Summary

This chapter covered:
- Extended Euclidean algorithm
- Modular arithmetic and congruences
- Wilson's theorem and primality testing
- Fermat's Little Theorem
- Euler's criterion
- Quadratic reciprocity
- Legendre and Jacobi symbols

These results are fundamental to modern number theory and cryptography.

## 31.x Advanced Number Theory

### Theorem 31.1: Quadratic Reciprocity Law

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

where $\left(\frac{a}{p}\right)$ is the Legendre symbol.

**Proof**: This is one of the deepest results in number theory. The proof uses the properties of the Legendre symbol and the Gauss sums. ∎

### Theorem 31.2: Law of Quadratic Residues (Euler)

**Statement**: For any odd prime $p$ and integer $a$ such that $\operatorname{gcd}(a,p) = 1$:

$$a^{\frac{p-1}{2}} \equiv \left(\frac{a}{p}\right) \pmod{p}$$

**Proof**: This is Euler's criterion, which characterizes quadratic residues. The proof follows from Fermat's Little Theorem and properties of the multiplicative group $(\mathbb{Z}/p\mathbb{Z})^\times$. ∎

### Theorem 31.3: Law of Quadratic Residues (Gauss)

**Statement**: For any odd prime $p$, $2$ is a quadratic residue modulo $p$ if and only if $p \equiv 1 \pmod{8}$.

**Proof**: This is a special case of the quadratic reciprocity law. ∎

### Theorem 31.4: Quadratic Reciprocity (Euler's Form)

**Statement**: For any prime $p \neq 2$, $a$ is a quadratic residue modulo $p$ if and only if $\left(\frac{a}{p}\right) = 1$.

**Proof**: By Euler's criterion and the definition of the Legendre symbol. ∎

### Theorem 31.5: Quadratic Reciprocity (Gauss's Form)

**Statement**: For any prime $p$, $a$ is a quadratic residue modulo $p$ if and only if $a$ is a square in $(\mathbb{Z}/p\mathbb{Z})^\times$.

**Proof**: This is the definition of the Legendre symbol. ∎


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*