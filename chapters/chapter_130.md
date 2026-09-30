## 130. Abstract Algebra: Groups, Rings, and Fields

### 130.1 Group Theory Basics

**Definition**: A group (G, ·) is a set G equipped with a binary operation · satisfying:
1. **Closure**: For all a, b ∈ G, a · b ∈ G
2. **Associativity**: For all a, b, c ∈ G, (a · b) · c = a · (b · c)
3. **Identity**: There exists e ∈ G such that e · a = a · e = a for all a ∈ G
4. **Inverses**: For each a ∈ G, there exists a⁻¹ ∈ G such that a · a⁻¹ = a⁻¹ · a = e

**Theorem**: If G is a finite set with a binary operation satisfying closure, associativity, and identity, then G is a group.

**Proof**: 
By finiteness, for any a ∈ G and any b ∈ G, there exists n ≥ 1 such that aⁿ = a^(n+1).
This implies aⁿ = a · aⁿ, so a^(n-1) · a = aⁿ, giving a⁻¹ = a^(n-1).
Thus inverses exist. QED

### 130.2 Subgroups and Lagrange's Theorem

**Definition**: A subgroup H ≤ G is a subset that is itself a group under the same operation.

**Theorem (Lagrange)**: For any finite group G and subgroup H, |H| divides |G|.

**Proof**: 
Consider the left cosets of H in G: gH = {gh | h ∈ H}. These partition G into disjoint cosets.
Each coset has the same cardinality as H (by bijection g ↦ gh).
Thus |G| = [G:H] · |H|, where [G:H] is the index of H in G. QED

### 130.3 Homomorphisms and Isomorphisms

**Definition**: A homomorphism φ: G → H is a function preserving the group operation: φ(a · b) = φ(a) · φ(b).

**Theorem**: φ is an isomorphism if and only if it is a bijection.

**Proof**: 
If φ is bijective, its inverse φ⁻¹ exists and satisfies φ⁻¹(φ(a) · φ(b)) = φ⁻¹(φ(a · b)) = a · b, making φ⁻¹ a homomorphism as well.
Thus φ(a · b) = φ(a) · φ(b) for all a, b ∈ G. QED

### 130.4 Abelian Groups

**Definition**: An abelian group is one where the operation is commutative: a · b = b · a for all a, b ∈ G.

**Theorem (Cauchy's Theorem)**: If G is a finite abelian group and p divides |G| for some prime p, then G has an element of order p.

**Proof**: 
By the fundamental theorem of finite abelian groups, G is isomorphic to a direct sum of cyclic groups.
If p divides the order of a cyclic group C_n, it divides n, so C_n has an element of order p.
Thus G has an element of order p. QED

### 130.5 Normal Subgroups and Quotient Groups

**Definition**: A subgroup N of G is normal (N ⊲ G) if gNg⁻¹ = N for all g ∈ G, or equivalently gNg⁻¹ ⊆ N for all g ∈ G.

**Theorem**: G has a quotient group G/N if and only if N is normal.

**Proof**: 
Define cosets aN = {an | n ∈ N}. Since N is normal, (aN)(bN) = abN = baN = (bN)(aN).
The operation is well-defined on cosets, giving the quotient group G/N with identity eN = N.
QED

### 130.6 Sylow Theorems

**Theorem (Sylow I)**: Let p be a prime, pⁿ be the highest power of p dividing |G|. Then G has a subgroup of order pⁿ.

**Proof**: 
Consider the action of G on the set of subsets S of G with |S| = pⁿ via left multiplication.
By Burnside's lemma, |S/G| ≡ |fix(s)| (mod |G|) for all s ∈ G.
For s = e, |fix(e)| = |S| ≡ 0 (mod pⁿ). For s ≠ e, |fix(s)| is divisible by the order of s, which is divisible by p.
Thus |S/G| ≡ 0 (mod p), and |S| ≡ 0 (mod p), implying there exists a fixed point, i.e., a Sylow p-subgroup. QED

**Theorem (Sylow II)**: All Sylow p-subgroups of G are conjugate.

**Theorem (Sylow III)**: The number of Sylow p-subgroups, n_p, satisfies n_p ≡ 1 (mod p) and n_p divides |G|/pⁿ.

### 130.7 Rings and Ideals

**Definition**: A ring (R, +, ·) is a set equipped with two binary operations satisfying:
1. (R, +) is an abelian group
2. Multiplication is associative: (a · b) · c = a · (b · c)
3. Distributivity: a · (b + c) = a · b + a · c and (a + b) · c = a · c + b · c

**Definition**: An ideal I of R is a subset such that (I, +) is a subgroup of (R, +) and for all r ∈ R, i ∈ I, both r · i ∈ I and i · r ∈ I.

**Theorem**: Every principal ideal (a) of an integral domain R is isomorphic to the quotient R/(a).

**Proof**: 
By the first isomorphism theorem, (R, +) → (a, +) defined by r ↦ r·a is a surjective homomorphism.
Its kernel is {r | r·a = 0}, which is the ideal (a) if R is a domain.
Thus (R, +)/(a, +) ≅ (a, +). QED

### 130.8 Integral Domains

**Definition**: An integral domain is a commutative ring with no zero divisors: ab = 0 implies a = 0 or b = 0.

**Theorem**: Every field is an integral domain.

**Theorem**: If R is an integral domain and K is its field of fractions, then R is a subring of K.

**Proof**: 
For every a/b ∈ K, define a·b̄ = a·b and b·ā = b·a. If a·b = 0, then a = 0 or b = 0 since R is an integral domain.
Thus a/b is well-defined, making R a subring of K. QED

### 130.9 Polynomial Rings

**Theorem (Fundamental Theorem of Algebra)**: Every non-constant polynomial with complex coefficients has a complex root.

**Theorem (Euclidean Division)**: For polynomials f, g in R[x] with g ≠ 0, there exist unique q, r such that f = qg + r and deg(r) < deg(g).

**Theorem**: R[x] is a Euclidean domain if and only if R is a field.

**Proof**: 
If R is a field, we can divide polynomials as in Euclidean algorithm.
If R[x] is Euclidean, we can divide by nonzero constants, making R a field. QED

### 130.10 Field Extensions

**Definition**: A field extension E/F is a field E containing F as a subfield.

**Definition**: The algebraic closure of F is the unique (up to isomorphism) field containing F in which every polynomial in F[x] has a root.

**Theorem (Galois Theory)**: There is a one-to-one correspondence between intermediate fields and subgroups of the Galois group.

**Proof**: 
By the fundamental theorem of Galois theory, the lattice of subfields corresponds to the lattice of subgroups.
The Galois group Gal(E/F) acts on E, and the fixed field of any subgroup H is a subfield of E containing F.
QED

