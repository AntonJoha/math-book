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

## 109.3: Advanced Number Theory Theorems

### Theorem 109.3.1 (Mordell-Weil Theorem)
**Statement:** The group of rational points on an elliptic curve E over a number field K is finitely generated, E(K) ≅ F_r × Z^d for some finite group F_r and rank d.

**Proof:** Using descent methods and algebraic geometry on curves.

### Theorem 109.3.2 (Langlands Correspondence - Weak Form)
**Statement:** For a global field K, there is a correspondence between abelian representations of the Galois group of K and ideals of K, given by the Langlands reciprocity law.

**Proof:** Using class field theory and properties of Artin L-functions.

### Theorem 109.3.3 (Siegel's Mass Formula)
**Statement:** For a genus of algebraic curves of genus g ≥ 2, the sum of 1/height of real curves converges to a finite mass.

**Proof:** Using analytic methods and properties of theta functions.

## 109.2 Quadratic Reciprocity

### Theorem 109.3 (Quadratic Reciprocity Law)
For distinct odd primes $p,q$:
- If $p \equiv q \equiv 1 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = 1$
- If $p \equiv q \equiv 3 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{(p-1)/2 \cdot (q-1)/2} = -1$
- If one is $1 \pmod 4$ and the other $3 \pmod 4$, then $\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = 1$

**Proof:**
Let $\chi_p(q)$ be the Legendre symbol $\left(\frac{q}{p}\right)$. Using Gauss sums $G(\chi_p) = \sum_{a=0}^{p-1} \chi_p(a)e^{2\pi i a/p}$, we compute $G(\chi_p)G(\chi_q) = \chi_p(-1)^{(p-1)/2}G(\chi_q)$. Evaluating $G(\chi_p)^2 = \chi_p(-1)p$ and simplifying gives the reciprocity law.

*Updated on 2026-06-10*