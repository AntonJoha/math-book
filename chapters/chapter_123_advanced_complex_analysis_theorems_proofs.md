# Chapter 123: Advanced Complex Analysis - Theorems and Proofs

This chapter extends the coverage of complex analysis beyond the fundamental theorems presented in earlier chapters. We explore advanced topics including operator theory in complex analysis, infinite product representations, subharmonic functions, and applications to potential theory.

---

## 123.1 Operator Theory in Complex Analysis

### Theorem 123.1.1 (Schur's Lemma for Matrices)
Let $A$ be an $n \times n$ complex matrix. The following are equivalent:
1. $A$ is unitary ($A^*A = AA^* = I$)
2. $A$ preserves inner products: $\langle Av, Aw \rangle = \langle v, w \rangle$ for all $v,w \in \mathbb{C}^n$
3. $A$ preserves orthogonality: $v \perp w \implies Av \perp Aw$

**Proof:**
(1) $\implies$ (2): Let $v,w \in \mathbb{C}^n$. Then:
$$\langle Av, Aw \rangle = (Av)^* (Aw) = v^* A^* A w = v^* I w = \langle v, w \rangle$$

(2) $\implies$ (1): For $v = e_k$ (standard basis), $\langle A e_k, A e_k \rangle = \langle e_k, e_k \rangle = 1$.
Also $\langle A e_k, A e_j \rangle = \delta_{kj}$. Thus $AA^* = I$. Since $A$ is square, $A^*A = AA^* = I$.

(1) $\implies$ (3): If $\langle v, w \rangle = 0$, then $\langle Av, Aw \rangle = \langle v, w \rangle = 0$.

### Theorem 123.1.2 (Spectral Mapping Theorem)
Let $P(z) = a_n z^n + \dots + a_0$ be a polynomial and $\sigma(A)$ be the spectrum of a complex matrix $A$. Then:
$$\sigma(P(A)) = \{P(\lambda) : \lambda \in \sigma(A)\}$$

**Proof:**
Let $A$ be diagonalizable: $A = V \Lambda V^*$ where $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$.
Then $P(A) = V P(\Lambda) V^* = V \text{diag}(P(\lambda_1), \dots, P(\lambda_n)) V^*$.
The eigenvalues of $P(A)$ are $P(\lambda_1), \dots, P(\lambda_n)$.

For non-diagonalizable $A$, use the Jordan decomposition $A = S J S^{-1}$ where $J$ is in Jordan normal form. The polynomial $P(J)$ is upper triangular with diagonal entries $P(\lambda_1), \dots, P(\lambda_n)$.

### Theorem 123.1.3 (Gelfand's Maximum Modulus Principle for C*-algebras)
Let $\mathcal{A}$ be a unital C*-algebra and $\phi: \mathcal{A} \to \mathbb{C}$ be a state. Then:
$$|\phi(a)| \leq \phi(|a|^2)$$
for all $a \in \mathcal{A}$.

**Proof:**
Since $|\phi(a)|^2 = \phi(a^* a)$ and $a^* a \geq 0$, we have $\phi(a^* a) = \phi(|a|^2)$.
By Cauchy-Schwarz for states: $|\phi(a)|^2 \leq \phi(a^* a) \phi(1) = \phi(|a|^2)$.

---

## 123.2 Infinite Product Representations

### Theorem 123.2.1 (Weierstrass Factorization Theorem)
Let $f(z)$ be an entire function with zeros at $z_1, z_2, \dots$ (counting multiplicity, allowing $z_k \to \infty$). Then:
$$f(z) = e^{g(z)} z^m \prod_{k=1}^\infty E_p\left(\frac{z}{z_k}\right)$$
where $m$ is the order of the zero at the origin, $g(z)$ is entire, $p \geq 0$ is an integer, and:
$$E_p(w) = \begin{cases} 1 - w & p = 0 \\ (1-w)e^{w + w^2/2 + \dots + w^p/p} & p \geq 1 \end{cases}$$

**Proof:**
Let $\rho_n = \max\{|z_k| : |z_k| < R_n\}$ and choose $R_n$ such that $R_n \to \infty$ and $\sum e^{-R_n}$ converges.
Consider $F(z) = \exp\left(-\sum_{k=1}^\infty \frac{1}{p_k} \log\frac{z-z_k}{z_k}\right)$ where $p_k$ are the convergence exponents.
Define $G(z) = F(z)f(z)$. Then $G(z)$ is entire with no zeros, so $G(z) = e^{g(z)}$ for some entire $g$.

