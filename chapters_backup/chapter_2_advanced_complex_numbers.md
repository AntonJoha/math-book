# Chapter: Advanced Complex Numbers

## 2.1 Complex Number Extensions

### Theorem 2.1: Gaussian Integer Prime Factorization

**Statement**: Every non-zero Gaussian integer $a + bi$ can be uniquely factored into Gaussian primes (up to multiplication by units).

**Proof**: The Gaussian integers form a Euclidean domain with norm $N(a + bi) = a^2 + b^2$. In any Euclidean domain, unique factorization into irreducibles (primes) holds. The units in $\mathbb{Z}[i]$ are $\{1, -1, i, -i\}$. ∎

### Theorem 2.2: Gaussian Primes

**Statement**: A rational prime $p \in \mathbb{Z}$ factors in $\mathbb{Z}[i]$ as:
1. $p = \pi_1 \overline{\pi_2}$ (product of conjugate Gaussian primes) if $p \equiv 1 \pmod 4$
2. $p$ remains prime in $\mathbb{Z}[i]$ if $p \equiv 3 \pmod 4$
3. $p = -i(1 + i)^2$ if $p = 2$

**Proof**: 
- For $p \equiv 1 \pmod 4$, by Fermat's theorem on sums of two squares, $p = a^2 + b^2$ for some integers $a, b$. Then $(a + bi)(a - bi) = a^2 + b^2 = p$.
- For $p \equiv 3 \pmod 4$, if $p = (a + bi)(c + di)$, then $N(a + bi) \cdot N(c + di) = p$. Since $p$ is prime, one factor must have norm 1, which means it's a unit. Thus $p$ is irreducible.
- For $p = 2$, we have $2 = (1 + i)(1 - i) = -i(1 + i)^2$. ∎

### Theorem 2.3: Sum of Two Squares

**Statement**: A positive integer $n$ can be expressed as a sum of two squares iff all prime factors of the form $4k + 3$ appear with even exponent in the prime factorization of $n$.

**Proof**: This follows from the properties of Gaussian primes. A rational prime $p$ factors in $\mathbb{Z}[i]$ iff $p = 2$ or $p \equiv 1 \pmod 4$. If $p \equiv 3 \pmod 4$ appears with odd exponent, then $n$ cannot be written as $a^2 + b^2 = (a + bi)(a - bi)$ in $\mathbb{Z}[i]$ since the conjugate factorization would require the conjugate prime to appear as well. ∎

## 2.2 Advanced Properties

### Theorem 2.4: Complex Conjugation in Fields

**Statement**: The complex conjugation $z \mapsto \overline{z}$ is a field automorphism of $\mathbb{C}$ that fixes $\mathbb{R}$ pointwise.

**Proof**: 
1. $\overline{z + w} = \overline{z} + \overline{w}$ (verified in Theorem 1.3)
2. $\overline{zw} = \overline{z}\overline{w}$ (verified in Theorem 1.3)
3. For $r \in \mathbb{R}$, $\overline{r} = r$ by definition
4. $\overline{z^n} = \overline{z}^n$ for any integer $n \ge 0$ by induction
5. $\overline{z^{-1}} = \overline{z}^{-1}$ for $z \ne 0$

Thus $\overline{z}$ is an automorphism of $\mathbb{C}$ fixing $\mathbb{R}$. ∎

### Theorem 2.5: Fixed Field of Complex Conjugation

**Statement**: The fixed field of complex conjugation is exactly $\mathbb{R} = \{z \in \mathbb{C} : \overline{z} = z\}$.

**Proof**: 
$(\implies)$ If $\overline{z} = z$, then writing $z = a + bi$, we have $a - bi = a + bi$, which implies $b = 0$, so $z = a \in \mathbb{R}$.

$(\impliedby)$ If $z \in \mathbb{R}$, then by definition $\overline{z} = z$. ∎

### Theorem 2.6: Real and Imaginary Parts as Linear Functionals

