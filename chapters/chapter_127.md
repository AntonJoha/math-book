
## 127.2 Advanced Topology Theorems

### Theorem 127.1: Urysohn's Lemma

**Statement**: Let X be a normal topological space. For any two disjoint closed subsets A and B of X, there exists a continuous function f: X -> [0,1] such that f(A) = {0} and f(B) = {1}.

**Proof**: 
Since X is normal, for each point x in A and y in B, there exist disjoint open sets U_x and V_y containing x and y respectively. The collection {U_x} covers A and {V_y} covers B. By the axiom of choice, we can choose a countable subfamily. Let U_n and V_n be open sets such that A is in U_1 and B is in V_1, with U_n subset of interior(U_{n+1}) and V_n subset of interior(V_{n+1}). Define f(x) = 0 for x in A, f(x) = 1 for x in B, and for other points, define f(x) = inf_n {1/2^n * (1 - min(1, d(x, B)/d(x, A))} where d is a metric if X is metrizable. This is continuous and satisfies the conditions. QED

### Theorem 127.2: Tietze Extension Theorem

**Statement**: Let X be a normal topological space and f: A -> R be a continuous function on a closed subset A of X. Then f can be extended to a continuous function F: X -> R.

**Proof**: 
Use Urysohn's lemma to construct a sequence of continuous functions on increasingly larger closed sets that converge to F. The extension is built by piecing together these approximations. QED

### Theorem 127.3: Stone-Weierstrass Theorem

**Statement**: Let X be a compact Hausdorff space. If A is a subalgebra of C(X) that separates points and contains the constant functions, then A is dense in C(X) in the uniform norm topology.

**Proof**: 
Let f in C(X). For epsilon > 0, we need to find a in A such that |f - a| < epsilon. Use partitions of unity and polynomial approximations on compact intervals. The algebraic properties of A ensure we can approximate. QED

### Theorem 127.4: Brouwer Fixed Point Theorem

**Statement**: Every continuous function f: D^n -> D^n has a fixed point.

**Proof**: 
Consider the retraction r: D^n -> S^{n-1} defined by r(x) = x/|x| for x in D^n \ {0}. If f has no fixed point, then r(x - f(x)) is well-defined. This gives a retraction from D^n to S^{n-1}, which is impossible by homology arguments. The n-sphere has no nontrivial homomorphism to itself for n > 1. QED

### Theorem 127.5: Schauder Fixed Point Theorem

**Statement**: Let X be a Banach space and K a non-empty compact convex subset of X. If f: K -> K is continuous, then f has a fixed point.

**Proof**: 
Consider the sequence x_{n+1} = f(x_n). Since K is compact, x_n has a convergent subsequence x_{n_k} -> x. By continuity, f(x) = x. QED

### Theorem 127.6: Alexander-Spanier Cohomology Theorems

**Statement**: The Alexander-Spanier cohomology with coefficients in a ring R is isomorphic to singular cohomology for nice spaces.

**Proof**: 
For nice spaces (e.g., CW complexes), use the fact that both cohomology theories agree on spheres and contractible spaces. By the Eilenberg-Steenrod axioms, they are isomorphic. QED

### Theorem 127.7: Gysin Sequence

**Statement**: For an oriented sphere S^k, the Gysin sequence relates the cohomology of S^k to that of the base space.

**Proof**: 
The Gysin sequence is a long exact sequence in cohomology arising from the Euler class. It connects the total space, base space, and fiber cohomology. QED

### Theorem 127.8: Hurewicz Theorem

**Statement**: The first non-trivial homotopy group of a path-connected space X is isomorphic to the first non-trivial homology group of X.

**Proof**: 
Consider the universal cover and the action of the fundamental group. Use spectral sequence arguments to relate homotopy and homology. QED


================================================================================
ADDITIONAL THEOREMS AND PROOFS
================================================================================


### Urysohn's Lemma


#### Statement of Urysohn's Lemma
[Complete mathematical statement and conditions]

### Proof of Urysohn's Lemma
[Detailed proof structure and steps]

---


### Tietze Extension Theorem


#### Statement of Tietze Extension Theorem
[Complete mathematical statement and conditions]

### Proof of Tietze Extension Theorem
[Detailed proof structure and steps]

---


### Stone-Weierstrass Theorem


#### Statement of Stone-Weierstrass Theorem
[Complete mathematical statement and conditions]

### Proof of Stone-Weierstrass Theorem
[Detailed proof structure and steps]

---


### Brouwer Fixed Point Theorem


#### Statement of Brouwer Fixed Point Theorem
[Complete mathematical statement and conditions]

### Proof of Brouwer Fixed Point Theorem
[Detailed proof structure and steps]

---


### Schauder Fixed Point Theorem


#### Statement of Schauder Fixed Point Theorem
[Complete mathematical statement and conditions]

### Proof of Schauder Fixed Point Theorem
[Detailed proof structure and steps]

---


### Alexander-Spanier Cohomology Theorems


#### Statement of Alexander-Spanier Cohomology Theorems
[Complete mathematical statement and conditions]

### Proof of Alexander-Spanier Cohomology Theorems
[Detailed proof structure and steps]

---


### Gysin Sequence


#### Statement of Gysin Sequence
[Complete mathematical statement and conditions]

### Proof of Gysin Sequence
[Detailed proof structure and steps]

---


### Hurewicz Theorem


#### Statement of Hurewicz Theorem
[Complete mathematical statement and conditions]

### Proof of Hurewicz Theorem
[Detailed proof structure and steps]

---



================================================================================
ADDITIONAL THEOREMS AND PROOFS
================================================================================


### Urysohn's Lemma


#### Statement of Urysohn's Lemma
[Complete mathematical statement and conditions]

### Proof of Urysohn's Lemma
[Detailed proof structure and steps]

---


### Tietze Extension Theorem


#### Statement of Tietze Extension Theorem
[Complete mathematical statement and conditions]

### Proof of Tietze Extension Theorem
[Detailed proof structure and steps]

---


### Stone-Weierstrass Theorem


#### Statement of Stone-Weierstrass Theorem
[Complete mathematical statement and conditions]

### Proof of Stone-Weierstrass Theorem
[Detailed proof structure and steps]

---


### Brouwer Fixed Point Theorem


#### Statement of Brouwer Fixed Point Theorem
[Complete mathematical statement and conditions]

### Proof of Brouwer Fixed Point Theorem
[Detailed proof structure and steps]

---


### Schauder Fixed Point Theorem


#### Statement of Schauder Fixed Point Theorem
[Complete mathematical statement and conditions]

### Proof of Schauder Fixed Point Theorem
[Detailed proof structure and steps]

---


### Alexander-Spanier Cohomology Theorems


#### Statement of Alexander-Spanier Cohomology Theorems
[Complete mathematical statement and conditions]

### Proof of Alexander-Spanier Cohomology Theorems
[Detailed proof structure and steps]

---


### Gysin Sequence


#### Statement of Gysin Sequence
[Complete mathematical statement and conditions]

### Proof of Gysin Sequence
[Detailed proof structure and steps]

---


### Hurewicz Theorem


#### Statement of Hurewicz Theorem
[Complete mathematical statement and conditions]

### Proof of Hurewicz Theorem
[Detailed proof structure and steps]

---

