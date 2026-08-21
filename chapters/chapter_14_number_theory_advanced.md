# Chapter 14: Advanced Number Theory

## 14.1 Introduction to Advanced Number Theory

Advanced number theory explores deep connections between number theory, algebra, analysis, and geometry. This chapter covers prime numbers, divisibility, congruences, and their applications in cryptography and computational number theory.

## 14.2 Divisibility and Prime Numbers

### Theorem 14.1: Infinitude of Primes (Euclid's Proof)

**Statement**: There are infinitely many prime numbers.

**Proof**:
Assume there are only finitely many primes: $p_1, p_2, \dots, p_n$.
Consider the number $N = p_1 p_2 \cdots p_n + 1$.

1. $N > 1$, so it has at least one prime divisor $q$.
2. $q$ must be one of $p_1, p_2, \dots, p_n$, otherwise $N$ would be a new prime.
3. But if $q = p_k$ for some $k$, then $p_k$ divides $N$ and $p_k$ divides $p_1 p_2 \cdots p_n$.
4. Therefore $p_k$ divides $N - p_1 p_2 \cdots p_n = 1$, which is impossible.
5. Contradiction! Therefore, there must be infinitely many primes. ∎

### Theorem 14.2: Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be uniquely written as the product of prime numbers, up to the order of the factors.

**Statement**: Every integer $n > 1$ can be uniquely written as the product of prime numbers, up to the order of the factors.

**Proof**:
We use strong induction on $n$.

**Base case**: $n = 2$. The prime factorization is simply $2$, which is unique.

**Inductive step**: Assume the theorem holds for all integers $m$ with $1 < m < n$.

- If $n$ is prime, its factorization is $n$ itself, which is unique.
- If $n$ is composite, $n = ab$ where $1 < a, b < n$.
  - By the inductive hypothesis, $a = p_1 p_2 \cdots p_k$ and $b = q_1 q_2 \cdots q_m$, where $p_i, q_j$ are primes.
  - Therefore, $n = p_1 p_2 \cdots p_k q_1 q_2 \cdots q_m$ is a factorization of $n$ into primes.
  - For uniqueness: Suppose $n = r_1 r_2 \cdots r_t$ is another prime factorization.
    - Suppose some $p_i = r_j$ for some $i, j$. Let $n' = n / p_i$.
    - Then $n' = (p_1 p_2 \cdots p_k q_1 q_2 \cdots q_m) / p_i = (r_1 r_2 \cdots r_t) / r_j$.
    - Since $p_i = r_j$, $n'$ is an integer $< n$.
    - By the inductive hypothesis, $n'$ has a unique factorization.
    - This implies the original factorizations are the same up to ordering.

The uniqueness of prime factorization is essential for many results in number theory, including the Chinese Remainder Theorem and the Euclidean algorithm. ∎

### Theorem 14.3: Euclid's Algorithm and GCD

**Statement**: For any two positive integers $a$ and $b$, there exist unique non-negative integers $x$ and $y$ such that $ax + by = \gcd(a, b)$.

**Proof**:
The existence follows from the Euclidean algorithm:
1. $\gcd(a, b) = \gcd(b, a \bmod b)$
2. Continue until $b$ divides $a$, at which point $\gcd(a, b) = a$.
3. Back-substitute to express $\gcd(a, b)$ as a linear combination of $a$ and $b$.

For uniqueness, suppose $ax + by = ax' + by' = g = \gcd(a, b)$.
Then $a(x - x') + b(y - y') = 0$, so $a(x - x') = -b(y - y')$.
By the definition of gcd, $a/\gcd(a,b)$ and $b/\gcd(a,b)$ are coprime.
Thus $x - x'$ must be divisible by $b/\gcd(a,b)$, but since $|x - x'|$ and $|y - y'|$ are non-negative, the only solution is $x = x'$ and $y = y'$. ∎

### Theorem 14.4: Bezout's Identity

**Statement**: For any integers $a$ and $b$ (not both zero), the set $\{ax + by : x, y \in \mathbb{Z}\}$ equals the set of all multiples of $\gcd(a, b)$.

**Proof**:
This is a direct consequence of the Euclidean algorithm and the division algorithm. The proof shows that any linear combination $ax + by$ is a multiple of $\gcd(a, b)$, and conversely, $\gcd(a, b)$ itself can be written as $ax + by$. ∎

