# Chapter 6: Advanced Complex Numbers

## 6.1 Euler's Formula and Exponential Form

### Theorem 6.1: Euler's Formula

**Statement**: For any real number $t$:

$$e^{it} = \cos t + i\sin t$$

**Proof**:

Consider the Maclaurin series expansions:

$$e^z = \sum_{n=0}^{\infty} \frac{z^n}{n!} = 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!} + \dots$$

$$\cos t = \sum_{n=0}^{\infty} \frac{(-1)^n t^{2n}}{(2n)!} = 1 - \frac{t^2}{2!} + \frac{t^4}{4!} - \dots$$

$$\sin t = \sum_{n=0}^{\infty} \frac{(-1)^n t^{2n+1}}{(2n+1)!} = t - \frac{t^3}{3!} + \frac{t^5}{5!} - \dots$$

Now consider $e^{it}$:

$$e^{it} = \sum_{n=0}^{\infty} \frac{(it)^n}{n!} = 1 + it + \frac{(it)^2}{2!} + \frac{(it)^3}{3!} + \frac{(it)^4}{4!} + \dots$$

Since $i^0 = 1, i^1 = i, i^2 = -1, i^3 = -i, i^4 = 1$, etc.:

$$e^{it} = 1 + it - \frac{t^2}{2!} - \frac{it^3}{3!} + \frac{t^4}{4!} + \frac{it^5}{5!} + \dots$$

Grouping real and imaginary parts:

$$e^{it} = \left(1 - \frac{t^2}{2!} + \frac{t^4}{4!} - \dots\right) + i\left(t - \frac{t^3}{3!} + \frac{t^5}{5!} - \dots\right)$$

$$e^{it} = \cos t + i\sin t$$

∎

### Corollary 6.1: De Moivre's Formula (Alternative Proof)

**Statement**: For any complex number $z = r(\cos \theta + i\sin \theta)$ and any integer $n$:

$$(\cos \theta + i\sin \theta)^n = \cos(n\theta) + i\sin(n\theta)$$

**Proof**:

From Theorem 6.1, we have $\cos \theta + i\sin \theta = e^{i\theta}$.

Then:

$$(\cos \theta + i\sin \theta)^n = (e^{i\theta})^n = e^{in\theta}$$

By Theorem 6.1 again:

$$e^{in\theta} = \cos(n\theta) + i\sin(n\theta)$$

∎

## 6.2 The n-th Roots of Unity

### Theorem 6.2: The n-th Roots of Unity

**Statement**: The equation $z^n = 1$ has exactly $n$ complex roots given by:

$$z_k = e^{i\frac{2\pi k}{n}} = \cos\left(\frac{2\pi k}{n}\right) + i\sin\left(\frac{2\pi k}{n}\right) \quad \text{for } k = 0, 1, \dots, n-1$$

These roots form a regular $n$-gon on the unit circle in the complex plane.

**Proof**:

Let $z = r(\cos \theta + i\sin \theta)$. Then:

$$z^n = r^n(\cos n\theta + i\sin n\theta)$$

For $z^n = 1$, we need:
1. $r^n = 1 \implies r = 1$ (since $r > 0$)
2. $\cos n\theta = 1$ and $\sin n\theta = 0$, which means $n\theta = 2\pi k$ for integers $k$

Thus $\theta = \frac{2\pi k}{n}$. Since the exponential function is $2\pi$-periodic, distinct values of $z$ correspond to $k = 0, 1, \dots, n-1$.

∎

### Theorem 6.3: Factorization of $z^n - 1$

**Statement**: The polynomial $z^n - 1$ factors as:

$$z^n - 1 = \prod_{k=0}^{n-1} (z - z_k) = \prod_{k=0}^{n-1} \left(z - e^{i\frac{2\pi k}{n}}\right)$$

**Proof**:

From Theorem 6.2, the roots of $z^n - 1 = 0$ are exactly $z_0, z_1, \dots, z_{n-1}$.

By the Fundamental Theorem of Algebra (Theorem 1.1), a monic polynomial of degree $n$ factors into $n$ linear terms over $\mathbb{C}$, with each root appearing once (since $z^n - 1$ has simple roots: its derivative $nz^{n-1}$ has no common roots with $z^n - 1$).

Thus:

$$z^n - 1 = \prod_{k=0}^{n-1} (z - z_k)$$

∎

## 6.3 Logarithms of Complex Numbers

### Theorem 6.4: Complex Logarithm

**Statement**: The complex logarithm is multi-valued:

$$\ln z = \ln|z| + i(\arg z + 2\pi k) \quad \text{for } k \in \mathbb{Z}$$

