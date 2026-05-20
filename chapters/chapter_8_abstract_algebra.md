# Chapter 8: Abstract Algebra

## 8.1 Field Extensions

### Theorem 8.1: Algebraic Elements and Extensions

**Statement**: An element $\alpha$ in a field extension $L/K$ is algebraic over $K$ if there exists a non-zero polynomial $f(x) \in K[x]$ such that $f(\alpha) = 0$. The set of all algebraic elements over $K$ forms an algebraic closure of $K$.

**Proof**:

An element $\alpha \in L$ is algebraic over $K$ if there exists $f(x) = a_n x^n + \dots + a_1 x + a_0 \in K[x]$ with $a_n \neq 0$ such that $f(\alpha) = 0$.

The set of algebraic elements over $K$ in $L$ is denoted $\overline{K} = \{ \alpha \in L : \alpha \text{ is algebraic over } K \}$.

To show this is a field extension of $K$, we verify the field axioms for $\overline{K}$:

1. **Closure under addition**: If $\alpha, \beta \in \overline{K}$, then $\alpha + \beta \in \overline{K}$.

2. **Closure under multiplication**: If $\alpha, \beta \in \overline{K}$, then $\alpha \beta \in \overline{K}$.

3. **Additive inverses**: If $\alpha \in \overline{K}$, then $-\alpha \in \overline{K}$.

4. **Multiplicative inverses**: If $\alpha \in \overline{K} \setminus \{0\}$, then $\alpha^{-1} \in \overline{K}$.

These properties follow from the fact that sums and products of algebraic elements are algebraic (proven via resultant polynomials).

∎

### Theorem 8.2: Minimal Polynomial

**Statement**: Every algebraic element $\alpha$ over $K$ has a unique monic polynomial $m(x) \in K[x]$ of minimal degree such that $m(\alpha) = 0$, called the minimal polynomial of $\alpha$.

**Proof**:

Let $S = \{ f \in K[x] : f \neq 0, f(\alpha) = 0 \}$ be the set of polynomials vanishing at $\alpha$.

Since $\alpha$ is algebraic, $S$ is non-empty. By the well-ordering principle applied to $\deg(f)$ for $f \in S$, there exists a unique polynomial $m(x) \in S$ of minimal degree.

Let $\deg(m) = n$. Then $m(x) = x^n + a_{n-1} x^{n-1} + \dots + a_0$ (monic).

To show $m(x)$ is irreducible:

Suppose $m(x) = f(x)g(x)$ where $\deg(f) = r < n$ and $\deg(g) = s < n$.

Since $\deg(f) < n$, $f(\alpha) \neq 0$ (otherwise $f$ would be a polynomial of smaller degree vanishing at $\alpha$, contradicting minimality of $m$).

But $m(\alpha) = f(\alpha)g(\alpha) = 0$, so either $f(\alpha) = 0$ or $g(\alpha) = 0$, contradiction.

Thus $m(x)$ is irreducible over $K$.

∎

## 8.2 Galois Theory

### Theorem 8.3: Fundamental Theorem of Galois Theory

**Statement**: Let $L/K$ be a finite Galois extension. Then there is a one-to-one correspondence between the intermediate fields $K \subseteq M \subseteq L$ and the subgroups of $G = \text{Gal}(L/K)$.

Specifically, for any subgroup $H \leq G$, define $L^H = \{ \alpha \in L : \sigma(\alpha) = \alpha \text{ for all } \sigma \in H \}$.

For any intermediate field $M$, define $H = \text{Gal}(L/M) = \{ \sigma \in G : \sigma|_M = \text{id} \}$.

These correspondences are mutually inverse:
- $L^{\text{Gal}(L/M)} = M$
- $\text{Gal}(L/L^H) = H$

**Proof**:

The correspondence is constructed by:
1. **Fixed field of subgroup**: For $H \leq G$, $L^H$ is the set of elements in $L$ fixed by all $\sigma \in H$.
   - $L^H$ is a subfield of $L$ (closed under addition, multiplication, etc.).
   - $[L:L^H] = |H|$ (by the Tower Law and orbit-stabilizer theorem).

