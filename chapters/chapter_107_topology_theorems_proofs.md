# Chapter 107: Topology - Theorems and Proofs

## 107.1 Connectedness

### Theorem 107.1 (Intermediate Value Theorem)
Let $f: [a,b] \to \mathbb{R}$ be continuous. If $f(a) < c < f(b)$, then there exists $c_0 \in [a,b]$ such that $f(c_0) = c$.

**Proof:**
By the least upper bound property. Let $S = \{x \in [a,b] : f(x) < c\}$. Since $f(a) < c$, $S$ is non-empty and bounded above by $b$. Let $c_0 = \sup S$. By continuity, $f(c_0) \leq c$. If $f(c_0) < c$, continuity implies $f$ is close to $f(c_0)$ near $c_0$, contradicting $c_0 = \sup S$. Thus $f(c_0) = c$.

### Theorem 107.2 (Connectedness Theorem)
A subset $X$ of a topological space is connected if and only if it cannot be written as the union of two disjoint non-empty open subsets.

**Proof:**
($\Rightarrow$) If $X = U \cup V$ with $U,V$ disjoint open and non-empty, then $U = X \cap U$ and $V = X \cap V$ are disjoint open sets in $X$ covering $X$, so $X$ is disconnected.
($\Leftarrow$) If $X$ is not connected, there exist open sets $U,V \subset X$ with $U \neq \emptyset$, $V \neq \emptyset$, $U \cap V = \emptyset$, $U \cup V = X$. Then $U,X\setminus V$ are disjoint open sets in $X$ covering $X$.

## 107.3: Advanced Topology Theorems

### Theorem 107.3.1 (Alexander Duality)
**Statement:** For a compact, locally contractible subspace A of the n-sphere Sn, there is a natural isomorphism H_i(A) ≅ H^{n-1-i}(Sn \ A).

**Proof:** By excision and properties of reduced homology, combined with the duality between reduced cohomology of the complement and reduced homology of the set.

### Theorem 107.3.2 (Urysohn's Lemma)
**Statement:** For any compact Hausdorff space X and disjoint closed subsets A, B, there exists a continuous function f: X → [0,1] such that f(A) = {0} and f(B) = {1}.

**Proof:** Construct f as a limit of step functions using normality of X.

### Theorem 107.3.3 (Sperner's Lemma)
**Statement:** For any proper labeling of a triangulated (n-1)-simplex with Sperner's conditions, at least one simplex has vertices labeled 1,...,n.

**Proof:** Use the Brouwer fixed-point theorem by considering the function that maps the simplex to itself.

## 107.2 Compactness

### Theorem 107.3 (Heine-Borel Theorem)
A subset $K \subset \mathbb{R}^n$ is compact if and only if it is closed and bounded.

**Proof:**
($\Rightarrow$) Compact sets are closed (limits of sequences are in $K$) and bounded (Heine-Borel characterization of finite subcovers).
($\Leftarrow$) Let $U$ be an open cover. For a bounded set $B$, we can enclose it in a closed cube $C$. By induction on dimension, if each face of $C$ has finite subcover, and $C$ is connected, $C$ itself has a finite subcover.

*Updated on 2026-06-10*
**Theorem 107.3.4** (Stone-Weierstrass Theorem)
Let $X$ be a compact Hausdorff space. The algebra $A$ of continuous real-valued functions on $X$ contains a subalgebra $B$ that separates points and vanishes at no point if and only if $B$ is dense in $C(X)$ with respect to the uniform norm.

**Proof**: This is a generalization of the classical Weierstrass approximation theorem. For compact metric spaces, use density of polynomials and Stone-Cech compactification properties. For general compact Hausdorff spaces, use the Urysohn lemma to separate points and the normality of compact Hausdorff spaces.

**Theorem 107.3.5** (Brouwer Fixed Point Theorem)
Every continuous function $f: D^n \to D^n$ (where $D^n$ is the unit disk in $\mathbb{R}^n$) has a fixed point.

**Proof**: Assume $f$ has no fixed point. Define a retraction $r: D^n \to S^{n-1}$ by $r(x) = f(x)/\|f(x)\|$. This retraction contracts the disk to its boundary, which is impossible by degree theory or homology arguments. For $n=2$, the winding number of the vector field $f(x)-x$ around the boundary must be zero, but the contraction property forces it to be nonzero.

**Theorem 107.3.6** (Schauder Fixed Point Theorem)
Let $K$ be a non-empty, compact, convex subset of a Banach space $X$. Every continuous map $f: K \to K$ has a fixed point.

**Proof**: Use the Kakutani fixed point theorem for upper semi-continuous maps, or directly use the Knaster-Kuratowski-Mazurkiewicz (KKM) lemma for finite-dimensional spaces. For infinite-dimensional spaces, the proof uses the fact that the unit ball in a reflexive Banach space is weakly compact.

**Theorem 107.3.7** (Alexander-Spanier Cohomology Theorems)
The Alexander-Spanier cohomology groups $H^p(X, \mathcal{A}; G)$ of a pair $(X, A)$ can be computed as the derived functors of the section functor, and they are isomorphic to the Čech cohomology groups for nice spaces.

