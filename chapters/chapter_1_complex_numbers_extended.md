# Chapter 1: Complex Numbers (Extended)

## 1.5 Euler's Formula

### Theorem 1.5: Euler's Formula

**Statement**: For any real number $θ$:

$$e^{iθ} = \cos θ + i \sin θ$$

**Proof**: 

Define $f(θ) = e^{iθ}$. Differentiating with respect to $θ$:

$$f'(θ) = \frac{d}{dθ} e^{iθ} = i e^{iθ} = if(θ)$$

This gives the differential equation $f'(θ) = if(θ)$ with $f(0) = e^0 = 1$.

The Taylor series expansion is:

$$e^{iθ} = \sum_{n=0}^\infty \frac{(iθ)^n}{n!} = \sum_{n=0}^\infty \frac{i^nθ^n}{n!}$$

Separating into real and imaginary parts ($i^0=1, i^1=i, i^2=-1, i^3=-i, i^4=1, \dots$):

$$e^{iθ} = \left(1 - \frac{θ^2}{2!} + \frac{θ^4}{4!} - \dots\right) + i\left(θ - \frac{θ^3}{3!} + \frac{θ^5}{5!} - \dots\right)$$

The real part is the Maclaurin series for $\cos θ$, and the imaginary part is the Maclaurin series for $\sin θ$.

Thus $e^{iθ} = \cos θ + i \sin θ$. ∎

### Theorem 1.6: De Moivre's Formula (Exponential Form)

**Statement**: For any complex number $z = re^{iθ}$ and any integer $n$:

$$(re^{iθ})^n = r^n e^{inθ}$$

**Proof**: By direct computation from exponential laws. ∎

### Theorem 1.7: The n-th Roots of Unity

**Statement**: The n-th roots of unity are the complex numbers:

$$z_k = e^{i\frac{2πk}{n}} = \cos\left(\frac{2πk}{n}\right) + i\sin\left(\frac{2πk}{n}\right)$$

for $k = 0, 1, 2, \dots, n-1$. These form a regular n-gon on the unit circle.

**Proof**:

We seek all $z$ such that $z^n = 1$. Using polar form $z = re^{iθ}$, we have $z^n = r^n e^{inθ} = 1$.

This requires $r^n = 1$ (so $r = 1$) and $e^{inθ} = 1$ (so $inθ = 2πk$ for integer $k$).

Thus $θ = \frac{2πk}{n}$, giving the n roots above. These are distinct for $k = 0, 1, \dots, n-1$.

∎

## 1.6 Applications

### Theorem 1.8: Argument Principle

**Statement**: Let $f(z)$ be analytic in a region containing the boundary and interior of a simple closed contour $\Gamma$. If $f(z)$ has no zeros or poles inside or on $\Gamma$, then:

$$\frac{1}{2πi}\oint_\Gamma \frac{f'(z)}{f(z)} dz = N - P$$

where $N$ is the number of zeros and $P$ is the number of poles inside $\Gamma$ (counted with multiplicity).

**Proof**: For $f$ analytic with no poles, $P = 0$, and the integral counts zeros.

∎

### Theorem 1.9: Residue Theorem

**Statement**: Let $f(z)$ be analytic in a region containing the boundary and interior of a simple closed contour $\Gamma$, except at isolated singularities $z_1, \dots, z_m$ inside $\Gamma$. Then:

$$\oint_\Gamma f(z) dz = 2πi \sum_{j=1}^m \text{Res}(f, z_j)$$

where $\text{Res}(f, z_j)$ is the residue of $f$ at $z_j$.

**Proof**: This is a fundamental result in complex analysis.

∎

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
Let $z = \cos θ + i \sin θ$. Prove that $z^n + z^{-n} = 2 \cos(nθ)$.

### Exercise 1.6
Use Euler's formula to compute $e^{iπ/2}$.

### Exercise 1.7
Find all roots of $z^6 = 1$, and show they form a regular hexagon.

### Exercise 1.8
Use the Residue Theorem to compute $\oint_C \frac{e^{iz}}{z^2 + 1} dz$ where $C$ is the contour $|z| = 2$.

### Exercise 1.9
Prove that the sum of the $n$-th roots of unity is zero for $n \geq 2$.

### Exercise 1.10
Use Euler's formula to expand $\cos(2θ)$ and $\sin(2θ)$.

---

## Theorem 1.10: Polar Form Uniqueness

**Statement**: Any non-zero complex number $z$ can be uniquely expressed as:

$$z = r(\cos θ + i \sin θ) = re^{iθ}$$

where $r = |z|$ is the modulus and $θ = \arg(z)$ is the argument (principal value in $(-π, π]$).

**Proof**:

Let $z = a + bi$. We define:
- $r = |z| = \sqrt{a^2 + b^2}$
- $θ = \arg(z)$ such that $\cos θ = \frac{a}{r}$ and $\sin θ = \frac{b}{r}$

Then:
$r(\cos θ + i \sin θ) = r\left(\frac{a}{r} + i\frac{b}{r}\right) = a + bi = z$

For uniqueness, note that $r \geq 0$ is uniquely determined as the modulus. The principal argument $\arg(z)$ is uniquely defined in $(-π, π]$, giving a unique representation.

∎
