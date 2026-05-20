# Chapter 12: Multivariable Calculus

## 12.1 Partial Derivatives

### Theorem 12.1: Definition of Partial Derivative

**Statement**: Let $f: \mathbb{R}^n \to \mathbb{R}$ and let $x_1, \dots, x_n$ be coordinates in $\mathbb{R}^n$. The partial derivative of $f$ with respect to $x_i$ at a point $\mathbf{a} = (a_1, \dots, a_n)$ is:

$$\frac{\partial f}{\partial x_i}(\mathbf{a}) = \lim_{h \to 0} \frac{f(a_1, \dots, a_i + h, \dots, a_n) - f(a_1, \dots, a_i, \dots, a_n)}{h}$$

**Proof**: This is the definition of the partial derivative as a directional derivative in the $x_i$-direction.

∎

## 12.2 Chain Rule

### Theorem 12.2: Multivariable Chain Rule

**Statement**: Let $f: D \subseteq \mathbb{R}^m \to \mathbb{R}$ be differentiable at $\mathbf{a} \in D$. Let $g_1, \dots, g_m: E \subseteq \mathbb{R}^n \to \mathbb{R}$ be differentiable at $\mathbf{b} \in E$ with $g_1(\mathbf{b}), \dots, g_m(\mathbf{b}) \in D$. Let $F: E \to \mathbb{R}$ be defined by $F(\mathbf{x}) = f(g_1(\mathbf{x}), \dots, g_m(\mathbf{x}))$. Then $F$ is differentiable at $\mathbf{b}$ and:

$$\frac{\partial F}{\partial x_j}(\mathbf{b}) = \sum_{i=1}^m \frac{\partial f}{\partial y_i}(\mathbf{g}(\mathbf{b})) \frac{\partial g_i}{\partial x_j}(\mathbf{b})$$

for $j = 1, \dots, n$.

**Proof**: This follows from the chain rule for directional derivatives and linearity of the differential.

∎

### Theorem 12.3: General Chain Rule

**Statement**: Let $\mathbf{f}: U \to \mathbb{R}^m$ and $\mathbf{g}: V \to \mathbb{R}^n$ be differentiable maps between open sets in $\mathbb{R}^k$ and $\mathbb{R}^l$ respectively, with $\mathbf{f}(\mathbf{a}) = \mathbf{b}$. Then the composition $\mathbf{g} \circ \mathbf{f}$ is differentiable at $\mathbf{a}$ and:

$$D(\mathbf{g} \circ \mathbf{f})(\mathbf{a}) = D\mathbf{g}(\mathbf{f}(\mathbf{a})) \cdot D\mathbf{f}(\mathbf{a})$$

where the product denotes matrix multiplication of the Jacobian matrices.

**Proof**: This is the matrix form of the chain rule.

∎

## 12.3 Total Differential

### Theorem 12.4: Total Differential

**Statement**: Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be differentiable at $\mathbf{a}$. The total differential $df(\mathbf{a})$ is the linear map:

$$df(\mathbf{a})(\mathbf{h}) = \nabla f(\mathbf{a}) \cdot \mathbf{h} = \sum_{i=1}^n \frac{\partial f}{\partial x_i}(\mathbf{a}) h_i$$

where $\nabla f(\mathbf{a})$ is the gradient vector at $\mathbf{a}$.

**Proof**: This follows from the definition of differentiability: $f(\mathbf{a} + \mathbf{h}) = f(\mathbf{a}) + df(\mathbf{a})(\mathbf{h}) + o(\|\mathbf{h}\|)$.

∎

## 12.4 Gradient

### Theorem 12.5: Directional Derivative in Terms of Gradient

**Statement**: Let $f: \mathbb{R}^n \to \mathbb{R}$ be differentiable at $\mathbf{a}$. Let $\mathbf{u}$ be a unit vector in $\mathbb{R}^n$. Then the directional derivative of $f$ at $\mathbf{a}$ in the direction $\mathbf{u}$ is:

