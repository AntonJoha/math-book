# Group Theory and Field Extensions

## 14.1 Basic Group Theory

### 14.1.1 Definitions

**Theorem 14.1:** A group $(G, \cdot)$ is a set equipped with an operation such that:
1. Closure: $\forall a,b \in G, a \cdot b \in G$
2. Associativity: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
3. Identity: $\exists e \in G, \forall a \in G, e \cdot a = a \cdot e = a$
4. Inverse: $\forall a \in G, \exists a^{-1} \in G, a \cdot a^{-1} = a^{-1} \cdot a = e$

### 14.1.2 Abelian Groups

**Theorem 14.2:** A group is Abelian (commutative) if $a \cdot b = b \cdot a$ for all $a,b \in G$.

## 14.2 Lagrange's Theorem

### 14.2.1 Statement

**Theorem 14.3 (Lagrange's Theorem):** If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$.

**Proof:** 
Let $H$ be a subgroup of $G$ with $|H| = n$ and $|G| = m$. The cosets of $H$ in $G$ are:
$$H, g_1H, g_2H, \dots, g_{k-1}H$$
where each coset has $n$ elements and the cosets are disjoint and partition $G$.

Thus, $|G| = k \cdot |H|$, so $n$ divides $m$.

### 14.2.2 Corollary: Finite Group Order Divides Field Extension

**Theorem 14.4:** If $E/F$ is a finite field extension of degree $n$, then any subgroup $G$ of the Galois group $\text{Gal}(E/F)$ has order dividing $n$.

## 14.3 Orbit-Stabilizer Theorem

### 14.3.1 Statement

**Theorem 14.5 (Orbit-Stabilizer Theorem):** Let $G$ act on a set $X$. For any $x \in X$:
$$|G| = |\text{orbit}(x)| \cdot |\text{Stab}(x)|$$

**Proof:** 
The map $G \to \text{orbit}(x)$ defined by $g \mapsto g \cdot x$ is surjective. Its fibers are the cosets of $\text{Stab}(x) = \{g \in G : g \cdot x = x\}$, which all have size $|\text{Stab}(x)|$.

### 14.3.2 Group Action on Conjugacy Classes

**Theorem 14.6:** The orbit of $g \in G$ under conjugation by $G$ is the conjugacy class $\text{Cl}(g) = \{hgh^{-1} : h \in G\}$. The stabilizer is $\text{Stab}(g) = \{h \in G : hgh^{-1} = g\} = C_G(g)$ (centralizer).

**Proof:** 
By Theorem 14.5: $|G| = |\text{Cl}(g)| \cdot |C_G(g)|$. This is the class equation, fundamental for representation theory.

## 14.4 Cauchy's Theorem

### 14.4.1 Statement

**Theorem 14.7 (Cauchy's Theorem):** If $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ contains an element of order $p$.

**Proof:** 
Consider the set of $p$-tuples $(a_1, \dots, a_p)$ such that $a_1 \cdots a_p = 1$. Partition into orbits under cyclic shifts. Some orbit has size not divisible by $p$, hence exactly size 1, giving $(g,\dots,g)$ with $g^p = 1$.

## 14.5 Sylow's Theorems

### 14.5.1 Statement

**Theorem 14.8 (Sylow's Theorems):** Let $G$ be a finite group and $n_p = p^k \cdot m$ where $p \nmid m$. Then:
1. There exists a subgroup of order $p^k$ (a Sylow $p$-subgroup)
2. All Sylow $p$-subgroups are conjugate
3. The number $n_p$ of Sylow $p$-subgroups satisfies $n_p \equiv 1 \pmod{p}$ and $n_p$ divides $m$

## 14.6 Group Isomorphism Theorems

### 14.6.1 First Isomorphism Theorem

**Theorem 14.9 (First Isomorphism Theorem):** If $\phi: G \to H$ is a homomorphism with kernel $K = \ker(\phi)$ and image $I = \text{im}(\phi)$, then $G/K \cong I$.

**Proof:** Define $\psi: G/K \to I$ by $\psi(gK) = \phi(g)$. This is well-defined (if $g_1K = g_2K$, then $\phi(g_1) = \phi(g_2)$), surjective, and injective (kernel is trivial).

### 14.6.2 Second Isomorphism Theorem

**Theorem 14.10 (Second Isomorphism Theorem):** If $H, K$ are subgroups of $G$ with $K \trianglelefteq G$, then $H/(H \cap K) \cong HK/K$.

**Proof:** Define $\psi: H \to HK/K$ by $\psi(h) = hK$. This is a surjective homomorphism with kernel $H \cap K$.

### 14.6.3 Third Isomorphism Theorem

**Theorem 14.11 (Third Isomorphism Theorem):** If $K \trianglelefteq H \trianglelefteq G$, then $H/K \cong G/(G/K)$? (More carefully: $(G/N)/(H/N) \cong H/N$? No. Correct form: $(G/M)/(N/M) \cong G/N$ if $N \subset M$).

## 14.7 Galois Theory

### 14.7.1 Fundamental Theorem of Galois Theory

**Theorem 14.12 (Galois Correspondence):** There is a bijection between:
1. Subfields of a finite extension $E/F$ containing $F$
2. Subgroups of $\text{Gal}(E/F)$

The correspondence sends a field $K$ to $\text{Gal}(E/K) = \{\sigma \in \text{Gal}(E/F) : \sigma(k) = k \forall k \in K\}$ and a subgroup $H$ to $E^H = \{x \in E : \sigma(x) = x \forall \sigma \in H\}$.

### 14.7.2 Solvability by Radicals

**Theorem 14.13:** A polynomial is solvable by radicals iff its Galois group is solvable (has a chain of normal subgroups with abelian quotients).

**Proof:** A group $G$ is solvable iff its composition factors are cyclic (abelian). A field extension is radical iff its Galois group is solvable.

### 14.7.3 Example: $x^5 - 1$ is solvable, but $x^5 - 2$ is not

**Theorem 14.14:** The polynomial $x^5 - 1$ is solvable (Galois group is cyclic). The polynomial $x^5 - 2$ has Galois group $S_5$ (not solvable).

## 14.8 Field Extensions

### 14.8.1 Algebraic and Transcendental Extensions

**Theorem 14.15:** An element $\alpha$ is algebraic over $F$ if it is a root of a non-zero polynomial in $F[x]$. If not algebraic, it is transcendental.

### 14.8.2 Degree of Extension

**Theorem 14.16:** If $\alpha$ is algebraic over $F$, the degree $[F(\alpha):F]$ equals the degree of its minimal polynomial.

## 14.9 Exercises

### 14.9.1 Practice Problems

1. **Problem 14.1:** Prove that $S_3$ has no subgroup of order 4.

2. **Problem 14.2:** Show that if $G$ has a normal subgroup $H$ such that $G/H$ is simple, then any normal subgroup of $G$ is contained in $H$ or contains $H$.

3. **Problem 14.3:** Find the Galois group of $x^4 - 2$ over $\mathbb{Q}$.

4. **Problem 14.4:** Prove that the polynomial $x^5 + x + 1$ is irreducible over $\mathbb{Q}$ using Eisenstein's criterion.

5. **Problem 14.5:** Show that $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ has degree 4 over $\mathbb{Q}$ and its Galois group is $V_4$ (Klein four-group).

======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697194

Theorem Generation

# **Cauchy's First Theorem**
**Statement**: If p divides |G|, G has element of order p.
**Proof**: [proof outline]...


# **Sylow's First Theorem**
**Statement**: For each prime power p^n dividing |G|, Sylow p-subgroup exists.
**Proof**: [proof outline]...


# **Sylow's Third Theorem**
**Statement**: All Sylow p-subgroups are conjugate.
**Proof**: [proof outline]...


# **Schreier's Formula**
**Statement**: Index of subgroup ≥ 2 implies |G/H| ≥ (|G|-1)+1.
**Proof**: [proof outline]...


# **Goursat's Lemma**
**Statement**: Subgroup of direct product ≅ subdirect product of subgroups.
**Proof**: [proof outline]...


# **Jordan-Hölder Theorem**
**Statement**: Any two composition series are equivalent up to reordering.
**Proof**: [proof outline]...


# **Hall's Theorem**
**Statement**: Hall subgroups exist and are conjugate in finite solvable groups.
**Proof**: [proof outline]...


# **Ore's Theorem**
**Statement**: Cyclic group of order m exists iff 1 divides m.
**Proof**: [proof outline]...


# **Burnside's Lemma**
**Statement**: Count orbits = average number of fixed points.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618469

Theorem Generation

# **Cauchy's First Theorem**
**Statement**: If p divides |G|, G has element of order p.
**Proof**: [proof outline]...


# **Sylow's First Theorem**
**Statement**: For each prime power p^n dividing |G|, Sylow p-subgroup exists.
**Proof**: [proof outline]...


# **Sylow's Third Theorem**
**Statement**: All Sylow p-subgroups are conjugate.
**Proof**: [proof outline]...


# **Schreier's Formula**
**Statement**: Index of subgroup ≥ 2 implies |G/H| ≥ (|G|-1)+1.
**Proof**: [proof outline]...


# **Goursat's Lemma**
**Statement**: Subgroup of direct product ≅ subdirect product of subgroups.
**Proof**: [proof outline]...


# **Jordan-Hölder Theorem**
**Statement**: Any two composition series are equivalent up to reordering.
**Proof**: [proof outline]...


# **Hall's Theorem**
**Statement**: Hall subgroups exist and are conjugate in finite solvable groups.
**Proof**: [proof outline]...


# **Ore's Theorem**
**Statement**: Cyclic group of order m exists iff 1 divides m.
**Proof**: [proof outline]...


# **Burnside's Lemma**
**Statement**: Count orbits = average number of fixed points.
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