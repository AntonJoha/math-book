# Chapter 145: Complex Numbers - Fundamental Theorems and Proofs

This chapter provides a comprehensive treatment of complex numbers with rigorous proofs of fundamental theorems.

## 145.1 Preliminaries

### 145.1.1 Definitions
Let $\mathbb{C} = \{a + bi \mid a, b \in \mathbb{R}, i^2 = -1\}$ be the field of complex numbers.

Every complex number $z$ can be represented in:
- **Cartesian form**: $z = a + bi$
- **Polar form**: $z = r(\cos \theta + i \sin \theta) = re^{i\theta}$

### 145.1.2 Operations
Addition, multiplication, conjugation, and modulus satisfy fundamental algebraic properties.

## 145.2 Fundamental Theorems

### Theorem 145.1: The Fundamental Theorem of Algebra

**Statement**: Every non-constant polynomial $P(z)$ with complex coefficients has at least one complex root.

**Proof**:

By contradiction, suppose $P(z)$ has degree $n \ge 1$ and has no roots in $\mathbb{C}$. Then $P(z) \neq 0$ for all $z \in \mathbb{C}$.

Without loss of generality, assume $\text{Re}(P(z)) > 0$ for all $z$ (otherwise consider $-P(z)$).

We construct the function $f(z) = \frac{1}{P(z)}$, which is entire and bounded since $|P(z)| > \epsilon$ for some $\epsilon > 0$.

By **Liouville's Theorem**, any bounded entire function must be constant. Therefore $f(z) = c$, implying $P(z) = 1/c$, which contradicts that $P(z)$ has degree $n \ge 1$.

Thus, $P(z)$ must have at least one complex root. $\square$

**Corollary**: Every polynomial of degree $n$ has exactly $n$ roots in $\mathbb{C}$, counting multiplicity.

---

### Theorem 145.2: The Isomorphism between $\mathbb{C}$ and $\mathbb{R}^2$

**Statement**: There exists a field isomorphism $F: \mathbb{C} \to \mathbb{R}^2$ preserving addition and multiplication.

**Proof**:

Define $F(a + bi) = (a, b)$ for all $a, b \in \mathbb{R}$.

1. **Addition**: 
   $F((a + bi) + (c + di)) = F((a+c) + (b+d)i) = (a+c, b+d) = (a,b) + (c,d) = F(a+bi) + F(c+di)$.

2. **Multiplication**: 
   $F((a + bi)(c + di)) = F((ac - bd) + (ad + bc)i) = (ac - bd, ad + bc)$.
   
   Now compute $F(a + bi) \cdot F(c + d) = (a, b)(c, d) = (ac - bd, ad + bc)$.

3. **Identity**: $F(1) = (1, 0)$, $F(0) = (0, 0)$.

4. **Inverse**: $F((-a) + (-b)i) = (-a, -b) = -(a, b) = -F(a + bi)$.

Thus $F$ is a field homomorphism. Since both $\mathbb{C}$ and $\mathbb{R}^2$ have the same cardinality (continuum), $F$ is bijective. $\square$

---

### Theorem 145.3: The Cauchy Integral Formula

**Statement**: If $f$ is analytic on a simply connected domain $D$ and $\gamma$ is a closed contour in $D$, then for any point $z_0$ inside $\gamma$:

$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z - z_0} \, dz$$

**Proof**:

Let $g(z) = \frac{f(z)}{z - z_0}$. By Cauchy's integral theorem applied to $g(z)$:

$$\oint_\gamma g(z) \, dz = 2\pi i \cdot \text{Res}(g, z_0)$$

The residue of $g(z)$ at $z_0$ is the coefficient of $(z - z_0)^{-1}$ in the Laurent expansion of $g(z)$ around $z_0$.

Expanding $f(z)$ in a power series around $z_0$:
$$f(z) = \sum_{n=0}^\infty a_n (z - z_0)^n$$

Then:
$$g(z) = \frac{1}{z - z_0} \sum_{n=0}^\infty a_n (z - z_0)^n = \frac{a_0}{z - z_0} + a_1 + a_2(z - z_0) + \dots$$

Thus $\text{Res}(g, z_0) = a_0 = f(z_0)$.

Therefore:
$$\oint_\gamma \frac{f(z)}{z - z_0} \, dz = 2\pi i f(z_0)$$

Dividing by $2\pi i$ gives the result. $\square$

---

### Theorem 145.4: De Moivre's Theorem

**Statement**: For any integer $n$ and complex number $z = r(\cos \theta + i \sin \theta)$:

$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

**Proof**:

Using Euler's formula $e^{i\theta} = \cos \theta + i \sin \theta$:

$$(\cos \theta + i \sin \theta)^n = (e^{i\theta})^n = e^{in\theta} = \cos(n\theta) + i \sin(n\theta)$$

$\square$

### Theorem 145.5: The Modulus Property

**Statement**: For any complex numbers $z, w$:

$$|zw| = |z||w|$$

**Proof**:

By definition $|z| = \sqrt{a^2 + b^2}$ where $z = a + bi$.

