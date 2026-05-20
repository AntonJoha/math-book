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
