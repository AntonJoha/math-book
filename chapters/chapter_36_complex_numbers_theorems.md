# Chapter 36: Complex Numbers - Complete Theorems

## 36.1 Complex Numbers Fundamentals

### Theorem 36.1: Definition of Complex Numbers

**Statement**: The set of complex numbers $\mathbb{C}$ is a field extension of $\mathbb{R}$ of degree 2, defined as $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}, i^2 = -1\}$.

**Proof**: The construction of $\mathbb{C}$ follows from considering the quotient ring $\mathbb{R}[x]/(x^2 + 1)$. Since $x^2 + 1$ is irreducible over $\mathbb{R}$, the quotient is a field. The isomorphism $a + bi \mapsto a + bx$ establishes the field structure. ∎

### Theorem 36.2: Fundamental Theorem of Algebra

**Statement**: Every non-constant polynomial $P(z)$ with complex coefficients has at least one complex root.

**Proof**: This follows from Liouville's Theorem in complex analysis. If $P(z)$ has no zeros in $\mathbb{C}$, then $1/P(z)$ is a bounded entire function, hence constant by Liouville's Theorem, which leads to a contradiction. ∎

### Theorem 36.3: Complex Conjugate Properties

**Statement**: For any complex numbers $z_1, z_2$:
1. $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
2. $\overline{z_1 z_2} = \overline{z_1}\overline{z_2}$
3. $\overline{\overline{z}} = z$
4. $|z|^2 = z\overline{z}$

**Proof**: Let $z_1 = a + bi$ and $z_2 = c + di$. Direct computation shows all four properties hold. ∎

## 36.2 Advanced Complex Number Theorems

### Theorem 36.4: De Moivre's Formula

**Statement**: For any complex number $z = r(\cos\theta + i\sin\theta)$ and any integer $n$:
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

**Proof**: By induction on $n$. The base case $n=1$ is trivial. The inductive step uses the angle addition formulas for cosine and sine. ∎

### Theorem 36.5: $n$-th Roots of Unity

**Statement**: The $n$-th roots of unity in $\mathbb{C}$ are given by:
$$\omega_k = e^{i\frac{2\pi k}{n}}, \quad k = 0, 1, \dots, n-1$$

**Proof**: We solve $z^n = 1$, which means $e^{in\theta} = 1$. This occurs when $in\theta = 2\pi k$ for integer $k$, giving $\theta = \frac{2\pi k}{n}$. The $n$ values $k = 0, 1, \dots, n-1$ give distinct roots. ∎

### Theorem 36.6: Gaussian Integers

**Statement**: The Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ form a Euclidean domain with norm $N(a + bi) = a^2 + b^2$.

**Proof**: The Euclidean division algorithm holds: for any $\alpha, \beta \in \mathbb{Z}[i]$ with $\beta \neq 0$, we can write $\alpha = q\beta + r$ with $N(r) < N(\beta)$. This follows from the fact that $\mathbb{Q}(i)$ is a quadratic extension of $\mathbb{Q}$. ∎

### Theorem 36.7: Unique Factorization in $\mathbb{Z}[i]$

**Statement**: Every Gaussian integer can be factored uniquely (up to order and units) into a product of Gaussian primes.

**Proof**: $\mathbb{Z}[i]$ is a Euclidean domain, hence a principal ideal domain, hence a unique factorization domain. The proof follows from the general theory of UFDs. ∎

## 36.3 Polar and Exponential Forms

### Theorem 36.8: Euler's Formula

**Statement**: For any real $\theta$:
$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Proof**: Consider the power series expansion of $e^z$, $\cos z$, and $\sin z$. Substituting $z = i\theta$ and using the series expansions gives Euler's formula. ∎

### Theorem 36.9: Polar Representation

**Statement**: Any non-zero complex number $z$ can be uniquely written as:
$$z = re^{i\theta}$$
where $r = |z|$ and $\theta \in \mathbb{R}$ is the argument of $z$ (determined up to multiples of $2\pi$).

**Proof**: Let $z = a + bi = r(\cos\theta + i\sin\theta)$ where $r = \sqrt{a^2 + b^2}$. Then $z = r(\frac{a}{r} + i\frac{b}{r}) = re^{i\theta}$ where $\theta = \arg(z)$. ∎

## 36.4 Arithmetic Theorems

### Theorem 36.10: Complex Modulus Properties

**Statement**: For any complex numbers $z_1, z_2$:
1. $|z_1 z_2| = |z_1||z_2|$
2. $|z_1/z_2| = |z_1|/|z_2|$ for $z_2 \neq 0$
3. $|z_1 + z_2| \leq |z_1| + |z_2|$ (Triangle Inequality)
4. $|z_1 - z_2| \leq |z_1| + |z_2|$ (Reverse Triangle Inequality)

**Proof**: Direct computation using the definition $|z| = \sqrt{a^2 + b^2}$ shows all properties hold. ∎

### Theorem 36.11: Inequalities in $\mathbb{C}$

**Statement**: For any complex numbers $z_1, z_2$:
$$||z_1| - |z_2|| \leq |z_1 \pm z_2| \leq |z_1| + |z_2|$$

**Proof**: This follows from the triangle inequality and the reverse triangle inequality. ∎

## 36.5 Advanced Topics

### Theorem 36.12: Algebraic Integers

**Statement**: The Gaussian integers $\mathbb{Z}[i]$ are the algebraic integers in the quadratic field $\mathbb{Q}(i)$.

**Proof**: An algebraic integer in a quadratic field is a root of a monic polynomial with integer coefficients. In $\mathbb{Q}(i)$, these are exactly $a + bi$ where $a, b \in \mathbb{Z}$. ∎

### Theorem 36.13: Algebraic Closure

**Statement**: The field $\mathbb{C}$ is algebraically closed, i.e., every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof**: This is the Fundamental Theorem of Algebra, proved using Liouville's Theorem in complex analysis. ∎

### Theorem 36.14: Primitive Elements of Roots of Unity

**Statement**: An $n$-th root of unity $\omega_k = e^{i\frac{2\pi k}{n}}$ is a primitive $m$-th root if and only if $\gcd(k, n) = \frac{n}{m}$.

**Proof**: $\omega_k$ has order $m$ if $m$ is the smallest positive integer such that $(\omega_k)^m = 1$. This means $\frac{2\pi k}{n}m = 2\pi j$ for some integer $j$, so $km = nj$. The smallest such $m$ is $n/\gcd(k, n)$. ∎

EOF

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

---

*Updated on 2026-06-10*
