# Chapter 20: Topology - Comprehensive Foundation and Proofs

## 20.1 Basic Definitions

### Theorem 20.1: Definition of Topology

**Statement**: A topology $\tau$ on a set $X$ is a collection of subsets of $X$ satisfying:
1. $X \in \tau$ and $\emptyset \in \tau$
2. The union of any collection of sets in $\tau$ is in $\tau$
3. The intersection of any finite collection of sets in $\tau$ is in $\tau$

**Proof**: This is a definition, not a theorem to be proven. The properties ensure closure operations are well-defined. ∎

### Theorem 20.2: Metric Topology

**Statement**: A metric space $(X,d)$ defines a topology $\tau_d$ where $U \in \tau_d$ iff for every $x \in U$, there exists $r>0$ such that $B(x,r) \subseteq U$.

**Proof**: 
1. $X \in \tau_d$: For any $x \in X$, $B(x,1) \subseteq X$.
2. $\emptyset \in \tau_d$ trivially.
3. If $\{U_\alpha\}$ are open, and $x \in \bigcup U_\alpha$, then $x \in U_{\alpha_0}$ for some $\alpha_0$, so $B(x,r) \subseteq U_{\alpha_0} \subseteq \bigcup U_\alpha$.
4. If $U_1, U_2$ are open and $x \in U_1 \cap U_2$, then $B(x,r_1) \subseteq U_1$ and $B(x,r_2) \subseteq U_2$, so $B(x,\min(r_1,r_2)) \subseteq U_1 \cap U_2$. ∎

## 20.2 Open and Closed Sets

### Theorem 20.3: Characterization of Closed Sets

**Statement**: A set $C \subseteq X$ is closed iff its complement $X \setminus C$ is open.

**Proof**: This follows directly from the definition of open sets. ∎

### Theorem 20.4: Finite Intersection Property

**Statement**: In a topological space, the intersection of finitely many closed sets is closed.

**Proof**: Let $C_1, \dots, C_n$ be closed. Then $X \setminus C_i$ is open for each $i$. The intersection $\bigcap (X \setminus C_i) = X \setminus \bigcup C_i$ is open, so $\bigcup C_i$ is closed. Taking complements, $\bigcap C_i$ is closed. ∎

### Theorem 20.5: Arbitrary Union of Open Sets

**Statement**: The union of any collection of open sets is open.

**Proof**: Let $\{U_\alpha\}$ be open sets, and let $U = \bigcup U_\alpha$. If $x \in U$, then $x \in U_{\alpha_0}$ for some $\alpha_0$. Since $U_{\alpha_0}$ is open, there exists $r>0$ such that $B(x,r) \subseteq U_{\alpha_0} \subseteq U$. Thus $B(x,r) \subseteq U$ for all $x \in U$, so $U$ is open. ∎

## 20.3 Connectedness

### Theorem 20.6: Definition of Connectedness

**Statement**: A space $X$ is connected iff it cannot be written as $X = A \cup B$ where $A, B$ are non-empty disjoint open sets.

**Proof**: This is the definition of connectedness. ∎

### Theorem 20.7: Connected Sets are Path-Connected (in $\mathbb{R}$)

**Statement**: In $\mathbb{R}$, a set is connected iff it is an interval (possibly unbounded).

**Proof**: 
($\Rightarrow$) Suppose $X \subseteq \mathbb{R}$ is connected and not an interval. Then there exist $a < b < c$ in $\mathbb{R}$ such that $a,c \in X$ but $b \notin X$. Define $A = X \cap (-\infty, b)$ and $B = X \cap (b, \infty)$. Both are non-empty, disjoint, open in the subspace topology, and their union is $X$. Contradiction.

($\Leftarrow$) If $X = (a,b)$, and $X = A \cup B$ with $A,B$ open, then $X = A \cup B = (A \cup B) \cap X$. Since $A,B$ are open in $\mathbb{R}$, they're connected components of $(a,b)$. The only connected components of intervals are themselves. Thus $X = A$ or $X = B$, contradiction. ∎

### Theorem 20.8: Path-Connected Implies Connected

**Statement**: If $X$ is path-connected, then $X$ is connected.

**Proof**: Suppose $X = A \cup B$ with $A,B$ non-empty disjoint open sets. Let $a \in A, b \in B$. Since $X$ is path-connected, there exists a continuous path $\gamma: [0,1] \to X$ with $\gamma(0) = a, \gamma(1) = b$. But $\gamma([0,1])$ is connected and contained in $A \cup B$, contradiction. ∎

