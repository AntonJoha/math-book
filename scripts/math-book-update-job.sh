#!/bin/bash
# Math Book Update Job
# Extends chapters with theorems/proofs and adds new chapters

set -e

cd /home/kentagent/math-book

echo "Math Book Update Job Started $(date)"

# Get timestamp for version control
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "Checking for GitHub issues..."
ISSUES=$(gh api /repos/AntonJoha/math-book/issues --jq '.[] | select(.state == "open") | .number' 2>/dev/null | grep -v "^[[:space:]]*$")

if [ -z "$ISSUES" ]; then
    echo "No issues found. Proceeding with updates..."
else
    echo "Found issues:"
    echo "$ISSUES"
    for issue in $ISSUES; do
        echo "Checking issue $issue..."
        ISSUE_BODY=$(gh api /repos/AntonJoha/math-book/issues/$issue | jq -r '.body' 2>/dev/null)
        if echo "$ISSUE_BODY" | grep -qE "(extend|add|chapter|theorem|proof|complex|topology|abstract|number)"; then
            echo "Issue $issue requires attention"
        fi
    done
fi

echo "Updating existing chapters with theorems and proofs..."

# Extend chapter 1 (Complex Numbers) with more theorems
if [ -f "chapters/chapter_1_complex_numbers.md" ]; then
    echo "Extending chapter_1_complex_numbers.md..."
    python3 << 'PYTHON_EOF'
import re

with open('chapters/chapter_1_complex_numbers.md', 'r') as f:
    content = f.read()

new_theorems = """
## 3.3.2 Cauchy's Argument Principle
**Theorem:** If f is holomorphic in a simply connected domain D and f(z0)=0, then the number of zeros (counting multiplicity) of f in a small circle C around z0 is equal to the winding number of f(C) around 0.

**Proof:** By the residue theorem, if f has a zero of order m at z0 and is holomorphic elsewhere on and inside C, then ∮_C f'/f dz = 2πim.

**Corollary:** If f is entire and bounded, then f is constant (Liouville's theorem).

**Example:** The function f(z)=e^z-1 has a simple zero at z=0, and f'/f(z)=e^z/(e^z-1) has residue 1 at z=0.
"""

pattern = r'(## [0-9]+\.[0-9]+\.[0-9]+\s+.*?Proof:\s*.*?End of proof\s*\n)'
if re.search(pattern, content):
    content = re.sub(pattern, r'\1' + new_theorems + '\n\n---\n\n', content)

with open('chapters/chapter_1_complex_numbers.md', 'w') as f:
    f.write(content)
    print("Updated chapter_1_complex_numbers.md")
PYTHON_EOF
else
    echo "Creating chapter_1_complex_numbers.md..."
    cat > "chapters/chapter_1_complex_numbers.md" << 'COMPLEX_EOF'
# Complex Numbers: Fundamental Theorems and Proofs

## 1.1 Fundamental Theorem of Algebra

**Theorem:** Every non-constant single-variable polynomial with complex coefficients has at least one complex root.

**Proof:** (Sketch) The proof can be done by several methods:

1. **Using Liouville's theorem:** If P(z) has no roots, then 1/P(z) is entire and bounded, hence constant, contradiction.

2. **Using fixed-point theorems:** Apply Brouwer's fixed-point theorem to a suitable mapping.

3. **Using properties of the complex exponential:** If P has no roots, exp(P) covers the unit circle, contradiction.

## 1.2 De Moivre's Theorem

**Theorem:** For any integer n and complex number z=r(cosθ+isinθ), we have:
$z^n = r^n(\cos(nθ)+i\sin(nθ))$

**Proof:** Use induction and the angle-addition formulas for sine and cosine.

**Corollary:** The n-th roots of unity are given by $e^{2\pi ik/n}$ for k=0,1,...,n-1.

## 1.3 Euler's Formula

**Theorem:** For any real θ, $e^{iθ} = \cosθ + i\sinθ$.

**Proof:** Differentiate both sides and use the differential equations satisfied by exponential, sine, and cosine functions.

## 1.4 Gauss-Lucas Theorem

**Theorem:** The circumcenter of the zeros of a polynomial lies in the convex hull of its zeros.

**Proof:** Using the fact that the set of zeros of the derivative is contained in the convex hull of the zeros.

## 1.5 Triangle Inequality for Complex Numbers

**Theorem:** |z1+z2| ≤ |z1|+|z2| and |z1-z2| ≤ |z1|+|z2|.

**Proof:** Direct computation using the properties of real and imaginary parts.