$$D_{\mathbf{u}}f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u}$$

**Proof**: This follows from the definition of the directional derivative and linearity of the dot product.

∎

### Theorem 12.6: Gradient Direction Property

**Statement**: Let $f: \mathbb{R}^n \to \mathbb{R}$ be differentiable. Then $\nabla f(\mathbf{a})$ points in the direction of greatest increase of $f$ at $\mathbf{a}$, and $-\nabla f(\mathbf{a})$ points in the direction of greatest decrease.

**Proof**: Let $\mathbf{u}$ be a unit vector. Then $D_{\mathbf{u}}f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u} \leq \|\nabla f(\mathbf{a})\| \|\mathbf{u}\| = \|\nabla f(\mathbf{a})\|$, with equality if and only if $\mathbf{u}$ is in the same direction as $\nabla f(\mathbf{a})$.

∎

## 12.5 Taylor Series

### Theorem 12.7: Multivariable Taylor Series

**Statement**: Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be $k$-times continuously differentiable on a domain $D$. Let $\mathbf{a} \in D$ and let $\mathbf{x} \in D$ such that the line segment connecting $\mathbf{a}$ and $\mathbf{x}$ lies in $D$. Then:

$$f(\mathbf{x}) = \sum_{|\alpha| \leq k} \frac{1}{\alpha!} D^\alpha f(\mathbf{a})(\mathbf{x} - \mathbf{a})^\alpha + R_k(\mathbf{x} - \mathbf{a})$$

where $\alpha = (\alpha_1, \dots, \alpha_n)$ is a multi-index, $\alpha! = \alpha_1! \dots \alpha_n!$, $D^\alpha f = \frac{\partial^{|\alpha|} f}{\partial x_1^{\alpha_1} \dots \partial x_n^{\alpha_n}}$, and the remainder term is:

$$R_k(\mathbf{x} - \mathbf{a}) = \sum_{|\alpha|=k+1} \frac{1}{\alpha!} \left( \int_0^1 (1-t)^k f^{(\alpha+1)}(\mathbf{a} + t(\mathbf{x}-\mathbf{a})) dt \right) (\mathbf{x}-\mathbf{a})^\alpha$$

**Proof**: This is the multivariable generalization of Taylor's theorem with integral remainder.

∎

## 12.6 Critical Points and Extrema

### Theorem 12.8: Second Derivative Test for Local Extrema

**Statement**: Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be $C^2$ in an open set $D$ containing a point $\mathbf{a}$. Let $\nabla f(\mathbf{a}) = \mathbf{0}$. Then:

1. If the Hessian matrix $H_f(\mathbf{a})$ is positive definite, then $f$ has a local minimum at $\mathbf{a}$.
2. If $H_f(\mathbf{a})$ is negative definite, then $f$ has a local maximum at $\mathbf{a}$.
3. If $H_f(\mathbf{a})$ is indefinite, then $f$ has a saddle point at $\mathbf{a}$.

**Proof**: This follows from analyzing the quadratic form $Q(\mathbf{h}) = \frac{1}{2} \mathbf{h}^T H_f(\mathbf{a}) \mathbf{h}$ and its behavior near $\mathbf{a}$.

∎

### Theorem 12.9: Hessian Matrix Definition

**Statement**: The Hessian matrix of $f: \mathbb{R}^n \to \mathbb{R}$ at $\mathbf{a}$ is the $n \times n$ matrix:

$$H_f(\mathbf{a}) = \left( \frac{\partial^2 f}{\partial x_i \partial x_j} \right)_{1 \leq i, j \leq n}$$

**Proof**: The matrix of second-order partial derivatives.

∎

### Theorem 12.10: Boundedness of Compact Functions

**Statement**: Let $f: K \to \mathbb{R}$ be continuous on a compact set $K \subseteq \mathbb{R}^n$. Then:
1. $f$ is bounded on $K$.
2. $f$ attains its maximum and minimum values on $K$.

