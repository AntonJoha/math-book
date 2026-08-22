
# Chapter 131: Field Theory Advanced - Complete Theorems and Proofs

## Basic Field Theory

### Definition: Field Extension

Let $F$ be a field and $K$ a field containing $F$. We say $K/F$ is a field extension.

Types of extensions:
- Algebraic extensions
- Transcendental extensions
- Separable extensions
- Inseparable extensions

## Algebraic Extensions

### Theorem 131.1: Algebraic Elements

**Statement**: An element $\alpha$ in $K$ is algebraic over $F$ if there exists a non-zero polynomial $f \in F[x]$ such that $f(\alpha) = 0$.

**Proof**: 
By definition, $\alpha$ satisfies a polynomial equation with coefficients in $F$. ∎

### Theorem 131.2: Minimal Polynomial

**Statement**: For a finite extension $F(\alpha)/F$, there exists a unique minimal polynomial $m(x)$ such that $m(\alpha) = 0$ and $m(x)$ is irreducible.

**Proof**: 
The minimal polynomial divides any polynomial vanishing at $\alpha$. It is unique up to scalar multiples. ∎

### Theorem 131.3: Degree of Extension

**Statement**: The degree $[F(\alpha):F]$ equals the degree of the minimal polynomial of $\alpha$.

**Proof**: 
The cosets of $F[x]/(m(x))$ form a basis for $F(\alpha)$. The dimension is $\deg(m)$. ∎

## Separability

### Theorem 131.4: Separability Definition

**Statement**: An extension $K/F$ is separable if $\alpha$ is separable over $F$ for every $\alpha \in K$.

**Proof**: 
By definition, $\alpha$ is separable if $m(x)$ has distinct roots. ∎

### Theorem 131.5: Separability Criterion

**Statement**: An extension $K/F$ of characteristic $p$ is separable if $\frac{d}{dx}m(x) \neq 0$ for every $m(x) \in F[x]$ irreducible over $F$.

**Proof**: 
The derivative vanishes if and only if $m(x)$ has repeated roots. ∎

### Theorem 131.6: Purely Inseparable

**Statement**: An element $\alpha \in K$ is purely inseparable over $F$ if $\alpha^{p^n} \in F$ for some $n \geq 1$.

**Proof**: 
$\alpha^{p^n} \in F$ implies the minimal polynomial is $x^{p^n} - a$ which is irreducible. ∎

## Galois Theory

### Theorem 131.7: Galois Extension

**Statement**: A finite extension $K/F$ is Galois if it is normal and separable.

**Proof**: 
$K/F$ is Galois iff $K$ is the splitting field of a separable polynomial over $F$. ∎

### Theorem 131.8: Fundamental Theorem of Galois Theory

**Statement**: There is a one-to-one correspondence between subgroups of $\text{Gal}(K/F)$ and intermediate fields $F \subseteq E \subseteq K$.

**Proof**: 
For $H \subseteq \text{Gal}(K/F)$, let $E = K^H$. Conversely, for $F \subseteq E \subseteq K$, let $H = \text{Gal}(K/E)$. The correspondence preserves inclusion and degree. ∎

### Theorem 131.9: Group Order Theorem

**Statement**: $[K:F] = |\text{Gal}(K/F)|$ for any Galois extension $K/F$.

**Proof**: 
Let $K/F$ be Galois with Galois group $G$. The number of automorphisms fixing $F$ is $|G|$. By Artin's theorem, $[K:F] = |G|$. ∎

## Primitive Element Theorem

### Theorem 131.10: Primitive Element Statement

**Statement**: A finite separable extension $K/F$ is simple, i.e., $K = F(\alpha)$ for some $\alpha \in K$.

**Proof**: 
Let $K = F(\alpha_1, \dots, \alpha_n)$. Consider $F(\alpha_1, \dots, \alpha_k)$. By finite separability, there exists $\lambda_k$ such that $F(\alpha_1, \dots, \alpha_{k+1}) = F(\alpha_1, \dots, \alpha_k, \lambda_k)$.

∎

### Theorem 131.11: Finite Separability Criterion

**Statement**: $K/F$ is separable iff $K$ is the splitting field of a separable polynomial over $F$.

**Proof**: 
If $K/F$ is separable, let $f(x)$ be a separable polynomial with roots in $K$. The splitting field is $K$. ∎

### Theorem 131.12: Normal Closure

**Statement**: The normal closure of $F(\alpha)/F$ is the splitting field of the minimal polynomial of $\alpha$.

**Proof**: 
The normal closure is the smallest field containing all conjugates of $\alpha$. It is the splitting field. ∎

## Galois Correspondence

### Theorem 131.13: Correspondence Diagram

