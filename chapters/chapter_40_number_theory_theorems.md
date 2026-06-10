# Chapter 40: Number Theory - Modular Forms, Elliptic Curves, and Class Field Theory

## 40.1 Modular Forms and Eisenstein Series

**Definition 40.1.** A **modular form** of weight $k$ for $SL(2,\mathbb{Z})$ is a holomorphic function $f: \mathbb{H} \to \mathbb{C}$ on the upper half-plane $\mathbb{H} = \{z \in \mathbb{C} \mid \text{Im}(z) > 0\}$ satisfying:
1. $f(\frac{az+b}{cz+d}) = (cz+d)^k f(z)$ for all $\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL(2,\mathbb{Z})$,
2. $f$ is holomorphic at the cusps ($f$ has a Fourier expansion $f(iy) = \sum_{n=0}^\infty a_n y^n$).

**Theorem 40.2 (Eisenstein Series Definition).** For $k \geq 4$ even, the Eisenstein series
$$G_k(\tau) = \sum_{(m,n) \in \mathbb{Z}^2 \setminus \{(0,0)\}} \frac{1}{(m\tau+n)^k} = 2\kappa_k + \frac{2(2\pi i)^k}{(k-1)!} \sum_{n=1}^\infty \sigma_{k-1}(n) q^n$$
where $\sigma_{k-1}(n) = \sum_{d|n} d^{k-1}$ and $q = e^{2\pi i \tau}$.

**Theorem 40.3 (Eisenstein Series are Modular Forms).** The Eisenstein series $G_k(\tau)$ is a modular form of weight $k$ for $SL(2,\mathbb{Z})$.

**Theorem 40.4 (Dimension Formula for Modular Forms).** Let $S_k$ be the space of cusp forms of weight $k$ for $SL(2,\mathbb{Z})$. Then
$$\dim S_k = \begin{cases} 0 & k \equiv 2 \pmod{12}, \\ \frac{k-13}{12} & k \equiv 0 \pmod{12}, \\ \frac{k-5}{12} & k \equiv 4,8 \pmod{12}. \end{cases}$$

**Theorem 40.5 (Modular Forms and Eisenstein Series).** Every modular form of weight $k$ for $SL(2,\mathbb{Z})$ is a linear combination of Eisenstein series and cusp forms.