### Theorem 14.5: GCD of Three Numbers

**Statement**: $\gcd(a, b, c) = \gcd(a, \gcd(b, c)) = \gcd(\gcd(a, b), c)$.

**Proof**:
By the associativity of the gcd operation, we can compute the gcd of three numbers in two steps. ∎

## 14.3 Congruences and Modular Arithmetic

### Theorem 14.6: Properties of Congruences

**Statement**: Let $a \equiv b \pmod{n}$ and $c \equiv d \pmod{n}$. Then:
1. $a + c \equiv b + d \pmod{n}$
2. $ac \equiv bd \pmod{n}$
3. $a^k \equiv b^k \pmod{n}$ for any positive integer $k$
4. $na \equiv n' a \pmod{n n'}$

**Proof**:
1. If $a = b + kn$ and $c = d + mn$, then $a + c = b + d + (k+m)n$, so $a + c \equiv b + d \pmod{n}$.
2. $ac = (b + kn)(d + mn) = bd + bmn + kdn + kmn^2 = bd + n(bm + kd + kmn)$, so $ac \equiv bd \pmod{n}$.
3. By induction on $k$: $a^1 \equiv b^1 \pmod{n}$ (given). If $a^k \equiv b^k \pmod{n}$, then $a^{k+1} = a \cdot a^k \equiv a \cdot b^k = b \cdot b^{k-1} \cdot a \equiv b \cdot b^k = b^{k+1} \pmod{n}$.
4. By definition of congruence, $na = n'a \pmod{nn'}$. ∎

### Theorem 14.7: Chinese Remainder Theorem

**Statement**: Let $n_1, n_2, \dots, n_k$ be pairwise coprime positive integers, and let $a_1, a_2, \dots, a_k$ be arbitrary integers. There exists a unique solution $x$ modulo $n_1 n_2 \cdots n_k$ to the system:
$$x \equiv a_i \pmod{n_i} \quad \text{for each } i = 1, 2, \dots, k$$

**Proof**:
Let $N = n_1 n_2 \cdots n_k$ and $N_i = N/n_i$. Since $\gcd(N_i, n_i) = 1$, there exist integers $y_i$ such that $N_i y_i \equiv 1 \pmod{n_i}$.

Consider $x = \sum_{i=1}^k a_i N_i y_i \pmod{N}$.

For each $j$:
- If $i \neq j$, then $N_i y_i$ is a multiple of $n_j$, so $a_i N_i y_i \equiv 0 \pmod{n_j}$.
- If $i = j$, then $N_j y_j \equiv 1 \pmod{n_j}$, so $a_j N_j y_j \equiv a_j \pmod{n_j}$.

Therefore, $x \equiv \sum_{i=1}^k a_i N_i y_i \equiv a_j \pmod{n_j}$ for each $j$.

For uniqueness, if $x_1 \equiv x_2 \pmod{n_i}$ for all $i$, then $x_1 \equiv x_2 \pmod{N_i}$ for all $i$.
Since $\gcd(N_1, \dots, N_k) = 1$, we have $x_1 \equiv x_2 \pmod{N}$ by Bézout's identity. ∎

### Theorem 14.8: Congruence for Powers

**Statement**: Let $a \equiv b \pmod{n}$. Then $a^k \equiv b^k \pmod{n^k}$ for any positive integer $k$.

**Proof**:
By induction on $k$.
- Base case: $k = 1$. $a \equiv b \pmod{n}$ is given.
- Inductive step: Assume $a^k \equiv b^k \pmod{n^k}$.
  - Then $a^k = b^k + q n^k$ for some integer $q$.
  - We have $a^{k+1} = a \cdot a^k = a(b^k + q n^k) = a b^k + a q n^k$.
  - Since $a \equiv b \pmod{n}$, let $a = b + r n$ for some integer $r$.
  - Then $a^{k+1} = (b + rn) b^k + (b + rn) q n^k = b^{k+1} + r n b^k + b q n^{k+1} + r q n^{k+2}$.
  - All terms except $b^{k+1}$ are multiples of $n^{k+1}$.
  - Therefore, $a^{k+1} \equiv b^{k+1} \pmod{n^{k+1}}$. ∎

