# Chapter 34: Lie Groups and Lie Algebras

## 34.1 Introduction to Lie Theory

Lie theory provides the bridge between continuous symmetries (Lie groups) and their local linear structure (Lie algebras). Originally developed to study continuous transformation groups, Lie theory has found applications in physics, geometry, and many other fields.

**Definition**: A **Lie group** is a group that is also a smooth manifold, such that the group operations (multiplication and inversion) are smooth maps.

**Example**: The general linear group $GL(n, \mathbb{R})$ of invertible $n \times n$ matrices is a Lie group.

**Example**: The circle group $S^1 = \{z \in \mathbb{C} : |z| = 1\}$ under complex multiplication is a Lie group.

**Example**: The orthogonal group $O(n)$ of $n \times n$ orthogonal matrices is a Lie group.

## 34.2 The Lie Algebra of a Lie Group

**Definition**: The **Lie algebra** $\mathfrak{g}$ of a Lie group $G$ at the identity element $e$ is the tangent space $T_e G$. The Lie bracket $[\cdot, \cdot]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ is defined using the commutator of left-invariant vector fields.

**Theorem 34.1**: If $X, Y$ are left-invariant vector fields on $G$, then the Lie bracket $[X, Y]$ is the Lie derivative $X(Y) - Y(X)$.

**Proof**: For left-invariant vector fields $X, Y$, the Lie bracket is computed at the identity using the Lie derivative:
$$[X, Y]_e = \mathcal{L}_X Y = [X, Y]$$

The Lie bracket satisfies:
1. Bilinearity: $[\alpha X + \beta Y, Z] = \alpha [X, Z] + \beta [Y, Z]$
2. Skew-symmetry: $[X, Y] = -[Y, X]$
3. Jacobi identity: $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$

**Theorem 34.2**: The map $\mathcal{L}_G: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ defined by $\mathcal{L}_G(X, Y) = [X, Y]$ is a Lie algebra homomorphism.

**Proof**: The commutativity of $[X, Y]$ with the bracket structure follows from the definition of the Lie bracket in terms of the commutator of vector fields. ∎

## 34.3 Exponential Map

**Definition**: The **exponential map** $\exp: \mathfrak{g} \to G$ is defined by $\exp(X) = \gamma(1)$ where $\gamma: \mathbb{R} \to G$ is the unique integral curve of the left-invariant vector field $X$ with $\gamma(0) = e$.

**Theorem 34.3**: The exponential map $\exp: \mathfrak{g} \to G$ maps the Lie algebra to the Lie group via one-parameter subgroups.

**Proof**: The integral curve $\gamma(t)$ of a left-invariant vector field $X$ satisfies $\gamma(t+s) = \gamma(t)\gamma(s)$, making it a one-parameter subgroup. ∎

**Theorem 34.4 (Local Injectivity)**: The exponential map $\exp: \mathfrak{g} \to G$ is a local diffeomorphism near $0 \in \mathfrak{g}$.

**Proof**: The exponential map is a local diffeomorphism near $0$ by the inverse function theorem. Specifically, $\exp$ is a smooth map whose derivative at $0$ is the identity map. ∎

**Corollary 34.1 (Global for Compact Groups)**: If $G$ is compact, then $\exp$ maps a neighborhood of $0$ in $\mathfrak{g}$ onto a neighborhood of $e$ in $G$.

## 34.4 Adjoint Representation

**Definition**: The **adjoint representation** $\mathrm{Ad}: G \to \mathrm{GL}(\mathfrak{g})$ is defined by $\mathrm{Ad}_g(X) = g \cdot X \cdot g^{-1}$ for $g \in G$ and $X \in \mathfrak{g}$.

**Theorem 34.5**: The adjoint representation is the differential of the conjugation map $c_g: G \to G$ defined by $c_g(h) = ghg^{-1}$.

**Proof**: The differential $d(c_g)_e: T_e G \to T_e G$ at the identity is precisely the adjoint action on the tangent space at the identity. ∎

**Theorem 34.6**: For any $g \in G$, $\mathrm{Ad}_g \in \mathrm{Aut}(\mathfrak{g})$.

**Proof**: The adjoint map is a Lie algebra homomorphism that preserves the bracket structure. ∎

## 34.5 Lie's Third Theorem

