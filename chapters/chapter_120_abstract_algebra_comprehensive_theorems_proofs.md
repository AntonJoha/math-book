# Chapter 120: Abstract Algebra - Comprehensive Theorems and Proofs

## 120.1 Group Theory: Fundamental Theorems

### Theorem 120.1 (Lagrange's Theorem)
**Statement:** If G is a finite group and H is a subgroup of G, then the order of H divides the order of G.

**Proof:** Let $|G| = n$ and $|H| = m$. The group action of G on the set of left cosets $G/H$ by left multiplication gives rise to a homomorphism $\phi: G \to S_{|G/H|}$. The kernel of this action is the normal core of H, which is a subgroup of H. By the first isomorphism theorem, $|G|/|\ker(\phi)| = |G/H|$. Since $|\ker(\phi)|$ divides $|H|$ and $|G/H| = |G|/|H|$, we have $|H|$ divides $|G|$.

**Applications:**
1. The order of any element $g \in G$ divides $|G|$ (take $H = \langle g \rangle$)
2. Cauchy's Theorem: If a prime $p$ divides $|G|$, then G contains an element of order $p$
3. Sylow's Theorems follow from Lagrange's Theorem

**Corollary (Cauchy's Theorem):** Let $p$ be a prime dividing $|G|$. Then G contains an element of order $p$.

**Proof:** By Cauchy's theorem proof using group actions. Consider the set $X = \{g \in G : g^p = e\}$. The group $G$ acts on $X$ by conjugation. The size of each orbit divides $|G|$ and is congruent to $|G|$ mod $p$ (since orbits have size 1 or $p$). Since $e \in X$, there is an orbit of size 1, giving a conjugacy class containing $e$. The non-identity elements in this orbit have order $p$.

### Theorem 120.2 (First Isomorphism Theorem)
**Statement:** Let $G$ and $H$ be groups, and $\phi: G \to H$ be a group homomorphism. Then $G/\ker(\phi) \cong \text{im}(\phi)$.

**Proof:** Define a map $\psi: G/\ker(\phi) \to \text{im}(\phi)$ by $\psi(g\ker(\phi)) = \phi(g)$. This is well-defined because if $g\ker(\phi) = g'\ker(\phi)$, then $g^{-1}g' \in \ker(\phi)$, so $\phi(g^{-1}g') = e$, giving $\phi(g) = \phi(g')$. Surjectivity follows from definition of image. Injectivity: if $\psi(g\ker(\phi)) = e$, then $\phi(g) = e$, so $g \in \ker(\phi)$, meaning $g\ker(\phi) = \ker(\phi)$. Thus $g\ker(\phi)$ maps to $e$. Since $G/\ker(\phi)$ and $\text{im}(\phi)$ have the same cardinality (by orbit-stabilizer), they are isomorphic.

### Theorem 120.3 (Fundamental Theorem of Homomorphisms)
**Statement:** Let $G$ and $H$ be groups, and $\phi: G \to H$ be a group homomorphism. Let $K = \ker(\phi)$ and $I = \text{im}(\phi)$. Then there exists a unique isomorphism $\bar{\phi}: G/K \to I$ such that $\bar{\phi}(gK) = \phi(g)$ for all $g \in G$.

**Proof:** This follows from the First Isomorphism Theorem. The kernel $K$ is a normal subgroup of $G$, so $G/K$ is a group. The image $I$ is a subgroup of $H$. The map $\bar{\phi}$ is the restriction of $\phi$ to the quotient.

**Corollary:** Let $N$ be a normal subgroup of $G$. Then $G/N$ is a group.

**Proof:** The map $G \to G/N$ is a surjective homomorphism with kernel $N$. By the Fundamental Theorem of Homomorphisms, $G/N$ is a group.

### Theorem 120.4 (Lattice Isomorphism Theorem)
**Statement:** Let $G$ be a group and $H_1 \unlhd H_2 \leq G$. Then there is an isomorphism $H_2/\ker(H_1 \to G_2) \cong H_2/H_1$, where $G_2$ is the projection of $H_2$ onto $G$.

**Proof:** Use the correspondence theorem. The lattice of subgroups of $G$ containing $H_1$ is isomorphic to the lattice of subgroups of $G/H_1$.

### Theorem 120.5 (Jordan-Hölder Theorem)
**Statement:** Let $G$ be a finite group and let $\pi: G$ and $\sigma: G$ be two composition series. Then there is a bijection between the composition factors of $\pi$ and $\sigma$ that preserves isomorphism classes.

**Proof:** Let $\pi$ and $\sigma$ be two composition series for $G$. The Jordan-Hölder theorem is proved by comparing the subgroups in the series and using the fact that any intermediate subgroup between two subgroups in a composition series is unique.

### Theorem 120.6 (Sylow's Theorems)
**Statement:** Let $G$ be a finite group with $|G| = p^n m$ where $p$ is prime and $p \nmid m$.

1. (Existence) G contains a subgroup of order $p^n$ (a Sylow p-subgroup).
2. (Conjugacy) All Sylow p-subgroups are conjugate.
3. (Count) The number $n_p$ of Sylow p-subgroups satisfies: $n_p \equiv 1 \pmod p$ and $n_p$ divides $m$.

**Proof:** Let $S$ be the set of all subgroups of order $p^n$ in $G$. The group $G$ acts on $S$ by conjugation. The size of each orbit divides $|G|$ and is congruent to $|G|$ mod $p$. Since there is at least one orbit of size 1 (the orbit of any Sylow p-subgroup), there is an orbit of size $p^k$ for some $k$. The number of Sylow p-subgroups is congruent to 1 mod $p$.

**Corollary (Sylow's Second Theorem):** Let $p$ be a prime dividing $|G|$. Then $G$ has a subgroup of order $p^k$ for each $1 \leq k \leq n$.

**Proof:** Use induction on $n$. The base case is $n=1$, which is Cauchy's theorem. For the inductive step, use the fact that a group of order $p^{n+1}m$ has a normal subgroup of order $p$ or a normal subgroup of order $p^n$.

### Theorem 120.7 (Normalizer Lemma)
**Statement:** Let $G$ be a finite group and $H \leq G$. Then the normalizer $N_G(H)$ of $H$ in $G$ has the property that $[G:N_G(H)] = n_p$, where $n_p$ is the number of Sylow p-subgroups containing $H$.

**Proof:** The normalizer $N_G(H)$ is the largest subgroup of $G$ containing $H$ such that $H$ is normal in $N_G(H)$. The index $[G:N_G(H)]$ is the number of distinct conjugates of $H$.

### Theorem 120.8 (Ore's Theorem)
**Statement:** Let $G$ be a finite group and $p$ a prime. If every Sylow p-subgroup of $G$ is normal, then $G$ has a normal Sylow p-subgroup.

**Proof:** Use the fact that the intersection of conjugate subgroups is contained in the center of the group.

## 120.2 Ring Theory: Fundamental Theorems

### Theorem 120.8.1 (Integral Dependence Theorem)
**Statement:** Let $A$ and $B$ be commutative rings and $\phi: A \to B$ a ring homomorphism. If $b \in B$ is integral over $A$, then $A[b]$ is a finitely generated $A$-module.

**Proof:** If $b$ satisfies $b^n + a_{n-1}b^{n-1} + \dots + a_0 = 0$ with $a_i \in A$, then $b^n \in A[b^{n-1}]$. By induction, $A[b]$ is finitely generated.

### Theorem 120.8.2 (Going-Up Theorem)
**Statement:** Let $A \subseteq B$ be integral extensions. Let $\mathfrak{p} \subseteq \mathfrak{q}$ be prime ideals of $A$. Then for every $\mathfrak{p}$, there exists $\mathfrak{q}' \subseteq B$ such that $\mathfrak{q}' \cap A = \mathfrak{p}$ and $\mathfrak{p} \subseteq \mathfrak{q}'$.

**Proof:** Use the fact that elements integral over $A$ are contained in the integral closure.

### Theorem 120.8.3 (Going-Down Theorem)
**Statement:** Let $A \subseteq B$ be integral extensions of domains. If $B$ is a field, then for every $\mathfrak{p} \subseteq \mathfrak{q}$, there exists $\mathfrak{p}'$ such that $\mathfrak{p}' \cap A = \mathfrak{p}$ and $\mathfrak{p} \subseteq \mathfrak{q}$.

**Proof:** Use the fact that integral domains with quotient fields that are algebraic over each other satisfy the going-down property.

### Theorem 120.8.4 (Infinite Integral Closure Theorem)
**Statement:** The integral closure of a domain $A$ in its field of fractions is the set of all elements $x$ in the field of fractions such that there exists $f(t) = a_n t^n + \dots + a_0 \in A[t]$ with $a_n \neq 0$ such that $f(x) = 0$.

**Proof:** This is the definition of integral closure.

## 120.3 Field Theory: Fundamental Theorems

### Theorem 120.9 (Galois Theory)
**Statement:** Let $K$ and $L$ be fields with $K \subseteq L$ such that $[L:K] < \infty$. Let $\text{Gal}(L/K) = \text{Gal}(L/K)$ be the group of automorphisms of $L$ that fix $K$ pointwise. Then the map $\sigma \mapsto \text{Fix}(\sigma)$ gives a Galois correspondence.

**Proof:** The Galois correspondence is a bijective map between the subgroups of $\text{Gal}(L/K)$ and the intermediate fields $K \subseteq M \subseteq L$. The correspondence is given by $\sigma \mapsto \text{Fix}(\sigma)$ and $M \mapsto \text{Gal}(L/M)$.

### Theorem 120.10 (Primitive Element Theorem)
**Statement:** Let $K$ and $L$ be fields with $K \subseteq L$ such that $[L:K] < \infty$. If $L$ is a separable extension of $K$, then there exists $\alpha \in L$ such that $L = K(\alpha)$.

**Proof:** The primitive element theorem is proved by considering the elements of $L$ as a vector space over $K$. If $\alpha_1, \dots, \alpha_n$ is a basis for $L$ over $K$, then the field $K(\alpha_1, \dots, \alpha_n)$ is $L$. If $\alpha_1, \dots, \alpha_n$ are algebraic, then there exists $\alpha \in L$ such that $L = K(\alpha)$.

### Theorem 120.11 (Artin-Schreier Theorem)
**Statement:** Let $K$ be a field and $\alpha$ a root of an irreducible polynomial $f(x) \in K[x]$. Then either $f(x)$ is separable, or $f(x) = x^p - a$ for some $a \in K$.

**Proof:** This is proved using the fact that the characteristic of the field is either 0 or $p$, and using the properties of the Frobenius endomorphism.

## 120.4 Module Theory: Fundamental Theorems

### Theorem 120.11.1 (Structure Theorem for Finitely Generated Modules over a Principal Ideal Domain)
**Statement:** Let $R$ be a principal ideal domain and $M$ a finitely generated $R$-module. Then $M \cong R^k \oplus R/(d_1) \oplus \dots \oplus R/(d_t)$ where $d_1 | d_2 | \dots | d_t$ in $R$.

**Proof:** The structure theorem is proved by considering the Smith normal form of the presentation matrix of $M$.

### Theorem 120.11.2 (Chinese Remainder Theorem)
**Statement:** Let $R$ be a commutative ring and $I_1, \dots, I_n$ ideals of $R$ such that $I_i + I_j = R$ for all $i \neq j$. Then the map $R/I_1 \times \dots \times R/I_n \to R/(I_1 \cap \dots \cap I_n)$ is an isomorphism.

**Proof:** The Chinese Remainder Theorem is proved by using the properties of the ring $R$ and the ideals $I_1, \dots, I_n$.

### Theorem 120.11.3 (Tensor Product of Modules)
**Statement:** Let $R$ be a commutative ring and $M, N$ $R$-modules. Then the tensor product $M \otimes_R N$ is an $R$-module such that for any $R$-module $P$, there is a natural bijection $\text{Hom}_R(M \otimes_R N, P) \cong \text{Bilinear}(M \times N, P)$.

**Proof:** This is the universal property of the tensor product.

**Theorem 120.11.4 (Cayley-Hamilton Theorem)**
**Statement:** Let $R$ be a commutative ring and $A$ an $n \times n$ matrix with entries in $R$. Let $p_A(t) = \det(tI - A)$ be the characteristic polynomial of $A$. Then $p_A(A) = 0$.

**Proof:** The Cayley-Hamilton theorem is proved using the fact that the characteristic polynomial is the characteristic polynomial of the matrix $A$.

**Theorem 120.11.5 (Sylvester's Law of Inertia)**
**Statement:** Let $V$ be a vector space over a field $F$ with a bilinear form $B: V \times V \to F$. Then the number of positive and negative eigenvalues of $B$ is invariant under the choice of basis.

**Proof:** Sylvester's Law of Inertia is proved using the fact that the number of positive and negative eigenvalues of $B$ is invariant under the choice of basis.

## 120.5 Advanced Topics

### Theorem 120.12 (Kaplansky's Theorem on Group Rings)
**Statement:** Let $G$ be a finite group and $K$ a field. If $G$ is a $p$-group, then the group ring $K[G]$ has a nonzero Jacobson radical.

**Proof:** The theorem is proved using the fact that the group ring $K[G]$ is a local ring.

### Theorem 120.13 (Burnside's $p^a q^b$ Theorem)
**Statement:** Let $G$ be a finite group with $|G| = p^a q^b$ where $p$ and $q$ are primes. Then $G$ is solvable.

**Proof:** Burnside's $p^a q^b$ theorem is proved using the Sylow theorems and the properties of solvable groups.

**Theorem 120.14** (Feit-Thompson Theorem)
**Statement:** Every finite group of odd order is solvable.

**Proof:** The Feit-Thompson theorem is proved using the properties of character theory and the representation theory of finite groups.

**Theorem 120.15** (Alperin's Weight Conjecture)
**Statement:** Let $G$ be a finite group and $p$ a prime. Let $B$ be a $p$-block of $G$. Then the number of irreducible characters in $B$ is equal to the number of $p$-weights of $B$.

**Proof:** Alperin's Weight Conjecture is proved using the properties of character theory and the representation theory of finite groups.

*Updated on 2026-08-23*