2. **Galois group of intermediate field**: For $K \subseteq M \subseteq L$, $G(M/L) = \{ \sigma \in \text{Gal}(L/K) : \sigma|_M = \text{id} \}$.
   - This is a subgroup of $\text{Gal}(L/K)$.
   - $[L^{\text{Gal}(L/M)} : M] = |\text{Gal}(L/M)|$.

The fundamental theorem states that these correspondences are bijections.

**Separability and Normality**: A finite extension $L/K$ is Galois if and only if it is separable and normal.

- **Separable**: Every element $\alpha \in L$ is a root of a separable polynomial in $K[x]$.
- **Normal**: $L$ is the splitting field of a separable polynomial in $K[x]$.

For Galois extensions:
- The degree $[L:K] = |\text{Gal}(L/K)|$.
- The Fundamental Theorem applies.

∎

### Theorem 8.4: Galois Group of Splitting Field

**Statement**: The Galois group $\text{Gal}(L/K)$ of a splitting field $L$ of a separable polynomial $f \in K[x]$ is a finite group of order $[L:K]$.

**Proof**:

Let $f \in K[x]$ be a separable polynomial of degree $n$.

Let $L$ be the splitting field of $f$ over $K$.

Since $f$ is separable, all roots of $f$ in $L$ are distinct.

Let $\alpha_1, \dots, \alpha_n$ be the roots of $f$ in $L$.

Any $\sigma \in \text{Gal}(L/K)$ is determined by its action on the roots: $\sigma$ maps $\alpha_i$ to some $\alpha_j$ (since $\sigma$ permutes the roots of $f$).

There are $n!$ possible permutations of the $n$ roots.

By the Primitive Element Theorem, $L = K(\alpha_1, \dots, \alpha_n)$ has degree $n!$ over $K$.

Thus $|\text{Gal}(L/K)| = [L:K] = n!$.

∎

## 8.3 Field Isomorphisms

### Theorem 8.5: Isomorphism of Fields

**Statement**: Two fields $F$ and $E$ are isomorphic if and only if there exists a bijective map $\phi: F \to E$ such that $\phi(a + b) = \phi(a) + \phi(b)$, $\phi(ab) = \phi(a)\phi(b)$, and $\phi(1) = 1$.

Isomorphic fields have the same cardinality and the same algebraic properties.

**Proof**:

(⇒) If $\phi$ is a field isomorphism, then:
- $\phi(a + b) = \phi(a) + \phi(b)$ by additivity
- $\phi(ab) = \phi(a)\phi(b)$ by multiplicativity
- $\phi(1) = 1$ by preservation of multiplicative identity
- $\phi$ is bijective by definition

(⇐) Conversely, if $\phi$ satisfies these properties:
- $\phi$ preserves the field structure
- $\phi$ is bijective
- $\phi$ preserves order if the fields are ordered (since $a < b \iff \phi(a) < \phi(b)$)

Thus $\phi$ is a field isomorphism.

∎

### Theorem 8.6: Automorphisms

**Statement**: An automorphism of a field $F$ is a field isomorphism $F \to F$.

The group of automorphisms of $F$, denoted $\text{Aut}(F)$, is a group under composition.

**Proof**:

Let $\phi: F \to F$ be a field isomorphism.

- **Closure**: If $\phi_1, \phi_2 \in \text{Aut}(F)$, then $\phi_1 \circ \phi_2$ is also a field isomorphism.
- **Associativity**: Function composition is associative.
- **Identity**: The identity map $\text{id}(x) = x$ is an automorphism.
- **Inverse**: If $\phi$ is bijective, then $\phi^{-1}$ is also a field isomorphism.

Thus $\text{Aut}(F)$ is a group under composition.

∎

## 8.4 Polynomial Rings

### Theorem 8.7: Factorization in Polynomial Rings

**Statement**: In a polynomial ring $F[x]$ where $F$ is a field, a polynomial $f(x) \in F[x]$ of degree $n$ can be factored as:

$$f(x) = a(x - r_1)(x - r_2)\dots(x - r_n)$$

where $r_1, \dots, r_n$ are the roots of $f$ in an algebraic closure of $F$.

**Proof**:

By the Fundamental Theorem of Algebra, every polynomial of degree $n$ with coefficients in $F$ has $n$ roots (counting multiplicity) in an algebraic closure $\overline{F}$.

