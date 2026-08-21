# Chapter 121: Complex Numbers - Fundamental Theorems and Proofs

## 121.1 Introduction

This chapter establishes the rigorous foundation of complex numbers through fundamental theorems, emphasizing their structural properties, algebraic completeness, and analytic characteristics. We explore:
- The Fundamental Theorem of Algebra
- Properties of complex conjugation
- De Moivre's Theorem
- Complex exponential properties
- The classification of complex fields

## 121.2 Fundamental Theorem of Algebra

**Theorem 121.1 (Fundamental Theorem of Algebra)**  
Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

*Proof:*  
Assume $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0$ with $a_n \neq 0$ has no roots in $\mathbb{C}$. Then $P(z) \neq 0$ for all $z$. Consider the function $1/P(z)$. If we can show $1/P(z)$ is bounded, we use Liouville's Theorem (see Chapter 36) to obtain a contradiction.

Alternatively, using topological arguments: The complex plane is the unique algebraically closed field. The proof relies on the completeness of $\mathbb{C}$ as a metric space.

**Corollary:**  
A polynomial of degree $n$ has exactly $n$ complex roots counting multiplicity.

*Proof (for corollary):*  
By induction. For $n=1$, the root is $-a_0/a_1$. Assume true for $n-1$. By Theorem 121.1, $P(z)$ has a root $z_0$. Then $P(z) = (z-z_0)Q(z)$ where $\deg(Q) = n-1$. By inductive hypothesis, $Q(z)$ has $n-1$ roots, so $P(z)$ has $n$ roots total.

## 121.3 Complex Conjugation Properties

**Theorem 121.2 (Conjugate of Product/Quotient)**  
For any complex numbers $z_1, z_2$:
$$\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$$
$$\overline{\frac{z_1}{z_2}} = \frac{\overline{z_1}}{\overline{z_2}} \quad (z_2 \neq 0)$$

*Proof:*  
Let $z_1 = a + bi$ and $z_2 = c + di$ where $a,b,c,d \in \mathbb{R}$. Then:
$$z_1 z_2 = (ac - bd) + (ad + bc)i$$
$$\overline{z_1 z_2} = (ac - bd) - (ad + bc)i$$

Now:
$$\overline{z_1} \cdot \overline{z_2} = (a - bi)(c - di) = (ac - bd) - (ad + bc)i$$

Thus $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$. The quotient follows similarly.

**Corollary:**  
$|z|^2 = z \cdot \overline{z}$

*Proof:*  
$z = a + bi$, $\overline{z} = a - bi$. Then:
$$z \cdot \overline{z} = (a + bi)(a - bi) = a^2 + b^2 = |z|^2$$

## 121.4 De Moivre's Theorem

**Theorem 121.3 (De Moivre's Theorem)**  
For any complex number $z = r(\cos \theta + i \sin \theta)$ and integer $n$:
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

*Proof:*  
By induction. Base case $n=1$ is trivial.

Assume true for $n$, then:
$$(\cos \theta + i \sin \theta)^{n+1} = (\cos \theta + i \sin \theta)^n (\cos \theta + i \sin \theta)$$
$$= (\cos(n\theta) + i \sin(n\theta))(\cos \theta + i \sin \theta)$$
$$= (\cos(n\theta)\cos \theta - \sin(n\theta)\sin \theta) + i(\sin(n\theta)\cos \theta + \cos(n\theta)\sin \theta)$$

Using addition formulas:
$$= \cos((n+1)\theta) + i \sin((n+1)\theta)$$

**Corollary (n-th roots of unity):**  
The solutions to $z^n = 1$ are $e^{2\pi k i/n}$ for $k = 0, 1, \dots, n-1$.

*Proof:*  
Let $z = r(\cos \theta + i \sin \theta)$. Then $z^n = r^n(\cos(n\theta) + i \sin(n\theta))$. For $z^n = 1$:
- $r^n = 1 \implies r = 1$
- $n\theta = 2\pi k$ for integer $k$

Thus $z = e^{2\pi k i/n}$.

## 121.5 Complex Exponential Properties

**Theorem 121.4 (Exponential Addition Formula)**  
$$e^{(z_1 + z_2)} = e^{z_1} \cdot e^{z_2}$$

*Proof:*  
Using the power series expansion $e^z = \sum_{n=0}^\infty \frac{z^n}{n!}$ and properties of absolute convergence, the Cauchy product of two absolutely convergent series can be shown to give the exponential of the sum.

**Theorem 121.5 (Complex Logarithm Properties)**  
For $z \neq 0$ and complex numbers $z_1, z_2$:
$$\log(z_1 z_2) = \log(z_1) + \log(z_2) + 2\pi k i$$
for some integer $k$ (branch dependent).

*Proof:*  
Let $z_1 = e^{w_1}$ and $z_2 = e^{w_2}$ where $w_1 = \log(z_1)$, $w_2 = \log(z_2)$. Then:
$$z_1 z_2 = e^{w_1} e^{w_2} = e^{w_1 + w_2}$$

Thus $\log(z_1 z_2) = w_1 + w_2 + 2\pi k i$ since logarithm is multi-valued.

## 121.6 Classification of Complex Numbers

**Theorem 121.6 (Real and Imaginary Classification)**  
A complex number $z = x + iy$ is:
- Real if and only if $y = 0$
- Purely imaginary if and only if $x = 0$
- Neither real nor purely imaginary otherwise

*Proof:*  
By definition of complex numbers as ordered pairs of real numbers. The classification follows directly from whether the imaginary part or real part vanishes.

**Theorem 121.7 (Argument Function)**  
For any non-zero complex number $z$, there exists a unique $\theta \in [0, 2\pi)$ such that:
$$z = |z| e^{i\theta}$$

*Proof:*  
Let $\theta = \text{Arg}(z) = \arctan_2(y, x)$ (the two-argument arctangent). Then:
$$z = x + iy = |z|(\cos \theta + i \sin \theta) = |z| e^{i\theta}$$

The uniqueness follows from the fact that $|\theta - \theta'| < 2\pi$ implies $e^{i\theta} = e^{i\theta'}$.

## 121.7 Applications and Extensions

**Theorem 121.8 (Gauss-Laplace Integral Formula)**  
For any complex number $z$:
$$e^z = \sum_{n=0}^\infty \frac{z^n}{n!} = \cos z + i \sin z \quad \text{(if } z \in \mathbb{R}\text{)}$$

*Proof:*  
Using Euler's formula $e^{i\theta} = \cos \theta + i \sin \theta$ and the power series expansions:
$$\cos z = \sum_{k=0}^\infty \frac{(-1)^k z^{2k}}{(2k)!}$$
$$\sin z = \sum_{k=0}^\infty \frac{(-1)^k z^{2k+1}}{(2k+1)!}$$

The sum of these equals the exponential series, establishing the formula for real arguments.

**Theorem 121.9 (Polar Decomposition)**  
Every complex number $z \neq 0$ has a unique polar decomposition $z = r e^{i\theta}$ where $r = |z| > 0$ and $\theta \in \mathbb{R}$ is determined modulo $2\pi$.

*Proof:*  
Let $z = x + iy$. Then $|z| = \sqrt{x^2 + y^2} = r$. Also $\tan \theta = y/x$ with $\theta \in (-\pi, \pi]$. Then:
$$r e^{i\theta} = r(\cos \theta + i \sin \theta) = r\left(\frac{x}{r} + i \frac{y}{r}\right) = x + iy = z$$

---

*End of Chapter 121*
