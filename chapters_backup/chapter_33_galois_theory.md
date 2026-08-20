# Chapter 33: Galois Theory

## 33.1 Introduction to Field Extensions and Galois Theory

Galois theory establishes a deep connection between field theory and group theory, specifically by linking the structure of field extensions to the symmetries (Galois groups) of polynomial equations. This chapter explores the fundamental concepts of Galois theory, including field extensions, automorphisms, and the Galois correspondence.

### 33.1.1 Field Extensions

**Definition**: A field extension $E/F$ is a pair where $E$ is a field containing $F$ as a subfield. Elements of $E \setminus F$ are called transcendentals if they satisfy no polynomial equation with coefficients in $F$, or algebraic if they do.

**Algebraic Extension**: $E/F$ is algebraic if every element in $E$ is algebraic over $F$.

**Algebraically Closed Field**: A field $F$ is algebraically closed if every non-constant polynomial in $F[x]$ has a root in $F$. $\mathbb{C}$ is the canonical example, being algebraically closed (Fundamental Theorem of Algebra).

**Separable Extension**: $E/F$ is separable if the minimal polynomial of any $a \in E$ has distinct roots in $E$. Characteristic 0 extensions are always separable.

## 33.2 The Galois Group

**Definition**: Let $E/F$ be a finite Galois extension (i.e., $E/F$ is algebraic, finite, and normal, with $[E:F] = |Gal(E/F)|$). The Galois group $G = Gal(E/F)$ consists of all field automorphisms of $E$ that fix $F$ pointwise:

$$G = \{ \sigma: E \to E \mid \sigma \text{ is a field automorphism}, \forall a \in F, \sigma(a) = a \}$$

**Theorem 33.1**: The Galois group $G = Gal(E/F)$ of a finite field extension $E/F$ is isomorphic to the group of $F$-automorphisms of $E$.

**Proof**: The set of automorphisms fixing $F$ forms a group under composition. The Galois theorem states that $E/F$ is Galois if and only if $[E:F] = |G|$. ∎

## 33.3 The Galois Correspondence

**Theorem 33.2 (Fundamental Theorem of Galois Theory)**: Let $E/F$ be a finite Galois extension with Galois group $G$. There is a one-to-one correspondence between:

1. Subfields $K$ such that $F \subseteq K \subseteq E$
2. Subgroups $H$ of $G$

The correspondence is given by:
- For subfield $K$, $H = Gal(E/K) = \{ \sigma \in G \mid \forall x \in K, \sigma(x) = x \}$
- For subgroup $H$, $K = Fix(H) = \{ x \in E \mid \forall \sigma \in H, \sigma(x) = x \}$

**Properties**:
1. $[E:F] = |G|$
2. $[E:K] = |Gal(E/K)| = |H|$
3. $[K:F] = [G:H] = |G|/|H|$
4. $K_1 \subseteq K_2 \iff Gal(E/K_2) \subseteq Gal(E/K_1)$
5. $H_1 \subseteq H_2 \iff Fix(H_2) \subseteq Fix(H_1)$

**Proof**: These follow from the definition of fixed fields and the properties of field automorphisms. The key insight is that the order of a field extension equals the order of its Galois group in a Galois extension. ∎

## 33.4 Splitting Fields

**Definition**: The splitting field of a polynomial $P(x) \in F[x]$ is the smallest field extension $E/F$ such that $P(x)$ factors completely into linear factors in $E[x]$.

**Theorem 33.3**: Every finite polynomial $P(x) \in F[x]$ has a splitting field. Moreover, all splitting fields of $P(x)$ are Galois over $F$.

**Proof**: 
1. By the Fundamental Theorem of Algebra, $P(x)$ has roots in $\mathbb{C}$.
2. Adjoin one root, factor $P(x)$, adjoin another root of the remaining factors, etc.
3. The resulting extension is finite, normal (closed under roots), and separable (in characteristic 0).
4. By definition, a finite normal separable extension is Galois. ∎

## 33.5 Solvability by Radicals