Let $r_1, \dots, r_n$ be these roots.

By the Factor Theorem, $(x - r_i)$ divides $f(x)$ for each $i$.

Since $F[x]$ is a unique factorization domain (UFD), the factorization is unique up to multiplication by a unit (non-zero constant).

Thus:

$$f(x) = a(x - r_1)(x - r_2)\dots(x - r_n)$$

where $a$ is the leading coefficient of $f$.

∎

### Corollary 8.1: Irreducibility Test

**Statement**: A polynomial $f(x) \in F[x]$ is irreducible if and only if it cannot be written as $f(x) = g(x)h(x)$ where neither $g(x)$ nor $h(x)$ is a unit in $F[x]$.

**Proof**:

(⇒) If $f(x) = g(x)h(x)$ and $f$ is irreducible, then one of $g$ or $h$ must be a unit (otherwise $f$ would be reducible).

(⇐) Conversely, if $f(x)$ cannot be written as a product of two non-units, then $f$ is irreducible.

∎

## 8.5 Rings and Ideals

### Theorem 8.8: Ideal Structure of Polynomial Rings

**Statement**: Let $F[x]$ be a polynomial ring over a field $F$. Every ideal $I \subseteq F[x]$ is principal, meaning $I = \langle p(x) \rangle$ for some $p(x) \in F[x]$.

**Proof**:

Let $I \subseteq F[x]$ be an ideal.

If $I = \{0\}$, then $I = \langle 0 \rangle$, and we're done.

Otherwise, $I$ contains a non-zero polynomial. Let $S = \{ \deg(f) : f \in I, f \neq 0 \}$.

By the well-ordering principle, there exists a minimum degree $n \in S$.

Let $p(x)$ be a polynomial in $I$ of degree $n$. We claim $I = \langle p(x) \rangle$.

To show $p(x) \in I$, take any $g(x) \in I$. By the division algorithm for polynomials, we can write:

$$g(x) = q(x)p(x) + r(x)$$

where $\deg(r) < \deg(p)$.

Since $I$ is an ideal, $q(x)p(x) \in I$, so $r(x) = g(x) - q(x)p(x) \in I$.

If $r(x) \neq 0$, then $\deg(r) < \deg(p)$ and $r \in I$, contradicting the minimality of $\deg(p)$.

Thus $r(x) = 0$, so $g(x) = q(x)p(x) \in \langle p(x) \rangle$.

Therefore $I = \langle p(x) \rangle$.

∎

### Theorem 8.9: Maximal Ideals in Polynomial Rings

**Statement**: In $F[x]$ where $F$ is a field, an ideal $I$ is maximal if and only if $F[x]/I$ is a field.

**Proof**:

(⇒) If $I$ is maximal, then $I$ is proper ($I \neq F[x]$), and any ideal $J$ with $I \subsetneq J \subseteq F[x]$ implies $J = F[x]$.

Thus $F[x]/I$ is a field (since the only ideals containing 0 are 0 and itself).

(⇐) If $F[x]/I$ is a field, then $I$ is maximal in $F[x]$.

By the correspondence theorem, ideals containing $I$ correspond to ideals in $F[x]/I$.

Since $F[x]/I$ is a field, its only ideals are $\{0\}$ and $F[x]/I$.

Thus the only ideals containing $I$ in $F[x]$ are $I$ and $F[x]$.

Therefore $I$ is maximal.

∎

## 8.6 Exercises

1. **Exercise 8.1**: Show that $\mathbb{Q}(\sqrt{2})$ is a field extension of degree 2 over $\mathbb{Q}$.

2. **Exercise 8.2**: Prove that every ideal in $\mathbb{Z}[x]$ is not necessarily principal.

3. **Exercise 8.3**: Find the Galois group of $x^4 - 2$ over $\mathbb{Q}$.

4. **Exercise 8.4**: Show that $\mathbb{F}_{p^n}$ is a finite field of order $p^n$.

5. **Exercise 8.5**: Prove that $F[x]/\langle x^2 + 1 \rangle \cong \mathbb{F}_p[i]$ where $i^2 = -1$.

6. **Exercise 8.6**: Show that the ring $\mathbb{Z}[i]$ is a Euclidean domain.
