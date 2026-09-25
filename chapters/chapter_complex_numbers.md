<<<<<<< HEAD
# Chapter 1: Complex Numbers

## 1.1 Introduction to Complex Numbers

Complex numbers are an extension of the real numbers that allow us to solve equations that have no real solutions. A complex number is expressed in the form:

$$z = a + bi$$

where $a$ and $b$ are real numbers, and $i$ is the imaginary unit satisfying $i^2 = -1$.

**Definition (Complex Number Representation):**
Any complex number $z$ can be represented in multiple equivalent forms:
1. **Rectangular form**: $z = a + bi$ where $a, b \in \mathbb{R}$
2. **Polar form**: $z = r(\cos \theta + i \sin \theta)$ where $r = |z|$ and $\theta = \arg(z)$
3. **Exponential form**: $z = re^{i\theta}$ (Euler's form)
4. **Gaussian form**: For Gaussian integers $a + bi$ where $a, b \in \mathbb{Z}$

### Theorem 1.1: The Fundamental Theorem of Algebra

**Statement**: Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

**Proof**:

We will use Liouville's Theorem from complex analysis.

1. Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0$ where $n \ge 1$ and $a_n \ne 0$.
2. Consider the function $f(z) = \frac{1}{P(z)}$.
3. If $P(z)$ has no zeros in $\mathbb{C}$, then $f(z)$ is entire (holomorphic everywhere).
4. As $|z| \to \infty$, we have $|P(z)| \to \infty$, so $|f(z)| \to 0$.
5. By Liouville's Theorem, a bounded entire function is constant. Since $\lim_{|z| \to \infty} f(z) = 0$, $f(z) = 0$.
6. But if $f(z) = 0$, then $P(z) \to \infty$, which is a contradiction.
7. Therefore, $P(z)$ must have at least one zero in $\mathbb{C}$. ∎

## 1.2 Complex Arithmetic

### Theorem 1.2: De Moivre's Formula

**Statement**: For any complex number $z = r(\cos \theta + i \sin \theta)$ and any integer $n$:

$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

**Proof**:

We use mathematical induction.

**Base case** ($n = 1$):
$$(\cos \theta + i \sin \theta)^1 = \cos \theta + i \sin \theta$$
This is trivially true.

**Inductive step**: Assume the formula holds for $n = k$:
$$(\cos \theta + i \sin \theta)^k = \cos(k\theta) + i \sin(k\theta)$$

For $n = k + 1$:
$$(\cos \theta + i \sin \theta)^{k+1} = (\cos \theta + i \sin \theta)^k (\cos \theta + i \sin \theta)$$
$$= (\cos(k\theta) + i \sin(k\theta))(\cos \theta + i \sin \theta)$$
$$= \cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta + i(\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta)$$
$$= \cos((k+1)\theta) + i\sin((k+1)\theta)$$

This uses the angle addition formulas for cosine and sine. ∎

### Theorem 1.3: De Moivre's Formula for Powers of Roots

**Statement**: If $z = e^{i\theta}$ is a root of unity of order $n$ (i.e., $z^n = 1$), then the $n$-th roots of unity are:

$$\omega_k = e^{i\frac{2\pi k}{n}}, \quad k = 0, 1, 2, \dots, n-1$$

**Proof**: 
We need $z^n = 1$, which means $e^{in\theta} = 1$. This occurs when $in\theta = 2\pi k$ for integer $k$. Thus $\theta = \frac{2\pi k}{n}$, giving us the roots above. ∎

## 1.3 Modulus and Conjugate

### Theorem 1.3: Properties of the Complex Conjugate

**Statement**: For any complex numbers $z_1$ and $z_2$:

1. $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
2. $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$
3. $\overline{\overline{z}} = z$
4. $|z|^2 = z \cdot \overline{z}$

**Proof**:

1. Let $z_1 = a + bi$ and $z_2 = c + di$. Then:
   $\overline{z_1 + z_2} = \overline{(a+c) + i(b+d)} = (a+c) - i(b+d) = \overline{z_1} + \overline{z_2}$

2. $\overline{z_1 z_2} = \overline{(a+bi)(c+di)} = \overline{(ac-bd) + i(ad+bc)} = (ac-bd) - i(ad+bc)$
   
   $\overline{z_1} \cdot \overline{z_2} = (a-bi)(c-di) = (ac-bd) - i(ad+bc)$
   
   These are equal.

3. $\overline{\overline{z}} = \overline{(a-bi)} = a + bi = z$

4. $|z|^2 = |a+bi|^2 = a^2 + b^2$
   
   $z \cdot \overline{z} = (a+bi)(a-bi) = a^2 - (bi)^2 = a^2 + b^2$ ∎

## 1.4 Polar Form

### Theorem 1.4: Polar Representation

**Statement**: Any non-zero complex number $z$ can be uniquely expressed as:

$$z = r(\cos \theta + i \sin \theta) = re^{i\theta}$$

where $r = |z|$ is the modulus and $\theta = \arg(z)$ is the argument (principal value in $(-\pi, \pi]$).

**Proof**:

Let $z = a + bi$. We define:
- $r = |z| = \sqrt{a^2 + b^2}$
- $\theta = \arg(z)$ such that $\cos \theta = \frac{a}{r}$ and $\sin \theta = \frac{b}{r}$

Then:
$r(\cos \theta + i \sin \theta) = r\left(\frac{a}{r} + i\frac{b}{r}\right) = a + bi = z$

The uniqueness of $\theta$ in $(-\pi, \pi]$ follows from the fact that sine and cosine uniquely determine an angle in this interval. ∎

### Theorem 1.5: Argument Addition Formula

**Statement**: For non-zero complex numbers $z_1, z_2$:

$$\arg(z_1 z_2) \equiv \arg(z_1) + \arg(z_2) \pmod{2\pi}$$

$$\arg\left(\frac{z_1}{z_2}\right) \equiv \arg(z_1) - \arg(z_2) \pmod{2\pi}$$

**Proof**: Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$ where $\theta_1, \theta_2$ are principal arguments.

Then:

$$z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}$$

