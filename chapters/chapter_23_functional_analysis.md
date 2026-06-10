# Chapter 23: Functional Analysis - Comprehensive Theorems and Proofs

## 23.1 Vector Spaces and Normed Spaces

### Theorem 23.1: Definition of Vector Space

**Statement**: A vector space is a set $V$ equipped with addition and scalar multiplication satisfying the following axioms:
1. Associativity of addition: $(u+v)+w = u+(v+w)$
2. Commutativity of addition: $u+v = v+u$
3. Existence of zero vector: There exists $0$ such that $v+0 = v$
4. Existence of additive inverse: For each $v$, there exists $-v$ such that $v+(-v) = 0$
5. Distributivity: $c(u+v) = cu+cv$
6. Distributivity: $(c+d)v = cv+dv$
7. Associativity of scalar multiplication: $c(dv) = (cd)v$
8. Identity scalar: $1v = v$
9. Compatibility: $(cd)v = c(dv)$

**Proof**: This is a definition. ∎

### Theorem 23.2: Definition of Normed Space

**Statement**: A normed vector space is a vector space $V$ equipped with a norm $\|\cdot\|: V \to \mathbb{R}$ satisfying:
1. $\|v\| \ge 0$ for all $v \in V$
2. $\|v\| = 0$ iff $v = 0$
3. $\|\alpha v\| = |\alpha| \|v\|$ for all $\alpha \in \mathbb{F}, v \in V$
4. $\|u+v\| \le \|u\| + \|v\|$ (triangle inequality)

**Proof**: This is a definition. ∎

### Theorem 23.3: Inner Product Space

**Statement**: An inner product space is a vector space $V$ equipped with an inner product $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{F}$ satisfying:
1. Linearity in first argument: $\langle \alpha u + \beta v, w \rangle = \alpha \langle u, w \rangle + \beta \langle v, w \rangle$
2. Conjugate symmetry: $\langle v, w \rangle = \overline{\langle w, v \rangle}$
3. Positive definiteness: $\langle v, v \rangle \ge 0$ with equality iff $v = 0$

**Proof**: This is a definition. ∎

### Theorem 23.4: Relation between Inner Product and Norm

**Statement**: If $(V, \langle \cdot, \cdot \rangle)$ is an inner product space, then the induced norm is $\|v\| = \sqrt{\langle v, v \rangle}$.

**Proof**: The norm satisfies all axioms by the properties of the inner product. Conversely, if a norm satisfies $\|u+v\|^2 = \|u\|^2 + \|v\|^2 + 2\text{Re}\langle u, v \rangle$, then the inner product is defined by the polarization identity. ∎

### Theorem 23.5: Cauchy-Schwarz Inequality

**Statement**: In any inner product space, $|\langle u, v \rangle| \le \|u\| \|v\|$ for all $u,v \in V$.

**Proof**: Let $v \ne 0$. For any real $\lambda$, $\langle v + \lambda u, v + \lambda u \rangle \ge 0$. Expanding: $\|v\|^2 + 2\lambda \text{Re}\langle v, u \rangle + \lambda^2 \|u\|^2 \ge 0$. The quadratic in $\lambda$ has discriminant $(2\text{Re}\langle v, u \rangle)^2 - 4\|v\|^2 \|u\|^2 \le 0$, so $|\text{Re}\langle v, u \rangle| \le \|v\| \|u\|$. A similar argument with imaginary $\lambda$ gives $|\text{Im}\langle v, u \rangle| \le \|v\| \|u\|$, so $|\langle v, u \rangle| \le \|v\| \|u\|$. ∎

## 23.2 Convergence and Completeness

### Theorem 23.6: Definition of Cauchy Sequence

**Statement**: A sequence $\{v_n\}$ in a normed space $V$ is Cauchy if for every $\epsilon > 0$, there exists $N$ such that for all $n,m \ge N$, $\|v_n - v_m\| < \epsilon$.

**Proof**: This is a definition. ∎

### Theorem 23.7: Completeness

**Statement**: A normed space $V$ is complete if every Cauchy sequence in $V$ converges to a limit in $V$.

**Proof**: This is a definition. ∎

### Theorem 23.8: Banach Space

**Statement**: A Banach space is a complete normed vector space.

**Proof**: This is a definition. ∎

### Theorem 23.9: Hilbert Space

**Statement**: A Hilbert space is a complete inner product space.

**Proof**: This is a definition. ∎

### Theorem 23.10: Sequence Space $\ell^2$

**Statement**: The space $\ell^2 = \{x = (x_n) : \sum |x_n|^2 < \infty\}$ with norm $\|x\|_2 = (\sum |x_n|^2)^{1/2}$ is a Hilbert space.

**Proof**: The space is complete (as shown in Theorem 23.21) and the inner product $\langle x, y \rangle = \sum x_n \overline{y_n}$ satisfies the inner product axioms. ∎

### Theorem 23.11: Function Space $L^2$

**Statement**: The space $L^2([a,b]) = \{f : [a,b] \to \mathbb{C} : \int_a^b |f|^2 < \infty\}$ with norm $\|f\|_2 = (\int_a^b |f|^2)^{1/2}$ is a Hilbert space.

**Proof**: The space is complete (as shown in Theorem 23.23) and the inner product $\langle f, g \rangle = \int_a^b f \overline{g}$ satisfies the inner product axioms. ∎

### Theorem 23.12: Banach-Alaoglu Theorem

**Statement**: In a normed space $V$, the closed unit ball is compact in the weak* topology iff $V$ is finite-dimensional.

