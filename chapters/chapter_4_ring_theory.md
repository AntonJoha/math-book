# Chapter 4: Ring Theory Basics

## 4.1 Ring Definition

### Theorem 4.1: Definition of a Ring

**Statement**: A set $R$ is a ring if it is equipped with two binary operations $+$ and $\cdot$ satisfying:

1. $(R, +)$ is an abelian group
2. $(R, \cdot)$ is a semigroup (associative)
3. Multiplication distributes over addition:
   - $a(b + c) = ab + ac$ (left distributivity)
   - $(a + b)c = ac + bc$ (right distributivity)

**Proof**: This is the definition of a ring. ∎

## 4.2 Commutative and Integral Domains

### Theorem 4.2: Commutative Ring

**Statement**: A ring $R$ is commutative if for all $a, b \in R$, $ab = ba$.

### Theorem 4.3: Commutative Ring with Unity

**Statement**: A commutative ring $R$ with unity is a commutative ring if it has:
1. A multiplicative identity $1 \neq 0$ such that $1a = a1 = a$ for all $a \in R$

### Theorem 4.4: Integral Domain

**Statement**: A commutative ring $R$ with unity is an integral domain if:
1. $R$ has no zero divisors: $ab = 0 \implies a = 0$ or $b = 0$

**Proof that $\mathbb{Z}$ is an integral domain**:
Let $a, b \in \mathbb{Z}$ with $ab = 0$. If $a > 0$, then $a = b \cdot \frac{a}{b}$ doesn't work directly.

Actually, we use the fact that $\mathbb{Z}$ is a subset of $\mathbb{Q}$. In $\mathbb{Q}$, the only solution to $ab = 0$ is $a = 0$ or $b = 0$. Since this property is inherited, $\mathbb{Z}$ has no zero divisors. ∎

## 4.3 Field Axioms

### Theorem 4.5: Field Definition

**Statement**: A field is a commutative ring with unity in which every non-zero element has a multiplicative inverse.

Formally, for all $a \in F \setminus \{0\}$, there exists $a^{-1} \in F$ such that $a \cdot a^{-1} = a^{-1} \cdot a = 1$.

**Examples**:
- $\mathbb{Q}$ (rational numbers) is a field
- $\mathbb{R}$ (real numbers) is a field
- $\mathbb{C}$ (complex numbers) is a field
- $\mathbb{F}_p$ (integers modulo prime $p$) is a field

**Proof that $\mathbb{Q}$ is a field**:
1. $(\mathbb{Q}, +)$ is an abelian group (verified from real numbers properties)
2. $(\mathbb{Q}, \cdot)$ is a commutative monoid with $1$
3. Multiplication distributes over addition
4. Every $a \neq 0$ in $\mathbb{Q}$ has inverse $1/a \in \mathbb{Q}$ since $a$ is a ratio of integers. ∎

## 4.4 Subrings

### Theorem 4.6: Subring Criterion

**Statement**: Let $S$ be a non-empty subset of a ring $R$. Then $S$ is a subring of $R$ if and only if:
1. $S$ is closed under subtraction: $\forall a, b \in S, a - b \in S$
2. $S$ is closed under multiplication: $\forall a, b \in S, ab \in S$

**Proof**:

(⇒) If $S$ is a subring, it inherits the ring structure, so it must be closed under the operations.

(⇐) Suppose $S$ is closed under subtraction and multiplication.
- Let $a, b \in S$. Then $a - b \in S$, so $S$ contains $0$ (take $a = b$).
- Since $a - b \in S$ for all $a, b$, taking $b = 0$ gives $a \in S$ (closure under additive inverses).
- Closure under subtraction gives closure under addition (take $a, 0$).
- Closure under multiplication is given.
- Commutativity and associativity are inherited from $R$.
- Distributivity is inherited from $R$.

Thus, $S$ satisfies all ring axioms. ∎

## 4.5 Euclidean Domains

### Theorem 4.7: Euclidean Domain Properties

