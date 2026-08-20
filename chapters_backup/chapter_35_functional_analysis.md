# Chapter 35: Functional Analysis

## 35.1 Introduction to Functional Analysis

Functional analysis is a branch of mathematical analysis that generalizes the notion of functions and spaces between which functions are defined and which theorems in analysis can be proved using them. It studies vector spaces equipped with additional structure, particularly normed vector spaces, Banach spaces, and Hilbert spaces.

**Definition**: A **functional space** is a vector space where elements are themselves functions, or more generally, elements of infinite-dimensional spaces equipped with a topology or norm.

**Theorem 35.1**: The space of continuous functions on a closed interval $[a, b]$ with the sup-norm is a Banach space.

**Proof**: Consider $C([a, b])$ with $\|f\|_\infty = \sup_{x \in [a, b]} |f(x)|$. For any Cauchy sequence $\{f_n\}$ in $C([a, b])$, the uniform limit exists and is continuous. ∎

## 35.2 Normed Vector Spaces

**Definition**: A **normed vector space** is a pair $(V, \|\cdot\|)$ where $V$ is a vector space and $\|\cdot\|: V \to [0, \infty)$ is a norm satisfying:
1. $\|x\| \ge 0$ for all $x \in V$, with $\|x\| = 0 \iff x = 0$
2. $\|\alpha x\| = |\alpha| \|x\|$ for all $\alpha \in \mathbb{R}$ (or $\mathbb{C}$)
3. $\|x + y\| \le \|x\| + \|y\|$ (triangle inequality)

**Theorem 35.2**: Every normed vector space is a metric space with metric $d(x, y) = \|x - y\|$.

**Proof**: The triangle inequality for norms implies $d(x, z) \le d(x, y) + d(y, z)$, making it a metric. ∎

**Theorem 35.3 (Riesz Lemma)**: Let $V$ be a normed vector space and $W$ a proper subspace of $V$. Then for every $\epsilon > 0$, there exists $x \in V$ such that $\|x\| = 1$ and $\text{dist}(x, W) > 1 - \epsilon$.

**Proof**: The proof uses the fact that the unit sphere is not contained in any finite-dimensional subspace of an infinite-dimensional space. ∎

## 35.3 Banach Spaces

**Definition**: A **Banach space** is a complete normed vector space.

**Theorem 35.4 (Banach-Steinhaus Theorem / Uniform Boundedness Principle)**: Let $X$ be a Banach space and $\{T_n\}$ a family of continuous linear operators from $X$ to a normed space $Y$. If $\{T_n(x)\}$ is bounded for each $x \in X$, then $\sup_n \|T_n\| < \infty$.

**Proof**: Suppose $\{T_n\}$ is not uniformly bounded. Then there exists $x_n \in X$ with $\|x_n\| \le 1$ such that $\|T_n(x_n)\| > n$. By Baire Category Theorem, there exists a closed ball $B$ of radius $\epsilon$ where $\sup_n \|T_n\| < \infty$. This leads to a contradiction. ∎

**Theorem 35.5**: If $X$ and $Y$ are Banach spaces and $T: X \to Y$ is a continuous linear bijection, then $T^{-1}: Y \to X$ is continuous (Open Mapping Theorem).

**Proof**: The Open Mapping Theorem states that any surjective bounded linear operator between Banach spaces is an open map. Since $T$ is bijective, $T^{-1}$ is continuous. ∎

## 35.4 Dual Spaces

**Definition**: The **dual space** $V^*$ of a normed space $V$ is the space of all continuous linear functionals on $V$. Each $f \in V^*$ can be viewed as a function $V \to \mathbb{R}$ (or $\mathbb{C}$).

**Theorem 35.6 (Riesz Representation Theorem for Hilbert Spaces)**: Every continuous linear functional $f$ on a Hilbert space $H$ has the form $f(x) = \langle x, y \rangle$ for a unique $y \in H$.

**Proof**: This is the core of the Riesz representation theorem. For each $f \in H^*$, define $y = \{z \in H : f(z) = \langle z, y \rangle \}$. Then $\|f\| = \|y\|$. ∎

**Theorem 35.7 (Hahn-Banach Theorem)**: Let $X$ be a real normed vector space and $p: X \to \mathbb{R}$ a sublinear functional. Then for any $x_0 \in X$ and $r < p(x_0)$, there exists a linear functional $f: X \to \mathbb{R}$ such that $f(x_0) = r$ and $f(x) \le p(x)$ for all $x \in X$.