So $\arg(z_1 z_2) = \theta_1 + \theta_2 + 2k\pi$ for some integer $k$.

Thus $\arg(z_1 z_2) \equiv \arg(z_1) + \arg(z_2) \pmod{2\pi}$.

Similarly for division:

$$\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}$$

So $\arg(z_1/z_2) \equiv \arg(z_1) - \arg(z_2) \pmod{2\pi}$.

∎

## 1.5 Euler's Formula

### Theorem 1.6: Euler's Formula

**Statement**: For any real number $\theta$ and integer $n$:

$$e^{i\theta} = \cos \theta + i \sin \theta$$

**Proof**:

We can prove this using Taylor series expansions:

1. The exponential function: $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
2. The cosine function: $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
3. The sine function: $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$

Substituting $x = i\theta$:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \dots$$

$$= 1 + i\theta - \frac{\theta^2}{2!} - i\frac{\theta^3}{3!} + \frac{\theta^4}{4!} + i\frac{\theta^5}{5!} + \dots$$

Grouping real and imaginary parts:

$$= \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \dots\right) + i\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots\right)$$

$$= \cos \theta + i \sin \theta$$

∎

**Corollary 1.1 (Euler's Identity)**:

$$e^{i\pi} + 1 = 0$$

**Proof**: Setting $\theta = \pi$ in Euler's Formula:

$$e^{i\pi} = \cos \pi + i \sin \pi = -1 + 0i = -1$$

Thus $e^{i\pi} + 1 = 0$. This is considered one of the most beautiful formulas in mathematics as it connects five fundamental mathematical constants: $e$, $i$, $\pi$, $1$, and $0$. ∎

### Theorem 1.7: Euler's Formula for Complex Powers

**Statement**: For any complex number $z = re^{i\theta}$ and any complex number $w$:

$$z^w = e^{w \ln z} = e^{w(\ln r + i\theta)}$$

**Proof**: 
By definition of complex exponentiation, $z^w = e^{w \ln z}$. Using the principal branch of the logarithm:

$$\ln z = \ln r + i\theta \quad \text{where } \theta \in (-\pi, \pi]$$

Therefore:

$$z^w = e^{w(\ln r + i\theta)} = e^{w\ln r} \cdot e^{iw\theta} = r^w e^{iw\theta}$$

∎

## 1.6 Complex Conjugates and Symmetries

### Theorem 1.8: Loci of Complex Numbers

**Statement 1**: The set of complex numbers satisfying $|z - c_1| = |z - c_2|$ forms the perpendicular bisector of the segment connecting $c_1$ and $c_2$.

**Proof**: Let $z = x + iy$, $c_1 = a_1 + ib_1$, and $c_2 = a_2 + ib_2$. Then:

$$|z - c_1|^2 = (x - a_1)^2 + (y - b_1)^2 = (x - a_2)^2 + (y - b_2)^2$$

Expanding:
$$(x^2 - 2xa_1 + a_1^2 + y^2 - 2yb_1 + b_1^2) = (x^2 - 2xa_2 + a_2^2 + y^2 - 2yb_2 + b_2^2)$$

Simplifying:
$$-2x(a_1 - a_2) - 2y(b_1 - b_2) + (a_1^2 + b_1^2 - a_2^2 - b_2^2) = 0$$

This is the equation of a line (the perpendicular bisector of the segment from $c_1$ to $c_2$). ∎

**Statement 2**: The set of complex numbers satisfying $|z - c_1| + |z - c_2| = d$ where $d > |c_1 - c_2|$ is an ellipse with foci at $c_1$ and $c_2$.

**Proof**: In Cartesian coordinates, this condition describes an ellipse where:
- The sum of distances from any point on the ellipse to the two foci is constant ($d$)
- The major axis length is $d$, and the minor axis length is $\sqrt{d^2 - |c_1 - c_2|^2}$

This is the geometric definition of an ellipse in complex plane geometry. ∎

### Theorem 1.9: Properties of Modulus Inequalities

**Statement**: For any complex numbers $z_1, z_2$:

1. **Triangle Inequality**: $|z_1 + z_2| \leq |z_1| + |z_2|$
2. **Reverse Triangle Inequality**: $||z_1| - |z_2|| \leq |z_1 - z_2|$
3. **Subtraction Triangle Inequality**: $|z_1 - z_2| \leq |z_1| + |z_2|$

**Proof**:

1. Triangle Inequality:
   $$|z_1 + z_2|^2 = (z_1 + z_2)(\overline{z_1 + z_2}) = (z_1 + z_2)(\overline{z_1} + \overline{z_2})$$
   $$= |z_1|^2 + |z_2|^2 + z_1\overline{z_2} + \overline{z_1}z_2 = |z_1|^2 + |z_2|^2 + 2\text{Re}(z_1\overline{z_2})$$

   Since $\text{Re}(z_1\overline{z_2}) \leq |z_1\overline{z_2}| = |z_1||z_2|$,
   
   $$|z_1 + z_2|^2 \leq |z_1|^2 + |z_2|^2 + 2|z_1||z_2| = (|z_1| + |z_2|)^2$$

   Taking square roots gives $|z_1 + z_2| \leq |z_1| + |z_2|$.

2. Reverse Triangle Inequality:
   $$|z_1 + z_2| \geq ||z_1| - |z_2||$$
   (using the triangle inequality with $z_1 = (z_1 + z_2) - z_2$)
   
   More directly: $|z_1 + z_2|^2 \geq (|z_1| - |z_2|)^2$, leading to the result.

3. Subtraction Triangle Inequality:
   $$|z_1 - z_2| \leq |z_1| + |-z_2| = |z_1| + |z_2|$$
   (applying the triangle inequality)

∎

### Theorem 1.10: Gaussian Integer Properties

**Statement**: Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ form a Euclidean domain.

**Proof**: 

The Gaussian integers form a ring under addition and multiplication. For the Euclidean algorithm, define the norm:

$$N(a + bi) = a^2 + b^2 \in \mathbb{Z}_{\geq 0}$$

For any $\alpha, \beta \in \mathbb{Z}[i]$ with $\beta \ne 0$, we have:

$$\frac{\alpha}{\beta} = \frac{\alpha \overline{\beta}}{|\beta|^2} = \frac{a + bi}{c^2 + d^2}$$

for some integers $a, b, c, d$. We can write:

$$\frac{\alpha}{\beta} = q + r$$

where $q = \text{round}(\text{Re}(\frac{\alpha}{\beta}), \text{Im}(\frac{\alpha}{\beta})) \in \mathbb{Z}[i]$ and $r = \frac{\alpha}{\beta} - q$.

Then:

$$|r|^2 \leq \frac{1}{4} \quad \text{or} \quad |r|^2 < 1$$

Thus $N(r) < N(\beta)$, satisfying the Euclidean domain condition. ∎

## 1.7 Polar and Exponential Forms

### Theorem 1.11: De Moivre's Formula in Exponential Form

**Statement**: For any complex number $z = re^{i\theta}$ and integer $n$:

$$z^n = r^n e^{in\theta}$$

**Proof**: By properties of the exponential function:

$$(re^{i\theta})^n = r^n (e^{i\theta})^n = r^n e^{i\theta \cdot n} = r^n e^{in\theta}$$

This can be used to compute powers of complex numbers efficiently without converting to polar coordinates first, though the result is the same as De Moivre's Formula.

∎

### Theorem 1.12: Argument Properties

**Statement**: For non-zero complex numbers $z_1, z_2$:

$$\arg(z_1 z_2) \equiv \arg(z_1) + \arg(z_2) \pmod{2\pi}$$

$$\arg\left(\frac{z_1}{z_2}\right) \equiv \arg(z_1) - \arg(z_2) \pmod{2\pi}$$

**Proof**: Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$ where $\theta_1, \theta_2$ are principal arguments.

Then:

$$z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}$$

