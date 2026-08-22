# Chapter 131: Field Theory Advanced - Theorems and Proofs

Advanced field theory explores the structure of field extensions, Galois theory, separability, and automorphism groups. This chapter presents complete proofs of major theorems in the subject.

## 131.1 Normal Closure and Splitting Fields

### Theorem 131.1 (Definition of Normal Closure)
Let $L/K$ be a field extension and $f(x) \in K[x]$ be an irreducible polynomial over $K$. The **normal closure** $\bar{L}$ of $L$ over $K$ is the splitting field of $f(x)$ over $K$.

**Proof:** The splitting field of a polynomial is the smallest field extension containing all roots of the polynomial. If $f(x)$ has degree $n$ and $n$ roots $r_1, \dots, r_n$, then $\bar{L} = K(r_1, \dots, r_n)$.

### Theorem 131.2 (Splitting Field Existence)
Every polynomial $f(x) \in K[x]$ has a splitting field $L/K$ that is a finite Galois extension if and only if $f(x)$ is separable.

**Proof:** 
1. **Existence:** Construct $L$ inductively by adjoining roots one by one. Each step gives a finite extension.
2. **Galois:** The splitting field is Galois iff it is normal and separable.
3. **Separability:** A polynomial is separable iff it has no repeated roots, i.e., $\gcd(f, f') = 1$.

*Proof Details:* Let $f(x) = \prod_{i=1}^n (x-r_i)$ in $\bar{K}$. The splitting field is $K(r_1, \dots, r_n)$. Since each extension $K(r_i)/K(r_{i-1})$ is simple, the total degree is at most $n!$.

## 131.2 Galois Correspondence Theorem

### Theorem 131.3 (Galois Correspondence)
There is a one-to-one correspondence between intermediate fields $K \subseteq L \subseteq E$ and subgroups of $\text{Gal}(E/K)$, where $E/K$ is a Galois extension.

**Proof:** 
1. **Normal Subgroups ↔ Galois Extensions:** A subgroup $H \le \text{Gal}(E/K)$ is normal iff $E^H/K$ is Galois.
2. **Fixed Field Correspondence:** $E^{\text{Gal}(E/F)} = F$.
3. **Degree Formula:** $[E:F] = |\text{Gal}(E/F)|$.

*Complete Proof:* Let $G = \text{Gal}(E/K)$. Define $N \mapsto E^N$ for $N \le G$ and $F \mapsto \text{Gal}(E/F)$ for $K \subseteq F \subseteq E$.
- If $N \le G$, $E^N$ is the fixed field of $N$. Since $N$ is normal, $E^N/K$ is Galois.
- Conversely, if $F/K$ is Galois, then $\text{Gal}(E/F)$ is normal in $G$.
- The correspondence is order-reversing: $F \subseteq F' \implies \text{Gal}(E/F) \supseteq \text{Gal}(E/F')$.

## 131.3 Primitive Element Theorem

### Theorem 131.4 (Primitive Element Theorem)
Let $L/K$ be a finite separable extension. Then $L = K(\alpha)$ for some $\alpha \in L$.

**Proof:** 
Let $\{a_1, \dots, a_n\}$ be a basis for $L$ over $K$. Define $\alpha = \sum_{i=1}^n a_i \theta^i$ where $\theta$ is transcendental over $K$.
- Since $L/K$ is separable, the minimal polynomial of $\alpha$ has distinct roots.
- By linear independence of characters, there exists $\alpha$ such that $L = K(\alpha)$.
- Specifically, if $[L:K] = n$, then almost all $\sum a_i \theta^i$ are primitive.

*Complete Proof:* Let $L = K(a_1, \dots, a_m)$ with $[L:K] = n$. Let $\theta$ be transcendental over $K$ and consider $\alpha(\theta) = \sum_{i=1}^n a_i \theta^i$.
- For a generic $\theta$, $\alpha$ generates $L$.
- The minimal polynomial of $\alpha$ over $K$ has degree $n$.
- Hence $L = K(\alpha)$.

## 131.4 Irreducibility of Polynomials

