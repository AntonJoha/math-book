# Chapter 202: Complex Numbers - Advanced Theorems and Proofs

## 202.1 Fundamental Theorems of Algebra and Polynomials

### Theorem 202.1.1 (Fundamental Theorem of Algebra - Liouville's Proof)
**Statement:** Every non-constant polynomial with complex coefficients has at least one complex root.

**Proof:** Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$ where $n \ge 1, a_n \neq 0$. Suppose $P$ has no zeros. Then $f(z) = 1/P(z)$ is entire (holomorphic everywhere). As $|z| \to \infty$, $|P(z)| \to \infty$ (since the leading term dominates), so $|f(z)| \to 0$. Thus $f$ is bounded. By Liouville's Theorem, bounded entire functions are constant. Since $\lim_{|z|\to\infty} f(z) = 0$, we must have $f(z) = 0$, implying $P(z) \to \infty$, a contradiction. Therefore, $P(z)$ has at least one complex root. ∎

### Theorem 202.1.2 (Polynomial Degree Formula)
**Statement:** A non-constant polynomial $P(z)$ of degree $n$ has exactly $n$ roots in $\mathbb{C}$ counting multiplicity.

**Proof:** This follows from the Fundamental Theorem of Algebra by induction. If $P(z)$ has no roots, contradiction as above. If $P(z)$ has $k$ distinct roots, factor $P(z) = (z-r_1)^{m_1} \dots (z-r_k)^{m_k} Q(z)$ where $\deg(Q) = n-k$. By induction $Q(z)$ has $n-k$ roots, so $P(z)$ has $k + (n-k) = n$ roots total. ∎

### Theorem 202.1.3 (Rouche's Theorem)
**Statement:** Let $f(z)$ and $g(z)$ be holomorphic functions inside and on a simple closed contour $\Gamma$. If $|f(z)| > |g(z)|$ for all $z \in \Gamma$, then $f(z)$ and $f(z) + g(z)$ have the same number of zeros inside $\Gamma$ (counting multiplicity).

**Proof:** Let $N_h(P)$ denote the number of zeros of polynomial $P$ inside $\Gamma$. Consider the winding number $W(h) = \frac{1}{2\pi} \Delta_\Gamma \arg h$. For the function $F(z) = f(z) + g(z)$, since $|f| > |g|$ on $\Gamma$, $F(z) = f(z)(1 + g(z)/f(z))$ never vanishes on $\Gamma$. Thus $W(F) = W(f)$ because $g/f$ is bounded by $<1$ and cannot wind around zero. By the Argument Principle, $N_h(f) = W(f)$ and $N_h(F) = W(F)$, so $N_h(f) = N_h(F)$. ∎

## 202.2 Complex Arithmetic and Geometry

### Theorem 202.2.1 (Triangle Inequality)
**Statement:** For any complex numbers $z_1, z_2$, $|z_1 + z_2| \leq |z_1| + |z_2|$. Equality holds iff $z_1 = c z_2$ for some $c \geq 0$.

**Proof:** Consider $|z_1 + z_2|^2 = (z_1 + z_2)(\overline{z_1} + \overline{z_2}) = |z_1|^2 + |z_2|^2 + (z_1 \overline{z_2} + \overline{z_1} z_2) = |z_1|^2 + |z_2|^2 + 2 \text{Re}(z_1 \overline{z_2})$. By Cauchy-Schwarz, $|z_1 \overline{z_2}| \leq |z_1| |z_2|$, so $2 \text{Re}(z_1 \overline{z_2}) \leq 2 |z_1| |z_2|$. Thus $|z_1 + z_2|^2 \leq (|z_1| + |z_2|)^2$, taking square roots gives the result. Equality iff $z_1 \overline{z_2}$ is real and non-negative. ∎

### Theorem 202.2.2 (Parallelogram Law)
**Statement:** For any complex numbers $z_1, z_2$, $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$.

**Proof:** Expand both terms: $|z_1 + z_2|^2 = |z_1|^2 + |z_2|^2 + 2 \text{Re}(z_1 \overline{z_2})$ and $|z_1 - z_2|^2 = |z_1|^2 + |z_2|^2 - 2 \text{Re}(z_1 \overline{z_2})$. Adding gives $2(|z_1|^2 + |z_2|^2)$. ∎