where $\ln|z|$ is the real natural logarithm of the modulus.

**Proof**:

Let $z = r(\cos \theta + i\sin \theta) = re^{i\theta}$.

Then $\ln z = \ln(re^{i\theta}) = \ln r + \ln(e^{i\theta}) = \ln r + i\theta + 2\pi i k$

for any integer $k$, since $e^{i(\theta + 2\pi k)} = e^{i\theta}$.

The principal branch is defined as $\text{Log } z = \ln|z| + i\text{Arg } z$ where $\text{Arg } z \in (-\pi, \pi]$.

∎

### Corollary 6.1: Argument Principle

**Statement**: Let $f(z)$ be analytic in a domain $D$ containing a simple closed contour $\gamma$ that does not pass through any zeros or poles of $f$. Then:

$$\frac{1}{2\pi i} \oint_{\gamma} \frac{f'(z)}{f(z)} dz = Z - P$$

where $Z$ is the number of zeros of $f$ inside $\gamma$ (counted with multiplicity) and $P$ is the number of poles inside $\gamma$ (counted with multiplicity).

**Proof**:

Consider the residue theorem. The function $\frac{f'(z)}{f(z)}$ has simple poles at the zeros and poles of $f$.

At a zero of order $m$, the Laurent expansion of $f(z)$ is $f(z) = a(z-z_0)^m + \dots$ where $a \neq 0$.

Then $\frac{f'(z)}{f(z)} = \frac{ma(z-z_0)^{m-1} + \dots}{a(z-z_0)^m + \dots} = \frac{m}{z-z_0} + \text{analytic}$.

The residue at this zero is $m$.

Similarly, at a pole of order $n$, the residue is $-n$.

By the residue theorem:

$$\frac{1}{2\pi i} \oint_{\gamma} \frac{f'(z)}{f(z)} dz = \sum \text{residues} = Z - P$$

∎

## 6.4 The Gauss-Lucas Theorem

### Theorem 6.5: Gauss-Lucas Theorem

**Statement**: If $P(z) = a_nz^n + \dots + a_0$ has roots $z_1, z_2, \dots, z_n$, then all the roots of $P'(z)$ lie in the convex hull of $\{z_1, z_2, \dots, z_n\}$.

**Proof**:

Let $Q(z) = \frac{P'(z)}{P(z)}$. Then:

$$Q(z) = \sum_{k=1}^n \frac{1}{z - z_k}$$

If $Q(z) = 0$, then:

$$\sum_{k=1}^n \frac{1}{z - z_k} = 0$$

Let $\chi$ be the convex hull of $\{z_1, \dots, z_n\}$. We show $Q(z) \neq 0$ outside $\chi$.

If $z$ is outside $\chi$, then there exists a hyperplane $H$ such that $\chi$ lies entirely on one side of $H$ and $z$ is not on the other side.

Rotate the complex plane so that $H$ is vertical and $z$ is to the right of $H$.

Then $\text{Re}(z - z_k) > 0$ for all $k$.

Thus $\text{Re}\left(\frac{1}{z - z_k}\right) = \text{Re}\left(\frac{\overline{z - z_k}}{|z - z_k|^2}\right) = \frac{\text{Re}(z - z_k)}{|z - z_k|^2} > 0$.

Therefore:

$$\text{Re}(Q(z)) = \sum_{k=1}^n \text{Re}\left(\frac{1}{z - z_k}\right) > 0$$

So $Q(z) \neq 0$ outside $\chi$.

The roots of $P'(z)$ are exactly the zeros of $Q(z)$, hence they lie in $\chi$.

∎

## 6.5 Schwarz Reflection Principle

### Theorem 6.6: Schwarz Reflection Principle

**Statement**: Let $D$ be a domain in $\mathbb{C}$ with boundary segment $L$ on the real axis. If $f$ is holomorphic on $D$ and continuous on $D \cup L$, and $f$ maps $D$ to itself while fixing $L$ pointwise, then $f$ can be extended to a holomorphic function on $\mathbb{C} \setminus \mathbb{R}$ by:

$$f(\overline{z}) = \overline{f(z)} \quad \text{for } z \in D$$

This extension is holomorphic on $\mathbb{C} \setminus \mathbb{R}$ and preserves the real axis.

**Proof**:

Define $F(z) = \begin{cases} f(z) & z \in D \\ \overline{f(\overline{z})} & z \in \overline{D} \end{cases}$

where $\overline{D} = \{\overline{z} : z \in D\}$.

$F$ is continuous on $D \cup \overline{D}$ by construction.

For $z \in D \cap \overline{D}$ (i.e., $z$ on the real axis), $F(z) = f(z)$ and $\overline{f(\overline{z})} = \overline{f(z)} = f(z)$ since $f$ fixes the real axis.

By Morera's Theorem, if $F$ satisfies $\oint_\gamma F(z) dz = 0$ for every closed triangle $\gamma$ in $\mathbb{C}$, then $F$ is holomorphic everywhere.

For any triangle $\gamma$, we can split it into two halves. If both halves are in $D$, $\oint_\gamma F dz = \oint_\gamma f dz = 0$ by holomorphicity of $f$.

Similarly if both halves are in $\overline{D}$.

If $\gamma$ crosses the real axis, we can reflect the part in $D$ to $\overline{D}$ and use the relation between $f$ and $F$.

The integral over the reflected part cancels appropriately.

Thus $F$ is holomorphic on $\mathbb{C}$.

∎

## 6.6 Jensen's Formula

### Theorem 6.7: Jensen's Formula

**Statement**: Let $f$ be holomorphic and non-zero in a disk $|z| < R$, and let $z_1, \dots, z_k$ be the zeros of $f$ in $0 < |z| < r < R$ (counted with multiplicity). Then:

$$\ln|f(0)| + \frac{1}{2\pi} \int_0^{2\pi} \ln|f(re^{i\theta})| d\theta = \sum_{j=1}^k \ln\frac{r}{|z_j|}$$

**Proof**:

Apply the Cauchy integral formula to $g(z) = \frac{f(z)}{z^n}$ where $n$ is the order of the zero at the origin (if any), or $g(z) = \frac{f(z)}{z^k}$.

Actually, consider the function:

$$h(z) = \frac{f(0)f(re^{i\theta})e^{i\theta}}{f(re^{i\theta}e^{i\theta})f(0)}$$

Using the argument principle on $f(z)$ in the disk $|z| < r$:

$$\frac{1}{2\pi} \int_0^{2\pi} \ln|f(re^{i\theta})| d\theta - \ln|f(0)| = \sum_{j=1}^k \ln\frac{r}{|z_j|}$$

Rearranging gives Jensen's Formula. ∎

## 6.7 Applications

### Theorem 6.8: Maximum Modulus Principle (Complex Version)

**Statement**: If $f$ is holomorphic in a domain $D$ and $|f|$ attains a maximum at an interior point of $D$, then $f$ is constant.

**Proof**:

Suppose $|f(z_0)| = \max_{z \in D} |f(z)|$ for some interior point $z_0$.

By the Maximum Modulus Principle for harmonic functions (applied to $\ln|f|$), $\ln|f|$ cannot have a local maximum unless $f$ is constant.

Alternatively, use Cauchy's Integral Formula:

$$f(z) = \frac{1}{2\pi i} \oint_{\partial D} \frac{f(\zeta)}{\zeta - z} d\zeta$$

If $z$ is near $z_0$ in $D$, we can show that the derivative $f'(z)$ is zero, hence $f$ is constant.

∎

### Corollary 6.2: Uniqueness of Holomorphic Functions

**Statement**: If two holomorphic functions $f$ and $g$ agree on a set with an accumulation point in a domain $D$, then $f = g$ throughout $D$.

**Proof**:

Let $S = \{z \in D : f(z) = g(z)\}$.

Since $f - g$ is holomorphic and $S$ has an accumulation point, by the Identity Theorem, $f - g$ is identically zero on $D$.

Thus $f = g$ on $D$.

∎

## 6.8 Exercises

1. **Exercise 6.1**: Show that if $n$ is even, $z^n + 1 = 0$ has roots forming a regular $n$-gon rotated by $45^\circ$ compared to $z^n - 1 = 0$.

2. **Exercise 6.2**: Prove that the function $f(z) = z + \sin z$ has no zeros for $|z| > \pi/2$.

3. **Exercise 6.3**: Use Jensen's Formula to show that if $f$ is a polynomial of degree $n$ with all roots in the unit disk, then $|f(0)| \le \prod_{j=1}^n (1 - |z_j|^2)^{-1}$.

4. **Exercise 6.4**: Let $P(z)$ be a polynomial with real coefficients. Show that all non-real roots come in complex conjugate pairs.

5. **Exercise 6.5**: Prove that the roots of $z^n + az^{n-1} + b = 0$ lie in the disk $|z| < \max(1, |a|, |b|^{1/(n-1)})$.
<<<<<<< HEAD

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
>>>>>>> b99e2a35ba3ed90f15a535bf294bd9753445bc2d