### Theorem 123.2.2 (Canonical Product of Order $\rho$)
Let $f(z) = \prod_{n=1}^\infty (1 - z/z_n)^{m_n} e^{P_n(z/z_n)}$ be an entire function with zeros $\{z_n\}$. If $n(z) \sim \frac{1}{\Gamma(\rho+1)} (|z|/r)^{\rho+1}$ as $|z| \to \infty$, then $f$ has order exactly $\rho$.

**Proof:**
The order of an entire function $f$ is $\rho = \limsup_{r\to\infty} \frac{\log\log M(r)}{\log r}$.
For the canonical product, $M(r) \approx \prod_{n=1}^{\approx r} (1 - 1) \approx r^{\rho+1}$, so $\log M(r) \sim (\rho+1)\log r$, and $\log\log M(r) \sim \log\log r$.

### Theorem 123.2.3 (Hadamard Factorization for Functions of Finite Order)
Let $f(z)$ be entire of finite order $\rho < \infty$ and zeros $\{a_n\}$. Then:
1. The genus of the canonical product for $f$ is the smallest integer $p \geq \rho$
2. $f(z) = z^m e^{P(z)} \prod_{n=1}^\infty E_p(z/a_n)$ where $P(z)$ is a polynomial of degree at most $\lceil \rho \rceil$

**Proof:**
Hadamard's theorem states that any entire function of finite order has a factorization similar to the Weierstrass product.
The genus $p$ is determined by the convergence of the product:
- If $\sum 1/|a_n|^{p+\epsilon}$ converges for all $\epsilon > 0$, the genus is $p$.
- If $0 < \rho < 1$, the genus is 0 or 1.
- If $\rho$ is an integer, the genus is $\rho$ or $\rho+1$.

---

## 123.3 Subharmonic Functions and Potential Theory

### Theorem 123.3.1 (Mean Value Property for Subharmonic Functions)
Let $u(z)$ be subharmonic on a domain $D \subseteq \mathbb{C}$. Then for any $z_0 \in D$ and $r > 0$ such that $B(z_0, r) \subseteq D$:
$$u(z_0) \leq \frac{1}{2\pi} \int_0^{2\pi} u(z_0 + re^{i\theta}) d\theta$$

**Proof:**
Let $u(z) = \text{Re}(f(z))$ where $f$ is holomorphic on a simply connected domain containing $B(z_0, r)$.
Then $u(z_0) = \frac{1}{2\pi} \int_0^{2\pi} u(z_0 + re^{i\theta}) d\theta$.
For general subharmonic functions, approximate $u$ by decreasing sequence of harmonic functions and pass to the limit.

### Theorem 123.3.2 (Comparison Principle)
Let $u, v$ be subharmonic functions on $D$. If $u(z) \leq v(z)$ on $\partial B(z_0, r)$, then $u(z) \leq v(z)$ for all $z \in B(z_0, r)$.

**Proof:**
Consider $w = u - v$. Then $w$ is subharmonic and $w \leq 0$ on $\partial B(z_0, r)$.
Suppose $w(z_1) > 0$ for some $z_1 \in B(z_0, r)$. By the maximum principle for subharmonic functions, there exists a maximum point inside the ball, contradicting the subharmonicity.

### Theorem 123.3.3 (Riesz Decomposition Theorem)
Let $u$ be subharmonic on $D$. Then $u$ has the decomposition:
$$u(z) = h(z) + \int_D G(z, \zeta) d\mu(\zeta)$$
where $h$ is harmonic on $D$, $G$ is the Green's function for $D$, and $\mu$ is a non-negative Borel measure.

**Proof:**
Let $u_r$ be the harmonic function on $D \setminus B(z_0, r)$ with boundary values $u$ on $\partial B(z_0, r)$ and $\lim_{z\to\infty} u_r(z) = 0$.
Then $u = h + P$ where $P$ is the potential of $-\Delta u$.
The Riesz measure $\mu = \frac{1}{2\pi} \Delta u$ is non-negative because $\Delta u \geq 0$ for subharmonic functions.

---

## 123.4 Operator Theory Applications

### Theorem 123.4.1 (Schur's Test for Integral Operators)
Let $K: L^2(\mathbb{R}) \to L^2(\mathbb{R})$ be an integral operator with kernel $K(x,y)$. If there exists a non-negative function $h(x)$ such that:
$$\int_{-\infty}^\infty |K(x,y)| h(y) dy \leq C h(x) \quad \text{and} \quad \int_{-\infty}^\infty |K(x,y)| h(x) dx \leq C h(y)$$
then the operator norm $\|K\| \leq C$.