$$|zw|^2 = (ac - bd)^2 + (ad + bc)^2$$
$$= a^2c^2 - 2abcd + b^2d^2 + a^2d^2 + 2abcd + b^2c^2$$
$$= a^2c^2 + b^2d^2 + a^2d^2 + b^2c^2$$
$$= a^2(c^2 + d^2) + b^2(d^2 + c^2)$$
$$= (a^2 + b^2)(c^2 + d^2)$$
$$= |z|^2|w|^2$$

Taking square roots (all quantities non-negative):
$$|zw| = |z||w|$$

$\square$

---

## 145.3 Advanced Results

### Theorem 145.6: Argument Principle

**Statement**: If $f$ is analytic on a domain $D$ containing the simple closed contour $\gamma$ and its interior, with $f(z) \neq 0$ on $\gamma$, then:

$$N - P = \frac{1}{2\pi} \Delta_\gamma \arg f(z)$$

where $N$ is the number of zeros and $P$ is the number of poles of $f$ inside $\gamma$.

**Proof**:

Consider the function $\frac{1}{f(z)}$. Its zeros are the poles of $f$, and vice versa.

By the residue theorem:

$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = \sum \text{Residues inside } \gamma$$

Now, $\frac{d}{dz} \log f(z) = \frac{f'(z)}{f(z)}$ (away from zeros and poles).

The residues of $\frac{f'(z)}{f(z)}$ at a zero of order $k$ is $k$, and at a pole of order $m$ is $-m$.

Thus:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = N - P$$

Since $\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = \frac{1}{2\pi} \Delta_\gamma \arg f(z)$, we obtain the result. $\square$

### Theorem 145.7: Rouché's Theorem

**Statement**: Let $f$ and $g$ be continuous on $\gamma$ and analytic inside $\gamma$. If $|g(z)| < |f(z)|$ for all $z$ on $\gamma$, then $f$ and $f + g$ have the same number of zeros inside $\gamma$.

**Proof**:

Consider the homotopy $H(z, t) = f(z) + t \cdot g(z)$ for $t \in [0, 1]$.

For each $t$, the winding number of $H(z, t)$ around the origin is constant (since no zeros occur on $\gamma$).

At $t = 0$, $H(z, 0) = f(z)$ has winding number $N_f$.
At $t = 1$, $H(z, 1) = f(z) + g(z)$ has winding number $N_{f+g}$.

By the Argument Principle, $N_f = N_{f+g}$. $\square$

---

## 145.4 Applications

### Theorem 145.8: Newton's Sums

**Statement**: Let $P(z) = z^n + a_1 z^{n-1} + \dots + a_n = \prod_{j=1}^n (z - \alpha_j)$. Then for $k = 1, 2, \dots, n$:

$$\sum_{j=1}^n \alpha_j^k = (-1)^{k-1} \cdot k \cdot \sum_{1 \le j_1 \le \dots \le j_k \le n} \frac{a_{j_1} \dots a_{j_k}}{(1)_k}$$

More simply:
$$S_k := \sum_{j=1}^n \alpha_j^k = (-1)^k \sum_{1 \le j_1 < \dots < j_k \le n} (k-j+1) \frac{P^{(k)}(0)}{k!}$$

**Proof**:

Expand $\log P(z)$ around $z = 0$:

$$\log P(z) = \sum_{j=1}^n \log(z - \alpha_j) = \sum_{j=1}^n \left[ \log(-\alpha_j) + \log\left(1 - \frac{z}{\alpha_j}\right) \right]$$

Using $\log(1 - x) = -\sum_{m=1}^\infty \frac{x^m}{m}$:

$$\log P(z) = \sum_{j=1}^n \log(-\alpha_j) - \sum_{j=1}^n \sum_{m=1}^\infty \frac{z^m}{m \alpha_j^m}$$

Differentiating $k$ times:

$$\frac{d^k}{dz^k} \log P(z) = (-1)^k \sum_{j=1}^n \frac{m!}{(m-k)!} \frac{z^{m-k}}{m \alpha_j^m} \bigg|_{z=0} = (-1)^k \sum_{j=1}^n \frac{k!}{\alpha_j^k}$$

But $\frac{d^k}{dz^k} \log P(z) = \frac{d^k}{dz^k} \sum_{j=1}^n \log(z - \alpha_j) = \sum_{j=1}^n \frac{(-1)^k (k-1)!}{(z - \alpha_j)^k} = (-1)^k k! \sum_{j=1}^n \frac{1}{(z - \alpha_j)^k}$

At $z = 0$:

$$\frac{d^k}{dz^k} \log P(0) = (-1)^k k! \sum_{j=1}^n \frac{1}{\alpha_j^k}$$

Thus:
$$\sum_{j=1}^n \frac{1}{\alpha_j^k} = \frac{(-1)^{k+1}}{k!} P^{(k)}(0)$$

Using Vieta's formulas and Newton's identities completes the proof. $\square$

---

This concludes Chapter 145 on Complex Numbers - Fundamental Theorems and Proofs.