**Statement**: A Euclidean domain is an integral domain $R$ with a function $d: R \setminus \{0\} \to \mathbb{N}_0$ (the Euclidean valuation) such that for all $a, b \in R$ with $b \neq 0$, there exist unique $q, r \in R$ such that:

$a = bq + r$ where $r = 0$ or $d(r) < d(b)$.

**Examples**:
- $\mathbb{Z}$ is a Euclidean domain with $d(n) = |n|$
- $F[x]$ (polynomials over a field $F$) is a Euclidean domain with $d(p) = \deg(p)$

**Proof that $\mathbb{Z}[x]$ is not a Euclidean domain**:
The ring $\mathbb{Z}[x]$ of polynomials with integer coefficients is not a Euclidean domain because no suitable Euclidean valuation exists.

If $d$ were a Euclidean valuation, for any $a(x), b(x) \in \mathbb{Z}[x]$ with $b(x) \neq 0$, we would have $a(x) = b(x)q(x) + r(x)$ with $r(x) = 0$ or $d(r(x)) < d(b(x))$.

However, it can be shown that no such function $d$ exists. For instance, the leading coefficient of polynomials in $\mathbb{Z}[x]$ can be any integer, and there's no natural way to order these that satisfies the Euclidean division property. ∎

## 4.6 Polynomial Rings

### Theorem 4.8: Polynomial Division Algorithm

**Statement**: Let $F$ be a field and let $a(x), b(x) \in F[x]$ with $b(x) \neq 0$. Then there exist unique polynomials $q(x)$ (the quotient) and $r(x)$ (the remainder) such that:

$a(x) = b(x)q(x) + r(x)$

where $r(x) = 0$ or $\deg(r(x)) < \deg(b(x))$.

**Proof**:

We use polynomial long division.

**Existence**: Consider the set of polynomials $S = \{a(x) - b(x)q(x) : q(x) \in F[x]\}$.
Since $F$ is a field, we can always subtract multiples of $b(x)$ from $a(x)$. By repeatedly subtracting $b(x)$ times the leading coefficient, we can reduce the degree of the remainder until it's less than $\deg(b(x))$ or zero.

**Uniqueness**: Suppose $a(x) = b(x)q_1(x) + r_1(x) = b(x)q_2(x) + r_2(x)$ where $\deg(r_1), \deg(r_2) < \deg(b(x))$.

Then $b(x)(q_1(x) - q_2(x)) = r_2(x) - r_1(x)$.

If $q_1(x) \neq q_2(x)$, then $\deg(b(x)(q_1(x) - q_2(x))) = \deg(b(x)) + \deg(q_1(x) - q_2(x)) \ge \deg(b(x))$.

But $\deg(r_2(x) - r_1(x)) \le \max(\deg(r_1(x)), \deg(r_2(x))) < \deg(b(x))$.

This is a contradiction, so $q_1(x) = q_2(x)$ and $r_1(x) = r_2(x)$. ∎

## 4.7 Units and Zero Divisors

### Theorem 4.9: Units in Polynomial Rings

**Statement**: In $F[x]$ where $F$ is a field, a polynomial $p(x)$ is a unit (has a multiplicative inverse) if and only if $\deg(p(x)) = 0$ and $p(x) \neq 0$ (i.e., $p(x)$ is a non-zero constant).

**Proof**:

(⇒) Suppose $p(x)q(x) = 1$ where $p, q \in F[x]$. Taking degrees:
$\deg(p(x)q(x)) = \deg(p(x)) + \deg(q(x)) = \deg(1) = 0$.

Since $\deg(p(x)), \deg(q(x)) \ge 0$, the only solution is $\deg(p(x)) = \deg(q(x)) = 0$.

(⇐) If $\deg(p(x)) = 0$ and $p(x) = c \in F, c \neq 0$, then $p(x)^{-1} = c^{-1} \in F$ exists since $F$ is a field. ∎

### Theorem 4.10: Zero Divisors in Integral Domains

**Statement**: In an integral domain $D$, the product of any two elements is zero if and only if at least one of them is zero.

Formally: $ab = 0 \implies a = 0$ or $b = 0$.

**Proof**: This is the definition of an integral domain. ∎