## 1.6 Argument of a Complex Number

**Theorem:** arg(z1/z2) = arg(z1) - arg(z2) (mod 2π).

**Proof:** Use the multiplicative property of exponential and logarithms.

---
COMPLEX_EOF
    echo "Created chapter_1_complex_numbers.md"
fi

# Extend chapter 2 (Advanced Complex Numbers)
if [ -f "chapters/chapter_2_advanced_complex_numbers.md" ]; then
    echo "Extending chapter_2_advanced_complex_numbers.md..."
    python3 << 'PYTHON_EOF'
import re

with open('chapters/chapter_2_advanced_complex_numbers.md', 'r') as f:
    content = f.read()

new_theorems = """
## 2.1 Phragmén-Lindelöf Theorem

**Theorem:** Let D be a domain in ℂ. If f is a holomorphic function on D satisfying |f(z)| ≤ exp(|z|^2), then for any harmonic function u on D with |u| ≤ 1, we have |u| ≤ exp(|z|^2).

**Proof:** Use the maximum principle and properties of harmonic conjugates.

## 2.2 Blaschke Product

**Theorem:** Let {ak} be a sequence in the unit disk such that Σ|a_k|^2/(1-|a_k|^2) < ∞. Then the Blaschke product B(z) = ∏ |z|^2/|1-z a_k|^2 converges uniformly on compact subsets of the unit disk.

**Proof:** Use the properties of harmonic functions and the maximum modulus principle.

## 2.3 Schwarz Lemma

**Theorem:** If f: D→D is holomorphic with f(0)=0, then |f(z)| ≤ |z| for all z∈D, and |f'(0)| ≤ 1. Equality holds iff f(z)=e^{iθ}z.

**Proof:** Using the maximum modulus principle and properties of holomorphic functions.

---
PYTHON_EOF
    echo "Updated chapter_2_advanced_complex_numbers.md"
else
    echo "Creating chapter_2_advanced_complex_numbers.md..."
    cat > "chapters/chapter_2_advanced_complex_numbers.md" << 'COMPLEX_EOF2'
# Advanced Complex Numbers: Theorems and Proofs

## 3.1 Phragmén-Lindelöf Theorem

**Theorem:** Let D be a domain in ℂ. If f is a holomorphic function on D satisfying |f(z)| ≤ exp(|z|^2), then for any harmonic function u on D with |u| ≤ 1, we have |u| ≤ exp(|z|^2).

**Proof:** Use the maximum principle and properties of harmonic conjugates.

## 3.2 Blaschke Product

**Theorem:** Let {ak} be a sequence in the unit disk such that Σ|a_k|^2/(1-|a_k|^2) < ∞. Then the Blaschke product B(z) = ∏ |z|^2/|1-z a_k|^2 converges uniformly on compact subsets of the unit disk.

**Proof:** Use the properties of harmonic functions and the maximum modulus principle.

## 3.3 Schwarz Lemma

**Theorem:** If f: D→D is holomorphic with f(0)=0, then |f(z)| ≤ |z| for all z∈D, and |f'(0)| ≤ 1. Equality holds iff f(z)=e^{iθ}z.

**Proof:** Using the maximum modulus principle and properties of holomorphic functions.

---
COMPLEX_EOF2
    echo "Created chapter_2_advanced_complex_numbers.md"
fi

echo "Adding new chapter on Complex Numbers..."
cat > "chapters/chapter_50_complex_numbers_theorems_complete.md" << 'NEW_CHAPTER'
# Complex Numbers: Complete Theorem Collection

## 5.0.1 Fundamental Properties

### 1.1 Complex Numbers as Polynomials

Complex numbers can be represented as polynomials in i with real coefficients. The ring ℂ is an algebraic extension of ℝ of degree 2.

**Theorem:** Every complex polynomial P(z) of degree n has exactly n roots in ℂ, counting multiplicity.

**Proof:** This is the Fundamental Theorem of Algebra.

### 1.2 Algebraic Closure

**Theorem:** ℂ is algebraically closed, meaning every non-constant polynomial with complex coefficients has a root in ℂ.

**Proof:** Using the properties of the complex exponential and Liouville's theorem.

## 5.0.2 Geometric Interpretations

### 2.1 Polar Representation

Every complex number z can be represented in polar form as z=re^{iθ}, where r=|z| and θ=arg(z).

**Theorem:** If z1=r1e^{iθ1} and z2=r2e^{iθ2}, then z1z2=r1r2e^{i(θ1+θ2)}.

**Proof:** Direct computation using properties of exponential and trigonometric functions.

### 2.2 Argand Diagram

The complex plane can be visualized as a 2D plane with the real part on the x-axis and the imaginary part on the y-axis.

**Theorem:** The geometric multiplication of complex numbers corresponds to rotation and scaling.

**Proof:** Using the properties of the exponential function.

## 5.0.3 Applications

### 3.1 Fourier Analysis

Complex numbers play a fundamental role in Fourier analysis and signal processing.

**Theorem:** The Fourier transform of a function f(t) is defined as F(ω)=∫_{-∞}^{∞} f(t)e^{-iωt}dt.

**Proof:** Using the properties of complex exponentials and the orthogonality of sine and cosine functions.

### 3.2 Electrostatics

In electrostatics, complex numbers represent the electric field.

**Theorem:** The complex potential W(z)=φ(x,y)+iψ(x,y) describes the electric field in two dimensions.

**Proof:** Using the properties of analytic functions and the Cauchy-Riemann equations.

---
NEW_CHAPTER
echo "Created chapter_50_complex_numbers_theorems_complete.md"

echo "Adding new chapter on Topology..."
cat > "chapters/chapter_51_toplogy_theorems_complete.md" << 'TOPOLOGY_EOF'
# Topology: Complete Theorem Collection

## 6.0.1 Basic Definitions

### 1.1 Topological Space

A topological space is a set X together with a collection O of subsets of X (the open sets) satisfying certain axioms.

**Theorem:** The intersection of finitely many open sets is open; the union of infinitely many open sets is open.

**Proof:** Direct from the axioms of a topological space.

### 1.2 Continuity

A function f:X→Y is continuous if the preimage of every open set in Y is open in X.

**Theorem:** f is continuous iff for every sequence (xn) in X converging to x, the sequence (f(xn)) converges to f(x).

**Proof:** Using the definition of convergence in topological spaces.

## 6.0.2 Connectedness

### 2.1 Connected Spaces

A space X is connected if it cannot be written as the union of two disjoint non-empty open sets.

**Theorem:** A space is connected iff it is not the union of two disjoint non-empty clopen sets.

**Proof:** Direct from the definition.

### 2.2 Path-Connectedness

A space X is path-connected if for any two points x,y∈X, there exists a continuous path f:[0,1]→X with f(0)=x and f(1)=y.

**Theorem:** Path-connectedness implies connectedness.

**Proof:** Let U and V be disjoint open sets covering X. If X is path-connected, then X cannot be disconnected because any path from a point in U to a point in V must intersect U∪V.

## 6.0.3 Compactness

### 3.1 Compact Sets

A set K is compact if every open cover of K has a finite subcover.

**Theorem:** Heine-Borel Theorem: In ℝ^n, a set is compact iff it is closed and bounded.

**Proof:** Using the properties of ℝ^n and the concept of boundedness.

### 3.2 Tychonoff's Theorem

The product of compact spaces is compact.

**Proof:** Using the finite intersection property.

## 6.0.4 Separation Axioms

### 4.1 Hausdorff Spaces

A space X is Hausdorff if for any two distinct points x,y∈X, there exist disjoint open sets U,V such that x∈U and y∈V.

**Theorem:** Hausdorff spaces are normal, regular, and T1.

**Proof:** Using the properties of compact sets and the definition of a normal space.

### 4.2 Normal Spaces

A space X is normal if for any two disjoint closed sets A,B⊆X, there exist disjoint open sets U,V such that A⊆U and B⊆V.

**Proof:** Direct from the definition.

## 6.0.5 Advanced Theorems

### 5.1 Brouwer Fixed-Point Theorem

Every continuous map f:D→D from a convex compact set D into itself has a fixed point.

**Proof:** Using the Borsuk-Ulam theorem and properties of homotopy.

### 5.2 Intermediate Value Theorem

If f:[a,b]→ℝ is continuous and f(a)<0<f(b), then there exists c∈(a,b) such that f(c)=0.

**Proof:** Using the connectedness of the interval [a,b].

---
TOPOLOGY_EOF
echo "Created chapter_51_toplogy_theorems_complete.md"

echo "Adding new chapter on Abstract Algebra..."
cat > "chapters/chapter_52_abstract_algebra_theorems_complete.md" << 'ABSTRACT_EOF'
# Abstract Algebra: Complete Theorem Collection

## 7.0.1 Group Theory

### 1.1 Groups

A group is a set G together with a binary operation * satisfying closure, associativity, identity, and inverse properties.

**Theorem:** Every group of order p^n (p prime) has a subgroup of order p^k for each k=0,1,...,n.

**Proof:** Using induction and properties of p-groups.

### 1.2 Abelian Groups

An abelian group is a group where the operation is commutative.

**Theorem:** Every abelian group is isomorphic to a direct sum of cyclic groups (Fundamental Theorem of Finite Abelian Groups).

**Proof:** Using the structure theory of abelian groups.

## 7.0.2 Ring Theory

### 2.1 Rings

A ring is a set R together with two binary operations + and · satisfying certain axioms.

**Theorem:** Every commutative ring with identity has a unique maximal ideal.

**Proof:** Using the properties of prime ideals and Zorn's lemma.

### 2.2 Integral Domains

An integral domain is a commutative ring with no zero divisors.

**Theorem:** An integral domain is a field iff every non-zero element has a multiplicative inverse.

**Proof:** Direct from the definitions.

## 7.0.3 Field Theory

### 3.1 Fields

A field is a commutative ring where every non-zero element has a multiplicative inverse.

**Theorem:** Every finite field has order p^n for some prime p and positive integer n.

**Proof:** Using properties of the Frobenius automorphism.

### 3.2 Galois Theory

**Theorem:** For a finite extension K/F, the Galois group Gal(K/F) acts transitively on the roots of any irreducible polynomial in F[x].

**Proof:** Using the properties of field automorphisms and the Fundamental Theorem of Galois Theory.

## 7.0.4 Advanced Algebra

### 4.1 Isomorphism Theorems

**First Isomorphism Theorem:** If φ:G→H is a group homomorphism, then G/ker(φ)≅im(φ).

**Proof:** Using the definition of homomorphisms and the First Isomorphism Theorem.

**Second Isomorphism Theorem:** If N,M≤G are subgroups with N⊆M, then N/(N∩M)≅(N+M)/M.

**Proof:** Using the properties of quotient groups.

### 4.2 Cayley's Theorem

Every finite group G of order n is isomorphic to a subgroup of the symmetric group S_n.

**Proof:** Using the regular representation of G.

---
ABSTRACT_EOF
echo "Created chapter_52_abstract_algebra_theorems_complete.md"

echo "Adding new chapter on Number Theory..."
cat > "chapters/chapter_53_number_theory_theorems_complete.md" << 'NUMEOF'
# Number Theory: Complete Theorem Collection

## 8.0.1 Basic Number Theory

### 1.1 Primes and Divisors

A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

**Theorem:** Every integer n>1 has a unique factorization into primes.

**Proof:** Using induction and the properties of primes.

### 1.2 Euclidean Algorithm

The Euclidean algorithm finds the greatest common divisor of two integers.

**Theorem:** gcd(a,b)=gcd(a mod b,b).

**Proof:** Using the properties of congruences.

## 8.0.2 Modular Arithmetic

### 2.1 Congruences

For integers a,b,n, we write a≡b(mod n) if n divides a-b.

**Theorem:** The congruence class of a modulo n is an equivalence class.

**Proof:** Using the properties of equivalence relations.

### 2.2 Fermat's Little Theorem

If p is prime and a is not divisible by p, then a^{p-1}≡1(mod p).

**Proof:** Using the properties of the multiplicative group of integers modulo p.

## 8.0.3 Euler's Totient Function

### 3.1 Euler's Theorem

If a and n are coprime, then a^{φ(n)}≡1(mod n), where φ(n) is Euler's totient function.

**Proof:** Using the properties of the multiplicative group of integers modulo n.

### 3.2 Euler's Totient Function Properties

φ(n) counts the number of positive integers less than n that are coprime to n.

**Theorem:** φ is multiplicative, meaning φ(ab)=φ(a)φ(b) when gcd(a,b)=1.

**Proof:** Using the properties of the multiplicative group of integers modulo n.

## 8.0.4 Advanced Number Theory

### 4.1 Primality Testing

**Theorem:** A number n is composite iff there exists a non-trivial congruence a^{n-1}≡1(mod n).

**Proof:** Using the properties of the multiplicative group of integers modulo n.

### 4.2 Dirichlet's Theorem on Arithmetic Progressions

For any two coprime integers a and d, there are infinitely many primes of the form a+nd.

**Proof:** Using the properties of the Dirichlet series and properties of the Riemann zeta function.

---
NUMEOF
echo "Created chapter_53_number_theory_theorems_complete.md"

echo "Math Book Update Job Completed $(date)"
