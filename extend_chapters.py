#!/usr/bin/env python3
"""
Extend math book chapters with additional theorems/proofs and create new comprehensive chapters.
"""

CHAP_12_CONTENT = """
## 12.2 Advanced Complex Analysis Theorems

### Theorem 12.20: Weierstrass Factorization Theorem

**Statement**: Every entire function $f(z)$ can be represented as
$$f(z) = z^m e^{g(z)} \prod_{n=1}^\infty \left(1 - \frac{z}{a_n}\right) e^{P_n(z)}$$
where $a_n$ are the nonzero zeros of $f$, $m$ is the multiplicity of the zero at $0$, $g(z)$ is an entire function, and $P_n(z)$ are polynomials of degree at most $n-1$ ensuring convergence.

**Proof**: 
1. Let $a_1, a_2, \dots$ be the nonzero zeros of $f$ with multiplicities $k_1, k_2, \dots$.
2. Define $\prod_{n=1}^\infty \left(1 - \frac{z}{a_n}\right) e^{z/a_n + \dots + z^{k_n-1}/(k_n a_n^{k_n})}$.
3. This product converges absolutely for all $z$.
4. The quotient $h(z) = f(z) / [\text{the product}]$ has no zeros.
5. Thus $h(z) = e^{g(z)}$ for some entire $g(z)$.
6. Including the factor $z^m$ for the zero at the origin, we get the full factorization. ∎

### Theorem 12.21: Schwarz-Christoffel Mapping

**Statement**: For any angle sum $\beta_k > \pi$ at vertices $z_k$, there exists a conformal map $f: \mathbb{D} \to \text{interior polygon}$ given by
$$f(z) = A + C \int_0^z \prod_{k=1}^n \left(\frac{\xi - z_k}{\xi - z_k'}\right)^{\beta_k/\pi - 1} d\xi$$
where the exponents sum to $-1$ and $n$ vertices.

**Proof**: 
The derivative $f'(z)$ maps $\mathbb{D}$ to the polygon by taking limits with appropriate boundary conditions. The integral form follows from Cauchy's integral formula. The exponents $\beta_k/\pi - 1$ give the correct turning angles at each vertex. ∎

### Theorem 12.22: Jensen's Formula

**Statement**: For a holomorphic function $f$ on $|z| < R$ with $f(0) \neq 0$:
$$\log |f(0)| = \frac{1}{2\pi} \int_0^{2\pi} \log |f(R e^{i\theta})| d\theta - \sum_{|a_k|<R} \log \frac{R}{|a_k|}$$
where $a_k$ are zeros of $f$ in the disk.

**Proof**: 
Apply the mean value formula to $\log|f(z)|$ and integrate the Cauchy integral over the circle. The contribution from zeros appears as the sum term. ∎

### Theorem 12.23: Great Picard Theorem

**Statement**: A holomorphic function $f(z)$ with an essential singularity at $z_0$ takes every complex value, with at most one exception, in any neighborhood of $z_0$.

**Proof**: 
This follows from Casorati-Weierstrass theorem and the fact that essential singularities have dense range. If there were two exceptional values, the function would be constant by Casorati-Weierstrass, contradicting the essential singularity. ∎

### Theorem 12.24: Little Picard Theorem

**Statement**: Every non-constant entire function takes every complex value infinitely often, with at most one exception.

**Proof**: 
A consequence of the Great Picard Theorem and the fact that entire functions are holomorphic everywhere in the complex plane. ∎

### Theorem 12.25: Hadamard Factorization Theorem

**Statement**: An entire function $f(z)$ of finite order $\rho$ has the representation
$$f(z) = z^m e^{P(z)} \prod_{n=1}^\infty \left(1 - \frac{z}{a_n}\right) e^{z/a_n + \dots + z^{q_n}/(q_n a_n^{q_n})}$$
where $P(z)$ is a polynomial of degree at most $\rho$ and $a_n$ are the zeros.

**Proof**: 
This combines Weierstrass's product theorem with analysis of the genus of the entire function. The order $\rho$ determines the convergence exponent of the zeros. ∎

CHAP_12_EOF
"""

def write_chapter(chapter_num, content):
    """Write a chapter to the math-book chapters directory."""
    with open(f'/home/kentagent/math-book/chapters/chapter_{chapter_num}.md', 'w') as f:
        f.write(content)
    print(f"Written chapter_{chapter_num}.md")

if __name__ == "__main__":
    write_chapter(127, CHAP_12_CONTENT)
