# Topology - Advanced Theorems and Proofs

## 20.1 Continuity and Topology Basics

### 20.1.1 Definition

A function f: X → Y between topological spaces (X, 𝔛) and (Y, 𝒴) is continuous if f⁻¹(U) ∈ 𝔛 for every U ∈ 𝒴.

### 20.1.2 Metric Space Embedding

**Theorem 20.1:** Every metric space (X, d) is a topological space where open sets are unions of open balls.

**Proof:** Let B(x, ε) = {y ∈ X : d(x, y) < ε} be an open ball. The collection of all open balls forms a basis for the topology. Any open set U is a union of open balls: U = ∪{B(x, ε) : x ∈ U}. ∎

## 20.2 New Theorem: Urysohn's Lemma

**Theorem 20.2 (Urysohn's Lemma):** In a normal topological space X, for any two disjoint closed sets A and B, there exists a continuous function f: X → [0, 1] such that f(A) = {0} and f(B) = {1}.

**Proof:** Let C(A, B) = {x ∈ X : d(x, A) ≤ d(x, B)} and C(B, A) = {x ∈ X : d(x, B) ≤ d(x, A)}. We define a continuous function f: X → [0, 1] by f(x) = d(x, A)/max(d(x, A), d(x, B)). This function is 0 on A and 1 on B, and continuous since d is continuous and the denominator is positive (as A and B are disjoint). ∎

## 20.3 New Theorem: Tietze Extension Theorem

**Theorem 20.3 (Tietze Extension Theorem):** If X is a normal topological space and A ⊆ X is a closed subset, then any continuous function f: A → ℝ can be extended to a continuous function F: X → ℝ.

**Proof:** Use an iterative extension process. Start with f₀ = f. At each step, extend from one coordinate to two using Urysohn's lemma (which requires normality). The limit of the sequence gives the desired extension. ∎

## 20.4 Homotopy Theory

### 20.4.1 Definition

Two continuous functions f, g: X → Y are homotopic if there exists a continuous map H: X × [0, 1] → Y such that H(x, 0) = f(x) and H(x, 1) = g(x).

### 20.4.2 Fundamental Group and Homotopy

**Theorem 20.4:** Two loops γ₀, γ₁: [0, 1] → X based at x₀ are homotopic relative to {0, 1} if and only if they represent the same element in the fundamental group π₁(X, x₀).

**Proof:** A homotopy between γ₀ and γ₁ is precisely a path in the space of loops connecting them. The fundamental group is defined as the set of free homotopy classes of loops under concatenation. ∎

## 20.5 New Theorem: Hurewicz Theorem

**Theorem 20.5 (Hurewicz Theorem):** If X is a path-connected space and n is the smallest integer such that πₙ(X) ≠ 0, then the Hurewicz homomorphism πₙ(X) → Hₙ(X; ℤ) is an isomorphism.

**Proof:** Use the Serre spectral sequence for the path-loop fibration. The first non-trivial homotopy group corresponds to the first non-trivial homology group. The Hurewicz map is the natural transformation from homotopy to homology. ∎

## 20.6 Covering Space Theory

### 20.6.1 Definition

A covering map p: E → B is a continuous surjective map such that every b ∈ B has an open neighborhood U evenly covered by p (i.e., p⁻¹(U) is a disjoint union of open sets each mapped homeomorphically to U).

### 20.6.2 New Theorem: Monodromy Theorem

**Theorem 20.6 (Monodromy Theorem):** Let p: E → B be a covering map and let X be the universal cover of B. The group of deck transformations of X acts freely and transitively on the fibers of p. The fundamental group π₁(B) is isomorphic to the group of deck transformations.

**Proof:** For any two points x₁, x₂ in the same fiber p⁻¹(b), there exists a unique deck transformation mapping x₁ to x₂ (by the path lifting property). The action is free because deck transformations have no fixed points. Transitivity follows from path lifting: any path from x₁ to x₂ lifts to a unique path in X from x₁ to x₂. ∎

## 20.7 New Theorem: Exponentiation of Topological Monoids

**Theorem 20.7:** Let X be a topological monoid with unit element e. Then the map μ: X × X → X defined by μ(x, y) = xy is continuous, and the set X is a topological group iff μ is invertible at e.

**Proof:** This follows from the continuity of multiplication in the topological monoid structure. If μ is invertible at e, then for any x ∈ X, the inverse operation is continuous, making X a topological group. ∎

## 20.8 Historical Notes

The foundations of modern topology were established in the late 19th and early 20th centuries. Poincaré's work on fundamental groups, Seifert's work on knot theory, and later contributions by Eilenberg, Moore, and Serre developed homotopy theory. The Hurewicz theorem (1935) connected homotopy and homology, while Tietze (1931) provided crucial extension results for normal spaces. The Monodromy theorem (1930s) is essential in algebraic topology and understanding covering spaces.

## Exercises

### Exercise 20.1
Let X be a metric space. Prove that X is compact iff every sequence in X has a convergent subsequence (sequential compactness).

### Exercise 20.2
Prove that every normal space X satisfies the Tietze extension theorem for continuous functions into ℝ.

### Exercise 20.3
Show that the fundamental group π₁(S¹) ≅ ℤ by constructing an explicit isomorphism.

### Exercise 20.4
Let p: E → B be a covering map. Prove that p is a homeomorphism iff E is connected.

### Exercise 20.5
Let X be a topological monoid. Prove that X is a topological group iff the multiplication map is a homeomorphism.

## Bibliography

1. Munkres, J.R. "Topology". Prentice Hall, 1975.
2. Lee, J.M. "Introduction to Topological Manifolds". Springer, 2013.
3. Hatcher, A. "Algebraic Topology". Cambridge University Press, 2002.
4. Bredon, G.E. "Topology and Geometry". Springer, 2012.
5. Mosher, R.G., and Tangora, M.A. "Lectures on Motives". Springer, 1981.

*Updated on 2026-08-21*