### Theorem 14.9: Wilson's Theorem

**Statement**: A positive integer $p$ is prime if and only if $(p - 1)! \equiv -1 \pmod{p}$.

**Proof**:
**(Only if)** Let $p$ be prime. Consider the group $(\mathbb{Z}/p\mathbb{Z})^\times$, which has order $p-1$.
The elements $1, 2, \dots, p-1$ form this group. The product of all elements in a finite abelian group is the identity if there are no elements of order 2, or the product of elements of order 2.
For $(\mathbb{Z}/p\mathbb{Z})^\times$, the only element of order 2 is $-1 \equiv p-1$.
Therefore, $(p-1)! \equiv -1 \pmod{p}$.

**(If)** Suppose $(p-1)! \equiv -1 \pmod{p}$.
Then $p$ divides $(p-1)! + 1 = (p-1)(p-2)\cdots(1) + 1$.
Suppose $p$ is composite. Then $p = ab$ for some $1 < a < p$ and $1 < b < p$.
If $a \neq b$, then $a, b, \dots, p-1$ are all distinct and less than $p$, so $ab$ divides $(p-1)!$, which implies $p$ divides $(p-1)!$.
But $(p-1)! \equiv -1 \pmod{p}$, which is a contradiction.
Therefore, $p$ must be prime. ∎

### Theorem 14.10: Fermat's Little Theorem

**Statement**: Let $p$ be a prime number and $a$ an integer. Then $a^p \equiv a \pmod{p}$.

**Proof**:
If $p \nmid a$, then $(\mathbb{Z}/p\mathbb{Z})^\times$ is a cyclic group of order $p-1$.
By Fermat's little theorem in the language of group theory, $a^{p-1} \equiv 1 \pmod{p}$.
Multiplying by $a$, we get $a^p \equiv a \pmod{p}$.

If $p \mid a$, then $a^p \equiv 0 \equiv a \pmod{p}$.
In both cases, $a^p \equiv a \pmod{p}$. ∎

## 14.4 Quadratic Residues and Primitive Roots

### Theorem 14.11: Euler's Criterion

**Statement**: Let $p$ be an odd prime and $a$ an integer not divisible by $p$. Then:
$$a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod{p}$$
where $\left(\frac{a}{p}\right)$ is the Legendre symbol, which equals $1$ if $a$ is a quadratic residue modulo $p$, and $-1$ if $a$ is a quadratic non-residue modulo $p$.

**Proof**:
By Fermat's Little Theorem, $a^{p-1} \equiv 1 \pmod{p}$ if $p \nmid a$.
Therefore, $a^{(p-1)/2} \cdot a^{(p-1)/2} \equiv 1 \pmod{p}$.
This means $a^{(p-1)/2}$ is a solution to $x^2 \equiv 1 \pmod{p}$.
In $(\mathbb{Z}/p\mathbb{Z})^\times$, there are exactly two solutions to $x^2 \equiv 1 \pmod{p}$: $1$ and $-1$.
If $a$ is a quadratic residue, $a^{(p-1)/2}$ must be $1$. If $a$ is a quadratic non-residue, $a^{(p-1)/2}$ must be $-1$.
This follows because if $a^{(p-1)/2} = 1$, then $a$ is a quadratic residue (since $a$ would be a square of $a^{(p-1)/4}$ when $(p-1)/2$ is even).

Alternatively, let $g$ be a primitive root modulo $p$. Then any integer $a$ not divisible by $p$ can be written as $g^k \pmod{p}$ for some $0 \leq k < p-1$.
The Legendre symbol $\left(\frac{a}{p}\right) = \left(\frac{g^k}{p}\right) = \left(\frac{g}{p}\right)^k = (-1)^k$.
Also, $a^{(p-1)/2} = (g^k)^{(p-1)/2} = g^{k(p-1)/2} = (g^{p-1})^{k/2} = 1^k = 1$ if $k$ is even, and $g^{k(p-1)/2} = g^{(p-1)/2} = -1$ if $k$ is odd.
Thus $a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod{p}$. ∎

### Theorem 14.12: Quadratic Reciprocity Law

**Statement**: Let $p$ and $q$ be distinct odd primes. Then:
$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$

