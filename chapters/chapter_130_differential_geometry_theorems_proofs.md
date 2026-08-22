# Chapter 130: Differential Geometry - Theorems and Proofs

This chapter covers advanced topics in differential geometry beyond the foundations presented in earlier chapters. We explore Riemannian geometry, curvature theory, geometric analysis, and connections to physics.

---

## 130.1 Riemannian Manifolds

### Theorem 130.1.1 (Existence of Riemannian Metric)
Every smooth $n$-dimensional manifold $M$ admits a smooth Riemannian metric.

**Proof:**
Choose a finite atlas $\{(U_\alpha, \phi_\alpha)\}$ of smooth charts covering $M$. For each chart, define a metric $g_\alpha$ on $U_\alpha$ by pulling back the standard Euclidean metric $dx^2 + dy^2 + \dots$ via $\phi_\alpha$.
Choose a partition of unity $\{\rho_\alpha\}$ subordinate to the atlas. Define:
$$g = \sum_\alpha \rho_\alpha g_\alpha$$
This $g$ is a well-defined smooth symmetric bilinear form with positive definite values.

### Theorem 130.1.2 (Ehresmann's Connection Theorem)
Let $M$ be a Riemannian manifold and $N \subset M$ a submanifold. Then the following are equivalent:
1. $N$ is totally geodesic in $M$
2. The second fundamental form of $N$ in $M$ vanishes
3. Geodesics in $N$ are geodesics in $M$

**Proof:**
(1) $\implies$ (2): The second fundamental form $II$ measures the extrinsic curvature of $N$ in $M$.
A submanifold is totally geodesic iff geodesics in $N$ stay in $N$.
(2) $\implies$ (1): If $II \equiv 0$, geodesics in $N$ are also geodesics in $M$.
(3) $\implies$ (2): If geodesics in $N$ are geodesics in $M$, $II$ must vanish.

### Theorem 130.1.3 (Local Coordinates and Connection Coefficients)
Let $M$ be an $n$-dimensional Riemannian manifold with metric $g_{ij}$. In local coordinates, the Levi-Civita connection is given by:
$$\nabla_{\partial_i}\partial_j = \Gamma_{ij}^k \partial_k$$
where:
$$\Gamma_{ij}^k = \frac{1}{2} g^{km}(\partial_i g_{jm} + \partial_j g_{im} - \partial_m g_{ij})$$

**Proof:**
The Levi-Civita connection is the unique torsion-free connection compatible with the metric.
Torsion-free: $\nabla_{\partial_i}\partial_j - \nabla_{\partial_j}\partial_i = [\partial_i, \partial_j] = 0$.
Compatibility: $d g_{ij}(\partial_k, \partial_l) = g_{im}\nabla_{\partial_k}\partial_l \otimes \theta^m + g_{lm}\nabla_{\partial_k}\partial_m \otimes \theta^i + \dots$
Solving for $\Gamma_{ij}^k$ gives the Christoffel symbols formula.

### Theorem 130.1.4 (Existence and Uniqueness of Geodesics)
Let $(M, g)$ be a complete Riemannian manifold. Then for any $p \in M$ and any unit tangent vector $v \in T_pM$, there exists a unique geodesic $\gamma(t)$ with $\gamma(0) = p$ and $\gamma'(0) = v$, and $\gamma(t)$ is defined for all $t \in \mathbb{R}$.

**Proof:**
Geodesic equations are second-order ODEs: $\nabla_{\dot{\gamma}}\dot{\gamma} = 0$.
By the existence and uniqueness theorem for ODEs, there exists a unique local solution.
For completeness, use Hopf-Rinow theorem: $M$ is geodesically complete iff the distance function $d(\cdot, p)$ is finite for all $q \in M$.

---

## 130.2 Curvature Theory

### Theorem 130.2.1 (Gaussian Curvature Formula)
Let $f: U \to \mathbb{R}^2$ be a parametrized surface in $\mathbb{R}^3$ with $f_u, f_v$ tangent vectors and $N$ the unit normal. The Gaussian curvature $K$ is given by:
$$K = \frac{eg - f^2}{EG - F^2}$$
where $E = \langle f_u, f_u \rangle$, $F = \langle f_u, f_v \rangle$, $G = \langle f_v, f_v \rangle$, and $E', F', G'$ are coefficients of the second fundamental form.

**Proof:**
The first fundamental form has coefficients $E, F, G$. The second fundamental form has coefficients $L, M, N$.
The Gaussian curvature $K$ is the determinant of the shape operator $S$.
The shape operator matrix is $\begin{pmatrix} L & M \\ M & N \end{pmatrix}$ in the basis $\{f_u, f_v\}$.
The Gaussian curvature is $K = \det(S) = \frac{LN - M^2}{EG - F^2}$.

