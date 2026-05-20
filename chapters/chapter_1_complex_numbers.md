# Chapter 1: Complex Numbers

## 1.1 Introduction to Complex Numbers

Complex numbers are an extension of the real numbers that allow us to solve equations that have no real solutions. A complex number is expressed in the form:

$$z = a + bi$$

where $a$ and $b$ are real numbers, and $i$ is the imaginary unit satisfying $i^2 = -1$.

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
$r(\cos \theta + i \sin \theta) = r\left(\frac{a}{r} + i\frac{b}{r}\right) = a + bi = z

## Exercises

### Exercise 1.1
Write the complex number $3 + 4i$ in polar form, giving the argument in degrees.

### Exercise 1.2
Calculate $(1 + i)^3$ using De Moivre's Formula, showing all steps.

### Exercise 1.3
Prove that if $z$ is a root of unity of order $n$, then $\overline{z}$ is also a root of unity of order $n.$

### Exercise 1.4
Find all complex roots of the equation $z^4 = 1$, and express them in polar form.

### Exercise 1.5
Let $z = \cos \theta + i \sin \theta$. Prove that $z^n + z^{-n} = 2 \cos(n\theta)$.

## Exercises

### Exercise 1.1
Write the complex number $-3 + 4i$ in polar form, giving the argument in radians.

### Exercise 1.2
Calculate $(2 - i)^4$ using De Moivre's Formula, showing all steps.

### Exercise 1.3
Prove that if $z$ is a root of unity of order $n$, then $\overline{z}$ is also a root of unity of order $n.$

### Exercise 1.4
Find all complex roots of the equation $z^4 = 1$, and express them in polar form.

### Exercise 1.5
Let $z = \cos \theta + i \sin \theta$. Prove that $z^n + z^{-n} = 2 \cos(n\theta)$.$

For uniqueness of the principal argument in $(-\pi, \pi]$, note that sine and cosine are 2π-periodic, and the interval $(-\pi, \pi]$ contains exactly one angle whose sine and cosine match $\frac{b}{r}$ and $\frac{a}{r}$. ∎
