# Chapter 109: Number Theory - Theorems and Proofs

## 109.1 Primality and Divisibility

### Theorem 109.1 (Euclid's Lemma)
If $p$ is prime and $p \mid ab$, then $p \mid a$ or $p \mid b$.

**Proof:**
If $\gcd(a,p) = 1$, by Bézout's identity there exist integers $x,y$ such that $ax + py = 1$. Multiplying by $b$: $abx + bpy = b$. Since $p \mid ab$ and $p \mid py$, we have $p \mid b$. If $\gcd(a,p) = p$, then $p \mid a$.

### Theorem 109.2 (Euler's Totient Theorem)
If $\gcd(a,n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$.

**Proof:**
Let $U_n$ be the multiplicative group of integers modulo $n$. The order of $a$ in $U_n$ divides $|U_n| = \phi(n)$ by Lagrange's theorem. Thus $a^{\phi(n)} \equiv a^{\text{ord}(a)} \equiv 1 \pmod n$.

---

## 109.2 Quadratic Reciprocity

### Theorem 109.3 (Quadratic Reciprocity Law)
For distinct odd primes $p,q$:
- If $p \equiv q \equiv 1 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = 1$
- If $p \equiv q \equiv 3 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{(p-1)/2 \cdot (q-1)/2} = -1$
- If one is $1 \pmod 4$ and the other $3 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = 1$

**Proof:**
Let $\chi_p(q)$ be the Legendre symbol $\left(\frac{q}{p}\right)$. Using Gauss sums $G(\chi_p) = \sum_{a=0}^{p-1} \chi_p(a)e^{2\pi i a/p}$, we compute $G(\chi_p)G(\chi_q) = \chi_p(-1)^{(p-1)/2}G(\chi_q)$. Evaluating $G(\chi_p)^2 = \chi_p(-1)p$ and simplifying gives the reciprocity law.

---

## 109.3 Congruences

### Theorem 109.4 (Chinese Remainder Theorem)
Let $n_1, \dots, n_k$ be pairwise coprime positive integers and $a_1, \dots, a_k$ integers. There exists a unique solution modulo $\prod n_i$ to:
$$x \equiv a_i \pmod{n_i} \quad (i=1,\dots,k)$$

**Proof:**
Existence: For each $i$, let $N_i = \prod_{j \neq i} n_j$ and $M_i \equiv N_i^{-1} \pmod{n_i}$. Then $x = \sum a_i N_i M_i$ satisfies all congruences.
Uniqueness: If $x \equiv y \pmod{n_i}$ for all $i$, then $x-y$ is divisible by each $n_i$, hence by $\prod n_i$ (by Bézout's identity and coprimality).

### Theorem 109.5 (Fermat's Little Theorem)
For prime $p$ and integer $a$, $a^p \equiv a \pmod p$. Equivalently, if $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.

**Proof:**
Consider the set $\{a, 2a, \dots, (p-1)a\}$. Modulo $p$, this is a permutation of $\{1, 2, \dots, p-1\}$ (since $a \not\equiv 0$). Multiplying: $a^{p-1}(p-1)! \equiv (p-1)! \pmod p$. By Wilson's theorem $(p-1)! \equiv -1 \pmod p$, we get $a^{p-1} \equiv 1 \pmod p$.


## 109.1: Prime Number Theory

**Theorem 109.1.1** (Prime Number Theorem)
$$\pi(x) \sim \frac{x}{\ln x}$$
where $\pi(x)$ is the prime-counting function.

*Proof*: This follows from the Prime Number Theorem, which can be proved using Riemann's zeta function and the explicit formula. The asymptotic formula can be derived from the logarithmic integral function $Li(x)$.

**Theorem 109.1.2** (Chebyshev's Bounds)
There exist constants $c_1, c_2 > 0$ such that for all $x \ge 2$:
$$c_1 \frac{x}{\ln x} < \pi(x) < c_2 \frac{x}{\ln x}$$

*Proof*: Chebyshev used elementary methods involving binomial coefficients to establish these bounds.

**Theorem 109.1.3** (Erdős-Kac Theorem)
For any real $A, B > 0$, the proportion of primes $p \le x$ whose prime factors appear with multiplicity in a distribution with mean $\ln \ln x$ and variance $\ln \ln x$ tends to the normal distribution as $x \to \infty$.

*Proof*: This follows from the Turán-Kubilius inequality and the Hardy-Littlewood prime tuple conjecture.

## 109.2: Modular Forms and L-functions

**Theorem 109.2.1** (Modularity Theorem)
Every semistable elliptic curve over $\mathbb{Q}$ is the L-function of a modular form.

*Proof*: This is the Modularity Theorem (formerly the Taniyama-Shimura conjecture). The proof by Wiles and others used the theory of Galois representations and modular forms.

**Theorem 109.2.2** (Functional Equation of Riemann Zeta)
The Riemann zeta function satisfies:
$$\xi(s) = \xi(1-s)$$
where $\xi(s) = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(\frac{s}{2})\zeta(s)$.

*Proof*: This follows from the functional equation derived from the identity:
$$\zeta(s) = \chi(s)\zeta(1-s)$$
where $\chi(s)$ is the completed zeta function factor.

**Theorem 109.2.3** (Euler Product Formula)
$$\zeta(s) = \prod_{p \text{ prime}} \left(1 - p^{-s}\right)^{-1}$$

*Proof*: This is a consequence of the geometric series expansion:
$$\sum_{n=1}^\infty n^{-s} = \prod_{p \in \mathbb{P}} \left(\sum_{k=0}^\infty p^{-ks}\right)$$

## 109.3: Algebraic Number Theory

**Theorem 109.3.1** (Dedekind's Theorem on Ideal Class Groups)
The ideal class group $\text{Cl}(K)$ of a number field $K$ measures the failure of unique factorization in rings of integers.

*Proof*: Let $A$ be the ring of integers of $K$. The Dedekind domain property ensures that every ideal factors uniquely into prime ideals. However, elements may not factor uniquely.

**Theorem 109.3.2** (Minkowski's Bound)
For a number field $K$ with degree $n$, the Minkowski bound $M_K$ satisfies:
$$M_K = \frac{n!}{n^n} \left(\frac{4}{\pi}\right)^r_2 \sqrt{|D_K|}$$
where $r_2$ is the number of complex places and $D_K$ is the discriminant.

*Proof*: This bound follows from geometry of numbers and the study of lattice packings.

## 109.4: Exercises

**Exercise 109.4.1**: Prove the quadratic reciprocity law for distinct odd primes $p, q$.
**Exercise 109.4.2**: Show that the class number of $\mathbb{Q}(\sqrt{-19})$ is 2.
**Exercise 109.4.3**: Compute the Dirichlet L-function $L(s, \chi)$ for a non-principal Dirichlet character $\chi$.

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
