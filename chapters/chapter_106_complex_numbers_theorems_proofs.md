# Chapter 106: Complex Numbers - Theorems and Proofs

## 106.1 Fundamental Theorem of Algebra

### Theorem 106.1
Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

**Proof:**
By contradiction, assume there exists a polynomial $P(z) = a_n z^n + \dots + a_0$ with $a_n \neq 0$ that has no roots. Since polynomials are continuous functions and $\lim_{|z|\to\infty} P(z) = \infty$, and assuming no roots means $P(z) \neq 0$ everywhere, we can consider $1/P(z)$. By Liouville's theorem (analytic functions bounded on the complex plane must be constant), this leads to a contradiction. Thus, every non-constant polynomial has at least one complex root.

**Corollary:** Every polynomial of degree $n$ has exactly $n$ roots (counting multiplicity).

## 106.13: Additional Complex Number Theorems

### Theorem 106.13.1 (Brouwer Fixed-Point Theorem Application)
**Statement:** Every continuous function from a compact convex set in ℂ to itself has a fixed point.

**Proof:** For the unit disk (compact, convex), apply the Schwarz-Pick theorem. If f: D→D is holomorphic with no fixed point, then the iterates f^n(z) either escape or converge to a boundary point, contradicting compactness.

### Theorem 106.13.2 (Maximum Modulus Principle)
**Statement:** If f is holomorphic on a domain D and |f(z)| achieves a maximum at an interior point, then f is constant.

**Proof:** By the open mapping theorem, if f is non-constant, f(D) is open, so |f| cannot achieve a maximum in the interior.

### Theorem 106.10 (Weierstrass Factorization Theorem)
Every entire function $f(z)$ can be written as:
$$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_p\left(\frac{z}{z_n}\right)$$
where $z_n$ are the non-zero zeros of $f$, $m$ is the order of the zero at the origin, $g$ is entire, and $E_p(u) = (1-u)e^{u + u^2/2 + \dots + u^p/p}$ are elementary factors with $p \geq 0$ chosen so that $\sum |z_n|^{-(p+1)}$ converges.

**Proof**: This is a classic result in complex analysis. The construction uses Mittag-Leffler type ideas for entire functions. The elementary factors converge uniformly on compact sets away from the zeros, and $e^{g(z)}$ handles the genus of the function.

### Theorem 106.11 (Schwarz-Christoffel Mapping)
The map:
$$f(z) = A\int_z^1 \prod_{k=1}^n \frac{\xi-\alpha_k}{\xi-\beta_k} d\xi + B$$
maps the unit disk conformally onto the interior of a polygon with vertices at $A\beta_j + B$ and interior angles $(\alpha_k-1)\pi$.

**Proof**: The integrand has poles at $\beta_k$ with residue-related behavior that creates the required angle changes. By solving the differential equation for polygonal mappings, this gives an explicit conformal map.

### Theorem 106.12 (Jensen's Formula)
Let $f$ be holomorphic in $\overline{D(0,R)}$ with $f(0) \neq 0$. Then:
$$\log|f(0)| = \frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|d\theta - \sum_{|z_n|<R}\log\frac{R}{|z_n|}$$
where $z_n$ are the zeros of $f$ in $D(0,R)$.

**Proof**: Apply the argument principle to $f(z)$ on the circle $|z|=R$. The integral of $f'/f$ counts zeros, and relating this to the mean value of $\log|f|$ on the boundary gives the formula.

### Theorem 106.13 (Great Picard Theorem)
Let $f$ be holomorphic in a punctured neighborhood of an essential singularity $z_0$. Then $f$ takes every complex value (with at most one exception) infinitely often in any neighborhood of $z_0$.

**Proof**: This follows from Casorati-Weierstrass theorem and the properties of essential singularities. If $f$ omits two values, we can construct a bounded entire function that is not constant, contradicting Liouville's theorem.

### Theorem 106.14 (Little Picard Theorem)
An entire function that is not a polynomial must take every complex value infinitely often, with at most one exception.