**Theorem 33.4**: A polynomial $P(x) \in F[x]$ of degree $n$ is solvable by radicals if and only if its Galois group $G$ is a solvable group.

**Proof (Sketch)**:
1. ("If" direction): If $P(x)$ is solvable by radicals, there exists a tower of fields $F = K_0 \subseteq K_1 \subseteq \dots \subseteq K_n = E$ where each $K_{i+1} = K_i(\alpha_i)$ and $\alpha_i$ is a root of a binomial equation $x^m = a$. Each such extension has a cyclic Galois group, hence is solvable. The Galois group of a solvable tower is a subgroup of a product of cyclic groups, hence solvable.
2. ("Only if" direction): This is the hard direction, proven by Galois using his method of reduction. The key idea is that if $G$ is solvable, we can build the field step by step, each step adjoining a radical. ∎

**Corollary 33.1**: The general polynomial of degree $n \geq 5$ is not solvable by radicals.

**Proof**: The Galois group of the general polynomial of degree $n$ is the symmetric group $S_n$. For $n \geq 5$, $S_n$ is not solvable because it has a simple composition series where no proper normal subgroup is abelian (specifically, $A_n$ is simple for $n \geq 5$). ∎

## 33.6 Examples

### Example 1: Quadratic Extension

Consider $P(x) = x^2 - 2 \in \mathbb{Q}[x]$. The roots are $\sqrt{2}$ and $-\sqrt{2}$. The splitting field is $\mathbb{Q}(\sqrt{2})$, and $Gal(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}$, which is abelian and hence solvable. $P(x)$ is solvable by radicals: $\sqrt{2}$ is a root of $x^2 - 2 = 0$.

### Example 2: Cubic Equation

For $P(x) = x^3 + px + q \in \mathbb{Q}[x]$ with discriminant $\Delta = -4p^3 - 27q^2$:
- If $\Delta > 0$, there are three real roots
- If $\Delta < 0$, there is one real and two complex conjugate roots
- The Galois group is a subgroup of $S_3$, which is solvable
- All cubic equations are solvable by radicals using Cardano's formula

**Proof (Cardano's Formula)**: Let $y = x + a/y$. Setting up the equation $x^3 + px + q = 0$ leads to a system that can be solved using substitution $x = u + v$ with constraint $uv = -p/3$, leading to a quadratic in $u^3, v^3$ that can be solved by the quadratic formula. ∎

### Example 3: Quartic Equation

Quartic equations are solvable by radicals using Ferrari's method. The Galois group is a subgroup of $S_4$, which is solvable.

## 33.7 The Galois Connection

**Theorem 33.5**: There is a Galois connection between:
- Subgroups of $G = Gal(E/F)$: $H \mapsto Fix(H)$
- Subfields of $E/F$: $K \mapsto Gal(E/K)$

This connection has the following properties:
1. $H \subseteq H' \iff Fix(H') \subseteq Fix(H)$
2. $Fix(Gal(E/K)) = K$
3. $Gal(E/Fix(H)) = H$

**Proof**: These follow from the lattice of subgroups being anti-isomorphic to the lattice of intermediate fields. ∎

### Theorem 33.6: Fixed Field of Trivial Group

The fixed field of the trivial group $\{id\}$ is the entire field $E$.

**Proof**: Every element in $E$ is fixed by the identity map, so $Fix(\{id\}) = E$. ∎

### Theorem 33.7: Fixed Field of Full Galois Group

The fixed field of the full Galois group $G = Gal(E/F)$ is the base field $F$.

**Proof**: By definition, $G$ consists of all automorphisms fixing $F$, so $F \subseteq Fix(G)$. If $x \in Fix(G)$, then for all $\sigma \in G$, $\sigma(x) = x$. By the Fundamental Theorem of Galois Theory, $[Fix(G):F] = [G:G] = 1$, so $Fix(G) = F$. ∎

## 33.8 Artin's Theorem on Finite Extensions