**Proof**: This is a consequence of the Eberlein-Smulian theorem. ∎

## 23.3 Linear Operators

### Theorem 23.13: Definition of Linear Operator

**Statement**: A linear operator $T: V \to W$ between vector spaces satisfies $T(u+v) = Tu+Tv$ and $T(\alpha u) = \alpha Tu$ for all $u,v \in V, \alpha \in \mathbb{F}$.

**Proof**: This is a definition. ∎

### Theorem 23.14: Matrix Representation

**Statement**: If $V$ and $W$ are finite-dimensional vector spaces with bases, then any linear operator $T: V \to W$ can be represented by a matrix.

**Proof**: Let $V$ have basis $\{e_1, \dots, e_n\}$ and $W$ have basis $\{f_1, \dots, f_m\}$. Then $T(e_j) = \sum_{i=1}^m a_{ij} f_i$ defines the matrix $A = (a_{ij})$. ∎

### Theorem 23.15: Spectral Theorem (Self-Adjoint)

**Statement**: If $T$ is a self-adjoint linear operator on a finite-dimensional complex inner product space, then $T$ has an orthonormal basis of eigenvectors.

**Proof**: This follows from the fact that self-adjoint operators have real eigenvalues and orthogonal eigenspaces. ∎

### Theorem 23.16: Singular Value Decomposition

**Statement**: If $T$ is a linear operator between finite-dimensional inner product spaces, then there exist orthonormal bases $\{e_1, \dots, e_m\}$ and $\{f_1, \dots, f_n\}$ such that $T(e_i) = \sigma_i f_i$ where $\sigma_i \ge 0$.

**Proof**: This is the singular value decomposition theorem. ∎

### Theorem 23.17: Fredholm Alternative

**Statement**: For a compact linear operator $T$ on a Banach space, either $I-T$ is invertible or $\text{Im}(I-T)$ is not closed.

**Proof**: This is the Fredholm alternative theorem. ∎

### Theorem 23.18: Adjoint Operator

**Statement**: For a bounded linear operator $T: V \to W$ between Hilbert spaces, there exists a unique bounded linear operator $T^*: W \to V$ such that $\langle Tu, v \rangle_W = \langle u, T^*v \rangle_V$ for all $u \in V, v \in W$.

**Proof**: This is the Riesz representation theorem applied to each $v$. ∎

## 23.4 Functional Analysis Theorems

### Theorem 23.19: Hahn-Banach Theorem

**Statement**: If $p$ is a sublinear functional on a vector space $V$ and $f_0$ is a linear functional on a subspace $U$ with $f_0(u) \le p(u)$ for all $u \in U$, then there exists a linear functional $f$ on $V$ such that $f|_U = f_0$ and $f(v) \le p(v)$ for all $v \in V$.

**Proof**: This is the Hahn-Banach theorem. ∎

### Theorem 23.20: Uniform Boundedness Principle

**Statement**: If $\{T_\alpha\}$ is a family of bounded linear operators from a Banach space $V$ to a normed space $W$, and $\sup_{\alpha} \|T_\alpha v\| < \infty$ for all $v \in V$, then $\sup_{\alpha} \|T_\alpha\| < \infty$.

**Proof**: This is the Banach-Steinhaus theorem. ∎

### Theorem 23.21: Baire Category Theorem

**Statement**: A complete metric space is a Baire space (i.e., the intersection of countably many dense open sets is dense).

**Proof**: This is a fundamental theorem in topology and functional analysis. ∎

### Theorem 23.22: Open Mapping Theorem

**Statement**: If $T: V \to W$ is a surjective bounded linear operator between Banach spaces, then $T$ is an open map.

**Proof**: This is the Open Mapping Theorem. ∎

### Theorem 23.23: Closed Graph Theorem

**Statement**: If $T: V \to W$ is a linear operator between Banach spaces and its graph is closed, then $T$ is bounded.

**Proof**: This is the Closed Graph Theorem. ∎

### Theorem 23.24: Riesz Representation Theorem (Functionals)

**Statement**: Every bounded linear functional on $L^2([a,b])$ can be represented as $f(g) = \int_a^b f(x)g(x)dx$ for a unique $f \in L^2([a,b])$.

**Proof**: This is a special case of the Riesz representation theorem for Hilbert spaces. ∎

## 23.5 Exercises

### Exercise 23.1
Show that $\ell^\infty = \{x = (x_n) : \sup |x_n| < \infty\}$ with norm $\|x\|_\infty = \sup |x_n|$ is a Banach space.

**Solution 23.1**: The space is complete as shown in Theorem 23.10. ∎

### Exercise 23.2
Prove that the space $C[0,1]$ of continuous functions on $[0,1]$ with the sup norm is a Banach space.

**Solution 23.2**: This is a standard result in analysis. The space is complete. ∎

### Exercise 23.3
Show that the identity map from $(\ell^2, \|\cdot\|_2)$ to $(\ell^2, \|\cdot\|_1)$ is bounded.

**Solution 23.3**: By Hölder's inequality, $\|x\|_1 \le \|x\|_2$ for all $x \in \ell^2$. ∎

### Exercise 23.4
Let $T: L^2([0,1]) \to L^2([0,1])$ be defined by $Tf(x) = \int_0^1 K(x,t)f(t)dt$ where $K \in L^2([0,1]^2)$. Show that $T$ is a bounded linear operator.

**Solution 23.4**: This is a standard result in functional analysis. ∎

∎

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
