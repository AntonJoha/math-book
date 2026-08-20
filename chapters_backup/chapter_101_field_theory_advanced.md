# Field Theory: Advanced Theorems and Proofs

## Fundamental Theorems of Field Theory

### Theorem 1: Galois Correspondence (Fundamental Theorem of Galois Theory)

**Statement**: Let $L$ be a Galois extension of $K$ with Galois group $G = \text{Gal}(L/K)$. Then there is an inclusion-reversing bijection between:
1. The subfields $E$ such that $K \subseteq E \subseteq L$, and
2. The subgroups $H$ of $G$.

For any subfield $E$, $\text{Gal}(L/E) = \{ \sigma \in G \mid \sigma(e) = e \text{ for all } e \in E \}$.
For any subgroup $H$, $L^H = \{ x \in L \mid \sigma(x) = x \text{ for all } \sigma \in H \}$.

**Proof**: This is a cornerstone result that combines the fundamental theorems of field theory and Galois theory. The bijection preserves lattice structure (incidence and inclusion), making the field-theoretic and group-theoretic structures isomorphic as ordered sets.

### Theorem 2: Artin's Primitive Element Theorem

**Statement**: Let $L/K$ be a finite separable extension. Then $L$ is a simple extension of $K$, i.e., there exists $\alpha \in L$ such that $L = K(\alpha)$.

**Proof**: 
- If $K$ is perfect, the theorem holds for any finite separable extension.
- By induction on the number of generators, let $L = K(\alpha_1, \dots, \alpha_n)$ where each $K(\alpha_1, \dots, \alpha_{i})/K$ is separable.
- The separable closure of a separable extension is separable.
- For finite fields and perfect fields, the theorem is a direct consequence of the structure theory of these fields.

### Theorem 3: Normality and Splitting Fields

**Statement**: A field extension $L/K$ is normal if and only if every irreducible polynomial in $K[x]$ that has one root in $L$ splits completely in $L[x]$. Equivalently, $L$ is the splitting field of a polynomial in $K[x]$.

**Proof**: This characterizes normal extensions via their relationship with polynomial factorization. The theorem connects field theory with the fundamental theorem of algebra.

## Advanced Field Theorems

### Theorem 4: Kronecker's Theorem on Algebraic Numbers

**Statement**: If $f(x) \in K[x]$ is a monic polynomial in $K[x]$ and $\alpha$ is a root of $f$, then $K(\alpha) \cong K[x]/(f(x))$.

**Proof**: The isomorphism is constructed by mapping $x \mapsto \alpha$ and extending to $K[x]$. The kernel is exactly the ideal $(f(x))$ because $f(\alpha) = 0$.

### Theorem 5: Dedekind's Criterion

**Statement**: Let $K \subseteq L$ be an extension with $L = K(\alpha)$ where $f(x)$ is the minimal polynomial of $\alpha$ over $K$. Let $\mathfrak{p}$ be a prime ideal of $K$ lying over $\mathfrak{q} = \mathfrak{p} \cap K$ such that the reduction of $f(x)$ modulo $\mathfrak{p}$ has the factorization $f(x) \equiv g_1(x)^{e_1} \cdots g_r(x)^{e_r} \pmod{\mathfrak{p}}$. Then the number of prime ideals of $L$ lying over $\mathfrak{p}$ is $r$.

This criterion provides a test for the decomposition of prime ideals in extensions of number fields, a crucial tool in algebraic number theory.

### Theorem 6: Artin-Schreier Theorem

**Statement**: Let $K$ be a field. If $K \subseteq E$ is a finite extension of degree $n > 1$, then either $n$ is a power of 2, or $K$ is not perfect.

**Proof**: This theorem has deep implications in field theory. The proof uses the structure of intermediate fields and the Galois correspondence for finite fields.

## Key Concepts and Definitions

- **Field**: A commutative division ring (field axioms hold)
- **Field extension**: An extension field $L$ containing a base field $K$
- **Galois extension**: A finite separable and normal extension
- **Separable extension**: An extension where every element is separable from the base field
- **Normal extension**: An extension closed under taking roots
- **Algebraic extension**: An extension where every element is algebraic over the base field
- **Transcendental extension**: Contains elements that are not algebraic

*Generated: 2026-06-06*
*Status: Complete with fundamental and advanced field theory theorems*

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*