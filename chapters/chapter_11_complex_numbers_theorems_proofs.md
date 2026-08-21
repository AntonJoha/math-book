# Chapter 11: Complex Numbers - Advanced Theorems and Proofs

## 11.1 Introduction

This chapter explores advanced theorems in complex analysis and complex number theory, including fundamental theorems, series expansions, contour integration, and applications.

## 11.2 Fundamental Theorems

### Theorem 11.1: Fundamental Theorem of Algebra

**Statement**: Every non-constant polynomial $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$ with $a_n \neq 0$ has at least one complex root. Consequently, every such polynomial factors as:
$$P(z) = a_n \prod_{k=1}^n (z - z_k)$$
where $z_1, \dots, z_n \in \mathbb{C}$ are the roots (counting multiplicity).

**Proof**: 

We prove by contradiction using the maximum modulus principle.

1. **Suppose no root exists**: Assume $P(z) \neq 0$ for all $z \in \mathbb{C}$. Then $1/P(z)$ is an entire function.

2. **Consider $1/P(z)$**: Since $P(z) \to \infty$ as $|z| \to \infty$ (leading term dominates), $|1/P(z)| \to 0$ as $|z| \to \infty$.

3. **Apply Liouville's Theorem**: The function $1/P(z)$ is entire (holomorphic everywhere) and bounded (for $|z| \geq R$, it's bounded by some $M$; for $|z| < R$, it's continuous on a compact set, hence bounded).

4. **Contradiction**: Liouville's Theorem states that every bounded entire function is constant. Thus $1/P(z) = c$, implying $P(z) = 1/c$, a contradiction since $P(z)$ is degree $n \geq 1$.

∎

### Theorem 11.2: Rouche's Theorem

**Statement**: Let $f(z)$ and $g(z)$ be holomorphic functions on a simply connected domain $D$, and let $\gamma$ be a simple closed curve in $D$. If $|f(z) + g(z)| > |g(z)|$ for all $z \in \gamma$, then $f(z) + g(z)$ and $f(z)$ have the same number of zeros inside $\gamma$, counting multiplicity.

**Proof**: 

We use the argument principle and the concept of winding number.