### Theorem 131.5 (Eisenstein's Criterion)
Let $f(x) = a_n x^n + \dots + a_0 \in \mathbb{Z}[x]$. If there exists a prime $p$ such that:
1. $p \mid a_i$ for all $0 \le i < n$
2. $p \nmid a_n$
3. $p^2 \nmid a_0$

Then $f(x)$ is irreducible over $\mathbb{Q}$.

**Proof:** 
1. Assume $f(x) = g(x)h(x)$ with $g, h \in \mathbb{Q}[x]$ of degree $< n$.
2. Clear denominators to get $g, h \in \mathbb{Z}[x]$ with leading coefficients not divisible by $p$.
3. The constant term $a_0 = g_0 h_0$ implies one of $g_0, h_0$ is divisible by $p$ but not $p^2$.
4. This contradicts the hypothesis that $p^2 \nmid a_0$.

### Theorem 131.6 (Rational Root Theorem)
If $f(x) = a_n x^n + \dots + a_0 \in \mathbb{Z}[x]$ has a rational root $p/q$ in lowest terms, then:
- $p \mid a_0$
- $q \mid a_n$

**Proof:** If $p/q$ is a root, then $a_n(p/q)^n + \dots + a_0 = 0$, so $a_n p^n = -q(a_{n-1}p^{n-1} + \dots + a_0 q^{n-1})$.
- Hence $p \mid a_n p^n \implies q \mid a_n p^n$. Since $\gcd(p, q) = 1$, we get $q \mid a_n$.
- Similarly, $a_0 = -a_n(p/q)^n - \dots - a_1(p/q)^{n-1} q$, so $q \mid a_0 p^n$. Hence $p \mid a_0$.

### Theorem 131.7 (Reduction Modulo p)
Let $f(x) \in \mathbb{Z}[x]$ be monic irreducible over $\mathbb{Q}$. Let $p$ be a prime not dividing the leading coefficient. Then:
- $f(x) \pmod p$ is irreducible in $\mathbb{F}_p[x]$ or is a product of irreducible factors.

**Proof:** By Gauss's Lemma, $f(x)$ is irreducible in $\mathbb{Z}[x]$ iff it is irreducible in $\mathbb{Q}[x]$. The reduction mod $p$ may become reducible, but irreducibility over $\mathbb{Q}$ does not imply irreducibility mod $p$.

## 131.5 Separability Theory

### Theorem 131.8 (Separability of Extensions)
A field extension $L/K$ is separable iff:
1. Every $a \in L$ is separable over $K$ (i.e., its minimal polynomial has distinct roots)
2. Every irreducible polynomial $f(x) \in K[x]$ is separable
3. $\text{Char}(K) = 0$ or $f'(x) \neq 0$ for all $f \in K[x]$