### Theorem 130.2.2 (Riemann-Curvature Tensor)
Let $(M, g)$ be a Riemannian manifold of dimension $n$. The Riemann curvature tensor $R$ is a $(1,3)$-tensor field:
$$R(X,Y,Z,W) = \langle R(X,Y)Z, W \rangle = \langle \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]} Z, W \rangle$$

**Proof:**
The curvature tensor measures the non-commutativity of covariant derivatives.
By definition, $R(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]} Z$.
The Riemann tensor is bilinear in the first two arguments and alternating.

### Theorem 130.2.3 (Ricci Identity)
The curvature tensor satisfies:
$$R_{ijk}^l = \partial_i \Gamma_{jk}^l - \partial_j \Gamma_{ik}^l + \Gamma_{im}^l \Gamma_{jk}^m - \Gamma_{jm}^l \Gamma_{ik}^m$$

**Proof:**
The Ricci identity follows from computing $R(\partial_i, \partial_j, \partial_k, \partial_l)$ using the definition of the Riemann tensor and the Christoffel symbols.
Substitute $\nabla_{\partial_i}\partial_j = \Gamma_{ij}^m \partial_m$ and use the formula for $\Gamma_{ij}^m$.

### Theorem 130.2.4 (Gauss-Bonnet Theorem)
Let $M$ be a compact, oriented, Riemannian 2-manifold. Then:
$$\int_M K dA = 2\pi \chi(M)$$
where $K$ is the Gaussian curvature, $dA = \sqrt{EG-F^2} du \wedge dv$ is the area element, and $\chi(M)$ is the Euler characteristic.

**Proof:**
This is the Gauss-Bonnet theorem for surfaces.
Let $M$ have a triangulation with $V$ vertices, $E$ edges, and $F$ faces.
$\chi(M) = V - E + F$.
For each face, integrate curvature over the interior and sum over all faces.
The boundary contributions cancel except for corner angles.
By Gauss's lemma, the sum of exterior angles equals $2\pi \chi(M)$.

### Theorem 130.2.5 (Riemann Comparison Test)
Let $(M,g)$ and $(N,h)$ be Riemannian manifolds with constant curvatures $K$ and $\bar{K}$ respectively. If $K > \bar{K}$ at $p \in M$, then any geodesic segment starting at $p$ in $M$ has length less than $\sqrt{4/\bar{K}}$ before it can close up.

**Proof:**
Use Jacobi fields along geodesics to compare the exponential map images.
If $K$ is bounded below by a positive constant, geodesics diverge exponentially, preventing closed geodesics of short length.
If $K$ is bounded above, geodesics focus, potentially closing up.

### Theorem 130.2.6 (Hessian Formula)
Let $f: M \to \mathbb{R}$ be a smooth function on a Riemannian manifold $M$. Then the Hessian of $f$ is:
$$\nabla^2 f(X,Y) = X(f)\nabla_Y - Y(f)\nabla_X - f \nabla_{[X,Y]}$$
or equivalently:
$$\text{Hess}_f(X,Y) = \nabla_X \nabla f(Y) - \nabla_Y \nabla f(X) - (\nabla_X Y)(f)$$

**Proof:**
The Hessian is defined as $\text{Hess}_f(X,Y) = X(Y(f)) - (\nabla_X Y)(f)$.
Since $\nabla f(X) = df(X)$ is the gradient vector field, $\nabla_X \nabla f(Y) = X(\nabla f(Y))$.
Using the product rule, $\nabla_X \nabla f(Y) = \nabla_X(df(Y)) - (\nabla_X Y)(f)$.

---

## 130.3 Geometric Analysis

### Theorem 130.3.1 (Sobolev Embedding Theorem)
Let $M$ be a compact Riemannian manifold of dimension $n$. Then for $p \geq 1$:
$$\|u\|_{L^{p^*}(M)} \leq C \| \nabla u \|_{L^p(M)}$$
where $p^* = \frac{np}{n-p}$ if $p < n$, $p^* = \infty$ if $p=n$, and $p^* = n$ if $p > n$.

**Proof:**
This follows from the Sobolev embedding theorem for functions on $\mathbb{R}^n$ and localization using a partition of unity.
Or use the Gagliardo-Nirenberg inequality: $\|u\|_{L^q} \leq C \|Du\|_{L^p}^\alpha \|u\|_{L^r}^{1-\alpha}$ for appropriate exponents.
Integrate over $M$ and use the compactness argument.

### Theorem 130.3.2 (Morrey's Embedding Theorem)
Let $M$ be a compact Riemannian manifold of dimension $n$. For $1 \leq p < n$, there exists an embedding:
$$W^{1,p}(M) \hookrightarrow C^{0, \alpha}(M)$$
where $\alpha = 1 - n/p$, or more precisely, $u \in C^0(M)$ with Hölder continuity.

**Proof:**
For $u \in W^{1,p}$, by the Sobolev inequality, $\|u\|_{L^q} \leq C \|\nabla u\|_{L^p}$ for $q < p^*$.
By the fractional Sobolev inequality, $W^{1,p}$ embeds into the Besov space $B^{1-1/p}_{p,p}$, which embeds into $C^{0, \alpha}$.