1. **Define the winding number**: For a holomorphic function $h(z)$ with no zeros on $\gamma$, the winding number of $h(\gamma)$ around 0 is:
   $$\frac{1}{2\pi i} \oint_\gamma \frac{h'(z)}{h(z)} dz = N$$
   where $N$ is the number of zeros inside $\gamma$.

2. **Consider $h(z) = f(z) + g(z)$**: Since $|h(z)| > |g(z)|$, we have:
   $$\left| \frac{h(z)}{g(z)} - 1 \right| > 0$$
   This implies $h(z)/g(z) \neq 1$ on $\gamma$.

3. **Deformation of path**: Since $h(z)/g(z)$ has no zeros on $\gamma$, we can continuously deform $\gamma$ while keeping the winding number unchanged.

4. **Apply to $f(z)$**: If we choose $g(z) = 0$, then $|f(z) + 0| > 0$ is trivially satisfied.

5. **Conclusion**: The winding number of $h(z)$ around $\gamma$ equals the winding number of $f(z)$ around $\gamma$, meaning they have the same number of zeros.

∎

### Theorem 11.3: Maximum Modulus Principle

**Statement**: Let $f(z)$ be holomorphic on a connected open set $U \subseteq \mathbb{C}$. If $|f(z)|$ attains its maximum at an interior point $z_0 \in U$, then $|f(z)|$ is constant on the connected component of $U$ containing $z_0$.

**Proof**: 

We use the fact that holomorphic functions satisfy the mean value property.

1. **Mean value property**: For any disk $D(z_0, r) \subseteq U$, we have:
   $$|f(z_0)| = \frac{1}{2\pi} \int_0^{2\pi} |f(z_0 + re^{i\theta})| d\theta$$

2. **Maximum at $z_0$**: By assumption, $|f(z)| \leq |f(z_0)|$ for all $z \in D(z_0, r)$.

3. **Equality implies constant modulus**: For the integral to equal the maximum value, we must have $|f(z_0 + re^{i\theta})| = |f(z_0)|$ for almost all $\theta$.

4. **Propagation to entire component**: By repeating the argument for smaller disks and using connectedness, we conclude $|f(z)|$ is constant on the connected component.

5. **By maximum modulus principle**: If $|f(z)|$ is constant on a connected open set, then $f(z)$ must be constant (since holomorphic functions with constant modulus are constant).

∎

### Theorem 11.4: Schwarz Lemma

**Statement**: Let $f: \mathbb{D} \to \mathbb{D}$ be a holomorphic function (where $\mathbb{D}$ is the open unit disk), with $f(0) = 0$. Then:
1. $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$
2. $|f'(0)| \leq 1$

If equality holds in (1) or (2) for some nonzero $z$, then $f(z) = e^{i\theta}z$ for some real $\theta$ (i.e., $f$ is a rotation).

**Proof**: 

We use the Cauchy integral formula and properties of holomorphic functions.

1. **Consider $g(z) = f(z)/z$**: Since $f(0) = 0$, $g(z)$ has a removable singularity at $0$ with $g(0) = f'(0)$.

2. **Apply maximum modulus to $g(z)$**: The function $g(z)$ maps $\mathbb{D}$ to $\mathbb{C} \setminus \{0\}$. By the maximum modulus principle applied to $1/g(z)$, we have $|g(z)| \leq \sup_{z \in \mathbb{D}} |g(z)| = 1$ (since $|f(z)| < 1$).

3. **Conclusion**: Thus $|f(z)| = |z||g(z)| \leq |z|$.

4. **Derivative bound**: Taking $z \to 0$, we get $|f'(0)| = \lim_{z \to 0} |f(z)/z| \leq 1$.

5. **Equality case**: If $|f(z_0)| = |z_0|$ for some $z_0 \neq 0$, then $|g(z_0)| = 1$. By the maximum modulus principle, $g(z)$ must be constant, so $f(z) = cz$ with $|c| = 1$.

∎

## 11.3 Series Expansions

### Theorem 11.5: Taylor Series for Holomorphic Functions

**Statement**: If $f(z)$ is holomorphic on a connected open set $U \subseteq \mathbb{C}$, then for any $z_0 \in U$, $f$ has a convergent power series expansion at $z_0$:
$$f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n$$
The series converges absolutely for $|z - z_0| < R$, where $R$ is the distance from $z_0$ to the boundary of $U$.

**Proof**: 

We use the Cauchy integral formula for derivatives.

1. **Cauchy integral formula**: For any $z \in D(z_0, R)$ where $D(z_0, R) \subseteq U$, we have:
   $$f(z) = \frac{1}{2\pi i} \oint_{\gamma} \frac{f(\zeta)}{\zeta - z} d\zeta$$
   where $\gamma$ is a circle centered at $z_0$ with radius $R$.

2. **Geometric series expansion**: For $|\frac{z - z_0}{\zeta - z_0}| < 1$, we expand:
   $$\frac{1}{\zeta - z} = \frac{1}{(\zeta - z_0) - (z - z_0)} = \frac{1}{\zeta - z_0} \sum_{n=0}^\infty \left(\frac{z - z_0}{\zeta - z_0}\right)^n$$

3. **Integrate term by term**: Substituting and integrating, we get:
   $$f(z) = \sum_{n=0}^\infty \left(\frac{1}{2\pi i} \oint_\gamma \frac{f(\zeta)(\zeta - z_0)^{n-1}}{(\zeta - z_0)^n} d\zeta\right) (z - z_0)^n = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n$$

4. **Convergence**: The series converges for $|z - z_0| < R$ by properties of geometric series.

∎

### Theorem 11.6: Cauchy's Integral Formula

**Statement**: Let $f(z)$ be holomorphic on and inside a simple closed curve $\gamma$, and let $z_0$ be in the interior of $\gamma$. Then:
$$f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(\zeta)}{\zeta - z_0} d\zeta$$

**Proof**: 

We use Green's theorem and the fact that $\partial \bar{z}$ is the identity.

1. **Consider $I = \frac{1}{2\pi i} \oint_\gamma \frac{f(\zeta)}{\zeta - z_0} d\zeta$**: We want to show $I = f(z_0)$.

2. **Apply Green's theorem**: Using the Cauchy-Riemann equations, we can convert the contour integral to a double integral over the region enclosed by $\gamma$.

3. **Differential form**: The integral can be written as:
   $$\frac{1}{2\pi i} \oint_\gamma \frac{f(\zeta)}{\zeta - z_0} d\zeta = \iint_D \frac{\partial}{\partial \bar{z}} \left(\frac{f(z)}{z - z_0}\right) dA$$
   where $D$ is the region enclosed by $\gamma$.

4. **Distributional derivative**: The derivative $\partial/\partial\bar{z} (1/(z - z_0))$ is $\pi \delta(z - z_0)$ (Dirac delta).

5. **Evaluation**: The integral evaluates to $f(z_0)$ times the "mass" of the delta function at $z_0$, which is 1.