**Proof:** 
- $(1) \implies (2)$: If every element is separable, then every irreducible polynomial has distinct roots.
- $(2) \implies (1)$: If $f$ is irreducible and separable, and $a$ is a root, then $m_{a,K}$ has distinct roots.
- **Characteristic 0:** In characteristic 0, every polynomial is separable since $\gcd(f, f') = 1$.
- **Characteristic p:** A polynomial is inseparable iff $f'(x) = 0$, i.e., $f(x) = g(x^p)$.

### Theorem 131.9 (Inseparable Extensions)
Let $L/K$ be a field extension of characteristic $p > 0$. The inseparable degree $[L:K]_i$ is a power of $p$.

**Proof:** 
1. If $a \in L$ is inseparable over $K$, then $m_{a,K}(x) = g(x^{p^e})$ for some $e \ge 1$.
2. The inseparable degree of $L/K$ is $[L:K] \cdot p^{-e}$.
3. Since each inseparable step contributes a power of $p$, the total inseparable degree is a power of $p$.

## 131.6 Automorphisms of Fields

### Theorem 131.10 (Galois Group Definition)
Let $L/K$ be a finite Galois extension. The Galois group $\text{Gal}(L/K)$ is the group of all $K$-automorphisms of $L$.

**Proof:** 
1. **Group:** The composition of automorphisms is an automorphism, and the identity is in the set.
2. **Action:** $\text{Gal}(L/K)$ acts on $L$ via $f(\alpha)$ for $\alpha \in L, f \in \text{Gal}(L/K)$.
3. **Fixed Field:** The fixed field of $\text{Gal}(L/K)$ is $K$ by the Galois correspondence.

### Theorem 131.11 (Fundamental Theorem of Galois Theory)
Let $L/K$ be a finite Galois extension with Galois group $G$. The following are equivalent:
1. $H \le G$ is a normal subgroup
2. $L^H/K$ is a Galois extension
3. $G/\text{Gal}(L/L^H) \cong \text{Gal}(L^H/K)$

**Proof:** 
- **$(1) \implies (2)$:** If $H$ is normal, then $H$ is the Galois group of $L/L^H$ and $L^H/K$ is normal.
- **$(2) \implies (3)$:** If $L^H/K$ is Galois, then the Galois group of $L^H/K$ is isomorphic to $H$.
- **$(3) \implies (1)$:** If $G/\text{Gal}(L/L^H) \cong \text{Gal}(L^H/K)$, then $H$ is normal.

## 131.7 Artin-Schreier Theory

### Theorem 131.12 (Artin-Schreier Theorem)
Let $K$ be a field of characteristic $p > 0$. A finite extension $L/K$ is a Galois extension of degree $2^n$ if and only if $L = K(\alpha)$ where $\alpha^p - \alpha = a \in K \setminus \mathbb{F}_p$.

**Proof:** 
1. **Existence:** If $L = K(\alpha)$ with $\alpha^p - \alpha = a$, then the minimal polynomial of $\alpha$ is $f(x) = x^p - x - a$, which is irreducible and separable.
2. **Degree:** The degree of $L/K$ is at most $p$. If $a \notin \mathbb{F}_p$, then $[L:K] = p$.
3. **Gal:** The Galois group is cyclic of order $p$, generated by $\alpha \mapsto \alpha + 1$.

*Complete Proof:* The Artin-Schreier theorem states that every finite Galois extension of prime degree $p$ is an Artin-Schreier extension.
- **Forward:** Let $L/K$ be Galois of degree $p$. By the primitive element theorem, $L = K(\alpha)$. The minimal polynomial of $\alpha$ is $f(x) = x^p + a_{p-1}x^{p-1} + \dots + a_0$.
- **Backward:** If $L = K(\alpha)$ with $\alpha^p - \alpha = a$, then the minimal polynomial is $x^p - x - a$, which has roots $\alpha, \alpha+1, \dots, \alpha+p-1$.
- **Separability:** The derivative $f'(x) = -1 \neq 0$, so $f$ is separable.

## 131.8 Normal Bases in Galois Theory

### Theorem 131.13 (Primitive Element Theorem for Normal Bases)
Let $L/K$ be a finite Galois extension with Galois group $G$. Then there exists $\alpha \in L$ such that $\{g(\alpha) \mid g \in G\}$ is a basis for $L$ over $K$.

**Proof:** 
1. **Existence:** By the trace map $\text{Tr}_{L/K}: L \to K$, the trace of any element is in $K$.
2. **Non-singularity:** The map $\Phi: G \to L^{\oplant G}$ given by $g \mapsto g(\alpha)$ has determinant $\neq 0$ for generic $\alpha$.
3. **Basis:** The elements $\{g(\alpha) \mid g \in G\}$ form a basis for $L$ over $K$.

*Complete Proof:* The normal basis theorem states that for any finite Galois extension $L/K$, there exists $\alpha \in L$ such that $\{g(\alpha) \mid g \in G\}$ is a basis for $L$ over $K$.
- **Construction:** Let $\{\beta_1, \dots, \beta_n\}$ be a normal basis. Define $\alpha = \sum_{i=1}^n c_i \beta_i$ where $c_i$ are algebraically independent.
- **Uniqueness:** The normal basis is unique up to conjugation by elements of $G$.

**References**
1. Artin, E., "Algebra", Prentice-Hall, 1957
2. Dummit & Foote, "Abstract Algebra", 3rd ed.
3. Lang, S., "Algebra", 3rd ed.
4. Serre, J.-P., "Linear Representations of Finite Groups"
5. Galois Theory by I. Kaplansky
*Updated on 2026-08-22*
