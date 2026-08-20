# Chapter 28: Complex Numbers - Deeper Theory and Proofs

## 28.1 De Moivre's Theorem and Euler's Formula

### Theorem 28.1: De Moivre's Theorem

**Statement**: If \(z = r(\cos\theta + i\sin\theta)\) where \(r > 0\) and \(\theta \in \mathbb{R}\), then for any integer \(n\):
\[ z^n = r^n(\cos(n\theta) + i\sin(n\theta)) \]

**Proof**: We prove this by induction on \(n \geq 0\).

1. **Base case (\(n = 0\))**:
   \[ z^0 = 1 \quad \text{and} \quad r^0(\cos(0\theta) + i\sin(0\theta)) = 1(\cos 0 + i\sin 0) = 1 \]
   So the formula holds for \(n = 0\).

2. **Inductive step**: Assume the formula holds for some \(n \geq 0\). Then:
   \[
   \begin{aligned}
   z^{n+1} &= z^n \cdot z \\
           &= r^n(\cos(n\theta) + i\sin(n\theta)) \cdot r(\cos\theta + i\sin\theta) \\
           &= r^{n+1}(\cos(n\theta)\cos\theta - \sin(n\theta)\sin\theta + i(\cos(n\theta)\sin\theta + \sin(n\theta)\cos\theta)) \\
           &= r^{n+1}(\cos((n+1)\theta) + i\sin((n+1)\theta))
   \end{aligned}
   \]
   The real part uses \(\cos(A+B) = \cos A \cos B - \sin A \sin B\), and the imaginary part uses \(\sin(A+B) = \sin A \cos B + \cos A \sin B\).

For negative integers \(n < 0\), let \(n = -m\) where \(m > 0\). Then \(z^{-m} = (z^m)^{-1}\). Using the formula for \(z^m\) and taking the reciprocal with conjugation gives the result.

∎

### Theorem 28.2: Euler's Formula

**Statement**: For any real \(x\),
\[ e^{ix} = \cos x + i\sin x \]

**Proof**: Define \(f(x) = e^{ix} - (\cos x + i\sin x)\). Differentiating:
\[ f'(x) = ie^{ix} - (-\sin x + i\cos x) = ie^{ix} + \sin x - i\cos x \]
Substitute \(e^{ix} = \cos x + i\sin x\):
\[ f'(x) = i(\cos x + i\sin x) + \sin x - i\cos x = i\cos x - \sin x + \sin x - i\cos x = 0 \]
Since \(f'(x) = 0\), \(f(x)\) is constant. For \(x = 0\):
\[ f(0) = e^0 - (\cos 0 + i\sin 0) = 1 - (1 + 0) = 0 \]
Therefore \(f(x) = 0\) for all \(x\), proving the formula. ∎

Alternatively, using Taylor series:
\[ e^{ix} = 1 + ix + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + \cdots \]
\[ = 1 + ix - \frac{x^2}{2!} - \frac{ix^3}{3!} + \frac{x^4}{4!} + \frac{ix^5}{5!} + \cdots \]
\[ = \left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots\right) + i\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right) \]
\[ = \cos x + i\sin x \]

### Corollary 28.1: \(\ln(iz) = \ln|z| + i(\arg(z) + \frac{\pi}{2})\)

**Proof**: If \(z = re^{i\theta}\), then \(iz = re^{i(\theta + \pi/2)}\), so \(\ln(iz) = \ln r + i(\theta + \pi/2)\) modulo \(2\pi i\). ∎

## 28.2 Complex Roots and the Fundamental Theorem of Algebra

### Theorem 28.3: Existence of \(n\)-th Roots

**Statement**: Every complex number \(z \neq 0\) has exactly \(n\) distinct \(n\)-th roots.

**Proof**: By Euler's formula, any \(z = r(\cos\theta + i\sin\theta) = re^{i\theta}\). An \(n\)-th root \(w\) satisfies:
\[ w^n = r e^{i\theta} \]
In polar form, if \(w = \rho e^{i\phi}\), then \(w^n = \rho^n e^{in\phi}\). We need \(\rho^n = r\) and \(n\phi \equiv \theta \pmod{2\pi}\).

So \(\rho = r^{1/n}\) (unique positive solution), and \(\phi = \frac{\theta + 2\pi k}{n}\) for \(k = 0, 1, \dots, n-1\).

These give \(n\) distinct values since \(\frac{\theta + 2\pi k}{n} \neq \frac{\theta + 2\pi j}{n}\) for \(k \neq j \pmod n\).

∎

### Theorem 28.4: The Fundamental Theorem of Algebra

**Statement**: Every non-constant polynomial \(P(z)\) with complex coefficients has at least one complex root.

**Proof**: Suppose for contradiction that \(P(z)\) has no roots. Then \(1/P(z)\) is entire (holomorphic on \(\mathbb{C}\)). By Liouville's theorem, since \(|1/P(z)|\) is bounded (it goes to 0 as \(|z| \to \infty\)), \(1/P(z)\) is constant, so \(P(z)\) is constant, a contradiction.

### Corollary 28.2: Algebraic Closure of \(\mathbb{C}\)

**Statement**: The field \(\mathbb{C}\) is algebraically closed, meaning every polynomial \(P(z) \in \mathbb{C}[z]\) of degree \(n \geq 1\) has a root in \(\mathbb{C}\).

**Proof**: By Theorem 28.3, \(P(z)\) has exactly \(n\) roots counting multiplicity. Since these roots exist in \(\mathbb{C}\), \(\mathbb{C}\) is algebraically closed. ∎

## 28.3 Dealing with Complex Numbers in Calculus

### Theorem 28.5: Differentiation of Complex Functions

**Statement**: If \(f(z) = u(x,y) + iv(x,y)\) is differentiable at \(z = x + iy\), then its derivative is:
\[ f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} + i\frac{\partial u}{\partial y} \]

