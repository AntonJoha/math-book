# Field Theory

Field theory studies the properties of fields and the extensions between them. It connects field theory with Galois theory, which studies automorphism groups of field extensions.

## 7.1 Field Extensions

### Definition

**Definition (Field Extension)**: A field extension is a field $E$ containing a subfield $F$. We write $E/F$ for an extension, meaning $F \subseteq E$.

**Theorem 7.1 (Tower Law)**: 

If $F \subseteq E \subseteq L$ is a tower of field extensions, then:
$$[L:F] = [L:E][E:F]$$

**Proof**: Let $\{e_1, \dots, e_n\}$ be a basis for $E/F$ and $\{l_1, \dots, l_m\}$ be a basis for $L/E$. We construct a bilinear map $\Phi: E^m \times L^n \to L$ by $\Phi((e_{i_1}, \dots, e_{i_m}), (l_{j_1}, \dots, l_{j_n})) = \sum_{i,j} e_{i_1} \cdot l_{j_1} \cdot \dots$ and show it induces an isomorphism. ∎

### Degree of Extension

**Theorem 7.2 (Algebraic Elements)**: 

An element $\alpha \in E$ is algebraic over $F$ if there exists a non-zero polynomial $f(x) \in F[x]$ such that $f(\alpha) = 0$. The minimal polynomial of $\alpha$ over $F$ is unique up to scalar multiplication.

**Theorem 7.3 (Field of Fractions)**: 

If $R$ is an integral domain, its field of fractions $F(R)$ consists of fractions $a/b$ with $a, b \in R, b \neq 0$.

**Proof**: Define an equivalence relation $a/b \sim c/d$ iff $ad = bc$. Well-defined operations:
- $(a/b) + (c/d) = (ad+bc)/bd$
- $(a/b) \cdot (c/d) = ac/bd$
These satisfy field axioms. ∎

## 7.2 Algebraic Closure

### Existence

**Theorem 7.4 (Algebraic Closure)**: 

Every field $F$ has an algebraic closure $\overline{F}$, an algebraically closed field containing $F$ as a subfield, such that every element of $\overline{F}$ is algebraic over $F$.

**Proof**: Construct $\overline{F}$ as the direct limit of all algebraic extensions of $F$. By Zorn's lemma, there exists a maximal algebraic extension, which must be algebraically closed. ∎

**Theorem 7.5 (Unique Algebraic Closure)**: 

Every algebraic closure of $F$ is isomorphic to any other algebraic closure.

**Proof**: Let $\overline{F_1}$ and $\overline{F_2}$ be algebraic closures of $F$. Every element in $\overline{F_1}$ is a root of a polynomial in $F[x]$. There's an isomorphism between any two such algebraic closures. ∎

## 7.3 Galois Theory

### Basic Theory

**Definition (Galois Group)**: The Galois group $\operatorname{Gal}(E/F)$ of a Galois extension $E/F$ is the group of field automorphisms $\sigma: E \to E$ such that $\sigma(f) = f$ for all $f \in F$.

**Theorem 7.6 (Fundamental Theorem of Galois Theory)**: 

Let $E/F$ be a finite Galois extension with Galois group $G$. There is a bijection between:
1. Subfields $F \subseteq M \subseteq E$
2. Subgroups $H \leq G$

This correspondence reverses inclusion: $M_1 \subseteq M_2 \iff H_1 \supseteq H_2$.

**Proof**: For each subfield $M$, let $G(M) = \{\sigma \in G : \sigma|_M = \operatorname{id}_M\}$. For each subgroup $H$, let $E^H = \{x \in E : \sigma(x) = x \text{ for all } \sigma \in H\}$. The fixed field theorem shows $[E:E^H] = |H|$ and $[E^H:F] = [G:G(E^H)]$. ∎

**Corollary 7.7 (Galois Correspondence Properties)**: 

1. $E^{\operatorname{Gal}(E/F)} = F$
2. $\operatorname{Gal}(E/M) \leq \operatorname{Gal}(E/N)$ when $N \subseteq M$
3. $\operatorname{Gal}(E/M \cap N) = \operatorname{Gal}(E/M) \cdot \operatorname{Gal}(E/N)$

**Proof**: Follows directly from the fundamental theorem and properties of field intersections and subgroup products. ∎

### Solvability by Radicals

**Theorem 7.8 (Solvable Groups)**: 

A finite group $G$ is solvable if there exists a normal series:
$$G = G_0 \geq G_1 \geq \dots \geq G_n = \{1\}$$
such that $G_{i+1}/G_i$ is cyclic for all $i$.

**Theorem 7.9 (Galois Solvability)**: 

A polynomial $f(x) \in F[x]$ of degree $n$ is solvable by radicals if and only if its Galois group $G \leq S_n$ is solvable.