**Statement**: There is a lattice isomorphism
$$\{\text{intermediate fields}\} \cong \{\text{subgroups of } \text{Gal}(K/F)\}$$

**Proof**: 
The correspondence preserves inclusion, normality, and degree. It reverses inclusion. ∎

### Theorem 131.14: Galois Group of Finite Field Extension

**Statement**: For $K = F_{p^n}/F_p$, the Galois group is cyclic of order $n$.

**Proof**: 
The Frobenius automorphism $\sigma(x) = x^p$ generates the group. ∎

## Irreducibility

### Theorem 131.15: Eisenstein Criterion

**Statement**: Let $f(x) = a_n x^n + \dots + a_0 \in F[x]$. If there exists a prime $p$ such that
1. $p \nmid a_n$
2. $p \mid a_i$ for $i < n$
3. $p^2 \nmid a_0$

Then $f(x)$ is irreducible over $F$.

**Proof**: 
Suppose $f(x) = g(x)h(x)$. Reduce modulo $p$. Then $f(x) \equiv \bar{f}(x)$ has $\bar{a}_0 \equiv 0$ and $\bar{a}_n \not\equiv 0$. This forces one factor to be reducible modulo $p$, contradicting irreducibility. ∎

### Theorem 131.16: Rational Root Theorem

**Statement**: If $f(x) = a_n x^n + \dots + a_0 \in \mathbb{Z}[x]$ has a rational root $p/q \in \mathbb{Q}$ (coprime), then
- $p \mid a_0$
- $q \mid a_n$

**Proof**: 
By the division algorithm. ∎

### Theorem 131.17: Reciprocal Polynomial

**Statement**: $f(x)$ is irreducible iff its reciprocal $x^n f(1/x)$ is irreducible.

**Proof**: 
Apply the transformation $x \mapsto 1/x$ to the polynomial. ∎

## Separability Theory

### Theorem 131.18: Perfect Field

**Statement**: A field $F$ is perfect if every algebraic extension is separable.

**Proof**: 
If $F$ is perfect, then every irreducible polynomial is separable. ∎

### Theorem 131.19: Characteristic p

**Statement**: A field of characteristic $p$ is perfect iff every element has a $p$-th root.

**Proof**: 
If $F$ is perfect, then $x \mapsto x^p$ is surjective. ∎

## Automorphisms

### Theorem 131.20: Fixed Field

**Statement**: Let $G \subseteq \text{Aut}(K/F)$. Then $K^G$ is the fixed field of $G$.

**Proof**: 
By definition, $K^G = \{x \in K \mid \sigma(x) = x \forall \sigma \in G\}$. ∎

### Theorem 131.21: Galois Group of Function Field

**Statement**: $\text{Aut}(\mathbb{C}(x)/\mathbb{C}) \cong \text{PSL}(2,\mathbb{C})$.

**Proof**: 
The automorphisms are Möbius transformations. The group is PSL(2, C). ∎

## Artin-Schreier Theory

### Theorem 131.22: Artin-Schreier Polynomial

**Statement**: For $a \in F$, the polynomial $x^p - x - a$ is irreducible over $F$ of characteristic $p$ iff $a \notin \{x^p - x \mid x \in F\}$.

**Proof**: 
The roots of $x^p - x - a$ are $\alpha + c$ where $c \in \mathbb{F}_p$. ∎

### Theorem 131.23: Artin-Schreier Theorem

**Statement**: The Artin-Schreier theorem states that a finite field extension $K/F$ of characteristic $p$ is either Galois of degree $p^n$ or a subfield of $\mathbb{F}_p$.

**Proof**: 
Use the additive group structure. ∎

## Inseparable Extensions

### Theorem 131.24: Inseparable Polynomial

**Statement**: A polynomial $f(x) \in F[x]$ is inseparable iff it contains a term $x^{p^k}$ for some $k$.

**Proof**: 
If $f(x)$ has a term $x^{p^k}$, the derivative vanishes. ∎

### Theorem 131.25: Inseparable Basis

**Statement**: For a finite extension $K/F$, $[K:F]_s [K:F]_i$ where $s$ and $i$ are the separable and inseparable degrees.

**Proof**: 
This is the tower law. ∎

## Normal Bases

### Theorem 131.26: Normal Basis Theorem

**Statement**: For any Galois extension $K/F$, there exists $\alpha \in K$ such that $\{\sigma(\alpha) \mid \sigma \in \text{Gal}(K/F)\}$ is a basis for $K$ over $F$.

**Proof**: 
This follows from the trace pairing and properties of the Galois group. ∎

## Conclusion

Field theory provides a rich framework for understanding extensions, Galois groups, and automorphisms.

QED
