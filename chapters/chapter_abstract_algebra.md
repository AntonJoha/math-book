<<<<<<< HEAD
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

*Updated on 2026-06-10*
=======
# Abstract Algebra

## 3.1 Groups

### 3.1.1 Definition and Basic Properties

**Definition:** A group is a set $G$ equipped with a binary operation $\cdot$ satisfying:
1. **Closure:** For all $a, b \in G$, $a \cdot b \in G$.
2. **Associativity:** For all $a, b, c \in G$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3. **Identity:** There exists $e \in G$ such that for all $a \in G$, $a \cdot e = e \cdot a = a$.
4. **Inverses:** For each $a \in G$, there exists $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$.

**Theorem 3.1:** In any group $G$, the identity element is unique.

*Proof:* Suppose $e_1$ and $e_2$ are both identity elements. Then $e_1 = e_1 \cdot e_2 = e_2$. Thus the identity is unique. ∎

**Theorem 3.2:** In any group $G$, the inverse of an element is unique.

*Proof:* Suppose $a^{-1}$ and $b^{-1}$ are both inverses of $a$. Then $a^{-1} = a^{-1} \cdot e = a^{-1} \cdot (a \cdot b^{-1}) = (a^{-1} \cdot a) \cdot b^{-1} = e \cdot b^{-1} = b^{-1}$. Thus the inverse is unique. ∎

### 3.1.2 Finite and Infinite Groups

A group is **finite** if it has a finite number of elements; otherwise it is **infinite**.

**Theorem 3.3 (Cancellation Laws):** In any group $G$, for all $a, b, c \in G$:
1. $ab = ac \implies b = c$ (left cancellation)
2. $ba = ca \implies b = c$ (right cancellation)

*Proof:* 
- For left cancellation: $ab = ac$. Multiply by $a^{-1}$ on the left: $a^{-1}(ab) = a^{-1}(ac)$. By associativity, $(a^{-1}a)b = (a^{-1}a)c$. By the identity property, $eb = ec$. By the identity property, $b = c$.
- For right cancellation: Similar proof by multiplying by $a^{-1}$ on the right. ∎

### 3.1.3 Cyclic Groups

**Definition:** A group $G$ is **cyclic** if there exists $g \in G$ such that every element of $G$ can be written as $g^k$ for some integer $k$. The generator $g$ is called a **generator** of $G$.

**Theorem 3.4:** A finite group $G$ of order $n$ is cyclic if and only if $G$ has a primitive element $g$ such that $g^n = e$ and $g^k \neq e$ for all $1 \leq k < n$.

