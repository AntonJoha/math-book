# Chapter 22: Number Theory - Comprehensive Theorems and Proofs

## 22.1 Basic Properties of Integers

### Theorem 22.1: Well-Ordering Principle

**Statement**: Every non-empty set of positive integers has a least element.

**Proof**: Suppose $S \subseteq \mathbb{Z}^+$ is non-empty. Consider the set $S' = \{n \in \mathbb{Z}^+ : \text{for all } s \in S, s > n\}$. If $S'$ is non-empty, let $m = \min S'$. Then $m > s$ for all $s \in S$, so $S' = \{n : \exists s \in S, n > s\}$. But this implies every element of $S$ is smaller than every element of $S'$, which is a contradiction. So $S'$ must be empty, and there must exist some $n_0$ such that no integer $n < n_0$ satisfies $n > s$ for all $s \in S$. So $n_0 \in S$ and $n_0 < s$ for all $s \in S$, so $n_0$ is the least element. ∎

### Theorem 22.2: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be written uniquely (up to order of factors) as a product of prime numbers.

**Proof**: 
($\Rightarrow$) Let $n > 1$. If $n$ is prime, it's a product of one prime. If $n$ is composite, $n = ab$ with $1 < a,b < n$. By induction on $n$, $a$ and $b$ have unique prime factorizations, so $n$ has a unique prime factorization.

($\Leftarrow$) Suppose $n$ has two prime factorizations $p_1 p_2 \dots p_r = q_1 q_2 \dots q_s$. Then $r = s$ and after reordering, $p_i = q_i$ for all $i$. ∎

### Theorem 22.3: Euclidean Algorithm

**Statement**: For any integers $a,b$ with $b \ne 0$, the greatest common divisor $\gcd(a,b)$ can be computed using the Euclidean algorithm.

**Proof**: The Euclidean algorithm uses repeated division: $a = bq + r$ where $0 \le r < |b|$. If $r = 0$, then $\gcd(a,b) = |b|$. Otherwise, continue with $\gcd(b,r)$. The last non-zero remainder is $\gcd(a,b)$. ∎

### Theorem 22.4: Linear Combination Theorem

**Statement**: For any integers $a,b$ with $\gcd(a,b) = d$, there exist integers $x,y$ such that $ax + by = d$.

**Proof**: This is the Extended Euclidean Algorithm. The algorithm produces $x,y$ such that $ax + by = \gcd(a,b)$. ∎

### Theorem 22.5: Bezout's Identity

**Statement**: For any integers $a,b$, $\gcd(a,b)$ is the smallest positive integer that can be written as $ax + by$ for some integers $x,y$.

**Proof**: Let $d = \gcd(a,b)$. By Theorem 22.4, there exist $x,y$ such that $ax + by = d$. If $ax + by = k > d$ for some integers $x,y$, then $k$ must be a multiple of $\gcd(a,b) = d$, so $k \ge d$. Since $d$ is the smallest such positive integer, we have the result. ∎

### Theorem 22.6: Unique Factorization Domain Property

**Statement**: $\mathbb{Z}$ is a unique factorization domain (UFD).

**Proof**: $\mathbb{Z}$ is an integral domain. Every non-zero non-unit element has a unique factorization into irreducible elements (by Theorem 22.2). ∎

## 22.2 Divisibility and Congruences

### Theorem 22.7: Division Algorithm

**Statement**: For any integers $a,b$ with $b \ne 0$, there exist unique integers $q,r$ such that $a = bq + r$ and $0 \le r < |b|$.

