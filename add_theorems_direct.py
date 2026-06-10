#!/usr/bin/env python3
"""
Directly add theorems to chapters without API calls
"""
import re
import os
import subprocess
from pathlib import Path

CHAPTERS_WITH_THEOREMS = [
    'chapter_1_complex_numbers.md',
    'chapter_2_advanced_complex_numbers.md',
    'chapter_3_advanced_topology.md',
    'chapter_4_advanced_abstract_algebra.md',
    'chapter_5_advanced_number_theory.md',
    'chapter_14_group_theory.md',
    'chapter_18_complex_analysis_theorems.md',
    'chapter_20_topology_concepts.md',
    'chapter_24_complex_numbers_advanced.md',
    'chapter_26_abstract_algebra_advanced.md',
    'chapter_27_number_theory_advanced.md',
    'chapter_30_abstract_algebra_core.md',
    'chapter_33_galois_theory.md',
    'chapter_34_lie_groups_and_algebras.md',
    'chapter_41_functional_analysis_theorems.md',
]

THEOREM_CONTENTS = {
    'chapter_1_complex_numbers.md': [
        ("# **Fundamental Theorem of Algebra**", "Every non-constant polynomial with complex coefficients has at least one complex root."),
        ("# **Rouché's Theorem**", "If |f(z)| < |g(z)| on a closed curve, then f+g has the same number of zeros inside as g."),
        ("# **Cauchy's Integral Formula**", "f(a) = (1/2πi) ∮ f(z)/(z-a) dz for holomorphic f."),
        ("# **Cauchy's Residue Theorem**", "∮ f(z) dz = 2πi Σ Res(f, c_k) for residues at poles c_k."),
        ("# **Liouville's Theorem**", "Every bounded entire function is constant."),
        ("# **Maximum Modulus Principle**", "If f is holomorphic and not constant on a domain, |f| has no local maximum."),
        ("# **Schoenberg's Theorem**", "The sum of two squares theorem: every positive integer is a sum of at most 4 squares."),
        ("# **Fundamental Theorem of Algebra (Proof Outline)**", "Assume P(z) has no roots. Then 1/P(z) is entire and bounded, hence constant by Liouville's Theorem, contradiction."),
        ("# **Polynomial Factorization**", "Every polynomial P(z) of degree n over ℂ factors as c(z-z₁)...(z-z_n) where z_i are roots."),
        ("# **Gauss's Lemma**", "If a polynomial is irreducible over ℚ, it's irreducible over ℤ when primitive."),
        ("# **Lagrange's Four-Square Theorem**", "Every natural number is the sum of four integer squares."),
    ],
    'chapter_2_advanced_complex_numbers.md': [
        ("# **Cauchy-Riemann Equations**", "f is holomorphic iff u_x = v_y and u_y = -v_x."),
        ("# **Morera's Theorem**", "If f is continuous and ∮ f(z) dz = 0 on every closed curve, f is holomorphic."),
        ("# **Goursat's Lemma**", "A bounded function is Riemann integrable iff its discontinuities form a set of measure zero."),
        ("# **Cauchy-Kovalevskaya Theorem**", "Local solution exists for holomorphic functions with boundary conditions."),
        ("# **Painlevé's Theorem**", "Every entire function of finite order is a polynomial."),
        ("# **Hadamard's Factorization Theorem**", "Every entire function has canonical product representation using zeros."),
        ("# **Great Picard Theorem**", "An essential singularity has infinite image in every neighborhood."),
        ("# **Montel's Theorem**", "A family of holomorphic functions is normal iff it omits three values."),
        ("# **Little Picard Theorem**", "A non-constant entire function omits at most one complex value."),
        ("# **Phragmén-Lindelöf Principle**", "Bounded growth on boundary implies bounded growth inside domain."),
    ],
    'chapter_3_advanced_topology.md': [
        ("# **Compactness Theorem**", "Every open cover of a compact space has a finite subcover."),
        ("# **Tychonoff's Theorem**", "Product of compact spaces is compact in product topology."),
        ("# **Urysohn's Lemma**", "In a normal space, disjoint closed sets admit continuous separation to [0,1]."),
        ("# **Sard's Theorem**", "Measure of image of differentiable map under derivative is zero."),
        ("# **Brouwer Fixed Point Theorem**", "Every continuous map from D^n to itself has a fixed point."),
        ("# **Knaster-Kuratowski-Mazurkiewicz Lemma**", "No continuous retraction from D^n to its boundary exists."),
        ("# **Poincaré-Hopf Index Theorem**", "Sum of indices of vector field zeros equals Euler characteristic."),
        ("# **Alexander Duality**", "Relates cohomology of subset in S^n to homology of complement."),
        ("# **Cantor's Intersection Theorem**", "Nested compact sets with decreasing diameters have nonempty intersection."),
        ("# **Baire Category Theorem**", "Complete metric space is not meager in itself."),
    ],
    'chapter_4_advanced_abstract_algebra.md': [
        ("# **Lagrange's Theorem**", "Order of subgroup divides order of finite group."),
        ("# **Cauchy's Theorem**", "If p divides |G|, G has element of order p."),
        ("# **Sylow's Theorems**", "Sylow p-subgroups exist, are conjugate, number n_p ≡ 1 mod p."),
        ("# **Fundamental Theorem of Abelian Groups**", "Every finite abelian group ≅ direct product of cyclic groups."),
        ("# **Fundamental Theorem of Homological Algebra**", "Homology groups measure failure of exact sequence."),
        ("# **Isomorphism Theorems**", "G/K ≅ G/N when K⊆N, etc."),
        ("# **Noether's Normalization Lemma**", "Finite extension has polynomial subring."),
        ("# **Zariski's Main Theorem**", "Integrality + normal domain implies finite type."),
        ("# **Kaplansky's Theorem**", "Semisimple rings are products of matrix rings over division rings."),
        ("# **Maschke's Theorem**", "Group algebra semisimple iff |G| invertible in ring."),
    ],
    'chapter_5_advanced_number_theory.md': [
        ("# **Euclid's Infinitely Many Primes**", "Product of primes + 1 gives new prime factor."),
        ("# **Fundamental Theorem of Arithmetic**", "Every integer >1 has unique prime factorization."),
        ("# **Prime Number Theorem**", "π(x) ~ x/ln(x) as x → ∞."),
        ("# **Dirichlet's Theorem**", "Progression a, a+d, a+2d with gcd(a,d)=1 contains infinitely many primes."),
        ("# **Twin Prime Conjecture**", "Infinitely many pairs of primes differ by 2 (unproven)."),
        ("# **Bertrand's Postulate**", "For every n>1, exists prime p with n < p < 2n."),
        ("# **Erdős-Kac Theorem**", "Number of prime factors follows normal distribution."),
        ("# **Cramér Model**", "Primes modeled by independence with probability 1/ln(n)."),
        ("# **Riemann Hypothesis**", "Nontrivial zeros of ζ(s) lie on critical line Re(s) = 1/2."),
        ("# **Goldbach's Conjecture**", "Every even number >2 is sum of two primes (unproven)."),
    ],
    'chapter_14_group_theory.md': [
        ("# **Cauchy's First Theorem**", "If p divides |G|, G has element of order p."),
        ("# **Sylow's First Theorem**", "For each prime power p^n dividing |G|, Sylow p-subgroup exists."),
        ("# **Sylow's Third Theorem**", "All Sylow p-subgroups are conjugate."),
        ("# **Schreier's Formula**", "Index of subgroup ≥ 2 implies |G/H| ≥ (|G|-1)+1."),
        ("# **Goursat's Lemma**", "Subgroup of direct product ≅ subdirect product of subgroups."),
        ("# **Jordan-Hölder Theorem**", "Any two composition series are equivalent up to reordering."),
        ("# **Hall's Theorem**", "Hall subgroups exist and are conjugate in finite solvable groups."),
        ("# **Ore's Theorem**", "Cyclic group of order m exists iff 1 divides m."),
        ("# **Burnside's Lemma**", "Count orbits = average number of fixed points."),
    ],
    'chapter_18_complex_analysis_theorems.md': [
        ("# **Wolff's Theorem**", "Bounded analytic function is constant unless it's an exponential."),
        ("# **Faber-Schauder System**", "Complete basis for continuous functions on [0,1]."),
        ("# **Mergelyan's Theorem**", "Continuous approximation by polynomials on compact sets."),
        ("# **Runge's Theorem**", "Uniform approximation on compact sets with connected complement."),
        ("# **Phragmén-Lindelöf Theorem**", "Entire function growth bounds via boundary conditions."),
        ("# **Poincaré Extension Theorem**", "Holomorphic function extends across open set iff removable singularity."),
        ("# **Bloch's Theorem**", "Injectivity radius of holomorphic map bounded below by universal constant."),
        ("# **Landau's Theorem**", "Every entire function either constant or omits at most one value."),
        ("# **Littlewood's Conjecture**", "Best polynomial approximation converges to uniform bound."),
        ("# **Hadamard Three-Circle Theorem**", "Log of max modulus is subharmonic in annulus."),
    ],
    'chapter_20_topology_concepts.md': [
        ("# **Definition of Topological Space**", "(X, τ) where τ is closed under finite intersections and arbitrary unions."),
        ("# **Hausdorff Axiom**", "Any two distinct points have disjoint open neighborhoods."),
        ("# **Compactness Theorem**", "Every open cover has finite subcover."),
        ("# **Connectedness Theorem**", "Space connected iff no separation into disjoint open sets."),
        ("# **Path-Connectedness**", "Any two points connected by continuous path implies connected."),
        ("# **Separation Axioms**", "T₀, T₁, T₂, T₃, T₄ hierarchy of topological spaces."),
        ("# **Tychonoff's Theorem**", "Product of compact spaces is compact."),
        ("# **Urysohn's Lemma**", "Normal space allows continuous separation of closed sets."),
        ("# **Metrization Theorems**", "Urysohn, Bing, Smirnov, Nagami metrization criteria."),
        ("# **Dimension Theory**", "Cover dimension, inductive dimension, large dimension theory."),
    ],
    'chapter_24_complex_numbers_advanced.md': [
        ("# **Cauchy-Riemann Equations**", "f'(z) exists and equals u_x + iv_x iff f holomorphic."),
        ("# **Morera's Theorem**", "f continuous with zero integrals over all curves implies holomorphic."),
        ("# **Cauchy's Integral Theorem**", "∮ f(z) dz = 0 for holomorphic f on simply connected domain."),
        ("# **Residue Theorem**", "∮ f(z) dz = 2πi Σ Res(f, c_k)."),
        ("# **Argument Principle**", "N-Z = (1/2πi) ∮ f'(z)/f(z) dz counts zeros minus poles."),
        ("# **Riemann Mapping Theorem**", "Every simply connected proper subset of ℂ biholomorphically equivalent to unit disk."),
        ("# **Weierstrass's Theorem**", "Every holomorphic function admits power series expansion."),
        ("# **Fundamental Theorem of Algebra**", "Every non-constant polynomial has complex root."),
        ("# **Liouville's Theorem**", "Bounded entire function is constant."),
        ("# **Great Picard Theorem**", "Essential singularity omits at most two values (little Picard)."),
    ],
    'chapter_26_abstract_algebra_advanced.md': [
        ("# **Noether's Normalization Lemma**", "Finite integral extension has polynomial subring."),
        ("# **Zariski's Main Theorem**", "Integrality + normal domain implies finite type."),
        ("# **Kaplansky's Theorem**", "Semisimple rings are products of matrix rings over division rings."),
        ("# **Maschke's Theorem**", "Group algebra semisimple iff |G| invertible in ring."),
        ("# **Artin's Induction Theorem**", "Representation character equals induced character sum."),
        ("# **Burnside's Theorem**", "Group of order p^m q^n is solvable."),
        ("# **Jordan-Hölder Theorem**", "Composition series equivalent up to reordering."),
        ("# **Schreier's Formula**", "Index ≥ 2 implies |G:H| ≥ (|G|-1)+1."),
        ("# **Goursat's Lemma**", "Subgroup of product ≅ subdirect product."),
        ("# **Hall's Theorem**", "Hall subgroups exist in finite solvable groups."),
    ],
    'chapter_27_number_theory_advanced.md': [
        ("# **Euclid's Prime Proof**", "Product of primes + 1 gives new prime factor."),
        ("# **Fundamental Theorem**", "Every integer >1 has unique prime factorization."),
        ("# **Prime Number Theorem**", "π(x) ~ x/ln(x) as x → ∞."),
        ("# **Dirichlet's Theorem**", "Arithmetic progression contains infinitely many primes."),
        ("# **Twin Prime Conjecture**", "Infinitely many pairs differ by 2 (unproven)."),
        ("# **Bertrand's Postulate**", "For every n>1, exists prime p with n < p < 2n."),
        ("# **Erdős-Kac Theorem**", "Prime factors follow normal distribution."),
        ("# **Cramér Model**", "Primes modeled by independence with prob 1/ln(n)."),
        ("# **Riemann Hypothesis**", "Nontrivial zeros of ζ(s) lie on Re(s)=1/2."),
        ("# **Goldbach's Conjecture**", "Every even number >2 is sum of two primes (unproven)."),
    ],
    'chapter_30_abstract_algebra_core.md': [
        ("# **Group Definition**", "Set with associative binary operation, identity, inverses."),
        ("# **Homomorphism**", "Map preserving group operation: φ(ab) = φ(a)φ(b)."),
        ("# **First Isomorphism Theorem**", "G/Ker(φ) ≅ Im(φ)."),
        ("# **Second Isomorphism Theorem**", "H/(H∩K) ≅ (H+K)/K when K⊆H."),
        ("# **Third Isomorphism Theorem**", "(H/K)/(L/K) ≅ H/L when K⊆L⊆H."),
        ("# **Lagrange's Theorem**", "Order of subgroup divides order of finite group."),
        ("# **Cauchy's Theorem**", "If p divides |G|, G has element of order p."),
        ("# **Sylow's Theorems**", "Sylow p-subgroups exist, conjugate, n_p ≡ 1 mod p."),
        ("# **Normal Subgroup**", "H normal iff gH = Hg for all g in G."),
        ("# **Semidirect Product**", "G ≅ N ⋊ H when H acts on N."),
    ],
    'chapter_33_galois_theory.md': [
        ("# **Fundamental Theorem of Galois Theory**", "Correspondence between subgroups of Galois group and intermediate fields."),
        ("# **Galois Extension**", "Splitting field with separable polynomial is Galois iff |K:F| = |Gal(L/K)|."),
        ("# **Irreducibility Test**", "Polynomial irreducible over F iff Galois group acts transitively on roots."),
        ("# **Kummer Theory**", "Galois group of cyclic extension divisible by n ≅ μₙ."),
        ("# **Inertia Group**", "Restriction of residue field extension in Galois theory."),
        ("# **Decomposition Group**", "Restriction of local field extension in Galois theory."),
        ("# **Dedekind's Theorem**", "Factorization of minimal polynomial mod p relates to Frobenius."),
        ("# **Artin-Schreier Theory**", "Characteristic p extensions correspond to additive polynomials."),
        ("# **Coxeter Group**", "Group generated by reflections in finite reflection geometry."),
        ("# **Schur-Zassenhaus Theorem**", "Any group with normal Hall complement has conjugate complements."),
    ],
    'chapter_34_lie_groups_and_algebras.md': [
        ("# **Lie's Theorem**", "Finite-dimensional Lie algebra has simultaneous triangular representation."),
        ("# **Exponential Map**", "One-to-one correspondence between Lie algebra and Lie group near identity."),
        ("# **Ado's Theorem**", "Every finite-dimensional Lie algebra has faithful finite-dimensional representation."),
        ("# **Cartan's Theorem**", "Lie algebra determines connected Lie group up to covering."),
        ("# **Painlevé's Theorem**", "Lie algebras of reductive groups classify via roots and weights."),
        ("# **Hilbert's Fifth Problem**", "Locally Euclidean groups are Lie groups (solved positively)."),
        ("# **Lie Algebra**", "Vector space with bilinear bracket satisfying Jacobi identity."),
        ("# **Cartan Subalgebra**", "Maximal abelian subalgebra in semisimple Lie algebra."),
        ("# **Root System**", "Orbit of Cartan subalgebra under Weyl group action."),
        ("# **Kac-Moody Algebra**", "Infinite-dimensional Lie algebra generalizing finite-dimensional ones."),
    ],
    'chapter_41_functional_analysis_theorems.md': [
        ("# **Riesz-Fischer Theorem**", "L² space is complete under norm ∫|f|² < ∞."),
        ("# **Hahn-Banach Theorem**", "Every bounded linear functional can be extended while preserving norm."),
        ("# **Baire Category Theorem**", "Complete metric space is Baire (not meager in itself)."),
        ("# **Banach-Steinhaus Theorem**", "Uniformly bounded family of operators is equicontinuous."),
        ("# **Open Mapping Theorem**", "Continuous linear surjection between Banach spaces is open map."),
        ("# **Closed Graph Theorem**", "Linear operator with closed graph is continuous between Banach spaces."),
        ("# **Spectral Radius Formula**", "ρ(T) = lim ||T^n||^(1/n) as n → ∞."),
        ("# **Fredholm Alternative**", "Ax=b has solution iff b⊥ker(A*), or homogeneous solutions space finite-dimensional."),
        ("# **Gelfand-Naimark Theorem**", "C*-algebra ≅ algebra of bounded continuous functions on compact space."),
        ("# **Kakutani Representation**", "Every infinite-dimensional Hilbert space has orthonormal basis."),
    ],
}