**Proof**: The Alexander-Spanier complex is defined using open covers and star operators. The isomorphism with Čech cohomology follows from the comparison theorem for cohomology theories.

**Theorem 107.3.8** (Gysin Sequence)
For a sphere bundle $S^{n-1} \to E \to B$, there is a long exact sequence:
$$\dots \to H^{k}(B) \xrightarrow{\theta} H^{k}(E) \to H^{k-n+1}(B) \xrightarrow{\theta} H^{k+n-1}(B) \to \dots$$
where $\theta$ is the Gysin map associated to the Euler class.

**Proof**: This is the cohomology long exact sequence for a fibration with fiber $S^{n-1}$. The map $\theta$ is induced by the transgression of the Euler class.

**Theorem 107.3.9** (Hurewicz Theorem)
The first non-vanishing homotopy group of a path-connected space $X$ is isomorphic to the first non-vanishing homology group.

**Proof**: For a path-connected space $X$, the first non-vanishing homotopy group $\pi_k(X)$ is isomorphic to the first non-vanishing homology group $H_k(X)$ (for $k \leq n$ where $n$ is the first non-vanishing group). This is proved by the Hurewicz map being an isomorphism up to the first non-vanishing group.

## 107.4: Advanced Topology (Continued)

**Theorem 107.4.1** (Tietze Extension Theorem)
Let $X$ be a normal topological space and $A$ a closed subset of $X$. Any continuous function $f: A \to \mathbb{R}$ can be extended to a continuous function $F: X \to \mathbb{R}$.

**Proof**: Use Urysohn's lemma to construct the extension. The function can be extended by defining $F(x) = \max\{f(a) - d(x,a) : a \in A\}$, which preserves continuity by the triangle inequality.

**Theorem 107.4.2** (Urysohn's Lemma - Normal Spaces)
A topological space $X$ is normal if and only if for any two disjoint closed sets $A, B \subseteq X$, there exist disjoint open sets $U, V$ such that $A \subseteq U$ and $B \subseteq V$.

**Proof**: ($\Rightarrow$) By definition of normal spaces. ($\Leftarrow$) If for any disjoint closed sets there exist disjoint open neighborhoods, then $X$ is normal by definition.

**Theorem 107.4.3** (Tychonoff's Theorem)
The product of any collection of compact topological spaces is compact in the product topology.

**Proof**: Use the finite intersection property and nets or filters. For nets, a net in the product is a net in each factor; if every finite subcollection has a convergent subnet, the whole net has a convergent subnet in the product.

**Theorem 107.4.4** (Baire Category Theorem)
In a complete metric space, the intersection of countably many dense open sets is dense.

**Proof**: Let $\{U_n\}$ be dense open sets and $X = \bigcap U_n$. Suppose $V$ is a non-empty open set. We construct a sequence of points $x_n$ such that $x_n \in \overline{B(x_{n-1}, 1/n) \cap U_n}$ by the completeness of $X$ and the density of each $U_n$. The sequence $\{x_n\}$ converges to a point $x \in V \cap \bigcap U_n$.

**Theorem 107.4.5** (Urysohn Metrization Theorem)
A regular $T_1$ space is metrizable if and only if it has a countable base.

**Proof**: ($\Rightarrow$) Use Urysohn's lemma to construct a metric from the countable base. ($\Leftarrow$) A second-countable regular space is metrizable by the metrization theorems.

**Theorem 107.4.6** (Alexandrov-Urysohn Theorem)
A regular $T_1$ space with a countable base is metrizable.

**Proof**: Follows from the Urysohn metrization theorem. The regularity and countable base imply metrizability by constructing a metric compatible with the topology.

**Theorem 107.4.7** (Tietze Extension for Compact Spaces)
Let $X$ be a compact Hausdorff space and $A \subseteq X$ a closed subset. Any continuous function $f: A \to \mathbb{R}$ extends to $F: X \to \mathbb{R}$.

**Proof**: Compact Hausdorff spaces are normal, so by the Tietze extension theorem for normal spaces, $f$ extends to $F$.

**Theorem 107.4.8** (Urysohn's Lemma - General Form)
Let $X$ be a normal space and $A, B$ disjoint closed subsets. There exists a continuous function $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**: For each closed set $F$, define $d(x,F) = \inf\{d(x,y) : y \in F\}$ for a metric space. In general normal spaces, construct $f$ using partitions of unity or direct construction from open neighborhoods.

**Theorem 107.4.9** (Stone-Weierstrass Theorem - Algebraic Version)
Let $X$ be a compact Hausdorff space. A subalgebra $A \subseteq C(X)$ contains the constants, separates points, and vanishes at no point if and only if $A$ is dense in $C(X)$ under the uniform norm.

**Proof**: Use the Urysohn lemma to separate points and construct functions approximating any $f \in C(X)$.

**Theorem 107.4.10** (Alexander Compactification)
Let $X$ be a locally compact Hausdorff space. The one-point compactification $X^* = X \cup \{\infty\}$ is compact and Hausdorff.

**Proof**: Define open sets in $X^*$ as either open sets in $X$ or sets containing $\infty$ and having compact complements. This topology is Hausdorff and compact.

*Updated on 2026-08-23*