**Proof**:
We use the factorization of $x^2 - p$ in the finite field $\mathbb{F}_q$.
The polynomial $f(x) = x^2 - p \pmod{q}$ has a root if and only if $p$ is a quadratic residue modulo $q$.
Similarly, the polynomial $f(y) = y^2 - q \pmod{p}$ has a root if and only if $q$ is a quadratic residue modulo $p$.
The product of the roots of $x^2 - p \pmod{q}$ is $-p \equiv q-1 \equiv -1 \pmod{q}$.
The product of the roots of $y^2 - q \pmod{p}$ is $-q \equiv p-1 \equiv -1 \pmod{p}$.
This leads to a contradiction unless the product of Legendre symbols is $(-1)^{\frac{p-1}{2}\frac{q-1}{2}}$.
∎

## 14.5 Quadratic Fields and Class Number Formula

### Theorem 14.13: Quadratic Fields

**Statement**: The quadratic field $\mathbb{Q}(\sqrt{d})$ is generated by adjoining $\sqrt{d}$ to $\mathbb{Q}$, where $d$ is a square-free integer.

**Proof**:
By definition, $\mathbb{Q}(\sqrt{d}) = \{a + b\sqrt{d} : a, b \in \mathbb{Q}\}$.
This forms a field extension of $\mathbb{Q}$ of degree $2$ if $d$ is not a perfect square, and degree $1$ if $d$ is a perfect square. ∎

### Theorem 14.14: Fundamental Unit Theorem

**Statement**: Let $d$ be a square-free integer. Then the unit group of the ring of integers $\mathcal{O}_d$ in $\mathbb{Q}(\sqrt{d})$ is generated by $-1$ and a fundamental unit $\epsilon$ (if $d > 1$).

**Proof**:
The proof uses Dirichlet's Unit Theorem, which states that the unit group of a number field is isomorphic to $\mu_K \times \mathbb{Z}^{r_1 + r_2 - 1}$, where $\mu_K$ is the group of roots of unity, $r_1$ is the number of real embeddings, and $r_2$ is the number of complex conjugate pairs of embeddings.
For $\mathbb{Q}(\sqrt{d})$, we have $r_1 = 2$ and $r_2 = 0$ if $d > 0$, and $r_1 = 1$ and $r_2 = 0$ if $d < 0$.
This leads to a unit group of rank $1$, generated by a fundamental unit $\epsilon$. ∎

## 14.6 Applications in Cryptography

### Theorem 14.15: RSA Encryption

**Statement**: The RSA cryptosystem relies on the difficulty of factoring large integers. Given a large composite number $n = pq$, where $p$ and $q$ are large primes, it is computationally infeasible to determine $p$ and $q$ without knowing the private key $d$.

**Proof**:
The public key consists of $n$ and $e$, where $e$ is chosen such that $\gcd(e, \phi(n)) = 1$.
The private key is $d$, where $ed \equiv 1 \pmod{\phi(n)}$.
Encryption is $c \equiv m^e \pmod{n}$, and decryption is $m \equiv c^d \pmod{n}$.
The security of RSA relies on the fact that while factoring $n$ is easy if $p$ and $q$ are known, finding $p$ and $q$ from $n$ is computationally infeasible for sufficiently large $n$. ∎

### Theorem 14.16: Diffie-Hellman Key Exchange

**Statement**: The Diffie-Hellman key exchange protocol allows two parties to establish a shared secret key over an insecure channel, without having to send the key directly.

**Proof**:
Let $g$ be a primitive root modulo $p$, where $p$ is a large prime.
Party A chooses a secret integer $a$ and computes $A = g^a \pmod{p}$.
Party B chooses a secret integer $b$ and computes $B = g^b \pmod{p}$.
They exchange $A$ and $B$.
Party A computes $s = B^a \pmod{p} = (g^b)^a \pmod{p} = g^{ab} \pmod{p}$.
Party B computes $s = A^b \pmod{p} = (g^a)^b \pmod{p} = g^{ba} \pmod{p}$.
They share the same secret $s$.

This protocol relies on the discrete logarithm problem: given $g, p, g^x$, it is hard to find $x$. ∎

## Conclusion

Advanced number theory provides deep insights into prime numbers, divisibility, and modular arithmetic. The theorems presented here form the foundation for cryptographic protocols and computational number theory.

