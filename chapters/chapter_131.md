## 131. Number Theory: Congruences, Primes, and Diophantine Equations

### 131.1 Congruences and Modular Arithmetic

**Definition**: a ≡ b (mod n) if and only if n divides a-b.

**Theorem**: The Chinese Remainder Theorem. Let n₁, ..., n_k be pairwise coprime integers > 1. For any residues a₁, ..., a_k, there exists a unique solution x mod n₁...n_k satisfying:
x ≡ a₁ (mod n₁)
...
x ≡ a_k (mod n_k)

**Proof**: 
Let N = n₁...n_k and N_i = N/n_i. Since gcd(N_i, n_i) = 1, there exist x_i, y_i such that x_i N_i + y_i n_i = 1.
Set x = Σ a_i x_i N_i mod N.
Then x ≡ a_i x_i N_i + Σ_{j≠i} a_j x_j N_j ≡ a_i (mod n_i) since N_j is divisible by n_i for j ≠ i.
Uniqueness follows from the fact that if x satisfies all congruences, then x - a_i is divisible by n_i, hence by their product N. QED

### 131.2 Euclidean Algorithm and GCD

**Definition**: For a, b ∈ ℤ, the greatest common divisor gcd(a, b) is the largest positive integer dividing both a and b.

**Theorem (Euclidean Algorithm)**: For any a, b ∈ ℤ, gcd(a, b) = gcd(a, b-a) where |a| ≥ |b|.

**Theorem (Extended Euclidean Algorithm)**: For any a, b ∈ ℤ, there exist integers x, y such that ax + by = gcd(a, b).

**Proof**: 
By induction, at each step we reduce the problem to a pair where the second element is smaller.
The base case is trivial when gcd(a, b) = a (with b = 0).
The extended algorithm maintains the invariant: there exist x_n, y_n such that a x_n + b y_n = r_n.
QED

### 131.3 Euler's Theorem and Modular Exponentiation

**Theorem (Euler's Theorem)**: If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ(n) is Euler's totient function.

**Theorem**: φ(n) = n ∏_{p|n} (1 - 1/p) where the product is over distinct prime divisors p of n.

**Proof**: 
Count numbers less than n that are coprime to n.
In each congruence class mod p, exactly (1/p) fraction are coprime.
By inclusion-exclusion, φ(n) = n ∏_{p|n} (1 - 1/p). QED

### 131.4 Fermat's Little Theorem

**Theorem**: If p is prime and a is an integer not divisible by p, then a^(p-1) ≡ 1 (mod p).

**Proof**: 
Consider the cosets a·S where S = {1, 2, ..., p-1}. Multiplication by a permutes S mod p.
Thus the product ∏_{x∈S} x ≡ ∏_{x∈S} ax (mod p).
The right side is a^(p-1) · ∏ x ≡ a^(p-1) mod p.
Since ∏ x = (p-1)! ≡ -1 mod p by Wilson's theorem, and a^(p-1) · (-1) ≡ -1 mod p, we get a^(p-1) ≡ 1 mod p. QED

### 131.5 Primality Testing

**Definition**: A composite number n that passes the Fermat primality test for some base a is called a pseudoprime.

**Theorem (Miller-Rabin)**: Let n be an odd composite number. Then at least one of the following holds:
1. a^{(n-1)/2} ≡ 1 (mod n)
2. a^{(n-1)/2^r} ≢ ±1 (mod n) for some r where 1 ≤ r ≤ log₂(n-1)

**Proof**: 
By Euler's criterion and properties of quadratic residues, if n is prime, then a^(n-1) ≡ 1 (mod n) for all a coprime to n.
If n is composite, there are at most (n-1)/2 bases that pass the test.
The Miller-Rabin test is probabilistic but can be made deterministic with a fixed set of bases for n < 2^64. QED

### 131.6 Quadratic Residues and Reciprocity

**Theorem (Quadratic Reciprocity)**: Let p and q be distinct odd primes. Then (p/q)(q/p) = (-1)^{(p-1)/2 · (q-1)/2}.

**Theorem**: (a/p) ≡ a^((p-1)/2) (mod p) where (a/p) is the Legendre symbol.

**Theorem (Quadratic Formula)**: The equation x² ≡ a (mod p) has:
- 0 solutions if (a/p) = -1 (a is a quadratic non-residue)
- 2 solutions if (a/p) = 1 (a is a quadratic residue), given by x ≡ ±a^((p+1)/4) mod p

**Proof**: 
From Fermat's little theorem, a^((p-1)/2) ≡ ±1 mod p.
If ≡ 1, then a is a quadratic residue; if ≡ -1, it's not.
The formula x² ≡ a (mod p) has solutions iff (a/p) = 1.
QED

### 131.7 Dirichlet's Theorem on Arithmetic Progressions

**Theorem**: If a and d are coprime integers, there are infinitely many primes of the form a + nd where n is a non-negative integer.

**Theorem (Euclid's Proof)**: For coprime a, d, there are infinitely many primes ≡ a (mod d).

**Proof**: 
Consider primes p_n = (a + n·d) · p_{n-1} + 1 where p_0 = d.
The primes p_n satisfy p_n ≡ a (mod d).
As n grows, p_n grows without bound, hence infinitely many such primes exist. QED

### 131.8 Diophantine Equations

**Theorem (Fermat's Last Theorem)**: For n ≥ 3, the equation x^n + y^n = z^n has no solutions in positive integers.

**Proof (Sketch - Case n=4)**:
Suppose x⁴ + y⁴ = z⁴. Then x² and y² are squares of numbers less than z².
Assume (x²)² + (y²)² = (z²)². By Fermat's right triangle theorem, this has no solutions.
Thus x⁴ + y⁴ = z⁴ has no solutions.

**Theorem (Pythagorean Triples)**: All primitive Pythagorean triples (a, b, c) are given by:
a = m² - n², b = 2mn, c = m² + n²
where m > n > 0 are coprime integers with opposite parity.

**Proof**: 
Parametrize primitive triples using rational points on the unit circle x² + y² = 1.
Using Pythagorean parametrization (1-t²)/(1+t²), (2t)/(1+t²), we get all primitive triples.
QED

### 131.9 The Riemann Zeta Function

**Definition**: The Riemann zeta function ζ(s) = Σ_{n=1}^∞ 1/n^s for Re(s) > 1.

**Theorem (Euler Product)**: ζ(s) = ∏_{p prime} (1 - p^{-s})^{-1}.

**Proof**: 
Expanding the product gives the Dirichlet series Σ 1/n^s.
Each term n in the sum corresponds to a unique choice of prime factors in the product.
QED

**Theorem (Riemann Hypothesis)**: The non-trivial zeros of ζ(s) lie on the critical line Re(s) = 1/2.

**Proof**: 
This remains unproven. The Riemann Hypothesis is one of the most famous unsolved problems in mathematics.
The Prime Number Theorem, which states π(x) ~ x/log x, is equivalent to the Riemann Hypothesis.
QED

### 131.10 Quadratic Fields and Class Numbers

**Theorem**: The ring of integers in Q(√d) where d is a square-free integer is either ℤ[(1+√d)/2] or ℤ[√d].

**Theorem (Minkowski's Theorem)**: Every number field has a finite class group.

**Proof**: 
The class group classifies ideal classes.
Minkowski's bound shows every ideal class contains an ideal with norm bounded by a constant depending on the field.
By finite generation, the class group is finite. QED

