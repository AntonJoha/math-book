# Chapter 111: Differential Geometry - Comprehensive Theorems and Proofs

## 111.1 Curves in Euclidean Space

### Theorem 111.1.1 (Frenet-Serret Formulas)
Let $\alpha: I \to \mathbb{R}^3$ be a $C^3$ regular curve with non-zero curvature $\kappa(s)$ everywhere. Let $T(s), N(s), B(s)$ be the Frenet frame (tangent, normal, binormal). Then:
$$\frac{dT}{ds} = \kappa(s) N(s), \quad \frac{dN}{ds} = -\kappa(s) T(s) + \tau(s) B(s), \quad \frac{dB}{ds} = -\tau(s) N(s)$$

### Theorem 111.1.2 (Fundamental Theorem of Space Curves)
A regular curve $\alpha: I \to \mathbb{R}^3$ is determined up to rigid motion by its curvature $\kappa(s)$ and torsion $\tau(s)$ functions.

**Proof**: Given $\kappa, \tau$, construct the Frenet frame and integrate the Frenet equations. The resulting curve satisfies the given curvature and torsion. Rigid motion uniqueness follows from the definition of rigid motions.

### Theorem 111.1.3 (Total Curvature)
The total curvature of a closed curve $\alpha: S^1 \to \mathbb{R}^3$ satisfies:
$$\int_0^L \kappa(s) \, ds \geq 2\pi$$

**Proof**: Follows from the winding number interpretation of curvature.

## 111.3: Advanced Differential Geometry Theorems

### Theorem 111.3.1 (Hitchin's Equation for Integrable Systems)
**Statement:** The Hitchin equations characterize the moduli space of Higgs bundles on a Riemann surface with given Chern class.

**Proof:** Using gauge theory and holomorphic bundles on curved manifolds.

### Theorem 111.3.2 (Cartan-Hadamard Theorem)
**Statement:** A simply connected complete Riemannian manifold with non-positive sectional curvature is diffeomorphic to Euclidean space.

**Proof:** Using the exponential map and properties of geodesics in non-positive curvature.

### Theorem 111.3.3 (Weitzenböck Formula)
**Statement:** For a Dirac operator D on a Riemannian manifold M, the square D² equals the connection Laplacian plus terms involving curvature.

**Proof:** Using local coordinates and Clifford algebra properties.

## 111.2 Surfaces in Euclidean Space

### Theorem 111.2.1 (First and Second Fundamental Forms)
Let $S \subset \mathbb{R}^3$ be a smooth surface parametrized by $\mathbf{x}(u,v)$. The first fundamental form is $I = E \, du^2 + 2F \, du \, dv + G \, dv^2$ where $E = \mathbf{x}_u \cdot \mathbf{x}_u$, etc. The second fundamental form is $II = e \, du^2 + 2f \, du \, dv + g \, dv^2$ where $e = \mathbf{x}_{uu} \cdot \mathbf{n}$, with $\mathbf{n}$ the unit normal.

### Theorem 111.2.2 (Mean Curvature)
The mean curvature $H$ of a surface is given by $H = \frac{eG - 2fg + Ef}{2EG - 2F^2}$ (using the appropriate formula). Alternatively, $H = \frac{1}{2}(\kappa_1 + \kappa_2)$ where $\kappa_1, \kappa_2$ are the principal curvatures.

### Theorem 111.2.3 (Gaussian Curvature)
The Gaussian curvature $K$ of a surface is given by $K = \frac{eg - f^2}{EG - F^2}$. It is also equal to the product of principal curvatures: $K = \kappa_1 \kappa_2$.

## 111.4 Minimal Surfaces

### Theorem 111.4.1 (Hypothesis for Minimal Surfaces)
A surface $S$ is minimal (i.e., has mean curvature $H = 0$ everywhere) if and only if its mean curvature vector field vanishes identically.

### Theorem 111.4.2 (Existence of Minimal Surfaces)
For any boundary curve $\Gamma$ in $\mathbb{R}^3$, there exists a minimal surface with boundary $\Gamma$.

**Proof**: Use the Dirichlet principle and the method of descent for minimal surfaces.

### Theorem 111.4.3 (Weierstrass-Enneper Representation)
Every minimal surface can be represented locally as the real part of a Weierstrass-Enneper integral:
$$\mathbf{x}(z) = \text{Re} \int \left( (1 - \wp(z)) \, dz, i(1 + \wp(z)) \, dz, (1 - \wp(z)^2) \, dz \right)$$
where $\wp(z)$ is a meromorphic function.

## 111.5 Isometric Embeddings

### Theorem 111.5.1 (Nash-Kuiper Theorem)
Every $C^0$-isometric embedding of a compact Riemannian manifold into Euclidean space exists, although the embedding may not be $C^1$-smooth.

**Proof**: This deep result uses stability theory for $C^0$-isometries and the fact that $C^0$-isometries between Riemannian manifolds are determined by their first fundamental forms.

### Theorem 111.5.2 (Nash Embedding Theorem)
Every smooth compact Riemannian manifold $(M, g)$ can be isometrically embedded into some $\mathbb{R}^N$.