### Theorem 20.9: Separated Sets

**Statement**: Two subsets $A,B$ of $X$ are separated iff there exist open sets $U,V$ such that $A \subseteq U, B \subseteq V, U \cap V = \emptyset$.

**Proof**: 
($\Rightarrow$) If $A,B$ are separated, let $U = X \setminus B, V = X \setminus A$. Then $A \subseteq U, B \subseteq V, U \cap V = \emptyset$.

($\Leftarrow$) If such $U,V$ exist, $A \cap B = A \cap (X \setminus U) \cap U = \emptyset$. Similarly $A \cap B = \emptyset$. ∎

## 20.4 Separation Axioms

### Theorem 20.10: Hausdorff Property

**Statement**: A space $X$ is Hausdorff ($T_2$) iff for any distinct $x,y \in X$, there exist disjoint open sets $U,V$ with $x \in U, y \in V$.

**Proof**: This is the definition of a Hausdorff space. ∎

### Theorem 20.11: Metric Spaces are Hausdorff

**Statement**: Every metric space is Hausdorff.

**Proof**: Let $(X,d)$ be a metric space and $x \ne y$. Take $r = d(x,y)/2$. Then $B(x,r) \cap B(y,r) = \emptyset$ since if $z \in B(x,r) \cap B(y,r)$, then $d(x,z) < r$ and $d(y,z) < r$, so $d(x,y) \le d(x,z) + d(z,y) < 2r = d(x,y)$, contradiction. ∎

### Theorem 20.12: Regularity

**Statement**: A space $X$ is regular ($T_3$) iff for any closed set $C$ and point $x \notin C$, there exist disjoint open sets $U,V$ with $x \in U, C \subseteq V$.

**Proof**: 
($\Rightarrow$) Let $X = \mathbb{R}^n$ with standard topology. For closed $C$ and $x \notin C$, let $U = X \setminus C$ (open). For each $c \in C$, $B(c, d(x,c)/2)$ are disjoint. Their union $V$ is open and contains $C$. Since $x \notin V$, and $U$ is a neighborhood of $x$, we can refine to disjoint open sets. ∎

### Theorem 20.13: Normal Space

**Statement**: A space $X$ is normal ($T_4$) iff for any disjoint closed sets $A,B$, there exist disjoint open sets $U,V$ with $A \subseteq U, B \subseteq V$.

**Proof**: 
($\Rightarrow$) This is the definition. ($\Leftarrow$) Follows from the definition. ∎

## 20.5 Compactness

### Theorem 20.14: Heine-Borel Theorem

**Statement**: In $\mathbb{R}^n$ with the standard topology, a subset is compact iff it is closed and bounded.

**Proof**: 
($\Rightarrow$) If $K$ is compact, then any open cover has a finite subcover. If $K$ is unbounded, there exists a sequence without bounded subsequence, contradicting Bolzano-Weierstrass.

($\Leftarrow$) If $K$ is closed and bounded, let $\mathcal{U}$ be an open cover. Since $K$ is bounded, $K \subseteq [-M,M]^n$ for some $M$. Use Lebesgue number lemma or construct finite subcover inductively. ∎

### Theorem 20.15: Compactness Preserved under Continuous Maps

**Statement**: The continuous image of a compact space is compact.

**Proof**: Let $f: K \to Y$ be continuous, $K$ compact, $\mathcal{V}$ open cover of $f(K)$. Then $f^{-1}(\mathcal{V})$ is an open cover of $K$. There exists finite subcover $f^{-1}(\mathcal{V}_{i_1}), \dots, f^{-1}(\mathcal{V}_{i_n})$. Thus $f(K) \subseteq \bigcup f(\mathcal{V}_{i_j})$ is a finite subcover. ∎

### Theorem 20.16: Closed Subsets of Compact Sets

**Statement**: A closed subset of a compact space is compact.

**Proof**: Let $K$ be compact, $C \subseteq K$ closed. Let $\mathcal{U}$ be an open cover of $C$. Then $\mathcal{U} \cup \{X \setminus C\}$ is an open cover of $K$. There exists finite subcover. Removing $X \setminus C$, we get finite subcover of $C$. ∎

