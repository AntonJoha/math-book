# Chapter 30: Complex Numbers - Theorems and Advanced Proofs

## 30.1 The Fundamental Theorem of Algebra - Elementary Proof

**Theorem**: Every non-constant polynomial with complex coefficients has at least one complex root.

**Elementary Proof (Without Liouville's Theorem)**:

*Proof by contradiction using the minimum modulus principle*:

1. Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$ with $n \ge 1$.
2. Consider the set $S = \{|P(z)| : z \in \mathbb{C}\}$. Since $|P(z)| \to \infty$ as $|z| \to \infty$, the function $|P(z)|$ attains a minimum value $m$ at some point $z_0$.
3. We show $z_0$ is a root:
   - For any $r > 0$, consider $P(z_0 + re^{i\theta})$ for $\theta \in [0, 2\pi)$.
   - Differentiate $|P(z)|^2$ with respect to $\theta$ at $\theta = 0$.
   - The derivative is $\text{Re}\left((P'(z_0)\overline{P(z_0)} + \dots)\right) = 0$ (since $z_0$ is a minimum).
   - This implies $P'(z_0) = 0$.
4. By induction, all derivatives $P^{(k)}(z_0) = 0$ for $k < n$, which means $P(z) = a_n(z-z_0)^n$.
5. Thus $P(z_0) = 0$. ∎

## 30.2 De Moivre's Theorem - Rigorous Proof

**Theorem**: For any real $\theta$ and integer $n$:
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

**Proof using Complex Exponential**:

1. Let $e^{i\theta} = \cos \theta + i \sin \theta$ (Euler's formula).
2. Then $e^{in\theta} = (e^{i\theta})^n$ by properties of the exponential function.
3. By Euler's formula: $e^{in\theta} = \cos(n\theta) + i \sin(n\theta)$.
4. Therefore: $(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$. ∎

**Corollary (n-th Roots)**: The equation $z^n = 1$ has exactly $n$ distinct solutions:
$$z_k = e^{2\pi i k/n} = \cos\left(\frac{2\pi k}{n}\right) + i \sin\left(\frac{2\pi k}{n}\right)$$
for $k = 0, 1, \dots, n-1$.

## 30.3 Cauchy's Integral Theorem

**Theorem**: Let $f(z)$ be analytic in a simply connected domain $D$. If $\gamma$ is a closed contour in $D$, then:
$$\oint_\gamma f(z) \, dz = 0$$

**Proof using Cauchy-Riemann Equations**:

1. Write $f(z) = u(x,y) + iv(x,y)$ where $z = x+iy$.
2. Analyticity implies $u_x = v_y$ and $u_y = -v_x$.
3. Parameterize $\gamma$ as $x(t), y(t)$ for $t \in [a,b]$ with $(x(a),y(a)) = (x(b),y(b))$.
4. $\oint_\gamma f(z) \, dz = \int_a^b [u_x dx + v_x dy + i(u_y dx + v_y dy)]$.
5. Using Green's Theorem and Cauchy-Riemann, the integral reduces to zero. ∎

## 30.4 Cauchy's Residue Theorem

**Theorem**: Let $f(z)$ be analytic on and inside a simple closed contour $\gamma$, with isolated singularities $z_1, \dots, z_n$ inside $\gamma$. Then:
$$\oint_\gamma f(z) \, dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$$

**Proof Sketch**:

1. For a simple pole at $z_k$, $\text{Res}(f, z_k) = \lim_{z\to z_k} (z-z_k)f(z)$.
2. If $f$ is analytic everywhere inside $\gamma$, the sum is empty and the integral is zero (Cauchy's Theorem).
3. By deformation of contours, we can isolate each singularity.
4. Around each simple pole, the integral of $1/(z-z_k)$ is $2\pi i$.
5. Linearity gives the general result. ∎

## 30.5 Argument Principle

**Theorem**: If $f(z)$ is analytic and nonzero inside and on a simple closed contour $\gamma$, then:
$$\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = N - P$$
where $N$ and $P$ are the numbers of zeros and poles inside $\gamma$ (counted with multiplicity).

**Proof**:

1. $\frac{f'(z)}{f(z)}$ has simple poles at zeros and poles of $f$.
2. At a zero of order $k$, $\text{Res}(\frac{f'}{f}, z_0) = k$.
3. At a pole of order $m$, $\text{Res}(\frac{f'}{f}, z_0) = -m$.
4. By Residue Theorem: $\oint \frac{f'}{f} \, dz = 2\pi i(N - P)$. ∎

## 30.6 Maximum Modulus Principle

**Theorem**: If $f(z)$ is analytic in a domain $D$, then $|f(z)|$ attains its maximum value on the boundary of any bounded subdomain $D' \subset D$.

**Proof by Contradiction**:

1. Suppose $|f(z_0)| > \sup_{\partial D'} |f(z)|$ for some $z_0 \in D'$.
2. Consider $g(z) = 1/(f(z) - f(z_0))$, which is analytic except at $z_0$.
3. On $\partial D'$, $|g(z)| < 1/|f(z_0) - f(z_0)|$.
4. By the Maximum Modulus Principle for bounded domains, $|g(z)|$ must be bounded everywhere in $D'$.
5. But $g(z_0)$ is undefined, contradiction.
6. Therefore, $|f(z)|$ attains its maximum on $\partial D'$. ∎

## 30.7 Liouville's Theorem

**Theorem**: Every bounded entire function is constant.

**Proof**:

1. By Cauchy's Estimation Formula: $|f(z)| \le \frac{M_R}{R-n} |f^{(n)}(z)|$ for any $R > |z|$ and $n \ge 1$.
2. If $f$ is bounded, $|f(z)| \le M$ for all $z$.
3. Letting $R \to \infty$, we get $|f^{(n)}(z)| = 0$ for all $n \ge 1$.
4. Thus all derivatives vanish, so $f$ is constant. ∎

## 30.8 Schwarz's Lemma

**Theorem**: If $f: \mathbb{D} \to \mathbb{D}$ is analytic with $f(0) = 0$, then:
1. $|f(z)| \le |z|$ for all $z \in \mathbb{D}$.
2. $|f'(0)| \le 1$.
3. Equality in (1) or (2) holds iff $f(z) = e^{i\theta}z$ for some real $\theta$.

**Proof**:

1. Consider $g(z) = f(z)/z$ for $z \ne 0$, $g(0) = f'(0)$. Then $g$ is analytic on $\mathbb{D}$.
2. $|g(z)| = |f(z)|/|z| \le 1$ by the maximum modulus principle.
3. Thus $|f(z)| \le |z|$ and $|f'(0)| = |g(0)| \le 1$.
4. For equality, consider the auxiliary function and apply the maximum modulus principle again. ∎

## 30.9 The Phragmén-Lindelöf Principle

**Theorem**: If $f(z)$ is entire and satisfies:
1. $|f(z)| \le M$ for all $z$ with $|\text{Im}(z)| \le H$.
2. $|f(z)| \le C e^{k|\text{Re}(z)|}$ for $|z| \to \infty$.

Then $|f(z)| \le \max(M, C)e^{k|\text{Im}(z)|}$ everywhere.

**Application**: Used to extend boundedness properties from strips to the whole plane. ∎

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*