**Proof**: Let $\dim(M) = m$. Then there exists an embedding into $\mathbb{R}^{2m+2m(m+1)/2 + 1}$. The proof uses approximation and deformation techniques.

### Theorem 111.5.3 (Cohn-Vossen Theorem)
Every complete, simply connected, non-positively curved surface in $\mathbb{R}^3$ is the plane.

**Proof**: Follows from the properties of curvature and the uniqueness of the Euclidean plane.

## 111.6 Geodesics

### Theorem 111.6.1 (Geodesic Equation)
A curve $\gamma(t)$ is a geodesic on a Riemannian manifold $(M, g)$ if and only if it satisfies the geodesic equation:
$$\nabla_{\dot{\gamma}} \dot{\gamma} = 0$$
where $\nabla$ is the Levi-Civita connection.

### Theorem 111.6.2 (Geodesics as Local Minima)
Geodesics are locally length-minimizing curves.

**Proof**: Use the second variation formula for the length functional.

### Theorem 111.6.3 (Bishop-Gromov Inequality)
For a complete Riemannian manifold with sectional curvature bounded above by $K$, the volume of geodesic balls satisfies:
$$\text{Vol}(B(p, r)) \leq \text{Vol}_{\mathbb{R}^n}(B_{\mathbb{R}^n}(0, r))$$

## 111.7 Curvature of Submanifolds

### Theorem 111.7.1 (Euler Characteristic and Gauss-Bonnet)
For a compact, oriented, smooth surface $S \subset \mathbb{R}^3$:
$$\int_S K \, dA = 2\pi \chi(S)$$
where $\chi(S)$ is the Euler characteristic.

### Theorem 111.7.2 (Hermann's Theorem)
A complete surface in $\mathbb{R}^3$ with constant positive Gaussian curvature is a sphere, and one with constant negative Gaussian curvature is not possible in $\mathbb{R}^3$.

### Theorem 111.7.3 (Alexandrov's Theorem)
The only compact, strictly convex surface in $\mathbb{R}^3$ with constant principal curvature is a sphere.

## 111.8 Comparison Theorems

### Theorem 111.8.1 (Myers' Theorem)
If $M$ is a complete Riemannian manifold with Ricci curvature bounded below by a positive constant $K > 0$, then the diameter of $M$ is bounded above by $\pi/\sqrt{K}$.

**Proof**: Use the Bishop-Gromov volume comparison theorem and the fact that geodesic balls of radius $\pi/\sqrt{K}$ in the model space of constant curvature $K$ are not isometric.

### Theorem 111.8.2 (Cartan-Hadamard Theorem)
A simply connected, complete Riemannian manifold with non-positive sectional curvature is diffeomorphic to $\mathbb{R}^n$.

**Proof**: The exponential map at any point is a diffeomorphism from $T_p M$ to $M$.

### Theorem 111.8.3 (Toponogov's Theorem)
For a complete Riemannian manifold $M$ with sectional curvature bounded above by $K$, and geodesic $\gamma$ of length $l$, any comparison triangle in the space form of constant curvature $K$ satisfies:
$$d(\gamma(t_1), \gamma(t_2))^2 \leq d(\tilde{\gamma}(t_1), \tilde{\gamma}(t_2))^2 + o(l^2)$$

## 111.9 Isometries and Symmetries

### Theorem 111.9.1 (Lie Group of Isometries)
The group of isometries of a complete Riemannian manifold forms a Lie group.

### Theorem 111.9.2 (Maximal Symmetry)
A Riemannian manifold of constant curvature has maximal symmetry (isometric to $\mathbb{R}^n$, the $n$-sphere, or hyperbolic space).

### Theorem 111.9.3 (Fixed Point Theorem for Isometries)
If $f: M \to M$ is an isometry of a compact Riemannian manifold $M$, then $f$ has a fixed point.

**Proof**: Use the existence of a fixed point for compact sets and properties of the action.

## 111.10 Curvature and Topology

### Theorem 111.10.1 (Gauss-Bonnet for Manifolds)
For a compact, oriented, smooth $n$-manifold $M$ with Riemannian metric $g$, let $K$ be the sectional curvature and $K_n$ the $n$-th curvature component. Then:
$$\int_M K \, d\text{vol} = 2\pi \chi(M)$$
for surfaces ($n=2$), or more generally the generalized Gauss-Bonnet formula involving integrals of curvature invariants.

### Theorem 111.10.2 (Chern-Gauss-Bonnet Theorem)
For a compact, oriented, smooth manifold $M$ of dimension $n$ with Riemannian metric $g$, the Euler characteristic is given by:
$$\chi(M) = \frac{1}{(2\pi)^{n/2}} \int_M p_n\left(\frac{R}{2}\right) \, d\text{vol}_g$$
where $p_n$ is the $n$-th Pontryagin class and $R$ is the curvature tensor.

## 111.11 Additional Proofs and Results

### Proof of Gauss-Bonnet Theorem Sketch
The proof uses local triangulation, the relation between curvature and angle deficits, and the combinatorial Euler characteristic of the triangulation.

### Proof of Chern-Gauss-Bonnet Sketch
This proof uses differential forms, the Pontryagin classes, and the characteristic classes of the tangent bundle.

*Updated on 2026-06-10*