So $\arg(z_1 z_2) = \theta_1 + \theta_2 + 2k\pi$ for some integer $k$.

Thus $\arg(z_1 z_2) \equiv \arg(z_1) + \arg(z_2) \pmod{2\pi}$.

Similarly for division:

$$\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}$$

So $\arg(z_1/z_2) \equiv \arg(z_1) - \arg(z_2) \pmod{2\pi}$.

∎

### Theorem 1.13: Complex Roots of Unity

**Statement**: The $n$-th roots of unity are the complex numbers:

$$\omega_k = e^{i\frac{2\pi k}{n}}, \quad k = 0, 1, 2, \dots, n-1$$

**Proof**: 
We need $z^n = 1$, which means $e^{in\theta} = 1$. This occurs when $in\theta = 2\pi k$ for integer $k$. Thus $\theta = \frac{2\pi k}{n}$, giving us the roots above. ∎

**Corollary 1.2 (Sum and Product of Roots)**:

The sum of all $n$-th roots of unity is:
$$\sum_{k=0}^{n-1} e^{i\frac{2\pi k}{n}} = 0 \quad \text{for } n \geq 2$$

The product is:
$$\prod_{k=0}^{n-1} e^{i\frac{2\pi k}{n}} = (-1)^{n-1}$$

**Proof**: 
The sum is the sum of all roots of $z^n - 1 = 0$, which by Vieta's formulas equals the negative coefficient of $z^{n-1}$, which is 0 for $n \ge 2$.