**Proof**: The splitting field $E$ of $f(x)$ is a finite extension of $F$. By Galois theory, $E/F$ is Galois with group $G$. The extension is solvable by radicals iff $G$ has a subnormal series with abelian quotients. ∎

### Examples

**Theorem 7.10 (Galois Group of $x^5 - 2$)**: 

The Galois group of $x^5 - 2$ over $\mathbb{Q}$ is $D_5$, the dihedral group of order 10.

**Proof**: The roots are $\sqrt[5]{2}, \zeta_5 \sqrt[5]{2}, \zeta_5^2 \sqrt[5]{2}, \zeta_5^3 \sqrt[5]{2}, \zeta_5^4 \sqrt[5]{2}$ where $\zeta_5 = e^{2\pi i/5}$. The splitting field is $\mathbb{Q}(\sqrt[5]{2}, \zeta_5)$. The Galois group permutes the roots, giving $D_5$. ∎

**Theorem 7.11 (Impossibility of trisecting an angle)**: 

There is no field automorphism $\phi: \mathbb{Q}(\cos(2\pi/7)) \to \mathbb{Q}(\cos(2\pi/7))$ fixing $\mathbb{Q}$.

**Proof**: The minimal polynomial of $\cos(2\pi/7)$ over $\mathbb{Q}$ has degree 3 and its Galois group is $C_3$. A solution to $\cos(2\pi/7)$ by cube roots would require a solvable extension, but $C_3$ is not a 2-group. ∎

## 7.4 Transcendental Extensions

### Transcendence Basis

**Theorem 7.12 (Transcendence Degree)**: 

The transcendence degree of a field extension $E/F$ is the cardinality of a maximal linearly independent subset over $F$.

**Theorem 7.13 (Primitive Element Theorem)**: 

If $E/F$ is a finite separable extension, then there exists $\alpha \in E$ such that $E = F(\alpha)$.

**Proof**: Let $\{a_1, \dots, a_n\}$ be a basis for $E$ over $F$. For $\alpha \neq a_1$, consider the polynomial $f(x) = \prod_{i=2}^n (x - a_i + a_1 - \alpha)$. By separability, $f(\alpha) \neq 0$ implies $\alpha \notin \{a_2, \dots, a_n\}$. Thus there's an element generating $E$. ∎

**Theorem 7.14 (Separability)**: 

A polynomial $f \in F[x]$ is separable if it has no multiple roots in $\overline{F}$. $f$ is separable iff $f, f'$ are coprime in $F[x]$.

**Proof**: If $f = gh$ and $g, h$ are coprime, then $\gcd(f, f') = \gcd(g, f') \cdot \gcd(h, f')$. ∎

## 7.5 Normal Extensions

**Theorem 7.15 (Normal Extension)**: 

A finite extension $E/F$ is normal if every irreducible polynomial in $F[x]$ that has a root in $E$ splits completely in $E[x]$.

**Theorem 7.16 (Normality Conditions)**: 

An extension $E/F$ is normal iff:
1. $E$ is the splitting field of a polynomial in $F[x]$
2. Every embedding of $E$ into $\overline{F}$ maps $E$ to $E$
3. Every polynomial in $F[x]$ having a root in $E$ splits in $E$

**Proof**: These are equivalent characterizations of normal extensions. ∎

## 7.6 Field Invariants

**Theorem 7.17 (Discriminant)**: 

The discriminant $\Delta(f)$ of a polynomial $f(x) = a_n x^n + \dots + a_0$ is a symmetric function of the roots of $f$.

**Proof**: $\Delta(f) = a_n^{2n-2} \prod_{i<j} (r_i - r_j)^2$ where $r_i$ are roots. ∎

**Theorem 7.18 (Norm and Trace)**: 

For a finite extension $E/F$ and $\alpha \in E$, the norm $\operatorname{N}_{E/F}(\alpha)$ and trace $\operatorname{Tr}_{E/F}(\alpha)$ are coefficients of the characteristic polynomial of $\alpha$.

**Proof**: $\operatorname{N}_{E/F}(\alpha) = \det(\phi_\alpha)$ and $\operatorname{Tr}_{E/F}(\alpha) = \operatorname{Tr}(\phi_\alpha)$ where $\phi_\alpha: E \to E$ is $x \mapsto \alpha x$. ∎

## Exercises

- Prove the primitive element theorem for separable extensions.
- Show that $\mathbb{Q}(\sqrt[3]{2}, \sqrt[3]{3})$ has degree 18 over $\mathbb{Q}$.
- Prove that $x^5 - 1$ is solvable by radicals over $\mathbb{Q}$.
- Use Galois theory to show that $x^3 - 2$ has roots expressible by radicals.


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*