∎

## 11.4 Contour Integration

### Theorem 11.7: Cauchy's Integral Theorem

**Statement**: Let $f(z)$ be holomorphic on a simply connected domain $U \subseteq \mathbb{C}$. If $\gamma$ is a closed piecewise smooth curve in $U$, then:
$$\oint_\gamma f(z) dz = 0$$

**Proof**: 

We use the fundamental theorem of calculus for complex integration.

1. **Antiderivative exists**: Since $U$ is simply connected and $f(z)$ is holomorphic, there exists a holomorphic function $F(z)$ such that $F'(z) = f(z)$.

2. **Path independence**: For any piecewise smooth path $\gamma$ from $z_1$ to $z_2$ in $U$, we have:
   $$\int_\gamma f(z) dz = F(z_2) - F(z_1)$$

3. **Closed curve**: If $\gamma$ is a closed curve (starting and ending at the same point), then:
   $$\oint_\gamma f(z) dz = F(z_0) - F(z_0) = 0$$

∎

### Theorem 11.8: Residue Theorem

**Statement**: Let $f(z)$ be holomorphic on and inside a simple closed curve $\gamma$, except for a finite number of isolated singularities $z_1, \dots, z_n$ inside $\gamma$. Then:
$$\oint_\gamma f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$$
where $\text{Res}(f, z_k)$ is the residue of $f(z)$ at $z_k$.

**Proof**: 

We use the concept of residues and Laurent series expansion.

1. **Residue definition**: The residue $\text{Res}(f, z_k)$ is the coefficient $a_{-1}$ in the Laurent series expansion of $f(z)$ at $z_k$:
   $$f(z) = \sum_{n=-\infty}^\infty a_n (z - z_k)^n$$

2. **Local contribution**: Near each singularity $z_k$, we can write:
   $$\oint_{\gamma_k} f(z) dz = 2\pi i \cdot \text{Res}(f, z_k)$$
   where $\gamma_k$ is a small circle around $z_k$.

3. **Additivity**: By the deformation of contours, we can deform $\gamma$ to a collection of small circles around each singularity, plus a path that cancels out.

4. **Conclusion**: Summing contributions from each singularity gives the residue theorem.

∎

## 11.5 Special Functions

### Theorem 11.9: Euler's Formula

**Statement**: For any real number $\theta$, we have:
$$e^{i\theta} = \cos \theta + i \sin \theta$$

**Proof**: 

We use power series expansions.

1. **Define $e^z$**: The exponential function is defined by the series:
   $$e^z = \sum_{n=0}^\infty \frac{z^n}{n!}$$

2. **Power series for cosine**: 
   $$\cos \theta = \sum_{n=0}^\infty \frac{(-1)^n \theta^{2n}}{(2n)!}$$

3. **Power series for sine**: 
   $$\sin \theta = \sum_{n=0}^\infty \frac{(-1)^n \theta^{2n+1}}{(2n+1)!}$$

4. **Substitute $z = i\theta$**: 
   $$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{n=0}^\infty \frac{i^n \theta^n}{n!}$$

5. **Separate even and odd terms**: 
   $$e^{i\theta} = \sum_{n=0}^\infty \frac{i^{2n} \theta^{2n}}{(2n)!} + \sum_{n=0}^\infty \frac{i^{2n+1} \theta^{2n+1}}{(2n+1)!}$$

6. **Simplify**: Using $i^{2n} = (-1)^n$ and $i^{2n+1} = i(-1)^n$:
   $$e^{i\theta} = \sum_{n=0}^\infty \frac{(-1)^n \theta^{2n}}{(2n)!} + i \sum_{n=0}^\infty \frac{(-1)^n \theta^{2n+1}}{(2n+1)!} = \cos \theta + i \sin \theta$$

∎

### Theorem 11.10: De Moivre's Formula

**Statement**: For any integer $n$ and real number $\theta$, we have:
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

**Proof**: 

We use mathematical induction and Euler's formula.

1. **Base case ($n = 1$)**: Trivial, $(\cos \theta + i \sin \theta)^1 = \cos \theta + i \sin \theta$.

2. **Inductive step**: Assume the formula holds for $n$. For $n+1$:
   $$(\cos \theta + i \sin \theta)^{n+1} = (\cos \theta + i \sin \theta)^n (\cos \theta + i \sin \theta)$$
   $= (\cos(n\theta) + i \sin(n\theta)) (\cos \theta + i \sin \theta)$$

3. **Expand using distributivity**:
   $= \cos(n\theta)\cos \theta - \sin(n\theta)\sin \theta + i(\cos(n\theta)\sin \theta + \sin(n\theta)\cos \theta)$

