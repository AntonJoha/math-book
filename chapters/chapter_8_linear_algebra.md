# Chapter 8: Linear Algebra - Vector Spaces and Matrices

## 8.1 Vector Spaces

### Theorem 8.1: Vector Space Axioms

**Statement**: A vector space $V$ over a field $F$ is a set equipped with two operations, vector addition and scalar multiplication, satisfying:

1. $(V, +)$ is an abelian group:
   - Closure: $\forall u,v \in V, u+v \in V$
   - Associativity: $(u+v)+w = u+(v+w)$
   - Identity: $\exists 0_V \in V, u+0_V = 0_V+u = u$
   - Inverses: $\forall u \in V, \exists -u \in V, u+(-u) = 0_V$
   - Commutativity: $u+v = v+u$

2. Scalar multiplication distributes over vector addition: $\forall c \in F, \forall u,v \in V, c(u+v) = cu+cv$

3. Scalar multiplication distributes over scalar addition: $\forall a,b \in F, \forall u \in V, (a+b)u = au+bu$

4. Scalar multiplication is associative: $\forall a,b \in F, \forall u \in V, (ab)u = a(bu)$

5. Multiplicative identity: $\exists 1_F \in F$ such that $1_F u = u$ for all $u \in V$

**Proof**: This is a definition. ∎

### Theorem 8.2: Uniqueness of Zero Vector

**Statement**: If $(V,+)$ satisfies the vector space axioms, then the zero vector is unique.

**Theorem 8.2**: Let $V$ be a vector space over $F$. Suppose $0, 0' \in V$ both satisfy the zero vector property. Then $0 = 0'$.

**Proof**: Since $0$ is the zero vector, $0' + 0 = 0'$. Since $0'$ is also a zero vector, $0' + 0 = 0$. Thus $0 = 0'$. ∎

### Theorem 8.3: Zero Scalar Annihilates Vectors

**Statement**: For any vector space $V$ over $F$, $0_F u = 0_V$ for all $u \in V$.

**Proof**: $0_F u = (0_F + 0_F)u = 0_F u + 0_F u$. Adding $-(0_F u)$ to both sides gives $0 = 0_F u$. ∎

### Theorem 8.4: Non-Zero Scalar Preserves Non-Zero Vectors

**Statement**: If $V$ is a vector space over a field $F$, then for any $u \neq 0_V$ and any $c \in F \setminus \{0_F\}$, we have $cu \neq 0_V$.

**Theorem 8.4**: Let $u \in V, u \neq 0_V$, and $c \in F \setminus \{0_F\}$. Then $cu \neq 0_V$.

**Proof**: Suppose $cu = 0_V$. Multiply by $c^{-1}$ (which exists since $c \neq 0_F$): $c^{-1}(cu) = c^{-1}0_V$. By associativity and Theorem 8.3, $(c^{-1}c)u = 0_V$. So $1_F u = 0_V$. Thus $u = 0_V$, a contradiction. ∎

### Theorem 8.5: Finite-Dimensional Vector Spaces

**Statement**: A vector space $V$ is said to be finite-dimensional if there exists a finite basis for $V$.

**Theorem 8.5**: Let $V$ be a vector space over $F$. The following are equivalent:
1. $V$ has a finite basis
2. Every linearly independent subset of $V$ is finite
3. Every subset of $V$ is bounded (in terms of spanning)

**Proof**: (Sketch) If $V$ has a finite basis $B = \{v_1, \dots, v_n\}$, then any linearly independent subset must have at most $n$ elements (otherwise they would be dependent). Thus $V$ has no infinite linearly independent subsets. ∎

## 8.2 Linear Transformations

### Theorem 8.6: Linear Transformation Definition

**Statement**: A linear transformation $T: V \to W$ between vector spaces is a function such that:
1. $T(u+v) = T(u) + T(v)$ for all $u,v \in V$
2. $T(cu) = cT(u)$ for all $c \in F, u \in V$

**Proof**: This is a definition. ∎

### Theorem 8.7: Matrix Representation of Linear Transformation

**Statement**: Every linear transformation $T: V \to W$ (where $V$ and $W$ have finite dimensions) can be represented by a unique matrix.