**Proof**: If $f$ is entire and omits two values, then $e^{f(z)}$ would omit all but one value, leading to a contradiction via properties of exponential functions and Liouville's theorem.

### Theorem 106.15 (Hadamard Factorization Theorem)
Let $f$ be an entire function of finite order $\rho$. Then:
$$f(z) = z^m e^{Q(z)} \prod_{n=1}^\infty \left(1-\frac{z}{z_n}\right) e^{\frac{z}{z_n} + \frac{z^2}{2z_n^2} + \dots + \frac{z^p}{pz_n^p}}$$
where $Q(z)$ is a polynomial of degree at most $\lfloor\rho\rfloor$, $z_n$ are non-zero zeros, and $p \geq \rho$.

**Proof**: This is a refinement of Weierstrass factorization for entire functions of finite order. The exponential factor $e^{Q(z)}$ accounts for the growth order, and the elementary products handle the zeros.

## 106.10: Complex Analysis Theorems (Extended)

**Theorem 106.10.1** (Cauchy's Integral Formula - General Form)
Let $f$ be holomorphic on and inside a simple closed contour $\gamma$, and let $z_0$ be inside $\gamma$. Then:
$$f(z_0) = \frac{1}{2\pi i}\int_\gamma \frac{f(z)}{z-z_0}dz$$

**Proof**: Follows from Cauchy's theorem applied to $f(z)/(z-z_0)^k$ for $k=1$.

**Theorem 106.10.2** (Cauchy's Integral Formula for Derivatives)
Let $f$ be holomorphic on and inside $\gamma$, and $z_0$ inside $\gamma$. Then:
$$f^{(n)}(z_0) = \frac{n!}{2\pi i}\int_\gamma \frac{f(z)}{(z-z_0)^{n+1}}dz$$

**Proof**: Differentiate the Cauchy integral formula $n$ times under the integral sign, justified by uniform convergence.

**Theorem 106.10.3** (Cauchy's Estimate)
If $|f(z)| \leq M$ on $|z-z_0| = R$, then:
$$|f^{(n)}(z_0)| \leq \frac{n! M}{R^n}$$

**Proof**: Apply the derivative formula with $R$ large; optimize to get the bound.

**Theorem 106.10.4** (Taylor's Inequality)
If $|f^{(n+1)}(z)| \leq M$ on $D(z_0, R)$, then for $|z-z_0| \leq R$:
$$|f(z) - \sum_{k=0}^n \frac{f^{(k)}(z_0)}{k!}(z-z_0)^k| \leq \frac{M|z-z_0|^{n+1}}{((n+1)!)^\frac{n+2}{n+1}}$$

**Proof**: Follows from the Lagrange form of the remainder in Taylor's theorem.

**Theorem 106.10.5** (Laurent's Theorem)
If $f$ is holomorphic on an annulus $A = \{z : r < |z-z_0| < R\}$, then $f$ has a Laurent series expansion valid on $A$.

**Proof**: Expand $f(z)/(z-z_0)^{n+1}$ as a geometric series and integrate term by term.

**Theorem 106.10.6** (Residue Theorem)
Let $\gamma$ be a positively oriented simple closed contour, and let $f$ be holomorphic except for isolated singularities $z_1, \dots, z_n$ inside $\gamma$. Then:
$$\int_\gamma f(z)dz = 2\pi i\sum_{j=1}^n \text{Res}(f,z_j)$$

**Proof**: Apply Cauchy's integral formula to each singularity by deforming $\gamma$ into small circles around each $z_j$.

**Theorem 106.10.7** (Argument Principle)
Let $f$ be holomorphic on and inside $\gamma$, with only zeros inside $\gamma$. Let $N$ be the number of zeros and $P$ the number of poles (counted with multiplicity). Then:
$$\frac{1}{2\pi i}\int_\gamma \frac{f'(z)}{f(z)}dz = N - P$$

**Proof**: For each zero $z_j$ of order $m_j$, near $z_j$, $f(z) \approx c(z-z_j)^{m_j}$, so $f'/f \approx m_j/(z-z_j)$. Integrating gives $2\pi i m_j$.

## 106.2 De Moivre's Theorem

### Theorem 106.2
For any integer $n$ and complex number $z = r(\cos \theta + i \sin \theta)$:
$$z^n = r^n(\cos(n\theta) + i \sin(n\theta))$$

**Proof:**
By induction on $n \geq 0$. Base case $n=0$: $z^0 = 1 = r^0(\cos(0) + i \sin(0))$. 
For the inductive step, assume true for $n$, then:
$z^{n+1} = z^n \cdot z = r^n(\cos n\theta + i \sin n\theta) \cdot r(\cos \theta + i \sin \theta)$
$= r^{n+1}[(\cos n\theta \cos \theta - \sin n\theta \sin \theta) + i(\sin n\theta \cos \theta + \cos n\theta \sin \theta)]$
Using angle addition formulas, this equals $r^{n+1}(\cos(n+1)\theta + i \sin(n+1)\theta)$.

**Application:** Finding $n$-th roots of unity involves setting $r=1$ and solving $e^{in\theta} = 1$, giving $\theta_k = \frac{2\pi k}{n}$ for $k=0,1,\dots,n-1$.

## 106.3 Cauchy-Riemann Equations

### Theorem 106.3
A complex-valued function $f(z) = u(x,y) + iv(x,y)$ is differentiable at $z_0$ if and only if $u_x = v_y$ and $u_y = -v_x$ at $(x_0, y_0)$.

**Proof:**
Direct from the definition of complex differentiability: $f'(z) = \lim_{h\to 0} \frac{f(z+h) - f(z)}{h}$ exists iff partial derivatives exist and satisfy Cauchy-Riemann equations. Differentiation of $f(x) = f(z)$ w.r.t. $x$ and $y$ yields the system above.

## 106.4 Euler's Formula

### Theorem 106.4
For real $t$, $e^{it} = \cos t + i \sin t$.

**Proof:**
Define $e^z = \sum_{n=0}^\infty \frac{z^n}{n!}$ for complex $z$. For $z=it$:
$e^{it} = \sum_{n=0}^\infty \frac{(it)^n}{n!} = 1 + it + \frac{(it)^2}{2!} + \frac{(it)^3}{3!} + \dots$
$= (1 - \frac{t^2}{2!} + \frac{t^4}{4!} - \dots) + i(t - \frac{t^3}{3!} + \frac{t^5}{5!} - \dots)$
$= \cos t + i \sin t$.

**Converse:** Using polar form $z = re^{i\theta}$ and $r = |z|$, we get the polar representation of complex numbers.


## 106.1: Algebraic Conjugation Properties

**Theorem 106.1.1** (Algebraic Conjugation Distributes over Addition and Multiplication)
For all $z_1, z_2 \in \mathbb{C}$:
$$\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2} \quad \text{and} \quad \overline{z_1 z_2} = \overline{z_1}\overline{z_2}$$

*Proof*: Let $z_1 = a+bi$ and $z_2 = c+di$ where $a,b,c,d \in \mathbb{R}$.
Then $\overline{z_1} = a-bi$ and $\overline{z_2} = c-di$.

For addition:
$$\overline{z_1 + z_2} = \overline{(a+c) + (b+d)i} = (a+c) - (b+d)i = (a-bi) + (c-di) = \overline{z_1} + \overline{z_2}$$

For multiplication:
$$z_1 z_2 = (a+bi)(c+di) = (ac-bd) + (ad+bc)i$$
$$\overline{z_1 z_2} = (ac-bd) - (ad+bc)i$$

And $\overline{z_1}\overline{z_2} = (a-bi)(c-di) = (ac-bd) - (ad+bc)i$.

**Theorem 106.1.2** (Modulus is Multiplicatively Invariant under Conjugation)
For all $z \in \mathbb{C}$: $|z| = |\overline{z}|$

*Proof*: $z = x+yi$, $\overline{z} = x-yi$, so
$|z| = \sqrt{x^2+y^2}$ and $|\overline{z}| = \sqrt{x^2+(-y)^2} = \sqrt{x^2+y^2}$.

## 106.2: De Moivre's Theorem Extensions

**Theorem 106.2.1** (Generalized De Moivre's Formula)
For all $z \in \mathbb{C}$ and all $n \in \mathbb{Z}$:
$$(\rho e^{i\theta})^n = \rho^n e^{in\theta}$$

*Proof*: For $n=1$, trivial. Assume true for $n=k$, then:
$$(\rho e^{i\theta})^{k+1} = (\rho e^{i\theta})^k (\rho e^{i\theta}) = \rho^k e^{ik\theta} \cdot \rho e^{i\theta} = \rho^{k+1} e^{i(k+1)\theta}$$

For negative integers, use inverses and the positive case.

**Corollary 106.2.2** (Roots of Unity)
The $n$-th roots of unity are $e^{2\pi i k/n}$ for $k=0,1,\dots,n-1$.

*Proof*: Solve $z^n = 1$. Let $z = \rho e^{i\theta}$, then $\rho^n = 1$ implies $\rho=1$, and $e^{in\theta}=1$ implies $in\theta = 2\pi i k$ for integer $k$.

**Theorem 106.2.3** (Triple Angle Formula)
$$\cos 3\theta = 4\cos^3\theta - 3\cos\theta$$
$$\sin 3\theta = 3\sin\theta - 4\sin^3\theta$$

*Proof*: Using De Moivre's: $(\cos\theta + i\sin\theta)^3 = \cos 3\theta + i\sin 3\theta$
Expanding the LHS using binomial theorem and equating real/imaginary parts gives the formulas.

## 106.3: Polar Form and Exponential Representations

**Theorem 106.3.1** (Polar Form Uniqueness)
Any nonzero complex number $z$ has a unique representation $z = \rho e^{i(\theta + 2k\pi)}$ for $k \in \mathbb{Z}$.

*Proof*: $\rho = |z| \ge 0$ is unique. $\theta$ is determined modulo $2\pi$.

**Theorem 106.3.2** (Euler's Formula Derivative)
$$\frac{d}{dx} e^{ix} = ie^{ix}$$
$$\frac{d}{dx} \cos x = -\sin x, \quad \frac{d}{dx} \sin x = \cos x$$

*Proof*: From $e^{ix} = \cos x + i\sin x$, differentiate both sides:
$ie^{ix} = \cos'x + i\sin'x \implies i(\cos x + i\sin x) = -\sin x + i\cos x$.

## 106.4: Complex Analysis Theorems

**Theorem 106.4.1** (Cauchy-Riemann Equations)
Let $f(z) = u(x,y) + iv(x,y)$. If $f$ is differentiable at $z_0 = x_0 + iy_0$, then:
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

*Proof*: Let $\Delta z = \Delta x + i\Delta y$. Then:
$$\lim_{\Delta z \to 0} \frac{f(z_0+\Delta z) - f(z_0)}{\Delta z} = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial u}{\partial y}(-i) + i\frac{\partial v}{\partial y}$$
Equating real and imaginary parts gives the C-R equations.

**Theorem 106.4.2** (Liouville's Theorem)
Every bounded entire function is constant.

*Proof*: If $f$ is entire and bounded, consider the derivative $f'$. Using Cauchy's integral formula:
$$f'(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\zeta)}{(\zeta-z)^2} d\zeta$$
For large $\gamma$, the numerator is bounded and the denominator grows quadratically, so $f' \to 0$ as $|z| \to \infty$. By Liouville's corollary, $f'$ is constant, so $f$ is linear. Boundedness then implies $f$ is constant.

## 106.5: Exercises

**Exercise 106.5.1**: Prove that if $|f(z)| \le M$ for all $|z| \le 1$, then $|f'(0)| \le M$.
*Hint*: Use Cauchy's integral formula for derivatives.

**Exercise 106.5.2**: Show that the map $z \mapsto \overline{z}$ is not holomorphic.
*Hint*: Check the Cauchy-Riemann equations.

**Exercise 106.5.3**: Find all solutions to $z^7 = 8i$ in polar form.
*Answer*: $z_k = \sqrt[7]{8} e^{i(\frac{\pi}{2} + 2\pi k)/7}$ for $k=0,\dots,6$.

## 106.6: Advanced Topics

### Theorem 106.6.1 (Fundamental Theorem of Algebra via Liouville)
Let $P(z) = a_n z^n + \dots + a_0$ be a polynomial with complex coefficients, $a_n \neq 0, n \geq 1$. Then $P(z)$ has at least one complex root.

*Proof*: Suppose $P(z) \neq 0$ for all $z \in \mathbb{C}$. Then $1/P(z)$ is an entire function. Since $P(z) \to \infty$ as $|z| \to \infty$, $1/P(z)$ is bounded. By Liouville's theorem, $1/P(z)$ is constant, so $P(z)$ is constant, contradicting $a_n \neq 0$. Thus, $P(z)$ must have a root.

### Theorem 106.6.2 (Eneström–Kakeya Theorem)
Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$ with real coefficients $0 < a_0 \leq a_1 \leq \dots \leq a_n$. Then all zeros of $P(z)$ lie in the annulus:
$$\frac{a_0}{a_n} \leq |z| \leq 1$$

### Theorem 106.6.3 (Gauss–Lucas Theorem)
The critical points of a polynomial with complex coefficients lie in the convex hull of its zeros.

*Proof*: Let $P(z) = a_n \prod_{i=1}^n (z-z_i)$ and $P'(z) = a_n n \prod_{i=1}^n (z-c_j)$. The critical points $c_j$ satisfy the mean value property for polynomials, placing them in the convex hull of the roots.

### Theorem 106.6.4 (Fundamental Theorem of Algebra via Argument Principle)
For a polynomial $P(z)$ of degree $n \geq 1$, the number of zeros (counting multiplicity) is $n$.

*Proof*: The argument principle states that for a meromorphic function $f(z)$ and a simple closed contour $\gamma$:
$$\frac{1}{2\pi i} \int_\gamma \frac{f'(z)}{f(z)} dz = N - P$$
where $N$ and $P$ are the numbers of zeros and poles inside $\gamma$. For a polynomial, $P=0$, and as $|z| \to \infty$, $P(z) \sim a_n z^n$, so the winding number is $n$.

### Theorem 106.6.5 (Schwarz–Christoffel Mapping)
Any simply connected proper subset of the complex plane can be conformally mapped to the unit disk.

*Proof*: Use Riemann Mapping Theorem. The Schwarz–Christoffel formula gives explicit mappings for polygons.

### Theorem 106.6.6 (Rouché's Theorem)
Let $f(z)$ and $g(z)$ be analytic inside and on a simple closed contour $\gamma$. If $|g(z)| < |f(z)|$ on $\gamma$, then $f(z)$ and $f(z) + g(z)$ have the same number of zeros inside $\gamma$.

*Application*: Useful for proving existence of roots in specific regions without explicit computation.

### Theorem 106.6.7 (Maximum Modulus Principle)
If $f$ is analytic on a domain $D$ and continuous on $\overline{D}$, then $|f(z)|$ attains its maximum on $\partial D$.

*Proof*: If $|f(z_0)| = M > \max_{z \in \partial D} |f(z)|$ for some interior point $z_0$, then by the open mapping theorem, $f(D)$ contains a neighborhood of $f(z_0)$. But this contradicts the maximum being attained at an interior point.

### Theorem 106.6.8 (Minimum Modulus Principle)
Let $f$ be analytic and non-zero on a domain $D$ and continuous on $\overline{D}$. Then $|f(z)|$ attains its minimum on $\partial D$.

*Proof*: Apply the maximum modulus principle to $1/f(z)$, which is also analytic on $D$.

### Theorem 106.6.9 (Fundamental Theorem of Algebra via Argument Principle - Complete Proof)
Every non-constant polynomial of degree $n \geq 1$ has exactly $n$ complex roots counting multiplicity.

*Proof*: Consider $P(z) = a_n z^n + \dots + a_0$ with $a_n \neq 0, n \geq 1$. Apply the argument principle to the contour $\gamma_R = \{z : |z| = R\}$ for large $R$. As $R \to \infty$, $P(z) \sim a_n z^n$, so the winding number of $P(\gamma_R)$ around 0 is $n$. By the argument principle, $P(z)$ has exactly $n$ zeros.

### Theorem 106.6.10 (Isolated Zeros)
If $f$ is analytic at $z_0$ and $f(z_0) = 0$, then $z_0$ is an isolated zero if there exists a neighborhood $U$ of $z_0$ such that $f(z) \neq 0$ for all $z \in U \setminus \{z_0\}$.

*Proof*: Write $f(z) = (z-z_0)^m g(z)$ where $g(z_0) \neq 0$ and $g$ is analytic at $z_0$. Since $g$ is continuous and $g(z_0) \neq 0$, there exists a neighborhood where $g(z) \neq 0$.

## 106.7: References and Further Reading

1. J. B. Conway, *Functions of One Complex Variable I*, Springer, 1995.
2. W. Rudin, *Real and Complex Analysis*, McGraw-Hill, 1986.
3. E. Hille, *Analytic Function Theory I*, American Mathematical Society, 1959.
4. N. Stein and R. Shakarchi, *Complex Analysis*, Princeton University Press, 2003.

**Corollary:** The Riemann Mapping Theorem implies that there are no conformal equivalences between different domains unless they are conformally equivalent via a Möbius transformation.

## 106.8: Exercises

1. Prove that $|\sin z| \leq \sinh|z|$ for all $z \in \mathbb{C}$.
2. Show that the set of complex numbers $z$ such that $|z| \leq 1$ and $\text{Im}(z) \geq 0$ is convex.
3. Prove that $\mathbb{C} \setminus [0, \infty)$ is simply connected.
4. Show that the function $f(z) = e^z - z$ has infinitely many zeros.
5. Prove that any bounded entire function is constant (Liouville's theorem).

## 106.9: References and Further Reading

1. J. B. Conway, *Functions of One Complex Variable I*, Springer, 1995.
2. W. Rudin, *Real and Complex Analysis*, McGraw-Hill, 1986.
3. E. Hille, *Analytic Function Theory I*, American Mathematical Society, 1959.
4. N. Stein and R. Shakarchi, *Complex Analysis*, Princeton University Press, 2003.

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

**Updated on 2026-08-23**

================================================================================
ADDITIONAL THEOREMS AND PROOFS
================================================================================


### Weierstrass Factorization Theorem


#### Statement of Weierstrass Factorization Theorem
[Complete mathematical statement and conditions]

### Proof of Weierstrass Factorization Theorem
[Detailed proof structure and steps]

---


### Schwarz-Christoffel Mapping Theorem


#### Statement of Schwarz-Christoffel Mapping Theorem
[Complete mathematical statement and conditions]

### Proof of Schwarz-Christoffel Mapping Theorem
[Detailed proof structure and steps]

---


### Jensen's Formula


#### Statement of Jensen's Formula
[Complete mathematical statement and conditions]

### Proof of Jensen's Formula
[Detailed proof structure and steps]

---


### Great Picard Theorem


#### Statement of Great Picard Theorem
[Complete mathematical statement and conditions]

### Proof of Great Picard Theorem
[Detailed proof structure and steps]

---


### Little Picard Theorem


#### Statement of Little Picard Theorem
[Complete mathematical statement and conditions]

### Proof of Little Picard Theorem
[Detailed proof structure and steps]

---


### Hadamard Factorization Theorem


#### Statement of Hadamard Factorization Theorem
[Complete mathematical statement and conditions]

### Proof of Hadamard Factorization Theorem
[Detailed proof structure and steps]

---

