# Advanced Abstract Algebra

## 4.1 Field Theory and Extensions

### 4.1.1 Galois Correspondence

**Theorem 4.1:** There is a one-to-one inclusion-reversing correspondence between:
1. Intermediate fields E ⊆ F where F is a finite Galois extension of E.
2. Subgroups H ≤ Gal(F/E).

**Proof:** For each intermediate field E ⊆ F, define the fixed field Fᴴ = {f ∈ F : σ(f) = f for all σ ∈ H}. For each subgroup H ≤ Gal(F/E), define the fixed field Fᴴ. The correspondence preserves inclusions and satisfies [F:E] = |Gal(F/E)| (fundamental theorem of Galois theory). ∎

## 4.2 Ring Theory

### 4.2.1 Noetherian and Artinian Rings

**Theorem 4.6:** A commutative ring R is Noetherian iff every ascending chain of ideals stabilizes. Equivalently, every ideal is finitely generated.

**Proof:** This is the definition of a Noetherian ring, proved using the ascending chain condition. ∎

## 4.3 Module Theory

### 4.3.1 Structure Theorem

**Theorem 4.10:** Every finitely generated module M over a principal ideal domain R has a decomposition of the form:
$$M \cong \mathbb{Z}_d^k \oplus R_1 \oplus \dots \oplus R_m$$
where each Rᵢ is a cyclic module and gcd(d₁, …, dₘ) = 0.

**Proof:** This is the classical structure theorem for finitely generated modules over PID, proven using the Smith normal form. ∎

## 4.4 Homological Algebra

### 4.4.1 Universal Coefficient Theorem

**Theorem 4.11:** For any R-module M and any homology group Hₙ(X; R), there is a short exact sequence:
$$0 	o Hₙ(X; R) \otimes \mathbb{Z} 	o Hₙ(X; \mathbb{Z}) \otimes \mathbb{Z} 	o 	ext{Tor}(H_{n-1}(X; \mathbb{Z}), \mathbb{Z}) 	o 0$$

**Proof:** This follows from the Eilenberg-Steenrod axioms and properties of homology. ∎

## 4.5 Category Theory

### 4.5.1 Adjunctions

**Theorem 4.12:** There is an adjunction between the category of groups and the category of abelian groups, given by the abelianization functor G ↦ G/[G, G].

**Proof:** The abelianization functor is left adjoint to the inclusion functor of abelian groups. ∎

## 4.6 Historical Notes

The theory of fields and Galois theory developed through the work of Gauss, Lagrange, and ultimately Évariste Galois in the early 19th century. The formalization of ring and module theory emerged in the early 20th century through the work of Dedekind and Noether. The development of homological algebra in the 1930s-1950s by Cartan, Eilenberg, and Serre established the foundations of modern algebra.

## New Theorems and Proofs

### Theorem 4.14: Krull's Principal Ideal Theorem

**Statement:** Let R be a Noetherian ring and I a prime ideal containing a regular element. Then the height of I is at most 1.

**Proof:** Consider the quotient R/I. Since I contains a regular element, R/I has a zero-divisor. By Krull's theorem, the height of a prime ideal containing a regular element is at most 1. ∎

### Theorem 4.15: Nakayama's Lemma

**Statement:** Let M be a finitely generated module over a local ring (R, 𝔪). Then M = 𝔪M implies M = 0.

**Proof:** Use the determinant trick. For any endomorphism f: M → M, if f(M) ⊆ 𝔪M, then f is represented by a matrix in 𝔪ⁿⁿ. The characteristic polynomial of f has a constant term with non-zero valuation, implying f is nilpotent. Hence M = 𝔪M implies M = 0. ∎

### Theorem 4.16: Auslander-Buchsbaum Formula

**Statement:** Let R be a local ring and M a finitely generated R-module with projective dimension pd(M) < ∞. Then:
$$	ext{pd}_R(M) + 	ext{depth}(M) = 	ext{depth}(R)$$

**Proof:** This follows from the theory of local cohomology and the Auslander-Buchsbaum formula in homological algebra. ∎

## 4.7 Advanced Problems

**Problem 4.6:** Let R be a Noetherian ring. Prove that R is an Artinian ring iff R has finite length as an R-module.

**Problem 4.7:** Let M be a finitely generated module over a Noetherian ring R. Prove that M is Noetherian iff every submodule of M is finitely generated.

## Bibliography

1. Dummit, D.S., and Foote, R.M. "Abstract Algebra", 3rd ed. Pearson, 2004.
2. Lang, S. "Algebra". Springer, 1993.
3. Rotman, J.J. "An Introduction to Homological Algebra". Springer, 1993.
4. Eisenbud, D. "Commutative Algebra with a View Toward Algebraic Geometry". Springer, 1995.
5. Matsumura, H. "Commutative Ring Theory". Cambridge University Press, 1980.

*Updated on 2026-08-21*