**Statement**: For any $z \in \mathbb{C}$, we have $z = \text{Re}(z) + i\text{Im}(z)$, where $\text{Re}: \mathbb{C} \to \mathbb{R}$ and $\text{Im}: \mathbb{C} \to \mathbb{R}$ are $\mathbb{R}$-linear maps.

**Proof**: 
Let $z = a + bi$. Then $\text{Re}(z) = \frac{z + \overline{z}}{2} = a$ and $\text{Im}(z) = \frac{z - \overline{z}}{2i} = b$. Both formulas show linearity over $\mathbb{R}$. ∎

### Theorem 2.7: Complex Numbers as $\mathbb{R}^2$

**Statement**: The field $\mathbb{C}$ is isomorphic to $\mathbb{R}^2$ as a vector space over $\mathbb{R}$.

**Proof**: Define $\phi: \mathbb{R}^2 \to \mathbb{C}$ by $\phi(x, y) = x + iy$. This is an $\mathbb{R}$-linear bijection. The multiplication in $\mathbb{C}$ corresponds to bilinear operations in $\mathbb{R}^2$. ∎

## 2.3 Higher-Dimensional Complex Numbers

### Theorem 2.8: Octonions and Sedenions

**Statement**: The octonions $\mathbb{O}$ and sedenions $\mathbb{S}$ are non-associative division algebras over $\mathbb{R}$.

**Proof**: 
- Octonions $\mathbb{O} \cong \mathbb{R}^8$ with multiplication defined by Cayley-Dickson doubling from quaternions $\mathbb{H}$. The multiplication is alternative but not associative.
- Sedenions $\mathbb{S} \cong \mathbb{R}^{16}$ with multiplication defined by further Cayley-Dickson doubling. The product is not even alternative.
- Both satisfy the zero-product property: $xy = 0 \iff x = 0$ or $y = 0$.
- For octonions, the norm satisfies $|xy| = |x||y|$. For sedenions, this property fails. ∎

### Theorem 2.9: Cayley-Dickson Construction

**Statement**: The Cayley-Dickson construction produces a sequence of algebras: $\mathbb{C} \to \mathbb{H} \to \mathbb{O} \to \mathbb{S}$, each of dimension $2^n$ over $\mathbb{R}$.

**Proof**: 
The construction defines $x^*y$ (twisted product) from $x, y$ in dimension $2^n$ to produce dimension $2^{n+1}$. Starting with $\mathbb{C}$, we get $\mathbb{H}$, then $\mathbb{O}$, then $\mathbb{S}$. The construction preserves conjugation properties but loses associativity at each step. ∎

## 2.4 Complex Numbers in Analysis

### Theorem 2.10: Cauchy-Riemann Equations

**Statement**: Let $f(z) = u(x, y) + iv(x, y)$ where $z = x + iy$. If $f$ is complex differentiable at $z_0$, then $u$ and $v$ satisfy the Cauchy-Riemann equations at $z_0$:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

**Proof**: 
Let $f(z_0 + h) - f(z_0) = \ell(h) + o(|h|)$ where $\ell(h)$ is linear. Writing $h = h_1 + ih_2$, we expand both $f(z_0 + h)$ and $f(z_0 + ih)$ using differentiability. Equating real and imaginary parts yields the Cauchy-Riemann equations. ∎

### Theorem 2.11: Liouville's Theorem

**Statement**: A bounded entire function (holomorphic on all of $\mathbb{C}$) is constant.

**Proof**: This is the classical result proved in the Fundamental Theorem of Algebra proof (Theorem 1.1). A bounded entire function is constant by the maximum modulus principle. ∎

### Theorem 2.12: Fundamental Theorem of Calculus for Complex Functions

**Statement**: If $f$ is holomorphic on a simply connected domain $D$ and $f' = g$ exists, then for any path $\gamma$ from $a$ to $b$ in $D$:

$$\int_\gamma f'(z) \, dz = f(b) - f(a)$$

**Proof**: The fundamental theorem of calculus for contour integrals follows from the fact that the integral of a total differential is path-independent in simply connected domains. ∎