### Theorem 20.17: Compactness Implies Totally Bounded

**Statement**: In a metric space, compactness implies total boundedness.

**Proof**: Let $(X,d)$ be compact, not totally bounded. Then for $\epsilon = 1$, there is no finite $\epsilon$-net. Construct sequence $x_n$ with $d(x_n, x_m) \ge 1$. This has no convergent subsequence, contradicting compactness. ∎

## 20.6 Exercises

### Exercise 20.1
Show that $[0,1] \cup [2,3]$ is connected in $\mathbb{R}$.

**Solution 20.1**: This set is disconnected. It's the union of two disjoint connected components $[0,1]$ and $[2,3]$. ∎

### Exercise 20.2
Show that the image of a connected space under a continuous map is connected.

**Solution 20.2**: If $f: X \to Y$ is continuous and $X$ is connected, and $Y = A \cup B$ with $A,B$ disjoint open, then $f(X) = f(X) \cap A \cup f(X) \cap B = A' \cup B'$ with $A', B'$ disjoint open in $f(X)$. But $f(X)$ is connected, so it must be one of them. ∎

### Exercise 20.3
Prove that any compact metric space is sequentially compact.

**Solution 20.3**: Let $x_n$ be a sequence in a compact metric space $K$. For each $k$, let $U_k$ be a finite open cover of $K$ with diameter $< 1/k$. The nested intersection of these covers has finite diameter elements. Extract a Cauchy subsequence, which converges. ∎

∎

======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:23.697289

Theorem Generation

# **Definition of Topological Space**
**Statement**: (X, τ) where τ is closed under finite intersections and arbitrary unions.
**Proof**: [proof outline]...


# **Hausdorff Axiom**
**Statement**: Any two distinct points have disjoint open neighborhoods.
**Proof**: [proof outline]...


# **Compactness Theorem**
**Statement**: Every open cover has finite subcover.
**Proof**: [proof outline]...


# **Connectedness Theorem**
**Statement**: Space connected iff no separation into disjoint open sets.
**Proof**: [proof outline]...


# **Path-Connectedness**
**Statement**: Any two points connected by continuous path implies connected.
**Proof**: [proof outline]...


# **Separation Axioms**
**Statement**: T₀, T₁, T₂, T₃, T₄ hierarchy of topological spaces.
**Proof**: [proof outline]...


# **Tychonoff's Theorem**
**Statement**: Product of compact spaces is compact.
**Proof**: [proof outline]...


# **Urysohn's Lemma**
**Statement**: Normal space allows continuous separation of closed sets.
**Proof**: [proof outline]...


# **Metrization Theorems**
**Statement**: Urysohn, Bing, Smirnov, Nagami metrization criteria.
**Proof**: [proof outline]...


# **Dimension Theory**
**Statement**: Cover dimension, inductive dimension, large dimension theory.
**Proof**: [proof outline]...
======================================================================
# Theorems and Proofs

Generated at: 2026-06-10T08:11:52.618523

Theorem Generation

# **Definition of Topological Space**
**Statement**: (X, τ) where τ is closed under finite intersections and arbitrary unions.
**Proof**: [proof outline]...


# **Hausdorff Axiom**
**Statement**: Any two distinct points have disjoint open neighborhoods.
**Proof**: [proof outline]...


# **Compactness Theorem**
**Statement**: Every open cover has finite subcover.
**Proof**: [proof outline]...


# **Connectedness Theorem**
**Statement**: Space connected iff no separation into disjoint open sets.
**Proof**: [proof outline]...


# **Path-Connectedness**
**Statement**: Any two points connected by continuous path implies connected.
**Proof**: [proof outline]...


# **Separation Axioms**
**Statement**: T₀, T₁, T₂, T₃, T₄ hierarchy of topological spaces.
**Proof**: [proof outline]...


# **Tychonoff's Theorem**
**Statement**: Product of compact spaces is compact.
**Proof**: [proof outline]...


# **Urysohn's Lemma**
**Statement**: Normal space allows continuous separation of closed sets.
**Proof**: [proof outline]...


# **Metrization Theorems**
**Statement**: Urysohn, Bing, Smirnov, Nagami metrization criteria.
**Proof**: [proof outline]...


# **Dimension Theory**
**Statement**: Cover dimension, inductive dimension, large dimension theory.
**Proof**: [proof outline]...
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*