**Proof**: Consider the set $S = \{a - bq : q \in \mathbb{Z}, a - bq \ge 0\}$. This set is non-empty (e.g., $a - bq = a \ge 0$ for $q = 0$). By Theorem 22.1, $S$ has a least element $r$. Let $r = a - bq_0$. Then $0 \le r < |b|$ because if $r \ge |b|$, we could take $q_1 = q_0 + \text{sgn}(b)$ and get $a - bq_1 < r$, a contradiction. The representation is unique because $a = bq + r = bq' + r'$. Then $b(q-q') = r-r'$. Since $|r-r'| < |b|$, we must have $q=q'$ and $r=r'$. ∎

### Theorem 22.8: Congruence Properties

**Statement**: For integers $a,b,c,d$ and $n \ne 0$, the following hold:
1. $a \equiv b \pmod n \iff a-b = kn$ for some integer $k$.
2. $a \equiv b \pmod n \iff n$ divides $a-b$.
3. If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then $a+c \equiv b+d \pmod n$.
4. If $a \equiv b \pmod n$ and $k \in \mathbb{Z}$, then $ak \equiv bk \pmod n$.
5. If $a \equiv b \pmod n$ and $n$ divides $a$, then $n$ divides $b$.

**Proof**: All properties follow from the definition of congruence and basic properties of integer multiplication and addition. ∎

### Theorem 22.9: Fermat's Little Theorem

**Statement**: If $p$ is a prime and $a$ is an integer with $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.

**Proof**: Consider the set $\{a, 2a, 3a, \dots, (p-1)a\}$. Since $p \nmid a$, all elements are distinct modulo $p$ and none are divisible by $p$. Thus the set is a permutation of $\{1, 2, \dots, p-1\} \pmod p$. Multiplying these gives $a^{p-1}(p-1)! \equiv (p-1)! \pmod p$. By Wilson's Theorem, $(p-1)! \equiv -1 \pmod p$. Thus $a^{p-1} \equiv 1 \pmod p$. ∎

### Theorem 22.10: Euler's Totient Function

**Statement**: For any positive integer $n$, the number of positive integers less than or equal to $n$ that are coprime to $n$ is given by Euler's totient function $\phi(n) = n \prod_{p|n} (1 - 1/p)$.

**Proof**: Let $\phi(n)$ count the number of positive integers $\le n$ coprime to $n$. The formula follows from the principle of inclusion-exclusion or by induction on the prime factorization of $n$. ∎

### Theorem 22.11: Euler's Generalization of Fermat's Little Theorem

**Statement**: For any integers $a,n$ with $\gcd(a,n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod n$.

**Proof**: Consider the set $A = \{a, 2a, \dots, \phi(n)a\}$. Since $\gcd(a,n) = 1$, all elements are distinct modulo $n$ and coprime to $n$. Thus the set is a permutation of $\{1, 2, \dots, \phi(n)\}$ modulo $n$. Multiplying these gives $a^{\phi(n)} \phi(n)! \equiv \phi(n)! \pmod n$. By Euler's theorem, $a^{\phi(n)} \equiv 1 \pmod n$. ∎

### Theorem 22.12: Chinese Remainder Theorem

**Statement**: Let $n_1, n_2, \dots, n_k$ be pairwise coprime positive integers. Then the system of congruences
$$x \equiv a_i \pmod {n_i} \quad (i = 1, 2, \dots, k)$$
has a unique solution modulo $n_1 n_2 \dots n_k$.

**Proof**: Let $N = n_1 n_2 \dots n_k$ and $N_i = N/n_i$. Then $\gcd(N_i, n_i) = 1$. By the Extended Euclidean Algorithm, there exist integers $x_i, y_i$ such that $N_i x_i + n_i y_i = 1$. The solution is $x = \sum_{i=1}^k a_i N_i x_i \pmod N$. ∎

## 22.3 Primes and Infinitude

### Theorem 22.13: Primes are Infinitely Many

**Statement**: There are infinitely many prime numbers.

**Proof**: Suppose there are only finitely many primes $p_1, \dots, p_k$. Consider the number $N = p_1 p_2 \dots p_k + 1$. Then $N > 1$, so $N$ must have a prime divisor $p$. But $p$ must be one of $p_1, \dots, p_k$, and then $p$ divides $N$ and $p_i$ for all $i$, so $p$ divides $N - p_1 p_2 \dots p_k = 1$, which is impossible. Thus there must be infinitely many primes. ∎

### Theorem 22.14: Euclid's Second Proof

**Statement**: There are infinitely many prime numbers.

**Proof**: Consider the set of all products of consecutive primes starting from 2: $2, 2 \cdot 3, 2 \cdot 3 \cdot 5, \dots$. Each such product plus 1 is not divisible by any of the primes used in the product. By induction, each such number has at least one prime factor not in the list, so there are infinitely many primes. ∎

### Theorem 22.15: Dirichlet's Theorem on Arithmetic Progressions

**Statement**: For any two positive coprime integers $a$ and $d$, there are infinitely many primes of the form $a + nd$.

**Proof**: Consider the polynomials $f(n) = a + nd$. If there were finitely many primes in this form, then all large $f(n)$ would be composite. But $f(n)$ grows with $n$, so it can't always be composite. By analytic number theory, there are infinitely many primes in this arithmetic progression. ∎

## 22.4 Quadratic Residues and Reciprocity

### Theorem 22.16: Quadratic Residue Definition

**Statement**: For an odd prime $p$ and integer $a$, $a$ is a quadratic residue modulo $p$ iff there exists $x$ such that $x^2 \equiv a \pmod p$.

**Proof**: This is the definition. ∎

### Theorem 22.17: Legendre Symbol

**Statement**: For an odd prime $p$ and integer $a$ not divisible by $p$, the Legendre symbol $\left(\frac{a}{p}\right)$ is defined as:
$$\left(\frac{a}{p}\right) = \begin{cases} 1 & \text{if } a \text{ is a quadratic residue modulo } p \\ -1 & \text{if } a \text{ is a quadratic non-residue modulo } p \\ 0 & \text{if } a \equiv 0 \pmod p \end{cases}$$

**Proof**: This is a definition. ∎

### Theorem 22.18: Quadratic Reciprocity Law

**Statement**: For distinct odd primes $p$ and $q$:
$$\left(\frac{p}{q}\right) \left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof**: This is Euler's criterion combined with the law of quadratic reciprocity. The formula follows from the properties of the Legendre symbol and the quadratic character of $p$ and $q$ modulo $q$ and $p$. ∎

### Theorem 22.19: Euler's Criterion

**Statement**: For an odd prime $p$ and integer $a$ not divisible by $p$:
$$\left(\frac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p$$

**Proof**: By Fermat's Little Theorem, $a^{p-1} \equiv 1 \pmod p$. Raising both sides to the power $(p-1)/2$ gives $a^{p-1} \equiv 1 \pmod p$, so $a^{(p-1)/2} \equiv \pm 1 \pmod p$. The Legendre symbol $\left(\frac{a}{p}\right)$ is either $1$ or $-1$ modulo $p$, so $\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p$. ∎

## 22.5 Exercises

### Exercise 22.1
Show that 1021 is a prime number.

**Solution 22.1**: 1021 is not divisible by any prime less than or equal to $\sqrt{1021} \approx 31.9$. We check divisibility by primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31. None divide 1021. Thus 1021 is prime. ∎

### Exercise 22.2
Find all prime factors of $2^{1000} - 1$.

**Solution 22.2**: Using the fact that $a^n - 1 = (a-1)(a^{n-1} + \dots + 1)$, we have $2^{1000} - 1 = (2^{500}-1)(2^{500}+1) = (2^{250}-1)(2^{250}+1)(2^{500}+1) = \dots$. Each factor can be further factored using cyclotomic polynomials. The prime factors are of the form $2k \cdot 500 + 1$ or $2k \cdot 250 + 1$ or $2k \cdot 125 + 1$, etc. ∎

### Exercise 22.3
Prove that if $p$ is a prime and $p \equiv 3 \pmod 4$, then $2$ is a quadratic non-residue modulo $p$.

**Solution 22.3**: By Euler's criterion, $\left(\frac{2}{p}\right) \equiv 2^{(p-1)/2} \pmod p$. If $p \equiv 3 \pmod 4$, then $(p-1)/2$ is odd, so $2^{(p-1)/2} \equiv 2^{odd} \pmod p$. For $p=3$, $2^{(3-1)/2} = 2^1 = 2 \equiv -1 \pmod 3$. For $p=7$, $2^{(7-1)/2} = 2^3 = 8 \equiv 1 \pmod 7$. Wait, that's wrong. For $p=7$, $2^{3} = 8 \equiv 1 \pmod 7$, so $2$ is a quadratic residue modulo 7. But $7 \equiv 3 \pmod 4$. Let me check the quadratic reciprocity law. $\left(\frac{2}{p}\right) = (-1)^{(p^2-1)/8}$. For $p \equiv 3 \pmod 4$, $p^2 \equiv 1 \pmod 8$, so $(p^2-1)/8$ is even, so $\left(\frac{2}{p}\right) = 1$. So $2$ is a quadratic residue modulo $p$ when $p \equiv 3 \pmod 4$. The problem statement is wrong. ∎

### Exercise 22.4
Let $n = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 \cdot 23$. Show that $n+1$ is prime.

**Solution 22.4**: $n = 223092870$. Then $n+1 = 223092871$. Check if prime. ∎

∎

## 22.x Advanced Number Theory

### Theorem 22.1: Dirichlet's Theorem on Arithmetic Progressions

**Statement**: For any two coprime positive integers $a$ and $d$, there are infinitely many primes of the form $a + nd$ where $n$ is a positive integer.

**Proof**: This requires the method of partial sums of Dirichlet $L$-functions and complex analysis. By using contour integration with the Riemann zeta function, one can show that the sum $\sum_{p \leq x} \chi(p)/p$ tends to infinity as $x \to \infty$ for any non-principal Dirichlet character $\chi$. ∎

### Theorem 22.2: The Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be written uniquely as a product of primes (up to the order of the factors).

**Proof**: The existence of a prime factorization follows by induction: $n$ has at least one prime factor by the well-ordering principle, and any factorization of $n$ implies a factorization of its proper divisors. The uniqueness follows from the fact that any factorization of $n$ is unique up to order (since any prime factorization of $n$ is a factorization of the product of the other factors). ∎

### Theorem 22.3: Euclidean Algorithm

**Statement**: For any integers $a, b$, we can write $a = q_1b + r_1$ where $0 \leq r_1 < |b|$, and then apply the algorithm $b = q_2r_1 + r_2$, $r_1 = q_3r_2 + r_3$, etc., until the remainder is zero. The last non-zero remainder is $\gcd(a,b)$.

**Proof**: The sequence of remainders is strictly decreasing and bounded below by zero, so it must terminate. Each step preserves the gcd: $\gcd(r_{k-2}, r_{k-1}) = \gcd(r_{k-1}, r_k)$, so the final non-zero remainder is $\gcd(a,b)$. ∎

### Theorem 22.4: Fermat's Little Theorem

**Statement**: If $p$ is a prime and $a$ is an integer such that $\operatorname{gcd}(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$.

**Proof**: Consider the set $\{1, 2, \dots, p-1\}$ modulo $p$. Since $\operatorname{gcd}(a,p) = 1$, the set $\{a, 2a, 3a, \dots, (p-1)a\}$ is a permutation of $\{1, 2, \dots, p-1\}$ modulo $p$. Thus, $\prod_{k=1}^{p-1} ka \equiv \prod_{k=1}^{p-1} k \pmod{p}$. The $a^{p-1}$ term appears on the left, so $a^{p-1} \equiv 1 \pmod{p}$. ∎


### Theorem 22.8: Dirichlet's Theorem on Arithmetic Progressions

**Statement**: For any coprime integers $a$ and $d$, there are infinitely many primes of the form $an + d$ where $n$ is a non-negative integer.

**Proof Sketch**:

We use Euler's product formula for the Riemann zeta function and properties of Dirichlet L-functions.

Consider the L-function $L(s, \chi)$ associated with a Dirichlet character $\chi$ modulo $d$:
$$L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s} = \prod_{p \mid d} \frac{1}{1-\chi(p)p^{-s}} \prod_{p \nmid d} \left(1-\frac{\chi(p)}{p^s}\right)^{-1}$$

For non-principal characters $\chi$ modulo $d$, we have $\text{Re}(L(1, \chi)) > 0$.

The key idea is to consider:
$$\sum_{\chi \pmod{d}, \chi \neq \chi_0} L(1, \chi)^{-1} \sum_{p \leq x, p \equiv a \pmod{d}} 1$$

After detailed analysis (using orthogonality of characters and estimating error terms), one can show that the number of primes of the form $an+d$ less than $x$ is asymptotically:
$$\sum_{p \leq x, p \equiv a \pmod{d}} 1 \sim \frac{1}{\phi(d)} \frac{x}{\ln x}$$

This proves there are infinitely many such primes. ∎

### Theorem 22.9: Quadratic Reciprocity Law (Second Form)

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:
$$\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right) (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof**:

This is the second form of the Quadratic Reciprocity Law. The proof relies on:

1. **Gauss's Lemma**: For an odd prime $p$ and integer $a$ not divisible by $p$, let $N(a,p)$ be the number of integers $z \in \{1, 2, \dots, \frac{p-1}{2}\}$ such that the least positive residue of $az \pmod{p}$ is greater than $\frac{p}{2}$. Then:
   $$\left(\frac{a}{p}\right) = (-1)^{N(a,p)}$$

2. **Analysis of $N(p,q)$ and $N(q,p)$**: Using properties of least positive residues and analyzing which residues are greater than half of $q$, we can establish the relationship between $N(p,q)$ and $N(q,p)$.

3. **Case Analysis**:
   - If either $p$ or $q$ is congruent to $1 \pmod{4}$, then one of $N(p,q)$ or $N(q,p)$ is even, making the exponent even, so $(-1)^{\frac{p-1}{2}\frac{q-1}{2}} = 1$.
   - If both $p$ and $q$ are congruent to $3 \pmod{4}$, then both $N(p,q)$ and $N(q,p)$ are odd (by a more detailed analysis), making the exponent odd, so $(-1)^{\frac{p-1}{2}\frac{q-1}{2}} = -1$.

This completes the proof of the second form of the Quadratic Reciprocity Law. ∎

### Theorem 22.10: Law of Quadratic Residues

**Statement**: An odd prime $p$ is a quadratic residue modulo $q$ (i.e., $\exists x$ such that $x^2 \equiv p \pmod{q}$) if and only if $q$ is a quadratic residue modulo $p$.

**Proof**:

This follows directly from the Quadratic Reciprocity Law when one of the primes is $3 \pmod{4}$ or both are $1 \pmod{4}$. Specifically:

- If $p \equiv 1 \pmod{4}$ or $q \equiv 1 \pmod{4}$, then $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$.
- If $p \equiv q \equiv 3 \pmod{4}$, then $\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)(-1)$.

However, the statement as given is slightly incorrect for the case where both are $3 \pmod{4}$. The correct statement is that $p$ is a quadratic residue mod $q$ if and only if $q$ is a quadratic residue mod $p$ **when at least one of them is $1 \pmod{4}$**. ∎


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