## 2.5 Additional Exercises and Results

### Exercise 2.1
Prove that if $p \equiv 1 \pmod 4$, then $p$ can be written as a sum of two squares in exactly four distinct ways (up to order and sign).

### Exercise 2.2
Show that the field of complex numbers is the algebraic closure of $\mathbb{R}$.

### Exercise 2.3
Prove that if $a, b \in \mathbb{C}$ and $a^n = b^n$ for some integer $n \ge 2$, then $b = a\zeta$ for some $n$-th root of unity $\zeta$.

## 2.6 Historical Notes

The theory of complex numbers evolved from the solution of cubic equations by Cardano and Ferrari in the 16th century. The introduction of imaginary numbers was initially met with skepticism, leading to Newton's famous remark "I have not yet found out the nature of these numbers". By the 18th century, Euler had established the correspondence between complex numbers and points in the plane, and Lagrange provided a rigorous algebraic foundation. In the 19th century, Cauchy and Riemann established complex analysis, which has become central to mathematics.

======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697059

Theorem Generation

# **Cauchy-Riemann Equations**
**Statement**: f is holomorphic iff u_x = v_y and u_y = -v_x.
**Proof**: [proof outline]...


# **Morera's Theorem**
**Statement**: If f is continuous and ∮ f(z) dz = 0 on every closed curve, f is holomorphic.
**Proof**: [proof outline]...


# **Goursat's Lemma**
**Statement**: A bounded function is Riemann integrable iff its discontinuities form a set of measure zero.
**Proof**: [proof outline]...


# **Cauchy-Kovalevskaya Theorem**
**Statement**: Local solution exists for holomorphic functions with boundary conditions.
**Proof**: [proof outline]...


# **Painlevé's Theorem**
**Statement**: Every entire function of finite order is a polynomial.
**Proof**: [proof outline]...


# **Hadamard's Factorization Theorem**
**Statement**: Every entire function has canonical product representation using zeros.
**Proof**: [proof outline]...


# **Great Picard Theorem**
**Statement**: An essential singularity has infinite image in every neighborhood.
**Proof**: [proof outline]...


# **Montel's Theorem**
**Statement**: A family of holomorphic functions is normal iff it omits three values.
**Proof**: [proof outline]...


# **Little Picard Theorem**
**Statement**: A non-constant entire function omits at most one complex value.
**Proof**: [proof outline]...


# **Phragmén-Lindelöf Principle**
**Statement**: Bounded growth on boundary implies bounded growth inside domain.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618352

Theorem Generation

# **Cauchy-Riemann Equations**
**Statement**: f is holomorphic iff u_x = v_y and u_y = -v_x.
**Proof**: [proof outline]...


# **Morera's Theorem**
**Statement**: If f is continuous and ∮ f(z) dz = 0 on every closed curve, f is holomorphic.
**Proof**: [proof outline]...


# **Goursat's Lemma**
**Statement**: A bounded function is Riemann integrable iff its discontinuities form a set of measure zero.
**Proof**: [proof outline]...


# **Cauchy-Kovalevskaya Theorem**
**Statement**: Local solution exists for holomorphic functions with boundary conditions.
**Proof**: [proof outline]...


# **Painlevé's Theorem**
**Statement**: Every entire function of finite order is a polynomial.
**Proof**: [proof outline]...


# **Hadamard's Factorization Theorem**
**Statement**: Every entire function has canonical product representation using zeros.
**Proof**: [proof outline]...


# **Great Picard Theorem**
**Statement**: An essential singularity has infinite image in every neighborhood.
**Proof**: [proof outline]...


# **Montel's Theorem**
**Statement**: A family of holomorphic functions is normal iff it omits three values.
**Proof**: [proof outline]...


# **Little Picard Theorem**
**Statement**: A non-constant entire function omits at most one complex value.
**Proof**: [proof outline]...


# **Phragmén-Lindelöf Principle**
**Statement**: Bounded growth on boundary implies bounded growth inside domain.
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