**Theorem 34.7 (Lie's Third Theorem)**: Every finite-dimensional real Lie algebra $\mathfrak{g}$ is isomorphic to the Lie algebra of some Lie group $G$.

**Proof (Sketch)**: 
1. Given a finite-dimensional real Lie algebra $\mathfrak{g}$, we can construct a simply connected Lie group $G$ with Lie algebra $\mathfrak{g}$.
2. This construction uses the exponential map and the universal cover of the Lie group.
3. The resulting group $G$ satisfies $\mathrm{Lie}(G) = \mathfrak{g}$. ∎

**Corollary 34.2 (Uniqueness)**: Simply connected Lie groups are unique up to isomorphism for a given Lie algebra.

## 34.6 Subalgebras and Subgroups

**Definition**: A **Lie subalgebra** $\mathfrak{h}$ of $\mathfrak{g}$ is a subspace that is closed under the Lie bracket.

**Theorem 34.8**: A subset $H \subseteq G$ is a Lie subgroup if and only if its tangent space at the identity $T_e H$ is a Lie subalgebra of $\mathfrak{g}$.

**Proof**: 
1. If $H$ is a Lie subgroup, then $T_e H$ is closed under the Lie bracket by invariance of the bracket under left translations.
2. Conversely, if $\mathfrak{h} \subseteq \mathfrak{g}$ is a Lie subalgebra, then the unique connected Lie subgroup with Lie algebra $\mathfrak{h}$ exists and is a Lie subgroup. ∎

**Corollary 34.3**: Every finite-dimensional Lie algebra has a unique connected Lie group with that Lie algebra (up to isomorphism).

## 34.7 Classification of Classical Lie Groups

The classical Lie groups are:
1. **$GL(n, \mathbb{R})$**: The general linear group of invertible $n \times n$ matrices over $\mathbb{R}$.

**Lie Algebra**: $\mathfrak{gl}(n, \mathbb{R}) = \mathbb{R}^{n \times n}$ with the bracket $[A, B] = AB - BA$.

2. **$O(n)$**: The orthogonal group of $n \times n$ matrices with $A^T A = I$.

**Lie Algebra**: $\mathfrak{o}(n) = \{A \in \mathbb{R}^{n \times n} : A^T + A = 0\}$ (skew-symmetric matrices).

3. **$U(n)$**: The unitary group of $n \times n$ matrices with $A^* A = I$.

**Lie Algebra**: $\mathfrak{u}(n) = \{A \in \mathbb{R}^{n \times n} : A^* + A = 0\}$ (skew-Hermitian matrices).

4. **$SL(n, \mathbb{R})$**: The special linear group of $n \times n$ matrices with $\det(A) = 1$.

**Lie Algebra**: $\mathfrak{sl}(n, \mathbb{R}) = \{A \in \mathbb{R}^{n \times n} : \mathrm{tr}(A) = 0\}$ (trace-zero matrices).

5. **$SO(n)$**: The special orthogonal group of $n \times n$ matrices with $\det(A) = 1$ and $A^T A = I$.

**Lie Algebra**: $\mathfrak{so}(n) = \{A \in \mathbb{R}^{n \times n} : A^T + A = 0\}$ (skew-symmetric matrices).

## 34.8 Classification of Simple Lie Algebras

Cartan's classification theorem states that simple real Lie algebras fall into two families:
1. **Classical types**: $\mathfrak{so}(n)$, $\mathfrak{sl}(n)$, $\mathfrak{sp}(n)$
2. **Exceptional types**: $\mathfrak{g}_2$, $\mathfrak{f}_4$, $\mathfrak{e}_6$, $\mathfrak{e}_7$, $\mathfrak{e}_8$

**Theorem 34.9**: A finite-dimensional real Lie algebra $\mathfrak{g}$ is semisimple if and only if $\mathfrak{g} = \bigoplus_{i} \mathfrak{g}_i$ where each $\mathfrak{g}_i$ is a simple Lie algebra.

**Proof**: The Lie algebra is semisimple if its radical (maximal solvable ideal) is zero. The structure theory of semisimple Lie algebras was developed by Cartan, Killing, and others. ∎

**Corollary 34.4**: Simple Lie algebras over $\mathbb{R}$ are classified by their rank and dimension.

## 34.9 Applications in Physics

### 34.9.1 Classical Mechanics and Hamiltonian Mechanics

**Theorem 34.10**: The phase space of a mechanical system with configuration space $M$ and momenta $\mathbb{R}^k$ can be described by the symplectic manifold $T^*M$ with a Hamiltonian function $H: T^*M \to \mathbb{R}$.

**Proof**: A symplectic manifold is a smooth manifold equipped with a non-degenerate, closed 2-form $\omega$. The Hamiltonian vector field $X_H$ associated with $H$ satisfies $dH = \iota_{X_H} \omega$. ∎

### 34.9.2 Quantum Mechanics and Lie Symmetry

Lie groups and algebras play a crucial role in quantum mechanics through their representation theory. The Heisenberg algebra appears naturally in quantum mechanics as the algebra of position and momentum operators.

**Theorem 34.11**: The canonical commutation relation $[X, P] = i\hbar I$ defines the Heisenberg algebra, which is the Lie algebra of the infinite-dimensional unitary group preserving the quantum state space.

## 34.10 Exercises

### Exercise 34.1
Prove that $GL(n, \mathbb{R})$ is a Lie group.

### Exercise 34.2
Show that the exponential map $\exp: \mathfrak{gl}(n, \mathbb{R}) \to GL(n, \mathbb{R})$ is given by the matrix exponential.

### Exercise 34.3
Prove that $\mathfrak{so}(n)$ is a Lie algebra.

### Exercise 34.4
Let $\mathfrak{g}$ be a Lie algebra with basis $\{X_1, \dots, X_n\}$. Show that the dimension of the Lie algebra is $n$.

### Exercise 34.5
Classify all 2-dimensional Lie algebras over $\mathbb{R}$.

∎
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697448

--- Theorem Generation ---



# **Lie's Theorem**
**Statement**: Finite-dimensional Lie algebra has simultaneous triangular representation.
**Proof**: [proof outline]...


# **Exponential Map**
**Statement**: One-to-one correspondence between Lie algebra and Lie group near identity.
**Proof**: [proof outline]...


# **Ado's Theorem**
**Statement**: Every finite-dimensional Lie algebra has faithful finite-dimensional representation.
**Proof**: [proof outline]...


# **Cartan's Theorem**
**Statement**: Lie algebra determines connected Lie group up to covering.
**Proof**: [proof outline]...


# **Painlevé's Theorem**
**Statement**: Lie algebras of reductive groups classify via roots and weights.
**Proof**: [proof outline]...


# **Hilbert's Fifth Problem**
**Statement**: Locally Euclidean groups are Lie groups (solved positively).
**Proof**: [proof outline]...


# **Lie Algebra**
**Statement**: Vector space with bilinear bracket satisfying Jacobi identity.
**Proof**: [proof outline]...


# **Cartan Subalgebra**
**Statement**: Maximal abelian subalgebra in semisimple Lie algebra.
**Proof**: [proof outline]...


# **Root System**
**Statement**: Orbit of Cartan subalgebra under Weyl group action.
**Proof**: [proof outline]...


# **Kac-Moody Algebra**
**Statement**: Infinite-dimensional Lie algebra generalizing finite-dimensional ones.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618673

--- Theorem Generation ---



# **Lie's Theorem**
**Statement**: Finite-dimensional Lie algebra has simultaneous triangular representation.
**Proof**: [proof outline]...


# **Exponential Map**
**Statement**: One-to-one correspondence between Lie algebra and Lie group near identity.
**Proof**: [proof outline]...


# **Ado's Theorem**
**Statement**: Every finite-dimensional Lie algebra has faithful finite-dimensional representation.
**Proof**: [proof outline]...


# **Cartan's Theorem**
**Statement**: Lie algebra determines connected Lie group up to covering.
**Proof**: [proof outline]...


# **Painlevé's Theorem**
**Statement**: Lie algebras of reductive groups classify via roots and weights.
**Proof**: [proof outline]...


# **Hilbert's Fifth Problem**
**Statement**: Locally Euclidean groups are Lie groups (solved positively).
**Proof**: [proof outline]...


# **Lie Algebra**
**Statement**: Vector space with bilinear bracket satisfying Jacobi identity.
**Proof**: [proof outline]...


# **Cartan Subalgebra**
**Statement**: Maximal abelian subalgebra in semisimple Lie algebra.
**Proof**: [proof outline]...


# **Root System**
**Statement**: Orbit of Cartan subalgebra under Weyl group action.
**Proof**: [proof outline]...


# **Kac-Moody Algebra**
**Statement**: Infinite-dimensional Lie algebra generalizing finite-dimensional ones.
**Proof**: [proof outline]...
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