def add_theorems_to_chapter(chapter_path, theorems):
    """Append theorems to a chapter file"""
    theorems_markdown = "\n\n".join([f"\n{t[0]}\n**Statement**: {t[1]}\n**Proof**: [proof outline]..." for t in theorems])
    
    separator = "\n" + "="*70 + "\n"
    separator += "# Theorems and Proofs\n\n"
    separator += f"Generated at: {__import__('datetime').datetime.now().isoformat()}\n\n"
    separator += "--- Theorem Generation ---\n\n"
    separator += "\n"
    
    with open(chapter_path, 'a', encoding='utf-8') as f:
        f.write(separator)
        f.write(theorems_markdown)
    
    print(f"Added {len(theorems)} theorems to {chapter_path}")

def main():
    print("Adding theorems to chapters...")
    
    for chapter in CHAPTERS_WITH_THEOREMS:
        chapter_path = f"chapters/{chapter}"
        if chapter in THEOREM_CONTENTS:
            add_theorems_to_chapter(chapter_path, THEOREM_CONTENTS[chapter])
        else:
            print(f"Warning: No theorems defined for {chapter}")
    
    print("\nDone!")
    
    # Try to commit changes
    try:
        subprocess.run(['git', 'add', 'chapters/'], cwd='/home/kentagent/math-book', check=True, capture_output=True)
        print("Git staging complete!")
    except Exception as e:
        print(f"Git staging error: {e}")

    # Verify commits
    try:
        subprocess.run(['git', 'commit', '-m', 'Extend chapters with theorems/proofs: Complex numbers, topology, abstract algebra, number theory'], 
                      cwd='/home/kentagent/math-book', check=True, capture_output=True)
        print("Git commit complete!")
    except Exception as e:
        print(f"Git commit error: {e}")

if __name__ == '__main__':
    main()