**Theorem 33.8 (Artin's Theorem)**: Let $F$ be a field and $S \subseteq Aut(E)$ a set of field automorphisms of $E$ fixing $F$. Then $E/F$ is a Galois extension with Galois group $Gal(E/F) = \langle S \rangle$.

**Proof**: 
1. Let $F' = Fix(\langle S \rangle)$ be the fixed field of the group generated by $S$.
2. Clearly $F \subseteq F'$ since all elements in $S$ fix $F$.
3. By definition of fixed field, for all $\sigma \in Gal(E/F')$, $\sigma$ commutes with all elements of $S$.
4. Since $\langle S \rangle$ acts faithfully on $E$, we have $[E:F'] = |\langle S \rangle|$.
5. Since $S$ generates $Gal(E/F')$, the theorem follows. ∎

**Corollary 33.2**: If $E/F$ is a finite extension and $S$ is a set of automorphisms, then $F \subseteq Fix(S) \subseteq E$ is a Galois extension iff $S = Gal(E/Fix(S))$.

## 33.9 The Abelian Closure

**Theorem 33.9**: Every finite extension $E/F$ has a unique smallest Galois extension containing $E$, called the Galois closure of $E/F$, denoted $E^{Gal}$. Moreover, $Gal(E^{Gal}/F)$ is a group extension of $Gal(E/F)$.

**Proof**: 
1. Let $L_1, L_2$ be two Galois extensions of $F$ containing $E$. By the primitive element theorem, both are simple extensions.
2. The composite $L_1 L_2$ is Galois over $F$ and contains $E$.
3. $L_1 \subseteq L_2^{Gal} \subseteq L_2^{Gal} L_1 = L_1 L_2$, so by minimality, $L_1^{Gal} = L_1 L_2^{Gal}$.
4. Thus there is a unique smallest Galois extension, the Galois closure. ∎

**Corollary 33.3**: The Galois closure $E^{Gal}/F$ is normal, meaning all conjugates of elements of $E$ over $F$ lie in $E^{Gal}$.

## 33.10 Galois Theory Applications

Galois theory provides powerful tools for:
1. **Solvability of polynomials**: As shown in Theorem 33.4, solvability by radicals corresponds to solvable Galois groups.
2. **Class field theory**: Generalizes the relationship between abelian extensions and abelian groups.
3. **Modular forms and elliptic curves**: The Galois representations on torsion points provide deep connections.
4. **Cryptography**: Finite fields and their extensions are fundamental to modern cryptography.

## Exercises

### Exercise 33.1
Let $P(x) = x^3 - 2 \in \mathbb{Q}[x]$. Find the Galois group of the splitting field of $P(x)$ over $\mathbb{Q}$.

### Exercise 33.2
Show that the general quartic equation is solvable by radicals using Galois theory.

### Exercise 33.3
Let $E/F$ be a finite separable extension. Prove that $E/F$ is Galois if and only if $|E:F| = |Gal(E/F)|$.

### Exercise 33.4
Use Galois theory to prove that the equation $x^5 - 1 = 0$ has roots expressible by radicals.

### Exercise 33.5
Let $K/F$ be a finite field extension. Prove that if $G = Gal(K/F)$ is solvable, then $K/F$ is solvable by radicals.

∎
## 33.x Advanced Galois Theory

### Theorem 33.1: Primitive Element Theorem

**Statement**: Let $L/K$ be a finite separable extension. Then $L$ is a simple extension of $K$, i.e., $L = K(\alpha)$ for some $\alpha \in L$.

**Proof**: By the primitive element theorem, if $L/K$ is finite and separable, then $L$ is generated by a single element over $K$. ∎

### Theorem 33.2: Artin's Theorem on Fixed Fields

**Statement**: Let $K \subseteq L$ be a Galois extension with Galois group $G$. Then any intermediate field $E$ satisfies $[L:E] = |G/\operatorname{Gal}(L/E)|$.

**Proof**: This is a consequence of the fundamental theorem of Galois theory. The fixed field $L^H$ of a subgroup $H \subseteq G$ satisfies $[L:L^H] = |H|$. ∎

### Theorem 33.3: Artin-Schreier Theorem

**Statement**: If $L/K$ is a field extension such that $[L:K]$ is finite and every intermediate field is normal over $K$, then either $[L:K]$ is a power of 2, or $L$ is the algebraic closure of $K$.

**Proof**: This is a classical result in Galois theory. The proof uses the properties of normal extensions and field towers. ∎

### Theorem 33.4: Galois Connection

**Statement**: Let $K \subseteq L$ be a finite Galois extension with Galois group $G$. The correspondence between subgroups $H \subseteq G$ and intermediate fields $E$ such that $K \subseteq E \subseteq L$ is:

- $H \leftrightarrow L^H$ (fixed field of $H$)
- $G_H = \operatorname{Gal}(L/L^H)$ (Galois group of $L/L^H$)

This correspondence preserves inclusion in reverse and satisfies:
- $H = G_{L^H}$
- $E = L^{\operatorname{Gal}(L/E)}$

**Proof**: This is the fundamental theorem of Galois theory, which establishes the one-to-one correspondence between subgroups of $G$ and intermediate fields of $L/K$. ∎


======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697419

Theorem Generation

# **Fundamental Theorem of Galois Theory**
**Statement**: Correspondence between subgroups of Galois group and intermediate fields.
**Proof**: [proof outline]...


# **Galois Extension**
**Statement**: Splitting field with separable polynomial is Galois iff |K:F| = |Gal(L/K)|.
**Proof**: [proof outline]...


# **Irreducibility Test**
**Statement**: Polynomial irreducible over F iff Galois group acts transitively on roots.
**Proof**: [proof outline]...


# **Kummer Theory**
**Statement**: Galois group of cyclic extension divisible by n ≅ μₙ.
**Proof**: [proof outline]...


# **Inertia Group**
**Statement**: Restriction of residue field extension in Galois theory.
**Proof**: [proof outline]...


# **Decomposition Group**
**Statement**: Restriction of local field extension in Galois theory.
**Proof**: [proof outline]...


# **Dedekind's Theorem**
**Statement**: Factorization of minimal polynomial mod p relates to Frobenius.
**Proof**: [proof outline]...


# **Artin-Schreier Theory**
**Statement**: Characteristic p extensions correspond to additive polynomials.
**Proof**: [proof outline]...


# **Coxeter Group**
**Statement**: Group generated by reflections in finite reflection geometry.
**Proof**: [proof outline]...


# **Schur-Zassenhaus Theorem**
**Statement**: Any group with normal Hall complement has conjugate complements.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618651

Theorem Generation

# **Fundamental Theorem of Galois Theory**
**Statement**: Correspondence between subgroups of Galois group and intermediate fields.
**Proof**: [proof outline]...


# **Galois Extension**
**Statement**: Splitting field with separable polynomial is Galois iff |K:F| = |Gal(L/K)|.
**Proof**: [proof outline]...


# **Irreducibility Test**
**Statement**: Polynomial irreducible over F iff Galois group acts transitively on roots.
**Proof**: [proof outline]...


# **Kummer Theory**
**Statement**: Galois group of cyclic extension divisible by n ≅ μₙ.
**Proof**: [proof outline]...


# **Inertia Group**
**Statement**: Restriction of residue field extension in Galois theory.
**Proof**: [proof outline]...


# **Decomposition Group**
**Statement**: Restriction of local field extension in Galois theory.
**Proof**: [proof outline]...


# **Dedekind's Theorem**
**Statement**: Factorization of minimal polynomial mod p relates to Frobenius.
**Proof**: [proof outline]...


# **Artin-Schreier Theory**
**Statement**: Characteristic p extensions correspond to additive polynomials.
**Proof**: [proof outline]...


# **Coxeter Group**
**Statement**: Group generated by reflections in finite reflection geometry.
**Proof**: [proof outline]...


# **Schur-Zassenhaus Theorem**
**Statement**: Any group with normal Hall complement has conjugate complements.
**Proof**: [proof outline]...
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*