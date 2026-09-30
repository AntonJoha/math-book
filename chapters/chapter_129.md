## 129. Topology: Open Sets, Compactness, and Connectedness

### 129.1 Topological Spaces and Open Sets

**Definition**: A topological space is a pair (X, τ) where X is a set and τ is a collection of subsets of X (called open sets) satisfying:
1. ∅ ∈ τ and X ∈ τ
2. Arbitrary unions of sets in τ are in τ
3. Finite intersections of sets in τ are in τ

**Metric Spaces**: Given a metric space (M, d), the open balls B(x, r) = {y ∈ M | d(x, y) < r} form a basis for a topology τ_d on M.

**Theorem**: Let (M, d) be a metric space. The collection of all open balls forms a topology on M.

**Proof**: 
Let U, V be open sets (arbitrary unions of open balls).
- ∅ and M are unions of empty and all open balls respectively.
- Arbitrary union of open balls is an open set by definition.
- Finite intersection of open balls: B(x, r₁) ∩ B(x, r₂) = B(x, min(r₁,r₂)) and for y,z: B(y, r_y) ∩ B(z, r_z) is a union of open balls with radii d(y,z)/2, d(y,z)/2, ...
Thus the intersection of finite open sets is open. QED

### 129.2 Closed Sets and Closure

**Definition**: A subset C of topological space X is closed if X \ C is open. The closure of A, cl(A), is the smallest closed set containing A.

**Theorem**: In a metric space, cl(A) = {x | x is a limit point of A} ∪ A.

**Proof**: 
Let C = {x | x is a limit point of A} ∪ A.
- C is closed: The complement is the set of points not in cl(A), which is an open set by definition.
- A ⊆ C: trivial.
- C is the smallest closed set containing A: Any closed set containing A must contain all its limit points, hence must contain cl(A). QED

### 129.3 Compactness

**Definition**: A topological space K is compact if every open cover has a finite subcover.

**Theorem (Heine-Borel)**: In ℝⁿ with standard topology, K is compact if and only if K is closed and bounded.

**Proof**: 
(⇒) Suppose K is compact. Suppose K is not bounded. Then there exists a sequence {x_n} in K with ||x_n|| → ∞. This sequence has no convergent subsequence, contradicting compactness. Thus K is bounded.
Suppose K is not closed. Then there exists a limit point x ∉ K. Consider a sequence converging to x; its image is a compact set not containing x, contradicting compactness.
(⇐) Suppose K is closed and bounded. In ℝⁿ, the Heine-Borel theorem follows from Riesz's lemma and the fact that closed balls are compact. QED

### 129.4 Connectedness

**Definition**: A topological space X is connected if it cannot be written as the union of two disjoint non-empty open sets.

**Theorem**: The continuous image of a connected space is connected.

**Proof**: 
Let f: X → Y be continuous, where X is connected. Suppose f(X) = U ∪ V where U, V are disjoint non-empty open sets in Y.
Then f⁻¹(U) and f⁻¹(V) are disjoint open sets in X whose union is X. But X is connected, so this is impossible unless one is empty. Thus f(X) is connected. QED

### 129.5 Path-Connectedness

**Definition**: A space X is path-connected if for any x, y ∈ X, there exists a continuous function γ: [0,1] → X with γ(0) = x and γ(1) = y.

**Theorem**: Path-connected implies connected, but the converse does not necessarily hold.

**Counterexample**: The topologist's sine curve is connected but not path-connected.
- Define S = {(x, sin(1/x)) | x ∈ (0,1]} ∪ ({0} × [-1,1])
- S is the continuous image of the connected space ([0,1] × {0}) ∪ {(1/n, sin(nπ)) | n ∈ ℕ} which is connected.
- However, any path from a point on {(0} × [-1,1]) to a point on {(x, sin(1/x)) | x ∈ (0,1]} must oscillate infinitely near x = 0, making it impossible to be continuous. QED

### 129.6 Separated Axioms

**Definition**: A topological space X is Hausdorff (T₂) if for any distinct x, y ∈ X, there exist disjoint open neighborhoods U, V of x and y respectively.

**Theorem**: Compact Hausdorff spaces are normal (T₄).

**Proof**: 
Let X be compact Hausdorff, and A, B be disjoint closed sets. For each x ∈ A, y ∈ B, there exist disjoint open neighborhoods U_x, V_y.
By compactness, A is covered by finitely many U_x's and B by finitely many V_y's. Their finite intersections give disjoint open neighborhoods separating A and B. QED

### 129.7 Separability

**Definition**: A space X is separable if it contains a countable dense subset.

**Theorem**: Any separable metric space is second-countable.

**Proof**: 
Let D = {d_n} be a countable dense subset of separable metric space (X, d).
For each n, k ∈ ℕ, let B(d_n, 1/k) be the open ball of radius 1/k centered at d_n.
The collection {B(d_n, 1/k) | n, k ∈ ℕ} is countable.
For any open set U and any x ∈ U, there exists ε > 0 such that B(x, ε) ⊆ U. Choose k > 1/ε. Since D is dense, there exists d_n such that d(x, d_n) < ε/2. Then B(d_n, ε/2) ⊆ B(x, ε) ⊆ U, so B(d_n, ε/2) ⊆ U.
Thus the basis {B(d_n, 1/k)} generates the topology, making X second-countable. QED

### 129.8 Compactness Characterizations

**Theorem**: In a metric space, the following are equivalent:
1. X is compact
2. X is sequentially compact (every sequence has a convergent subsequence)
3. X is totally bounded and complete

**Proof**: 
(1) ⇒ (2): Standard result using open covers.
(2) ⇒ (3): If X is not totally bounded, there exists ε > 0 such that infinitely many ε-separated points exist, constructing a sequence with no Cauchy subsequence, contradicting sequential compactness.
(3) ⇒ (1): Given a sequence of ε > 0, construct a finite ε-net. Total boundedness and completeness imply the limit exists, giving compactness. QED

### 129.9 Local Compactness

**Definition**: A space X is locally compact if every point has a compact neighborhood.

**Theorem**: Every locally compact Hausdorff space is the direct limit of its compact neighborhoods.

**Proof**: 
Let {K_α} be the directed family of compact neighborhoods of x. Each K_α contains a compact neighborhood of x, and the union covers X in a neighborhood of x.
By the definition of local compactness and Hausdorff separation, the limit topology agrees with the original topology on compact neighborhoods. QED

### 129.10 Compactifications

**Definition**: A compactification of X is a compact Hausdorff space K containing X as a dense subspace.

**Theorem**: The one-point compactification of a non-compact locally compact Hausdorff space X is unique up to homeomorphism.

**Proof**: 
Let K = X ∪ {∞} with open sets being open sets of X not containing ∞, and sets of the form {∞} ∪ (X \ compact subset).
Any other compactification is homeomorphic to this via the unique continuous extension of the identity on X. QED