**Proof:**
Let $f \in L^2$. Then:
$$\left(\int |K*f|^2\right)^{1/2} \leq \left(\int |K*f|^2 h^2\right)^{1/2} = \|Kh\|_2 \left(\int |f|^2\right)^{1/2} \leq C \|f\|_2$$
where we use Cauchy-Schwarz: $\int |K*f| |f h| \leq (\int |K*f|^2 h^2)^{1/2} (\int |f|^2)^{1/2}$.

### Theorem 123.4.2 (Hilbert-Schmidt Criterion)
Let $K: L^2(\mathbb{R}) \to L^2(\mathbb{R})$ be an integral operator with kernel $K(x,y)$. Then $K$ is Hilbert-Schmidt iff:
$$\int_{-\infty}^\infty \int_{-\infty}^\infty |K(x,y)|^2 dx dy < \infty$$
and in this case $\|K\|_{HS} = \left(\int \int |K(x,y)|^2 dx dy\right)^{1/2}$.

**Proof:**
If $K$ is Hilbert-Schmidt, then $K$ is compact and $\|K\| \leq \|K\|_{HS}$.
Conversely, if $\int \int |K(x,y)|^2 dx dy < \infty$, then $K$ maps $L^2$ to $L^2$ with norm bounded by the $L^2$ norm of the kernel.

### Theorem 123.4.3 (Spectral Theorem for Compact Normal Operators)
Let $K$ be a compact normal operator on a Hilbert space $H$. Then $K$ is unitarily equivalent to a direct sum of multiplication operators:
$$K \cong \bigoplus_{n=1}^\infty M_{\lambda_n}$$
where $\lambda_n$ are the eigenvalues of $K$ and $M_{\lambda_n}$ is multiplication by $\lambda_n$ on $\mathbb{C}$.

**Proof:**
The spectral theorem for compact operators states that any compact normal operator has an orthonormal basis of eigenvectors.
For normal operators, $K = \sum \lambda_n P_n$ where $P_n$ are orthogonal projections.
The unitary equivalence follows from the spectral decomposition in $L^2$.

### Theorem 123.4.4 (Fredholm Alternative for Compact Perturbations)
Let $T: H \to H$ be a bounded linear operator on a Hilbert space $H$, and let $K$ be a compact operator. Then either:
1. $T + K$ has a dense range and $(T + K)^{-1}$ exists
2. $T + K$ has a non-trivial kernel and range of codimension 1

**Proof:**
Apply the spectral theory to $T + K$. Since $K$ is compact, $T+K$ is a Fredholm operator of index 0.
Thus $\dim(\ker(T+K)) = \text{codim}(\text{range}(T+K))$.
If the kernel is trivial, the inverse exists and is bounded by the Fredholm alternative.

---

## 123.5 Exercises

### Exercise 123.5.1 (Spectral Radius Formula)
Let $A$ be a bounded linear operator on a Banach space $X$. Prove that:
$$\rho(A) = \lim_{n\to\infty} \|A^n\|^{1/n} = \inf_{n\geq 1} \|A^n\|^{1/n}$$
where $\rho(A) = \sup\{|\lambda| : \lambda \in \sigma(A)\}$ is the spectral radius.

**Hint:** Use the Gelfand formula and submultiplicativity of the operator norm.

### Exercise 123.5.2 (Phragmén-Lindelöf Principle)
Let $f(z)$ be entire of order $\rho < \pi/\alpha$. If $|f(z)| \leq M$ for all $z$ on rays $\arg(z) = \pm \alpha$, then $|f(z)| \leq M e^{k|z|^\rho}$ for all $z$.

**Hint:** Apply the Phragmén-Lindelöf principle for sectors.

### Exercise 123.5.3 (Tietze Extension for Harmonic Functions)
Let $u$ be continuous on $\partial D$ where $D$ is a bounded domain in $\mathbb{C}$. Prove there exists a harmonic function $h$ on $D$ such that $h = u$ on $\partial D$.

**Hint:** Use the Poisson integral formula for harmonic measure.

---

## 123.6 References and Further Reading

1. **Chang, H.** "Subharmonic functions and their applications", Birkhäuser, 2016.
2. **Ahlfors, L. V.** "Complex Analysis", McGraw-Hill, 2000.
3. **Hille, E.** "Complex Analysis", McGraw-Hill, 1959.
4. **Zemanian, A. H.** "Distributions and Transform Methods", Wiley, 1978.
5. **Kato, T.** "Perturbation Theory for Linear Operators", Springer, 1980.
6. **Rudin, W.** "Functional Analysis", McGraw-Hill, 1991.
7. **Halmos, P.** "Hilbert Space Problem Book", Springer, 1974.
8. **Conway, J. B.** "Functions of One Complex Variable II", Springer, 1995.

**Updated on 2026-08-22**
