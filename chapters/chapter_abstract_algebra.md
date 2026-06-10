# Chapter: Advanced Abstract Algebra

## 4.1 Field Theory and Extensions

### Theorem 4.1: Galois Correspondence

**Statement**: There is a one-to-one inclusion-reversing correspondence between:
1. Intermediate fields $E \subseteq F$ where $F$ is a finite Galois extension of $E$.
2. Subgroups $H \le \text{Gal}(F/E)$.

**Proof**: 
For each intermediate field $E \subseteq F$, define the fixed field $F^H = \{f \in F : \sigma(f) = f \text{ for all } \sigma \in H\}$. For each subgroup $H \le \text{Gal}(F/E)$, define the fixed field $F^H$. The correspondence preserves inclusions and satisfies $[F:E] = |\text{Gal}(F/E)|$ (fundamental theorem of Galois theory). ∎

### Theorem 4.2: Primitive Element Theorem

**Statement**: Let $F$ be a finite Galois extension of $K$. Then $F = K(\alpha)$ for some $\alpha \in F$ (i.e., $F/K$ is a simple extension).

**Proof**: 
Let $\{a_1, \dots, a_n\}$ be a basis for $F/K$. Choose $\alpha = a_1 + c a_2$ for some generic $c \in K$. Then $F = K(\alpha)$. This is proved using the fact that $\text{Gal}(F/K)$ acts transitively on roots of irreducible polynomials. ∎

### Theorem 4.3: Separability

**Statement**: An algebraic extension $F/K$ is separable iff the minimal polynomial of every $\alpha \in F$ has distinct roots. Equivalently, $F/K$ is separable iff $F \otimes_K K(t)$ has no nilpotent elements.

**Proof**: 
The condition of having distinct roots is equivalent to the derivative of the minimal polynomial not being identically zero. The tensor product characterization follows from the inseparable extension properties in positive characteristic. ∎

### Theorem 4.4: Normality

**Statement**: A finite extension $F/K$ is normal iff $F$ is the splitting field of some polynomial in $K[x]$.

**Proof**: 
If $F/K$ is normal and $f(x)$ is the minimal polynomial of any $\alpha \in F$, then $F$ contains all roots of $f(x)$. Conversely, if $F$ is the splitting field of $f(x)$, then $F$ contains all conjugates of $\alpha \in F$, so $F/K$ is normal. ∎

### Theorem 4.5: Galois Group Properties

**Statement**: Let $F/K$ be a finite Galois extension. Then:
1. $\text{Gal}(F/K)$ is finite with order $[F:K]$.
2. $\text{Gal}(F/K)$ acts transitively on the roots of any irreducible polynomial in $K[x]$ that splits in $F$.
3. $\text{Gal}(F/K) \subseteq S_n$ where $n$ is the degree of the splitting field over $K$.

**Proof**: 
These are standard results from Galois theory. The group order follows from the fundamental theorem. Transitivity and group structure follow from the normality and separability properties. ∎

## 4.2 Ring Theory

### Theorem 4.6: Noetherian Rings

**Statement**: A commutative ring $R$ is Noetherian iff every ascending chain of ideals stabilizes. Equivalently, every ideal is finitely generated.

**Proof**: 
This is the definition of a Noetherian ring, proved using the ascending chain condition. ∎

### Theorem 4.7: Artinian Rings

**Statement**: A commutative ring $R$ is Artinian iff every descending chain of ideals stabilizes. Equivalently, every ideal is finitely generated (and $R$ is Noetherian).

**Proof**: 
This is the definition of an Artinian ring. For Noetherian rings, every ideal is finitely generated, but Artinian rings have additional structure. ∎

### Theorem 4.8: Jacobson Radical

**Statement**: The Jacobson radical $J(R) = \{a \in R : 1 - ra \text{ is invertible for all } r \in R\}$ satisfies:
1. $J(R) = \bigcap \{M \text{ maximal ideals of } R\}$
2. $R/J(R)$ is semisimple
3. If $I \subseteq J(R)$, then $I$ is the Jacobson radical of some quotient.