This is the **Cauchy-Riemann equations**.

**Proof**: The derivative is defined as:
\[ f'(z) = \lim_{h \to 0} \frac{f(z+h) - f(z)}{h} \]
Taking limits along the real axis (\(h \to 0\) real) and imaginary axis (\(h \to 0 = i\delta\), \(\delta\) real) gives:
\[ f'(z) = u_x + iv_x = v_y + iu_y \]
Equating real and imaginary parts gives the Cauchy-Riemann equations. ∎

### Corollary 28.3: The Derivative of \(e^{iz}\)

**Statement**: \(\frac{d}{dz}(e^{iz}) = ie^{iz}\).

**Proof**: Using the chain rule with the substitution \(w = iz\):
\[ \frac{d}{dz}(e^{iz}) = \frac{d}{dw}(e^w) \cdot \frac{dw}{dz} = e^w \cdot i = ie^{iz} \]

## 28.4 Exercises

1. **Exercise 28.1**: Find all 5th roots of \(-32\) using De Moivre's theorem.

2. **Exercise 28.2**: Prove that if \(z^n = 1\), then \(1 + z + z^2 + \cdots + z^{n-1} = 0\) for \(z \neq 1\).

3. **Exercise 28.3**: Show that \(\sum_{k=1}^n \cos(kx) = \frac{\sin(nx/2)}{\sin(x/2)}\cos((n+1)x/2)\).

4. **Exercise 28.4**: Let \(z_1, z_2, z_3\) be vertices of an equilateral triangle. Prove that \(z_1 + z_2\omega + z_3\omega^2 = 0\) where \(\omega = e^{2\pi i/3}\).

5. **Exercise 28.5**: If \(f\) is entire and \(|f(z)| \leq M|z|^2 + C\), prove \(f(z) = az^2 + bz + c\).

## 28.6 Summary

This chapter explored:
- De Moivre's theorem and its applications
- Euler's formula and its derivation via Taylor series
- The existence and uniqueness of complex roots
- The fundamental theorem of algebra
- Complex differentiation and Cauchy-Riemann equations
- Applications to trigonometric sums and polynomial roots

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*