**Proof**: This is a standard result from real analysis using the extreme value theorem.

∎

## 12.7 Mean Value Theorem

### Theorem 12.11: Mean Value Theorem for Vector-Valued Functions

**Statement**: Let $\mathbf{f}: [a, b] \subseteq \mathbb{R}^n \to \mathbb{R}^m$ be continuous on $[a, b]$ and differentiable on $(a, b)$. Then there exists a point $c \in (a, b)$ such that:

$$\|\mathbf{f}(b) - \mathbf{f}(a)\| \leq \max_{c \in (a, b)} \|\mathbf{f}'(c)\| (b - a)$$

**Proof**: This follows from applying the scalar Mean Value Theorem to each component function.

∎

### Theorem 12.12: Multivariable Mean Value Theorem

**Statement**: Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be differentiable on an open set $D$ containing a line segment connecting $\mathbf{a}$ and $\mathbf{b}$. Then there exists a point $\mathbf{c}$ on the segment such that:

$$f(\mathbf{b}) - f(\mathbf{a}) = \nabla f(\mathbf{c}) \cdot (\mathbf{b} - \mathbf{a})$$

**Proof**: This is the generalization of the single-variable MVT to multivariable functions.

∎

## 12.8 Lagrange Multipliers

### Theorem 12.13: Lagrange Multiplier Theorem

**Statement**: Let $f: \mathbb{R}^n \to \mathbb{R}$ and $g_1, \dots, g_m: \mathbb{R}^n \to \mathbb{R}$ be $C^2$ functions. Let $S = \{\mathbf{x} \in \mathbb{R}^n : g_1(\mathbf{x}) = 0, \dots, g_m(\mathbf{x}) = 0\}$ be a smooth constraint surface. If $\nabla f(\mathbf{a})$ and the gradients $\nabla g_1(\mathbf{a}), \dots, \nabla g_m(\mathbf{a})$ are linearly independent at $\mathbf{a} \in S$, then any local extremum of $f$ on $S$ at $\mathbf{a}$ satisfies:

$$\nabla f(\mathbf{a}) = \sum_{j=1}^m \lambda_j \nabla g_j(\mathbf{a})$$

for some scalars $\lambda_1, \dots, \lambda_m$ (the Lagrange multipliers).

**Proof**: This is the method of Lagrange multipliers, derived from the implicit function theorem and constrained optimization theory.

∎

## Exercises

1. **Exercise 12.1**: Compute the partial derivatives of $f(x, y, z) = x^2y + \sin(yz)$.

2. **Exercise 12.2**: Find the gradient of $f(x, y, z) = e^{xy} \sin(z)$.

3. **Exercise 12.3**: Use the chain rule to compute $\frac{d}{dt} f(t^2, t^3)$ where $f(u, v) = uv$.

4. **Exercise 12.4**: Compute the Hessian matrix of $f(x, y) = x^2y^2$.

5. **Exercise 12.5**: Find the critical points of $f(x, y) = x^3 + y^3 - 3xy$.

6. **Exercise 12.6**: Use the Second Derivative Test to determine the nature of the critical points of $f(x, y) = x^2 + 2xy + y^2 - 4x - 4y$.

7. **Exercise 12.7**: Find the maximum and minimum values of $f(x, y) = x + y$ subject to $x^2 + y^2 = 1$.

8. **Exercise 12.8**: Use the method of Lagrange multipliers to find the maximum value of $f(x, y, z) = xyz$ subject to $x^2 + y^2 + z^2 = 1$.

9. **Exercise 12.9**: Prove that if $f$ has a local extremum at $\mathbf{a}$ and the Hessian matrix is non-singular, then it is a strict local extremum.

10. **Exercise 12.10**: Find the critical points and classify them for $f(x, y, z) = x^2 + 2y^2 + 3z^2 - 2xy - 4yz - 6zx$.