**Proof**: 
These are standard properties of the Jacobson radical in ring theory. ∎

## 4.3 Module Theory

### Theorem 4.9: Finitely Generated Modules

**Statement**: Let $R$ be a Noetherian ring. Then every submodule of a finitely generated $R$-module is finitely generated.

**Proof**: 
This follows from the ascending chain condition on ideals. For a finitely generated module $M$, any submodule $N$ satisfies an ascending chain of submodules, which must stabilize. ∎

### Theorem 4.10: Structure Theorem for Finitely Generated Modules

**Statement**: Every finitely generated module $M$ over a principal ideal domain $R$ has a decomposition of the form:
$$M \cong \mathbb{Z}_d^k \oplus R_1 \oplus \dots \oplus R_m$$
where each $R_i$ is a cyclic module and $\gcd(d_1, \dots, d_m) = 0$.

**Proof**: 
This is the classical structure theorem for finitely generated modules over PID, proven using the Smith normal form. ∎

## 4.4 Homological Algebra

### Theorem 4.11: Universal Coefficient Theorem

**Statement**: For any $R$-module $M$ and any homology group $H_n(X; R)$, there is a short exact sequence:
$$0 \to H_n(X; R) \otimes \mathbb{Z} \to H_n(X; \mathbb{Z}) \otimes \mathbb{Z} \to \text{Tor}(H_{n-1}(X; \mathbb{Z}), \mathbb{Z}) \to 0$$

**Proof**: 
This follows from the Eilenberg-Steenrod axioms and properties of homology. ∎

## 4.5 Category Theory

### Theorem 4.12: Adjunctions

**Statement**: There is an adjunction between the category of groups and the category of abelian groups, given by the abelianization functor $G \mapsto G/[G, G]$.

**Proof**: 
The abelianization functor is left adjoint to the inclusion functor of abelian groups. ∎

### Theorem 4.13: Fiber Products

**Statement**: In the category of groups, the fiber product of $A$ and $B$ over $C$ (with maps $f: A \to C$, $g: B \to C$) is the pullback of the diagram $A \to C \leftarrow B$.

**Proof**: 
This follows from the universal property of the pullback in group theory. ∎

## 4.6 Historical Notes

The theory of fields and Galois theory developed through the work of Gauss, Lagrange, and ultimately Évariste Galois in the early 19th century. The formalization of ring and module theory emerged in the early 20th century through the work of Dedekind and Noether. The development of homological algebra in the 1930s-1950s by Cartan, Eilenberg, and Serre established the foundations of modern algebra.

## Exercises

### Exercise 4.1
Show that every field extension of prime degree is separable.

### Exercise 4.2
Prove that if $R$ is a Noetherian ring, then every ideal of $R$ is finitely generated.

### Exercise 4.3
Show that the fundamental theorem of Galois theory is preserved under taking quotients.

### Exercise 4.4
Prove that $\text{Gal}(F/E)$ is abelian iff all intermediate fields are normal over $E$.

### Exercise 4.5
Show that the direct product of two groups $G_1 \times G_2$ is not necessarily a simple group.

## Advanced Problems

**Problem 4.1**: Let $F/K$ be a Galois extension. Show that the Galois group acts transitively on the roots of any irreducible polynomial $f(x) \in K[x]$ that splits in $F$.

**Problem 4.2**: Let $R$ be a Noetherian ring. Prove that the set of regular elements (non-zero-divisors) is multiplicatively closed.

## Bibliography

1. Dummit, D.S., and Foote, R.M. "Abstract Algebra", 3rd ed. Pearson, 2004.
2. Lang, S. "Algebra". Springer, 1993.
3. Dummit and Foote, "Abstract Algebra", 2004.
4. Rotman, J.J. "An Introduction to Homological Algebra". Springer, 1993.
5. Mac Lane, S. "Categories for the Working Mathematician", Springer, 1971.
6. Weibel, C.A. "An Introduction to Homological Algebra", Cambridge UP, 1994.

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
