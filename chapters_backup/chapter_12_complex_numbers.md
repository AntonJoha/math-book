# Complex Numbers and the Fundamental Theorem of Algebra

## 12.1 Complex Numbers

### 12.1.1 Definition and Structure

The complex numbers form a field $\mathbb{C}$ that extends the real numbers $\mathbb{R}$. Every complex number $z$ can be expressed as:

$$z = a + bi$$

where $a, b \in \mathbb{R}$ and $i$ is the imaginary unit satisfying $i^2 = -1$.

### 12.1.2 Operations on Complex Numbers

**Addition:**
$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

**Multiplication:**
$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

### 12.1.3 Complex Conjugate Theorem

**Theorem 12.1:** For any complex number $z = a + bi$, its complex conjugate is $\overline{z} = a - bi$. The product $z\overline{z} = |z|^2$ is always real and non-negative.

**Proof:** 
$$z\overline{z} = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2i^2 = a^2 + b^2 \in \mathbb{R}_{\geq 0}$$

### 12.1.4 Polar Form and Euler's Formula

**Theorem 12.2:** Any non-zero complex number $z$ can be expressed in polar form as $z = re^{i\theta}$, where $r = |z|$ is the modulus and $\theta = \arg(z)$ is the argument.

**Proof (Euler's Formula):** 
For $\theta \in \mathbb{R}$, we have:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

This follows from the Taylor series expansions:
$$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!}$$
$$= \sum_{k=0}^\infty \frac{(-1)^k\theta^{2k}}{(2k)!} + i\sum_{k=0}^\infty \frac{(-1)^k\theta^{2k+1}}{(2k+1)!} = \cos\theta + i\sin\theta$$

### 12.1.5 De Moivre's Theorem

**Theorem 12.3 (De Moivre's Theorem):** For any complex number $z = re^{i\theta}$ and integer $n$:
$$z^n = r^n e^{in\theta}$$

**Proof:** By induction. Base case $n=1$ is trivial. Assume true for $n=k$, then:
$$z^{k+1} = z^k \cdot z = r^k e^{ik\theta} \cdot re^{i\theta} = r^{k+1} e^{i(k+1)\theta}$$

## 12.2 Fundamental Theorem of Algebra

### 12.2.1 Statement

**Theorem 12.4 (Fundamental Theorem of Algebra):** Every non-constant polynomial $P(z)$ with complex coefficients has at least one complex root.

**Equivalently:** A polynomial of degree $n$ has exactly $n$ roots in $\mathbb{C}$, counting multiplicity.

### 12.2.2 Polynomial Factorization

**Theorem 12.5:** If $P(z)$ is a polynomial of degree $n$ with complex coefficients and $z_1, z_2, \dots, z_n$ are its roots (counting multiplicity), then:
$$P(z) = c(z - z_1)(z - z_2)\cdots(z - z_n)$$
where $c$ is the leading coefficient.

### 12.2.3 Algebraic Proof Sketch

**Theorem 12.6 (Algebraic Proof of FTA):** Every complex polynomial has a root.

**Proof Sketch:**
1. Consider a polynomial $P(z)$ with complex coefficients.
2. Define the modulus function $|P(z)|$.
3. If $P(z)$ has no roots, then $|P(z)|$ attains a minimum on compact sets.
4. However, as $|z| \to \infty$, $|P(z)| \to \infty$.
5. The function $|P(z)|^2$ is continuous and positive.
6. By the maximum modulus principle (applied to $1/P(z)$), $1/P(z)$ must be bounded on $\mathbb{C}$.
7. However, this leads to a contradiction with the growth behavior of polynomials.
8. Therefore, $P(z)$ must have at least one root.

### 12.2.4 Application: Complex Integration

**Theorem 12.7:** The Fundamental Theorem of Algebra ensures that the integral of a rational function over a closed contour can be computed using residue calculus.

**Proof:** The existence of roots allows partial fraction decomposition of rational functions:
$$\frac{P(z)}{Q(z)} = \sum_{k=1}^n \frac{c_k}{z - z_k}$$
where $Q(z) = \prod_{k=1}^n (z - z_k)$.

## 12.3 Exercises

### 12.3.1 Practice Problems

1. **Problem 12.1:** Prove that if $z_1, z_2 \in \mathbb{C}$ are roots of a polynomial $P(z)$ of degree $n$, then $z_1 = z_2$ implies $(z - z_1)^2$ divides $P(z)$.

2. **Problem 12.2:** Show that the equation $z^4 + 1 = 0$ has four distinct complex roots. Express them in polar form.

3. **Problem 12.3:** Use De Moivre's Theorem to compute $(\sqrt{3} + i)^{10}$.

4. **Problem 12.4:** Prove that every quadratic equation $az^2 + bz + c = 0$ with $a, b, c \in \mathbb{C}$ has at least one solution.

5. **Problem 12.5:** Let $P(z) = z^3 - 2$. Find all roots of $P(z)$ in polar form and verify they satisfy $P(z) = 0$.

**Solutions** (see end of section for verification)

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*