**Corollary 35.1**: For every $x \in X$ with $\|x\| = 1$, there exists $f \in X^*$ such that $f(x) = \|x\| = 1$ and $\|f\| = 1$.

**Corollary 35.2**: $X^{**}$ (the dual of $X^*$) always contains a copy of $X$ via the canonical embedding $x \mapsto \hat{x}$ where $\hat{x}(f) = f(x)$.

## 35.5 Hilbert Spaces

**Definition**: A **Hilbert space** is a complete inner product space.

**Theorem 35.8 (Orthogonal Decomposition Theorem)**: If $H$ is a Hilbert space and $M$ is a closed subspace of $H$, then $H = M \oplus M^\perp$.

**Proof**: For any $x \in H$, define $p_M(x)$ as the unique point in $M$ minimizing $\|x - m\|$. The orthogonal complement $M^\perp = \{y \in H : \langle y, m \rangle = 0 \forall m \in M\}$ satisfies $H = M \oplus M^\perp$. ∎

**Theorem 35.9**: A subset $K$ of a Hilbert space $H$ is closed if and only if it is complete under the metric induced by the norm.

**Proof**: This follows from the characterization of complete metric spaces. ∎

## 35.6 Compact Operators

**Definition**: A bounded linear operator $T: X \to Y$ between Banach spaces is **compact** if for every bounded sequence $\{x_n\} \subseteq X$, the sequence $\{Tx_n\}$ has a convergent subsequence in $Y$.

**Theorem 35.10**: If $T: X \to Y$ is a compact operator and $Y$ is infinite-dimensional, then the image $T(X)$ cannot contain a basis for $Y$.

**Proof**: Since $T(X)$ is the continuous image of a compact set, it is relatively compact. An infinite-dimensional Banach space cannot have a compact open subset. ∎

**Theorem 35.11 (Fredholm Alternative)**: Let $T: H \to H$ be a bounded linear operator on a Hilbert space. Then either:
1. $T - \lambda I$ is bijective for some $\lambda$, or
2. The equation $(T - \lambda I)x = y$ has solutions for $y \in \text{range}(T - \lambda I)$ only if $y \perp \ker(T^* - \bar{\lambda} I)$.

## 35.7 Spectral Theory

**Definition**: The **spectrum** $\sigma(T)$ of a bounded linear operator $T$ on a Banach space $X$ is the set of complex numbers $\lambda$ such that $T - \lambda I$ is not invertible.

**Theorem 35.12 (Spectral Radius Formula)**: For any bounded operator $T$ on a Banach space $X$, the spectral radius $r(T) = \lim_{n \to \infty} \|T^n\|^{1/n}$.

**Proof**: The spectral radius formula follows from the properties of the resolvent set and the fact that $\sigma(T)$ is bounded by $R(T)$. ∎

**Theorem 35.13**: If $T$ is a normal operator on a Hilbert space $H$, then $T$ is unitarily equivalent to a multiplication operator $M_\phi$ on $L^2(\mu)$ for some measure $\mu$ and function $\phi$.

## 35.8 Dual and Bidual Spaces

**Theorem 35.14**: For any normed space $X$, the canonical embedding $J: X \to X^{**}$ defined by $J(x)(f) = f(x)$ is isometric.

**Proof**: $\|J(x)\| = \sup_{\|f\|=1} |f(x)| = \|x\|$ by the Hahn-Banach theorem. ∎

**Theorem 35.15 (Goldstine's Theorem)**: If $X$ is a normed space and $J(X)$ is dense in $X^{**}$, then $X$ is not reflexive.

## 35.9 Applications

### 35.9.1 Partial Differential Equations

Functional analysis provides the framework for studying partial differential equations. Many PDEs can be reformulated as operator equations in function spaces.

### 35.9.2 Quantum Mechanics

Hilbert spaces provide the mathematical foundation for quantum mechanics. States are vectors in a Hilbert space, and observables are self-adjoint operators.

### 35.9.3 Signal Processing

$L^2$ spaces (square-integrable functions) are central to signal processing and Fourier analysis.

## Exercises

### Exercise 35.1
Prove that $C^1([a, b])$ with the norm $\|f\|_{C^1} = \max(|f|_\infty, |f'|_\infty)$ is a Banach space.

### Exercise 35.2
Show that $L^2([a, b])$ is a Hilbert space.

### Exercise 35.3
Prove that the identity operator on an infinite-dimensional Banach space is not compact.

### Exercise 35.4
Show that the dual of $c_0$ (sequences converging to 0) is $\ell_1$.

### Exercise 35.5
Prove the spectral radius formula for a bounded operator on a Banach space.

∎
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*