**Theorem 8.7**: Let $T: V \to W$ be a linear transformation where $\dim(V) = n$ and $\dim(W) = m$. Then there exists a unique $m \times n$ matrix $A$ such that for all $v \in V$, $T(v)$ is the linear combination of the basis vectors of $W$ with coefficients given by $A \cdot [v]$, where $[v]$ is the coordinate vector of $v$ relative to a basis of $V$.

**Proof**: Let $\{e_1, \dots, e_n\}$ be a basis for $V$ and $\{f_1, \dots, f_m\}$ be a basis for $W$. Write $T(e_j) = \sum_{i=1}^m A_{ij} f_i$. The matrix $A = (A_{ij})$ is unique and satisfies the claim. ∎

### Theorem 8.8: Composition of Linear Transformations

**Statement**: The composition of two linear transformations is a linear transformation.

**Theorem 8.8**: Let $U, V, W$ be vector spaces over $F$. If $T: U \to V$ and $S: V \to W$ are linear transformations, then $S \circ T: U \to W$ is a linear transformation.

**Proof**: Let $u, u' \in U$ and $c \in F$. Then:
$(S \circ T)(u + u') = S(T(u + u')) = S(T(u) + T(u')) = S(T(u)) + S(T(u')) = (S \circ T)(u) + (S \circ T)(u')$

And $(S \circ T)(cu) = S(T(cu)) = S(cT(u)) = cS(T(u)) = c(S \circ T)(u)$.

Thus $S \circ T$ is linear. ∎

### Theorem 8.9: Identity Linear Transformation

**Statement**: The identity map $I_V: V \to V$ defined by $I_V(v) = v$ for all $v \in V$ is a linear transformation.

**Proof**: Let $u, v \in V$ and $c \in F$. Then:
$I_V(u+v) = u+v = I_V(u) + I_V(v)$ and $I_V(cu) = cu = cI_V(u)$.

Thus $I_V$ is linear. ∎

## 8.3 Determinants

### Theorem 8.10: Determinant Definition

**Statement**: The determinant $\det(A)$ of an $n \times n$ matrix $A$ is defined recursively:

For $n=1$: $\det(a) = a$.
For $n>1$: $\det(A) = \sum_{j=1}^n (-1)^{1+j} A_{1j} M_{1j}$, where $M_{1j}$ is the minor obtained by deleting row 1 and column $j$.

**Theorem 8.10**: Let $A$ be an $n \times n$ matrix. The determinant of $A$ is unique and satisfies:
1. $\det(I_n) = 1$
2. $\det(AB) = \det(A)\det(B)$
3. $\det(A^T) = \det(A)$

**Proof**: These are standard properties of the determinant function.

### Theorem 8.11: Zero Row/Column Property

**Statement**: If a matrix $A$ has a row or column of zeros, then $\det(A) = 0$.

**Theorem 8.11**: Let $A$ be an $n \times n$ matrix with all zeros in row $i$. Then $\det(A) = 0$.

**Proof**: By Theorem 8.10, $\det(A) = \sum_{j=1}^n (-1)^{i+j} A_{ij} M_{ij}$. Since $A_{ij} = 0$ for all $j$, we have $\det(A) = 0$. ∎

### Theorem 8.12: Row/Column Operations

**Statement**: The determinant of a matrix can be computed using elementary row/column operations.

**Theorem 8.12**: Let $A$ be an $n \times n$ matrix. Then:
1. $\det(PA) = \det(P)\det(A)$ if $P$ is a permutation matrix
2. $\det(A) = 0$ if rows/columns are dependent
3. $\det(I_n) = 1$

**Proof**: These are standard determinant properties. ∎

## 8.4 Eigenvalues and Eigenvectors

### Theorem 8.13: Eigenvalue Definition

**Statement**: An eigenvalue $\lambda$ of a square matrix $A$ is a scalar such that there exists a nonzero vector $v$ with $Av = \lambda v$. Such a vector $v$ is called an eigenvector.

**Theorem 8.13**: Let $A$ be an $n \times n$ matrix. The scalar $\lambda$ is an eigenvalue of $A$ if and only if $\det(A - \lambda I_n) = 0$.

**Proof**: $Av = \lambda v$ is equivalent to $(A - \lambda I)v = 0$. Since $v \neq 0$, the null space of $A - \lambda I$ is nontrivial, so $\det(A - \lambda I) = 0$. ∎

### Theorem 8.14: Characteristic Polynomial

**Statement**: The characteristic polynomial of $A$ is $\det(A - \lambda I_n)$, and the eigenvalues of $A$ are the roots of this polynomial.

**Theorem 8.14**: Let $A$ be an $n \times n$ matrix. The characteristic polynomial $p_A(\lambda) = \det(A - \lambda I_n)$ has degree $n$, and the eigenvalues of $A$ are the roots of $p_A(\lambda) = 0$.

**Proof**: By Theorem 8.13, $\lambda$ is an eigenvalue iff $\det(A - \lambda I) = 0$. ∎

### Theorem 8.15: Trace Property

**Statement**: The trace of a matrix $A$, denoted $\text{tr}(A)$, is the sum of its diagonal entries, and $\text{tr}(A) = \sum \lambda_i$ where $\lambda_i$ are the eigenvalues of $A$.

**Theorem 8.15**: Let $A$ be an $n \times n$ matrix with eigenvalues $\lambda_1, \dots, \lambda_n$. Then $\text{tr}(A) = \sum_{i=1}^n \lambda_i$.

**Proof**: $\det(A - \lambda I) = \prod_{i=1}^n (\lambda_i - \lambda)$, and comparing coefficients of the characteristic polynomial, $\text{tr}(A)$ is the negative of the coefficient of $\lambda^{n-1}$. ∎

## 8.5 Linear Independence

### Theorem 8.16: Linear Independence Definition

**Statement**: A set of vectors $\{v_1, \dots, v_k\}$ in a vector space $V$ is linearly independent if the equation $\sum_{i=1}^k c_i v_i = 0$ implies $c_i = 0$ for all $i$.

**Theorem 8.16**: Let $\{v_1, \dots, v_k\}$ be a set of vectors in $V$. The following are equivalent:
1. $\{v_1, \dots, v_k\}$ is linearly independent
2. No vector in $\{v_1, \dots, v_k\}$ is a linear combination of the others
3. Every subset of $\{v_1, \dots, v_k\}$ is linearly independent

**Proof**: (1) $\implies$ (2): Suppose $v_i$ is a linear combination of $\{v_1, \dots, v_{i-1}, v_{i+1}, \dots, v_k\}$. Then $\sum c_j v_j + c_i v_i = 0$ with some $c_j \neq 0$, contradicting linear independence.

(2) $\implies$ (3): Every subset satisfies the definition of linear independence.

(3) $\implies$ (1): Every subset, including the whole set, is linearly independent. ∎

### Theorem 8.17: Basis and Dimension

**Statement**: A vector space $V$ has a basis if and only if $V$ has the property that every subset is either linearly independent or spans $V$.

**Theorem 8.17**: Let $V$ be a vector space. The following are equivalent:
1. $V$ has a basis
2. Every linearly independent subset of $V$ can be extended to a basis of $V$
3. $V$ has the property that every subset is either linearly independent or spans $V$

**Proof**: These are equivalent by the definition of a basis (a maximal linearly independent set). ∎

### Theorem 8.18: Cardinality of Bases

**Statement**: If $V$ has a basis, then all bases of $V$ have the same cardinality.

**Theorem 8.18**: Let $V$ be a vector space with bases $B_1$ and $B_2$. Then $|B_1| = |B_2|$.

**Proof**: This is a standard result in vector space theory. If $|B_1| < |B_2|$, then we can construct a contradiction by extending $B_1$ to include elements from $B_2$.

## 8.6 Rank-Nullity Theorem

### Theorem 8.19: Rank-Nullity Theorem

**Statement**: Let $T: V \to W$ be a linear transformation between finite-dimensional vector spaces. Then $\dim(V) = \dim(\text{ker}(T)) + \dim(\text{im}(T))$.

**Theorem 8.19**: The Rank-Nullity Theorem states: $\dim(V) = \dim(\text{ker}(T)) + \dim(\text{im}(T))$.

**Proof**: Consider the restriction of $T$ to a basis of $\text{ker}(T)$. Extend it to a basis of $V$ by adding vectors whose images form a basis of $\text{im}(T)$. The number of added vectors is $\dim(V) - \dim(\text{ker}(T))$, and the number of images is $\dim(\text{im}(T))$. By Theorem 8.7, these correspond. ∎

### Theorem 8.20: Invertible Linear Transformations

**Statement**: A linear transformation $T: V \to V$ is invertible if and only if $T$ is both injective and surjective.

**Theorem 8.20**: Let $T: V \to V$ be a linear transformation on a finite-dimensional vector space. Then $T$ is invertible iff $T$ is both injective and surjective.

**Proof**: Since $\dim(V) < \infty$, $T$ is injective iff $\ker(T) = \{0\}$ iff $\dim(\text{ker}(T)) = 0$. By the Rank-Nullity Theorem, $\dim(\text{im}(T)) = \dim(V)$, so $T$ is surjective. ∎

---

## Exercises

### Exercise 8.1: Show that any finite-dimensional vector space over a field $F$ has a basis.

### Exercise 8.2: Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be the linear transformation defined by the matrix $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$. Find the dimension of $\text{ker}(T)$ and $\text{im}(T)$.

### Exercise 8.3: Prove that the set $\{I_n, A, A^2, \dots, A^k\}$ is linearly dependent for some $k$.

### Exercise 8.4: Show that a matrix $A$ is invertible if and only if its determinant is nonzero.

---

## 8.x Advanced Linear Algebra

### Theorem 8.1: Rank-Nullity Theorem

**Statement**: Let $V$ be a finite-dimensional vector space and $T: V \to W$ be a linear transformation. Then:

$$\dim(V) = \dim(\ker(T)) + \dim(\operatorname{im}(T))$$

**Proof**: Consider a basis for $\ker(T) = \{v \in V : T(v) = 0\}$. Extend this basis to a basis $\{v_1, \dots, v_k, w_1, \dots, w_m\}$ for $V$, where $k = \dim(\ker(T))$. Then $\{T(w_1), \dots, T(w_m)\}$ is a basis for $\operatorname{im}(T)$. Thus $\dim(\operatorname{im}(T)) = m$, and we have $\dim(V) = k + m$. ∎

### Theorem 8.2: Jordan Normal Form

**Statement**: Every square matrix $A \in M_n(\mathbb{C})$ is similar to an upper triangular matrix.

**Proof**: Since $\mathbb{C}$ is algebraically closed, the characteristic polynomial of $A$ has a root $\lambda$. Then $\ker(A - \lambda I) \neq \{0\}$, so we can pick an eigenvector $v_1$. The quotient space $V/\ker(A - \lambda I)$ has dimension $n-1$, and we can inductively find eigenvectors for the quotient. The matrix representation in this basis is upper triangular. ∎

### Theorem 8.3: Singular Value Decomposition

**Statement**: Every matrix $A \in M_{m \times n}(\mathbb{C})$ can be written as

$$A = U\Sigma V^*$$

where $U$ and $V$ are unitary matrices and $\Sigma$ is diagonal with non-negative real entries (the singular values of $A$).

**Proof**: This is a classical result in linear algebra. The SVD exists for every complex matrix and can be derived from the spectral theorem applied to $A^*A$ and $AA^*$. ∎

### Theorem 8.4: Spectral Radius Theorem

**Statement**: For any matrix $A \in M_n(\mathbb{C})$, the spectral radius satisfies:

$$\rho(A) \leq \|A\|$$

for any induced matrix norm $\|\cdot\|$.

**Proof**: The spectral radius $\rho(A) = \max\{|\lambda| : \lambda \text{ is an eigenvalue of } A\}$. If $v$ is an eigenvector with eigenvalue $\lambda$, then $\|Av\| = |\lambda|\|v\|$. Thus $|\lambda| = \frac{\|Av\|}{\|v\|} \leq \sup_{x \neq 0} \frac{\|Ax\|}{\|x\|} = \|A\|$. ∎


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