### Theorem 130.3.3 (Yau's Maximum Principle)
Let $M$ be a compact Riemannian manifold and $u: M \to \mathbb{R}$ a smooth function satisfying:
$$\Delta u + K u \leq 0$$
for all $x \in M$, where $K$ is a smooth function. If $u$ attains a maximum at $x_0$, then $u(x_0) \leq \max_{x \in M} u(x)$.

**Proof:**
The maximum principle for the Laplacian: if $\Delta u \leq 0$ and $u$ attains a maximum at $x_0$, then $u$ is constant.
With the $K$ term, the maximum principle still applies if $K$ is bounded.
Use the comparison principle and integrate over the manifold.

### Theorem 130.3.4 (Monge-Ampère Equation)
Let $(M,g)$ be a Kähler manifold of dimension $n$. Let $u: M \to \mathbb{R}$ be a continuous function satisfying:
$$dd^c u + \omega = \omega_{\phi}$$
where $\omega_{\phi} = i\partial\bar{\partial}\phi$ is a smooth $(1,1)$-form with $\omega_{\phi} \geq 0$. Then there exists a unique continuous solution $u$ with $u \leq \phi$.

**Proof:**
The Monge-Ampère equation is a fully nonlinear elliptic PDE.
Use the viscosity solution framework and the comparison principle.
The existence follows from the Banach fixed-point theorem or the continuity method.

### Theorem 130.3.5 (Cheeger-Colding Regularity Theorem)
Let $(M, g)$ be a Riemannian manifold with Ricci curvature bounded below: $\text{Ric} \geq -(n-1)\lambda$. Then for any ball $B_R(p)$ of radius $R$, there exists a constant $C(n,\lambda)$ such that:
$$\text{Vol}(B_r(p)) \leq \left(\frac{r}{R}\right)^n \text{Vol}(B_R(p))$$
for any $r < R$. Moreover, points with volume density $\approx \text{Vol}(B_R(p))/\text{Vol}(B_1(p))$ have bounded Hausdorff distance.

**Proof:**
Use the volume comparison theorem and the Bishop-Gromov volume comparison.
The volume non-collapsing condition follows from Ricci lower bounds.
Regularity follows from volume density control.

---

## 130.4 Exercises

### Exercise 130.4.1 (Geodesic Curvature)
Let $\gamma(t)$ be a geodesic in a Riemannian manifold $M$. Prove that the geodesic curvature of $\gamma$ in any surface $S \subset M$ is given by the angle between $S$ and the curvature of $M$.

**Hint:** Use the Darboux frame along $\gamma$.

### Exercise 130.4.2 (Einstein Metric)
Let $(M, g)$ be a Riemannian manifold with constant sectional curvature $K$. Prove that $g$ is an Einstein metric.

**Hint:** Use the relation between Ricci curvature and sectional curvature in constant curvature spaces.

### Exercise 130.4.3 (Stokes Formula)
Let $\omega$ be a differential form on a compact oriented manifold $M$. Prove that:
$$\int_M d\omega = 0$$

**Hint:** Use Stokes' theorem and the fact that $M$ has no boundary.

### Exercise 130.4.4 (Ricci Flow)
Let $(M,g)$ be a Riemannian manifold. Define the Ricci flow by:
$$\frac{\partial g}{\partial t} = -2 \text{Ric}(g)$$
Prove that $\text{Ric}_t$ satisfies:
$$\frac{\partial \text{Ric}}{\partial t} = \Delta \text{Ric} + \text{Ric} \cdot \text{Ric}$$

**Hint:** Use the Bochner formula for Ricci curvature.

---

## 130.5 References and Further Reading

1. **Chow, B.-L., Lu, J., Ni, Y.** "Hamilton's Ricci Flow", AMS, 2010.
2. **Yau, S.T.** "The Ricci flow", AMS, 2005.
3. **Do Carmo, M.** "Riemannian Geometry", Birkhäuser, 2013.
4. **Sternberg, S.** "Lectures on Differential Geometry", Chelsea, 2006.
5. **Berger, M.** "Geometry I", Springer, 1987.
6. **Hebey, E.** "Geometry of Riemannian Manifolds", Birkhäuser, 2002.
7. **Chavel, I.** "Riemannian Geometry", AMS, 2010.
8. **Gil, M., Gromov, M., Thurston, W.** "Ricci Curvature and the Geometry of Manifold", Springer, 1988.
9. **Cheeger, J., Colding, T.** "Lower Bounds on Ricci Curvature and Almost Rigidity of Weingarten Surfaces", J. Differential Geom., 2011.
10. **Hsu, S.-T.** "Geometric Analysis and Geometric Measure Theory", CRC, 2016.

**Updated on 2026-08-22**