**Theorem 40.6 (Moldenhauer's Theorem).** The Eisenstein series $G_{2m}$ are algebraically independent over $\mathbb{C}$ for $m \geq 2$.

**Theorem 40.7 (Euler's Partition Function).** The generating function for partition numbers $p(n)$ is
$$\sum_{n=0}^\infty p(n) q^n = \prod_{n=1}^\infty \frac{1}{(1-q^n)}.$$

**Theorem 40.8 (Ramanujan's Congruences).** For prime $p \geq 5$, $G_{12}(\tau)$ satisfies:
$$G_{12}(\tau) \pmod{G_{12}(\tau)} \cdot \frac{1}{q} \equiv 0 \pmod{p}, \quad \text{if } p-1 \text{ divides } 12.$$

**Theorem 40.9 (Ramanujan's Differential Equations).** The Eisenstein series satisfy:
$$q \frac{d}{dq} G_k = \frac{k}{12} G_k - \frac{k}{12} \sum_{n=1}^\infty \sigma_{k-1}(n) n q^n.$$

## 40.2 Elliptic Curves

**Definition 40.10.** An **elliptic curve** $E$ over $\mathbb{C}$ is given by the Weierstrass equation:
$$y^2 = x^3 + ax + b,$$
where the discriminant $\Delta = -16(4a^3 + 27b^2) \neq 0$.

**Theorem 40.11 (J-Invariant for Elliptic Curves).** For $E: y^2 = x^3 + ax + b$, the $j$-invariant is
$$j(E) = \frac{4a^3}{4a^3 + 27b^2}.$$

**Theorem 40.12 (Modularity Theorem - Wiles).** Every semistable elliptic curve over $\mathbb{Q}$ is modular, i.e., corresponds to a modular form of weight 2.

**Theorem 40.13 (Mordell-Weil Theorem).** For an elliptic curve $E$ over $\mathbb{Q}$, the group of rational points $E(\mathbb{Q})$ is finitely generated:
$$E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus T,$$
where $r$ is the rank and $T$ is the torsion subgroup.

**Theorem 40.14 (Néron-Polya-Schwarz Theorem).** The group $E(\mathbb{Q})$ of rational points on $E$ is a finitely generated abelian group.

**Theorem 40.15 (Weierstrass $\wp$-Function).** The $\wp$-function satisfies
$$\wp'(z)^2 = 4\wp(z)^3 - g_2 \wp(z) - g_3,$$
where $g_2, g_3$ are invariants of the elliptic curve.

**Theorem 40.16 (Complex Multiplication).** An elliptic curve $E$ has **CM** by an imaginary quadratic order $\mathcal{O} \subset \mathbb{C}$ if $\text{End}(E)$ contains $\mathcal{O}$.

**Theorem 40.17 (Shimura-Taniyama-Weierstrass).** Every elliptic curve over $\mathbb{Q}$ is isomorphic to a curve defined over $\mathbb{Q}$ with CM by an imaginary quadratic field.

**Theorem 40.18 (Tate's Theorem on Complex Multiplication).** Let $E/\mathbb{Q}$ be an elliptic curve with CM by $\mathbb{Q}(\sqrt{-d})$ where $d > 0$. Then there are only finitely many such curves.

**Theorem 40.19 (Siegel's Upper Bound).** For a number field $K$, the group $E(K)$ of rational points on an elliptic curve $E$ is finite.

**Theorem 40.20 (Mazur's Theorem on Torsion).** The torsion subgroup $E(\mathbb{Q})_{tors}$ of an elliptic curve over $\mathbb{Q}$ is one of the following groups: $\mathbb{Z}/n\mathbb{Z}$ for $n \leq 10$ or $n=12$, or $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2n\mathbb{Z}$ for $n \leq 4$.

**Theorem 40.21 (Frey Curve - Fermat's Last Theorem).** If $x^n + y^n + z^n = 0$ has a solution in $\mathbb{Z}$ with $n \geq 3$, then there exists an elliptic curve $E$ with $j(E)$ related to the solution.

## 40.3 Class Field Theory

**Theorem 40.22 (Artin Reciprocity Law).** For an abelian extension $L/K$ of global fields, there is a surjective homomorphism
$$\text{Cl}_K^0 \to \text{Gal}(L/K)$$
called the Artin map.

**Theorem 40.23 (Class Field Theory - Main Conjecture).** For a global field $K$ and abelian extension $L/K$, the Artin map induces an isomorphism
$$\text{Cl}_K^0 \cong \text{Gal}(L/K)^{\text{ab}}.$$

**Theorem 40.24 (Main Conjecture of Class Field Theory).** For an abelian extension $L/K$ of number fields, the Artin map is an isomorphism
$$\text{Cl}_K \cong \text{Gal}(L/K).$$

**Theorem 40.25 (Global Class Field Theory).** For a global field $K$ and abelian extension $L/K$, there is a canonical isomorphism
$$\text{Gal}(L/K) \cong \text{Cl}_K^{\text{ab}}.$$

**Theorem 40.26 (Kronecker-Weber Theorem).** Every abelian extension of $\mathbb{Q}$ is contained in a cyclotomic field $\mathbb{Q}(\zeta_n)$ for some $n$.

**Theorem 40.27 (Kronecker's Inequality).** For any finite abelian extension $L/\mathbb{Q}$, there exists an integer $n$ such that $L \subseteq \mathbb{Q}(\zeta_n)$.

**Theorem 40.28 (Main Theorem of Local Class Field Theory).** For a local field $K$ and abelian extension $L/K$, there is a canonical isomorphism
$$\text{Gal}(L/K) \cong K^{\text{ab}}/O_K^{\times}.$$

**Theorem 40.29 (Global to Local - Hasse Principle).** For a global field $K$ and abelian extension $L/K$, the global Artin map restricts to local Artin maps for each place $v$ of $K$.

**Theorem 40.30 (Hilbert Class Field).** For a number field $K$, the Hilbert class field $H_K$ is the maximal unramified abelian extension of $K$.

**Theorem 40.31 (Primary Genus Theory).** For a number field $K$, the primary genus theory describes the class group structure modulo $2$.

**Theorem 40.32 (Kronecker-Weber Theorem - General).** Every abelian extension of a global field $K$ is contained in a ray class field of $K$.

## 40.4 Analytic Number Theory

**Theorem 40.33 (Riemann Zeta Function).** The Riemann zeta function is defined by
$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \prod_{p} \frac{1}{1-p^{-s}}$$
for $\text{Re}(s) > 1$.

**Theorem 40.34 (Analytic Continuation of $\zeta$).** The Riemann zeta function extends to a meromorphic function on $\mathbb{C}$ with a simple pole at $s=1$.

**Theorem 40.35 (Euler Product Formula).** For $\text{Re}(s) > 1$,
$$\zeta(s) = \prod_{p \in \mathbb{P}} \frac{1}{1-p^{-s}}.$$

**Theorem 40.36 (Dirichlet Series).** For $\text{Re}(s) > 1$, a Dirichlet series $D(s) = \sum a_n n^{-s}$ has an analytic continuation to a meromorphic function on $\mathbb{C}$.

**Theorem 40.37 (Möbius Inversion Formula).** For arithmetic functions $f, g: \mathbb{Z}^+ \to \mathbb{C}$,
$$\sum_{d|n} g(d) = f(n) \iff g(n) = \sum_{d|n} \mu(n/d) f(d),$$
where $\mu$ is the Möbius function.

**Theorem 40.38 (Möbius Inversion for Dirichlet Series).** Let $F(s) = \sum a_n n^{-s}$ and $G(s) = \sum b_n n^{-s}$. Then
$$F(s) = G(s) \zeta(s) \iff a_n = \sum_{d|n} b_d \mu(n/d).$$

**Theorem 40.39 (Prime Number Theorem).** The prime number theorem states
$$\pi(x) \sim \frac{x}{\ln x} \quad \text{as } x \to \infty,$$
where $\pi(x)$ is the number of primes less than or equal to $x$.

**Theorem 40.40 (Riemann Hypothesis - Conjecture).** The Riemann Hypothesis states that all non-trivial zeros of $\zeta(s)$ have real part equal to $1/2$.

**Theorem 40.41 (Riemann Hypothesis - Statement).** The Riemann Hypothesis is equivalent to
$$|\zeta(1/2 + it)| \ll t^{1/4 + \epsilon} \quad \text{for all } t > 1.$$

**Theorem 40.42 (Class Number Formula).** For a number field $K$, the class number $h_K$ satisfies
$$\lim_{s \to 1} (s-1)\zeta_K(s) = \frac{2^{r_1} (2\pi)^{r_2} \text{Reg}}{\omega_R} \cdot h_K,$$
where $\text{Reg}$ is the regulator.

**Theorem 40.43 (Generalized Riemann Hypothesis).** The Generalized Riemann Hypothesis states that for any Dirichlet L-function $L(s,\chi)$, all non-trivial zeros have real part $1/2$.


## 40.x Number Theory Theorems

### Theorem 40.1: Dirichlet's Theorem on Arithmetic Progressions

**Statement**: For any two coprime positive integers $a$ and $d$, there are infinitely many primes of the form $a + nd$ where $n$ is a positive integer.

**Proof**: 
This is one of the deepest results in number theory. The proof uses the method of partial sums of Dirichlet $L$-functions and complex analysis. By using contour integration with the Riemann zeta function, one can show that the sum $\sum_{p \leq x} \chi(p)/p$ tends to infinity as $x \to \infty$ for any non-principal Dirichlet character $\chi$. ∎

### Theorem 40.2: The Fundamental Theorem of Arithmetic

**Statement**: Every integer $n > 1$ can be written uniquely as a product of primes (up to the order of the factors).

**Proof**: 
The existence of a prime factorization follows by induction: $n$ has at least one prime factor by the well-ordering principle, and any factorization of $n$ implies a factorization of its proper divisors. The uniqueness follows from the fact that any factorization of $n$ is unique up to order. ∎

### Theorem 40.3: Euclidean Algorithm

**Statement**: For any integers $a, b$, we can write $a = q_1b + r_1$ where $0 \leq r_1 < |b|$, and then apply the algorithm $b = q_2r_1 + r_2$, $r_1 = q_3r_2 + r_3$, etc., until the remainder is zero. The last non-zero remainder is $\gcd(a,b)$.

**Proof**: 
The sequence of remainders is strictly decreasing and bounded below by zero, so it must terminate. Each step preserves the gcd: $\gcd(r_{k-2}, r_{k-1}) = \gcd(r_{k-1}, r_k)$, so the final non-zero remainder is $\gcd(a,b)$. ∎

### Theorem 40.4: Fermat's Little Theorem

**Statement**: If $p$ is a prime and $a$ is an integer such that $\operatorname{gcd}(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$.

**Proof**: 
Consider the set $\{1, 2, \dots, p-1\}$ modulo $p$. Since $\operatorname{gcd}(a,p) = 1$, the set $\{a, 2a, 3a, \dots, (p-1)a\}$ is a permutation of $\{1, 2, \dots, p-1\}$ modulo $p$. Thus, $\prod_{k=1}^{p-1} ka \equiv \prod_{k=1}^{p-1} k \pmod{p}$. The $a^{p-1}$ term appears on the left, so $a^{p-1} \equiv 1 \pmod{p}$. ∎


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