The product equals the constant term of $z^n - 1$, which is $(-1)^{n-1}$. ∎

## Exercises

### Exercise 1.1
Write the complex number $-3 + 4i$ in polar form, giving the argument in radians.

### Exercise 1.2
Calculate $(-1 + i\sqrt{3})^3$ using Euler's Formula, showing all steps.

### Exercise 1.3
Prove that if $z$ is a root of unity of order $n$, then $\overline{z}$ is also a root of unity of order $n.$

### Exercise 1.4
Find all complex roots of the equation $z^4 = 1$, and express them in exponential form.

### Exercise 1.5
Let $z = \cos \theta + i \sin \theta$. Prove that $z^n + z^{-n} = 2 \cos(n\theta)$.

### Exercise 1.6
Prove the triangle inequality $|z_1 + z_2| \leq |z_1| + |z_2|$ for complex numbers using the conjugate method.

### Exercise 1.7
Show that if $|z| = 1$, then $z + \overline{z} = 2 \text{Re}(z)$.

**Solution 1.5**: Let $z = e^{i\theta}$. Then $z^{-1} = e^{-i\theta}$, so:

$$z^n + z^{-n} = e^{in\theta} + e^{-in\theta} = (\cos(n\theta) + i\sin(n\theta)) + (\cos(n\theta) - i\sin(n\theta)) = 2\cos(n\theta)$$

∎

**Solution 1.7**: If $|z| = 1$, then $z\overline{z} = |z|^2 = 1$, so $\overline{z} = 1/z$. Then:

$$z + \overline{z} = z + \frac{1}{z} = \frac{z^2 + 1}{z}$$

For $z = \cos \theta + i \sin \theta$, we have $\text{Re}(z) = \cos \theta$, so:

$$2\text{Re}(z) = 2\cos \theta$$

∎

## 1.8 Additional Exercises

### Exercise 1.8
Prove that $e^{i\pi/2} = i$ using Euler's Formula.

### Exercise 1.9
Find the four fourth roots of $-1$ and express them in exponential form.