### Theorem 202.2.3 (De Moivre's Theorem)
**Statement:** For any real $\theta$ and integer $n$, $(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$.

**Proof:** Using induction and the angle addition formulas for sine and cosine. For $n=1$, trivial. Assume true for $n$, then:
$(\cos \theta + i \sin \theta)^{n+1} = (\cos(n\theta) + i \sin(n\theta))(\cos \theta + i \sin \theta) = \cos((n+1)\theta) + i \sin((n+1)\theta)$ by angle addition. ∎

### Theorem 202.2.4 (Roots of Unity)
**Statement:** The $n$-th roots of unity are $\omega_k = e^{2\pi i k/n}$ for $k = 0, 1, \dots, n-1$, and they form a regular $n$-gon in the complex plane.

**Proof:** We need $e^{2\pi i k/n \cdot n} = e^{2\pi i k} = 1$ for all $k$. These are all distinct for $k = 0, \dots, n-1$. Geometrically, $|\omega_k| = 1$ and $\arg(\omega_k) = 2\pi k/n$, equally spaced on the unit circle. ∎

## 202.3 Complex Conjugation and Modulus

### Theorem 202.3.1 (Conjugate Properties)
**Statement:** For any complex numbers $z_1, z_2$:
1. $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
2. $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$
3. $\overline{z_1 + z_2 i} = \overline{z_1} - \overline{z_2} i$
4. $\overline{\overline{z}} = z$

**Proof:** Direct computation using $z = a + bi$, $\overline{z} = a - bi$.
1. $\overline{(a+bi) + (c+di)} = (a+c) - i(b+d) = (a-bi) + (c-di)$.
2. $\overline{(a+bi)(c+di)} = \overline{(ac-bd) + i(ad+bc)} = (ac-bd) - i(ad+bc) = (a-bi)(c-di)$.
3. $\overline{z_1 + i z_2} = \overline{z_1} - i \overline{z_2}$.
4. $\overline{\overline{(a+bi)}} = \overline{(a-bi)} = a+bi$. ∎

### Theorem 202.3.2 (Modulus Properties)
**Statement:** For any complex number $z = a + bi$:
1. $|z| = \sqrt{a^2 + b^2}$
2. $|z|^2 = z \cdot \overline{z}$
3. $|z_1 z_2| = |z_1| |z_2|$
4. $|z_1 + z_2| \leq |z_1| + |z_2|$ (Triangle inequality)

**Proof:** 
1. $|z|^2 = z \overline{z} = (a+bi)(a-bi) = a^2 + b^2$, so $|z| = \sqrt{a^2 + b^2}$.
2. $z \overline{z} = (a+bi)(a-bi) = a^2 + b^2 = |z|^2$.
3. Let $z_1 = r_1 e^{i\theta_1}, z_2 = r_2 e^{i\theta_2}$. Then $|z_1 z_2| = |r_1 e^{i\theta_1} r_2 e^{i\theta_2}| = r_1 r_2 = |z_1| |z_2|$.
4. Follows from Theorem 202.2.1. ∎

### Theorem 202.3.3 (Polar Representation)
**Statement:** Every complex number $z \neq 0$ can be uniquely written as $z = r e^{i\theta}$ where $r = |z| > 0$ and $\theta = \arg(z) \in [0, 2\pi)$.

**Proof:** Let $r = |z| = \sqrt{a^2 + b^2} > 0$. Then $z/r = (a/r) + i(b/r)$. Let $\cos \theta = a/r$, $\sin \theta = b/r$. Then $\theta = \arctan2(b, a) \in [0, 2\pi)$. Conversely, $r e^{i\theta} = r(\cos \theta + i \sin \theta) = r(a/r + ib/r) = a + ib = z$. ∎

## 202.4 Euler's Formula and Complex Exponentials

### Theorem 202.4.1 (Euler's Formula)
**Statement:** For any real number $t$, $e^{it} = \cos t + i \sin t$.

**Proof:** Define $e^z = \sum_{n=0}^\infty z^n/n!$. For $z = it$:
$e^{it} = \sum_{n=0}^\infty (it)^n/n! = 1 + it - t^2/2! - it^3/3! + t^4/4! + \dots$
$= (1 - t^2/2! + t^4/4! - \dots) + i(t - t^3/3! + t^5/5! - \dots)$
$= \cos t + i \sin t$. ∎

### Theorem 202.4.2 (General Exponential Formula)
**Statement:** For any complex number $z = x + iy$, $e^z = e^x(\cos y + i \sin y)$.

**Proof:** $e^{x+iy} = e^x e^{iy} = e^x(\cos y + i \sin y)$. ∎

### Theorem 202.4.3 (Logarithm of Complex Numbers)
**Statement:** For any non-zero complex number $z$, the complex logarithm is defined as $\log z = \ln|z| + i(\arg z + 2\pi k)$ for $k \in \mathbb{Z}$.

**Proof:** Let $z = r e^{i\theta}$. Then $e^{\ln r + i(\theta + 2\pi k)} = e^{\ln r} e^{i(\theta + 2\pi k)} = r e^{i(\theta + 2\pi k)} = r e^{i\theta} e^{i2\pi k} = z \cdot 1 = z$. ∎

## 202.5 Complex Analysis Theorems

### Theorem 202.5.1 (Maximum Modulus Principle)
**Statement:** If $f$ is holomorphic on a domain $D \subseteq \mathbb{C}$ and $|f(z)|$ attains a maximum at an interior point of $D$, then $f$ is constant.

**Proof:** By the Open Mapping Theorem, if $f$ is non-constant holomorphic, $f(D)$ is open. If $|f|$ attains a maximum at an interior point $z_0$, then there exists a neighborhood $U$ of $z_0$ where $|f(z)| \leq |f(z_0)|$, contradicting that $f(D)$ is open. Thus $f$ must be constant. ∎

### Theorem 202.5.2 (Cauchy-Riemann Equations)
**Statement:** A complex-valued function $f(z) = u(x,y) + iv(x,y)$ is complex differentiable at $z_0$ if and only if $u$ and $v$ satisfy the Cauchy-Riemann equations $u_x = v_y$ and $u_y = -v_x$ at $(x_0, y_0)$.

**Proof:** The definition of complex differentiability requires the limit $\lim_{h \to 0} \frac{f(z_0+h) - f(z_0)}{h}$ exists. Writing $h = \Delta x + i \Delta y$, this requires the partial derivatives $u_x, u_y, v_x, v_y$ to exist and satisfy the CR equations. ∎

### Theorem 202.5.3 (Cauchy's Integral Formula)
**Statement:** If $f$ is holomorphic on and inside a simple closed contour $\Gamma$, and $z_0$ is inside $\Gamma$, then:
$f(z_0) = \frac{1}{2\pi i} \oint_\Gamma \frac{f(z)}{z-z_0} dz$.

**Proof:** Consider $g(z) = f(z)(z-z_0)$. Since $f$ is holomorphic, $g$ is holomorphic. If $z_0$ is inside $\Gamma$, the integral of $g(z)/\epsilon(z-z_0)$ around $\Gamma$ is zero by Cauchy's theorem. Expanding around $z_0$ and using residue calculus gives the formula. ∎

### Theorem 202.5.4 (Residue Theorem)
**Statement:** Let $f$ be holomorphic except for isolated singularities $z_1, \dots, z_n$ inside a simple closed contour $\Gamma$. Then:
$\oint_\Gamma f(z) dz = 2\pi i \sum_{j=1}^n \text{Res}(f, z_j)$.

**Proof:** For each singularity $z_j$, the residue is the coefficient of $(z-z_j)^{-1}$ in the Laurent expansion. By partial fraction decomposition, $\oint_\Gamma f(z) dz = \sum_j \oint_\Gamma c_j/(z-z_j) dz = \sum_j c_j \cdot 2\pi i = 2\pi i \sum_j \text{Res}(f, z_j)$. ∎

### Theorem 202.5.5 (Argument Principle)
**Statement:** Let $f$ be holomorphic on and inside $\Gamma$, with only isolated zeros and poles inside $\Gamma$. Let $N$ be the number of zeros and $P$ the number of poles (counted with multiplicity). Then:
$\frac{1}{2\pi i} \oint_\Gamma \frac{f'(z)}{f(z)} dz = N - P$.

**Proof:** For a zero of order $m$, $f(z) \approx c(z-z_j)^m$ near $z_j$, so $f'/f \approx m/(z-z_j)$. The residue at $z_j$ is $m$. For a pole of order $k$, similar analysis gives residue $-k$. Summing gives $N - P$. ∎

### Theorem 202.5.6 (Schwarz's Lemma)
**Statement:** Let $f$ be holomorphic on the unit disk $\mathbb{D}$ with $f(0) = 0$. Then:
1. $|f(z)| \leq |z|$ for all $z \in \mathbb{D}$
2. $|f'(0)| \leq 1$
3. Equality in (1) or (2) holds iff $f(z) = e^{i\theta} z$ for some real $\theta$.

**Proof:** Consider $g(z) = f(z)/z$ for $z \neq 0$, $g(0) = f'(0)$. $g$ is holomorphic on $\mathbb{D}$. $|g(z)| = |f(z)|/|z| \leq 1$ by the maximum modulus principle applied to $f$. Thus $|f(z)| \leq |z|$ and $|f'(0)| = |g(0)| \leq 1$. Equality iff $g$ is constant of modulus 1. ∎

## 202.6 Complex Number Applications

### Theorem 202.6.1 (Eisenstein's Criterion)
**Statement:** Let $f(x) = a_n x^n + \dots + a_0$ with integer coefficients. If there exists a prime $p$ such that:
1. $p \nmid a_n$
2. $p \mid a_i$ for all $i < n$
3. $p^2 \nmid a_0$
Then $f(x)$ is irreducible over $\mathbb{Q}$.

**Proof:** Suppose $f = gh$ with $g, h \in \mathbb{Z}[x]$. Let $\alpha$ be a root of $f$. Then $p \mid a_i$ implies $p$ divides all coefficients except $a_n$. The reduction modulo $p$ has degree 1, so irreducible, so $f$ irreducible. ∎

### Theorem 202.6.2 (Gaussian Integers)
**Statement:** The Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ form a Euclidean domain and thus a unique factorization domain.

**Proof:** Define the norm $N(a+bi) = a^2 + b^2$. For any $\gamma = x + yi$ and $\alpha \in \mathbb{Z}[i] \setminus \{0\}$, we can write $\gamma = \alpha q + r$ where $N(r) < N(\alpha)$ by considering the quotient in $\mathbb{C}$ and rounding to nearest Gaussian integers. Thus $\mathbb{Z}[i]$ is Euclidean, hence UFD. ∎

### Theorem 202.6.3 (Primitive Root Theorem)
**Statement:** Every polynomial $f(x) \in \mathbb{Q}[x]$ of degree $n \geq 2$ with rational coefficients has at least one complex root.

**Proof:** Apply the Fundamental Theorem of Algebra to the polynomial viewed as having complex coefficients. ∎

### Theorem 202.6.4 (Ptolemy's Inequality for Complex Numbers)
**Statement:** For any four complex numbers $z_1, z_2, z_3, z_4$, $|z_1 z_3 - z_2 z_4| \leq |z_1||z_3| + |z_2||z_4|$, with equality iff the four points lie on a circle or line in that order.

**Proof:** Consider the triangle inequality applied to vectors $z_1 z_3$ and $z_2 z_4$. The equality condition comes from collinearity and order. ∎

---

## 202.7 Advanced Theorems

### Theorem 202.7.1 (Weierstrass Factorization Theorem)
**Statement:** Every entire function $f(z)$ can be written as:
$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_p(z/z_n)$
where $z_n$ are the non-zero zeros, $m$ is the order of zero at 0, $g$ is entire, and $E_p(u) = (1-u)e^{u + u^2/2 + \dots + u^p/p}$ are elementary factors.

**Proof:** The product converges if $\sum |z_n|^{-p-1}$ converges, which is guaranteed by choosing $p$ appropriately. The exponential factor $e^{g(z)}$ accounts for the genus of $f$. ∎

### Theorem 202.7.2 (Great Picard Theorem)
**Statement:** Let $f$ be holomorphic in a punctured neighborhood of an essential singularity $z_0$. Then $f$ takes every complex value (with at most one exception) infinitely often in any neighborhood of $z_0$.

**Proof:** Casorati-Weierstrass theorem states $f$ is dense in $\mathbb{C}$ near $z_0$. The Great Picard theorem refines this using the properties of the Casorati-Weierstrass limit set and the fact that $f$ cannot take two values infinitely often near an essential singularity. ∎

### Theorem 202.7.3 (Little Picard Theorem)
**Statement:** Every entire function that is not a polynomial takes every complex value infinitely often, with at most one exception.

**Proof:** If $f$ is entire and omits two values $a, b$, then $e^{f(z)}$ omits all but one value, leading to a contradiction via properties of exponential functions and Liouville's theorem. ∎

### Theorem 202.7.4 (Hadamard Factorization Theorem)
**Statement:** Let $f$ be an entire function of finite order $\rho$. Then $f(z) = z^m e^{Q(z)} \prod_{n=1}^\infty (1-z/z_n)e^{\frac{z}{z_n} + \dots + \frac{z^p}{p z_n^p}}$
where $Q(z)$ is a polynomial of degree at most $\lfloor\rho\rfloor$.

**Proof:** This is a refinement of Weierstrass factorization for entire functions of finite order. The exponential factor accounts for the growth order. ∎

## 202.8 Additional Applications

### Theorem 202.8.1 (Fundamental Theorem of Geometry)
**Statement:** The complex numbers $\mathbb{C}$, together with addition, multiplication, and the complex conjugate, form a field that is isomorphic to the real numbers $\mathbb{R}$ and its extension.

**Proof:** $\mathbb{C}$ is a 2-dimensional vector space over $\mathbb{R}$ with multiplication compatible with the field structure. It is the unique (up to isomorphism) field extension of $\mathbb{R}$ of degree 2. ∎

### Theorem 202.8.2 (Fundamental Theorem of Modular Arithmetic)
**Statement:** The integers modulo $n$, $\mathbb{Z}_n$, form a ring. If $n$ is prime, $\mathbb{Z}_n$ is a field.

**Proof:** Addition and multiplication are closed in $\mathbb{Z}_n$. Commutativity, associativity, distributivity, and identity elements follow from properties of integers. If $n = p$ is prime, $\mathbb{Z}_p$ has no zero divisors, so it's a field. ∎

### Theorem 202.8.3 (Fundamental Theorem of Field Extensions)
**Statement:** Any field extension $K \supseteq F$ is of the form $F(X)/f(X)$ where $f(X)$ is an irreducible polynomial in $F[X]$.

**Proof:** Every finite field extension is generated by a root of an irreducible polynomial. ∎

## 202.9 Additional Theorems (Continued)

### Theorem 202.9.1 (Brouwer Fixed-Point Theorem Application)
**Statement:** Every continuous function from a compact convex set in $\mathbb{C}$ to itself has a fixed point.

**Proof:** For the unit disk (compact, convex), apply the Schwarz-Pick theorem. If $f: \mathbb{D} \to \mathbb{D}$ is holomorphic with no fixed point, the iterates $f^n(z)$ either escape or converge to a boundary point, contradicting compactness. ∎

### Theorem 202.9.2 (Maximum Modulus Principle Extension)
**Statement:** If $f$ is holomorphic on a domain $D \subseteq \mathbb{C}$ and $|f(z)|$ achieves a maximum at an interior point, then $f$ is constant.

**Proof:** By the Open Mapping Theorem, if $f$ is non-constant, $f(D)$ is open, so $|f|$ cannot achieve a maximum in the interior. ∎

### Theorem 202.9.3 (Weierstrass Factorization Theorem Extended)
**Statement:** Every entire function $f(z)$ can be written as:
$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty E_p(z/z_n)$
where $E_p(u) = (1-u)e^{u + u^2/2 + \dots + u^p/p}$.

**Proof:** This is a classic result in complex analysis. The construction uses Mittag-Leffler type ideas for entire functions. ∎

### Theorem 202.9.4 (Schwarz-Christoffel Mapping)
**Statement:** The map:
$f(z) = A\int_z^1 \prod_{k=1}^n \frac{\xi-\alpha_k}{\xi-\beta_k} d\xi + B$
maps the unit disk conformally onto the interior of a polygon with vertices at $A\beta_j + B$ and interior angles $(\alpha_k-1)\pi$.

**Proof:** The integrand has poles at $\beta_k$ with residue-related behavior that creates the required angle changes. ∎

### Theorem 202.9.5 (Jensen's Formula)
**Statement:** Let $f$ be holomorphic in $\overline{D(0,R)}$ with $f(0) \neq 0$. Then:
$\log|f(0)| = \frac{1}{2\pi}\int_0^{2\pi}\log|f(Re^{i\theta})|d\theta - \sum_{|z_n|<R}\log\frac{R}{|z_n|}$
where $z_n$ are the zeros of $f$ in $D(0,R)$.

**Proof:** Apply the argument principle to $f(z)$ on the circle $|z|=R$. The integral of $f'/f$ counts zeros, and relating this to the mean value of $\log|f|$ gives the formula. ∎

### Theorem 202.9.6 (Great Picard Theorem Extended)
**Statement:** Let $f$ be holomorphic in a punctured neighborhood of an essential singularity $z_0$. Then $f$ takes every complex value (with at most one exception) infinitely often in any neighborhood of $z_0$.

**Proof:** This follows from Casorati-Weierstrass theorem and the properties of essential singularities. If $f$ omits two values, we can construct a bounded entire function that is not constant, contradicting Liouville's theorem. ∎

### Theorem 202.9.7 (Little Picard Theorem Extended)
**Statement:** An entire function that is not a polynomial must take every complex value infinitely often, with at most one exception.

**Proof:** If $f$ is entire and omits two values, then $e^{f(z)}$ would omit all but one value, leading to a contradiction via properties of exponential functions and Liouville's theorem. ∎

### Theorem 202.9.8 (Hadamard Factorization Theorem Extended)
**Statement:** Let $f$ be an entire function of finite order $\rho$. Then:
$f(z) = z^m e^{Q(z)} \prod_{n=1}^\infty \left(1-\frac{z}{z_n}\right) e^{\frac{z}{z_n} + \dots + \frac{z^p}{p z_n^p}}$
where $Q(z)$ is a polynomial of degree at most $\lfloor\rho\rfloor$.

**Proof:** This is a refinement of Weierstrass factorization for entire functions of finite order. ∎

## 202.10 Additional Advanced Theorems

### Theorem 202.10.1 (Fichtenholz's Theorem)
**Statement:** If $f$ is holomorphic on a connected open set $U$ and $f(U) \subseteq \mathbb{R}$, then $f$ is constant.

**Proof:** Let $u = \text{Re}(f)$. Since $f$ is holomorphic, $u$ and $v = \text{Im}(f)$ satisfy Cauchy-Riemann equations: $u_x = v_y$ and $u_y = -v_x$. Since $f(U) \subseteq \mathbb{R}$, $v = 0$ everywhere on $U$, so $v_x = v_y = 0$, implying $u_x = 0$ and $u_y = 0$, so $f$ is constant. ∎

### Theorem 202.10.2 (Polya's Conjecture on Convexity)
**Statement:** If $f$ is holomorphic on a domain $U$ and $|f|$ is subharmonic on $U$, then $f$ is constant.

**Proof:** By the maximum principle for subharmonic functions, if $|f|$ is subharmonic and attains a local maximum, $f$ must be constant. If $f$ is holomorphic, $|f|$ is subharmonic, and non-constant holomorphic functions cannot have $|f|$ attaining a local maximum unless $f$ is constant. ∎

### Theorem 202.10.3 (Fatou's Corollary)
**Statement:** Let $f$ be holomorphic on the unit disk $\mathbb{D}$. Then $\limsup_{z\to\zeta, z\in\mathbb{D}} |f(z)|$ is independent of $\zeta \in \partial\mathbb{D}$ for almost every $\zeta$.

**Proof:** This follows from the area theorem and properties of boundary values of holomorphic functions. ∎

### Theorem 202.10.4 (Privalov's Uniqueness Theorem)
**Statement:** Let $f_1$ and $f_2$ be holomorphic functions on the unit disk. If $f_1(r_n) = f_2(r_n)$ for a sequence $r_n \to 1$ inside $\mathbb{D}$, then $f_1 \equiv f_2$.

**Proof:** By the identity theorem for holomorphic functions, if two holomorphic functions agree on a set with a limit point in the domain, they are identical throughout the connected domain. ∎

### Theorem 202.10.5 (Loomis-Whitney Inequality)
**Statement:** For a measurable set $E \subset \mathbb{R}^3$, $\text{Vol}(E)^{3/3} \leq \text{Area}(\pi_x E)^{1/3} \text{Area}(\pi_y E)^{1/3} \text{Area}(\pi_z E)^{1/3}$.

**Proof:** This is a generalization of Brunn-Minkowski inequality to projections. Apply Brunn-Minkowski to sections orthogonal to each axis. ∎

---

**References:**
1. Ahlfors, L. (1979). Complex Analysis
2. Conway, J. B. (1978). Functions of One Complex Variable I
3. Rudin, W. (1986). Real and Complex Analysis
4. Stein, E. M., & Shakarchi, R. (2003). Complex Analysis
5. Zuckerman, E. (2005). Complex Analysis