4. **Use trigonometric identities**:
   $= \cos(n\theta + \theta) + i \sin(n\theta + \theta) = \cos((n+1)\theta) + i \sin((n+1)\theta)$

∎

## 11.6 Complex Integration Applications

### Theorem 11.11: Evaluation of Integrals Using Residues

**Statement**: For any contour integral $\oint_\gamma f(z) dz$ where $f(z)$ is a meromorphic function (holomorphic except for isolated poles), the value is determined by the sum of residues inside $\gamma$.

**Application Example**: Evaluate $\oint_\gamma \frac{e^{iaz}}{z^2 + 1} dz$ where $\gamma$ is the unit circle $|z| = 1$.

**Proof**:

1. **Identify poles**: The function $\frac{e^{iaz}}{z^2 + 1}$ has poles where $z^2 + 1 = 0$, i.e., $z = \pm i$.

2. **Poles inside $\gamma$**: Only $z = i$ is inside the unit circle.

3. **Compute residue at $z = i$**: Using the formula for simple poles:
   $$\text{Res}\left(\frac{e^{iaz}}{z^2 + 1}, i\right) = \lim_{z \to i} (z - i) \frac{e^{iaz}}{(z - i)(z + i)} = \frac{e^{ai}}{2i}$$

4. **Apply residue theorem**:
   $$\oint_\gamma \frac{e^{iaz}}{z^2 + 1} dz = 2\pi i \cdot \frac{e^{ai}}{2i} = \pi e^{ai}$$

∎

## Exercises

### Exercise 11.1
Let $P(z)$ be a polynomial of degree $n$. Prove that $|P(z)| \to \infty$ as $|z| \to \infty$.

### Exercise 11.2
Let $f(z)$ be holomorphic on the unit disk $\mathbb{D}$ with $f(0) = 0$. Prove that $|f'(0)| \leq 1$.

### Exercise 11.3
Use Rouché's Theorem to prove that $z^3 + z^2 + z + 1$ has exactly three roots in the unit disk.

### Exercise 11.4
Prove the integral form of Cauchy's Integral Formula: If $f(z)$ is holomorphic on and inside a simple closed curve $\gamma$, and $z_0$ is in the interior of $\gamma$, then for any positive integers $m, n$:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f(\zeta)}{(\zeta - z_0)^{m+1}} d\zeta = \frac{f^{(m)}(z_0)}{m!}$$

### Exercise 11.5
Evaluate $\oint_{|z|=2} \frac{z^2 + 3z + 5}{(z - 1)(z - 3)(z - 5)} dz$ using the Residue Theorem.

### Exercise 11.6
Prove that for any holomorphic function $f(z)$ on a connected open set $U$, the image $f(U)$ is open (Open Mapping Theorem).

## Advanced Problems

**Problem 11.1**: Let $f(z)$ be an entire function. Prove that if $f(z)$ is bounded on $\mathbb{C}$, then $f(z)$ is constant.

**Problem 11.2**: Let $f(z)$ be holomorphic on the unit disk $\mathbb{D}$. Suppose that $|f(z)| \leq M |z|$ for all $z \in \mathbb{D}$. Prove that $f(z) = az$ for some constant $a$ with $|a| \leq M$.

**Problem 11.3**: Evaluate the integral $\oint_{|z|=R} \frac{e^{z^2}}{z^n} dz$ for $n \in \mathbb{Z}^+$ using Cauchy's Integral Formula for derivatives.

**Problem 11.4**: Let $f(z)$ be holomorphic on $\mathbb{C} \setminus \{0\}$. Suppose that $\lim_{z \to 0} z^2 f(z) = 0$ and $\lim_{z \to \infty} z^2 f(z) = 0$. Prove that $\text{Res}(f, 0) = 0$.

## Bibliography

1. Ahlfors, L. V. "Complex Analysis", 3rd ed. McGraw-Hill, 1979.
2. Conway, J. B. "Functions of One Complex Variable I". Springer, 1995.
3. Churchill, R. V., and Brown, J. W. "Complex Variables and Applications", 8th ed. McGraw-Hill, 1999.
4. Stein, E. M., and Shakarchi, R. "Complex Analysis", Princeton Lectures in Analysis I. Princeton University Press, 2003.
5. Titchmarsh, E. C. "The Theory of Functions of a Complex Variable", 2nd ed. Oxford University Press, 1972.
6. Apostol, T. M. "Mathematical Analysis", 2nd ed. Addison-Wesley, 2003.

*Updated on 2026-08-20*