### Exercise 1.10
Let $z = 2e^{i\pi/3}$. Compute $z^5$ using the exponential form.

**Solution 1.10**: 
$$z^5 = (2e^{i\pi/3})^5 = 2^5 e^{i5\pi/3} = 32 e^{i5\pi/3}$$

Since $e^{i5\pi/3} = \cos(5\pi/3) + i\sin(5\pi/3) = \frac{1}{2} - i\frac{\sqrt{3}}{2}$, we have:

$$z^5 = 32\left(\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = 16 - 16i\sqrt{3}$$

∎

## 1.9 Complex Analysis Connections

### Theorem 1.14: Maximum Modulus Principle

**Statement**: If $f(z)$ is holomorphic on a domain $D$ and continuous on $\overline{D}$, then the maximum of $|f(z)|$ on $\overline{D}$ is attained on the boundary $\partial D$, unless $f(z)$ is constant.

**Proof**: 
Suppose $|f(z)|$ attains a maximum at an interior point $z_0$. By the Cauchy-Riemann equations, $f$ is holomorphic at $z_0$, and the modulus cannot have a local extremum at an interior point unless $f$ is constant. This can be shown using the fact that holomorphic functions satisfy the mean value property. ∎

### Theorem 1.15: Cauchy's Integral Formula

**Statement**: If $f(z)$ is holomorphic on and inside a simple closed contour $C$, and $z_0$ is inside $C$, then:

$$f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} \, dz$$

**Proof**: 
This is a fundamental result in complex analysis. The proof uses Cauchy's theorem for simply connected domains and the fact that $\frac{1}{z - z_0}$ is analytic everywhere except at $z_0$. The kernel $\frac{1}{z - z_0}$ is used to "pick out" the value of $f$ at $z_0$. ∎

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
=======
# Complex Numbers

## 1.1 The Complex Number System

Complex numbers extend the real number system to include solutions to equations like $x^2 = -1$. A complex number is expressed as:

$$z = a + bi$$

where $a, b \in \mathbb{R}$ and $i$ is the imaginary unit with $i^2 = -1$.

### 1.1.1 The Complex Plane

The complex plane (or Argand plane) is a two-dimensional coordinate system where:
- The horizontal axis represents the real part ($\text{Re}(z) = a$)
- The vertical axis represents the imaginary part ($\text{Im}(z) = b$)

A complex number $z = a + bi$ corresponds to the point $(a, b)$ or the vector from the origin to $(a, b)$.

### 1.1.2 Operations with Complex Numbers

**Addition:**
$$(a + bi) + (c + di) = (a + c) + (b + d)i$$

**Subtraction:**
$$(a + bi) - (c + di) = (a - c) + (b - d)i$$

**Multiplication:**
$$(a + bi)(c + di) = (ac - bd) + (ad + bc)i$$

**Division:**
To divide $z_1 = a + bi$ by $z_2 = c + di$ (where $d \neq 0$), multiply by the conjugate:
$$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i$$

## 1.2 Modulus and Conjugate

### 1.2.1 The Modulus

The modulus (or absolute value) of a complex number $z = a + bi$ is:
$$|z| = \sqrt{a^2 + b^2}$$

**Theorem 1.1:** For any complex numbers $z, w$, the triangle inequality holds:
$$|z + w| \leq |z| + |w|$$

*Proof:* Let $z = a + bi$ and $w = c + di$. Then:
$$|z + w|^2 = |(a + c) + (b + d)i|^2 = (a + c)^2 + (b + d)^2 = a^2 + 2ac + c^2 + b^2 + 2bd + d^2$$

Also:
$$|z|^2 + |w|^2 = a^2 + b^2 + c^2 + d^2$$

And:
$$|z||w| = \sqrt{(a^2 + b^2)(c^2 + d^2)}$$

Using the Cauchy-Schwarz inequality $(a c + b d)^2 \leq (a^2 + b^2)(c^2 + d^2)$, we have:
$$|z + w|^2 = |z|^2 + |w|^2 + 2(ac + bd) \leq |z|^2 + |w|^2 + 2|z||w| = (|z| + |w|)^2$$

Taking square roots gives $|z + w| \leq |z| + |w|$. ∎

### 1.2.2 The Conjugate

The complex conjugate of $z = a + bi$ is $\overline{z} = a - bi$.