*Proof:* 
- **Forward direction:** If $G = \langle g \rangle$ and $|G| = n$, then the powers $g, g^2, \dots, g^n$ are all equal to $e$ and no smaller power is equal to $e$. (Cauchy's Theorem on cyclic groups.)
- **Reverse direction:** If $g$ is a primitive element of $G$, then $G = \langle g \rangle$, so $G$ is cyclic. ∎

## 3.2 Subgroups and Lagrange's Theorem

### 3.2.1 Subgroups

**Definition:** A subset $H \subseteq G$ is a **subgroup** if $(H, \cdot)$ is a group under the same operation as $G$.

**Subgroup Test:** A non-empty subset $H \subseteq G$ is a subgroup if and only if for all $a, b \in H$, $ab^{-1} \in H$.

### 3.2.2 Lagrange's Theorem

**Theorem 3.5 (Lagrange's Theorem):** If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$.

*Proof:* Consider the left cosets $gH = \{gh : h \in H\}$ for $g \in G$. These cosets partition $G$ and each coset has the same cardinality as $H$. If $[G:H] = k$ (the number of cosets), then $|G| = k|H|$. Thus $|H|$ divides $|G|$. ∎

### 3.2.3 Examples

**Example 3.6:** The cyclic group $C_n = \mathbb{Z}/n\mathbb{Z}$ under addition modulo $n$.
- Order: $n$
- Subgroups: For each divisor $d$ of $n$, there is exactly one subgroup of order $d$.

## 3.3 Homomorphisms and Quotient Groups

### 3.3.1 Homomorphisms

**Definition:** A function $\phi: G \to H$ between groups is a **homomorphism** if for all $a, b \in G$, $\phi(ab) = \phi(a)\phi(b)$.

**Theorem 3.7:** If $\phi: G \to H$ is a homomorphism, then $\phi(e_G) = e_H$ and $\phi(a^{-1}) = (\phi(a))^{-1}$ for all $a \in G$.

*Proof:* 
- $\phi(e_G) = \phi(e_G \cdot e_G) = \phi(e_G)\phi(e_G)$. Multiply by $\phi(e_G)^{-1}$ to get $\phi(e_G) = e_H$.
- $\phi(a^{-1}) = \phi(a^{-1} \cdot a) = \phi(a^{-1})\phi(a) = e_H$, so $\phi(a^{-1}) = (\phi(a))^{-1}$. ∎

### 3.3.2 Kernel and Image

**Definition:** For a homomorphism $\phi: G \to H$:
- The **kernel** is $\ker(\phi) = \{a \in G : \phi(a) = e_H\}$
- The **image** is $\text{im}(\phi) = \{\phi(a) : a \in G\} \subseteq H$

**Theorem 3.8 (Fundamental Homomorphism Theorem):** For any homomorphism $\phi: G \to H$, $\phi(G)$ is a subgroup of $H$, and $G/\ker(\phi)$ is isomorphic to $\phi(G)$.

*Proof sketch:* Define $\psi: G/\ker(\phi) \to \phi(G)$ by $\psi(a\ker(\phi)) = \phi(a)$. This is well-defined and bijective. For any $a, b \in G$, $\psi((a\ker(\phi))(b\ker(\phi))) = \psi((ab)\ker(\phi)) = \phi(ab) = \phi(a)\phi(b) = \psi(a\ker(\phi))\psi(b\ker(\phi))$. Thus $\psi$ is a homomorphism. Since $\psi$ is bijective, $G/\ker(\phi) \cong \phi(G)$. ∎

## 3.4 Group Actions

**Definition:** A group $G$ acts on a set $X$ if there is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, satisfying:
1. $e \cdot x = x$ for all $x \in X$
2. $(gh) \cdot x = g \cdot (h \cdot x)$ for all $g, h \in G, x \in X$

**Orbit-Stabilizer Theorem:** Let $G$ act on $X$, $x \in X$, $G_x = \{g \in G : g \cdot x = x\}$ be the stabilizer of $x$. Then $|G| = |G_x| \cdot |G \cdot x|$, where $G \cdot x$ is the orbit of $x$.

## Exercises

1. Prove that if $G$ is a finite group and $|G| = p^k$ where $p$ is prime and $k \geq 1$, then $G$ has a subgroup of order $p$.
2. Show that if $G$ is a finite group and $|G|$ is even, then $G$ has an element of order 2.
3. Prove that if $G$ is a cyclic group of order $n$, then $G$ has a unique subgroup of order $d$ for each divisor $d$ of $n$.
4. Show that the direct product of two finite groups is finite and its order is the product of their orders.
5. Prove Cauchy's Theorem: If $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ has an element of order $p$.


### Lagrange's Theorem

**Theorem:** If $G$ is a finite group of order $n$ and $H$ is a subgroup of $G$, then $|H|$ divides $|G|$.

**Proof:** The index of $H$ in $G$ is $[G:H] = |G|/|H|$. Since the number of distinct left cosets of $H$ in $G$ is finite and each coset has the same cardinality as $H$, the number of cosets must be an integer. Thus $[G:H] \cdot |H| = |G|$, proving that $|H|$ divides $|G|$.

---
*Abstract algebra provides the language for modern mathematics.*
>>>>>>> b99e2a35ba3ed90f15a535bf294bd9753445bc2d