**Theorem 1.2:** For any complex number $z = a + bi$:
1. $z \cdot \overline{z} = |z|^2 = a^2 + b^2$
2. $\overline{z + w} = \overline{z} + \overline{w}$
3. $\overline{zw} = \overline{z}\overline{w}$
4. $|\overline{z}| = |z|$

*Proof of (1):* $z \cdot \overline{z} = (a + bi)(a - bi) = a^2 - (bi)^2 = a^2 - b^2(-1) = a^2 + b^2 = |z|^2$. ∎

### 1.2.3 Polar Form

Any non-zero complex number can be expressed in polar form:
$$z = r(\cos \theta + i \sin \theta) = re^{i\theta}$$

where:
- $r = |z|$ is the modulus
- $\theta = \arg(z)$ is the argument (angle with the positive real axis)

**Theorem 1.3 (De Moivre's Formula):** For any integer $n$ and complex number $z = r(\cos \theta + i \sin \theta)$:
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

*Proof (inductive):* 
- Base case ($n = 1$): Trivially true.
- Assume true for $n = k$: $(\cos \theta + i \sin \theta)^k = \cos(k\theta) + i \sin(k\theta)$.
- For $n = k + 1$:
  $$(\cos \theta + i \sin \theta)^{k+1} = (\cos \theta + i \sin \theta)(\cos(k\theta) + i \sin(k\theta))$$
  $$= \cos\theta\cos(k\theta) - \sin\theta\sin(k\theta) + i(\sin\theta\cos(k\theta) + \cos\theta\sin(k\theta))$$

Using the angle addition formulas, this equals $\cos((k+1)\theta) + i\sin((k+1)\theta)$. ∎

## 1.3 Euler's Formula

**Theorem 1.4 (Euler's Formula):** For any real number $\theta$:
$$e^{i\theta} = \cos \theta + i \sin \theta$$

*Proof:* Define $f(\theta) = e^{i\theta} = \cos \theta + i \sin \theta$. Differentiating:
$$f'(\theta) = -\sin \theta + i \cos \theta = i(\cos \theta + i \sin \theta) = i f(\theta)$$

This differential equation has the unique solution $f(\theta) = f(0)e^{i\theta} = e^{i\theta}$. ∎

## 1.4 The $n$-th Roots of Unity

The $n$-th roots of unity are the complex numbers satisfying $z^n = 1$.

**Theorem 1.5:** The $n$-th roots of unity are given by:
$$z_k = e^{i\frac{2\pi k}{n}} = \cos\left(\frac{2\pi k}{n}\right) + i\sin\left(\frac{2\pi k}{n}\right)$$
for $k = 0, 1, 2, \dots, n-1$.

These roots form a regular $n$-gon in the complex plane with one vertex at $1$.

## 1.5 Gaussian Integers

Gaussian integers are complex numbers of the form $a + bi$ where $a, b \in \mathbb{Z}$.

**Theorem 1.6 (Gaussian Integer Factorization):** Every non-zero Gaussian integer can be uniquely factorized into irreducible Gaussian primes, up to the order of factors and multiplication by units ($\pm 1, \pm i$).

*Proof sketch:* The Gaussian integers $\mathbb{Z}[i]$ form a Euclidean domain with the norm $N(a+bi) = a^2 + b^2$. Since every Euclidean domain is a Unique Factorization Domain (UFD), the theorem follows. ∎

## Exercises

1. Prove that if $|z| = 1$, then $\overline{z} = \frac{1}{z}$.
2. Show that the set of complex numbers $\{z : |z - i| = |z + i|\}$ is the real axis.
3. Prove the parallelogram law for complex numbers: $|z + w|^2 + |z - w|^2 = 2(|z|^2 + |w|^2)$.
4. Find all complex solutions to $z^4 = 16$.
5. Prove that $\mathbb{Z}[i]$ is not a field (e.g., find $z \in \mathbb{Z}[i] \setminus \{0\}$ that has no multiplicative inverse in $\mathbb{Z}[i]$).


### Fundamental Theorem of Algebra

**Theorem:** Every non-constant polynomial equation with complex coefficients has at least one complex root.

**Proof:** This can be proven using the maximum modulus principle and Liouville's theorem. Since a non-constant polynomial function tends to infinity as z approaches infinity, and by Liouville's theorem any bounded entire function is constant, a polynomial with no roots would lead to a contradiction.

---
*This theorem is the cornerstone of complex analysis and field theory.*
>>>>>>> b99e2a35ba3ed90f15a535bf294bd9753445bc2d
