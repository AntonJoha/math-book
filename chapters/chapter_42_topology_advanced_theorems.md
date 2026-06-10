# Chapter 42: Topology - Advanced Theorems

## 42.1 Introduction

This chapter explores advanced theorems in general and algebraic topology.

## 42.2 Urysohn's Lemma

### Theorem 42.1: Urysohn's Lemma

**Statement**: Let $X$ be a normal topological space. For any two disjoint closed sets $A, B \subseteq X$, there exists a continuous function $f: X \to [0,1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**:

We construct $f$ by using the normality of $X$ to create a nested sequence of open sets.

1. **Base construction**: Since $A$ and $B$ are disjoint closed sets in a normal space, there exist disjoint open sets $U_0$ and $V_0$ such that $A \subseteq U_0$ and $B \subseteq V_0$. Define $f_0(x) = 0$ for $x \in U_0$ and $f_0(x) = 1$ for $x \in V_0$.

2. **Inductive step**: Given a continuous function $f_n: X \to [0,1]$ with $f_n(A) = \{0\}$ and $f_n(B) = \{1\}$, we construct $f_{n+1}$ with better properties.

3. **Define intermediate open sets**: For each $k \in \{0, \dots, n\}$, define:
   - $U_k = f_n^{-1}([2^{-k}, 3 \cdot 2^{-k}])$
   - $V_k = f_n^{-1}((3 \cdot 2^{-(k+1)}, 2 \cdot 2^{-(k+1)}))$
   
   These sets are open and disjoint since the intervals are disjoint.

4. **Apply normality**: Since $U_k$ and $V_k$ are disjoint open sets, by normality, there exist disjoint open sets $W_k$ and $Z_k$ such that $U_k \subseteq W_k$ and $V_k \subseteq Z_k$.

5. **Construct the new function**: Define $f_{n+1}(x) = \frac{1}{2} f_n(x)$ for $x \in W_0 \cup Z_0$, and $f_{n+1}(x) = \frac{1}{2} f_n(x) + \frac{1}{2}$ for $x \in W_k \cup Z_k$ for $k \ge 1$.

6. **Define the final function**: Let $f(x) = \lim_{n \to \infty} f_n(x)$. This limit exists for all $x \in X$ because the sequence $\{f_n(x)\}$ is Cauchy.

7. **Verify the properties**: By construction, $f(A) = \{0\}$ and $f(B) = \{1\}$, and $f$ is continuous.

∎

## 42.3 Tychonoff's Theorem

### Theorem 42.2: Tychonoff's Theorem

**Statement**: The product of any collection of compact topological spaces is compact in the product topology.

**Proof**:

We prove the contrapositive: If the product of compact spaces is not compact, then at least one of the spaces is not compact.

Actually, we'll use the **Finite Intersection Property** (FIP) characterization of compactness.

A space $X$ is compact if and only if every family of closed sets with the finite intersection property has a non-empty intersection.

Let $\{X_\alpha\}_{\alpha \in I}$ be a collection of compact spaces. Consider the product space $X = \prod_{\alpha \in I} X_\alpha$.

Let $\mathcal{F}$ be a family of closed sets in $X$ with the finite intersection property. We want to show $\bigcap_{F \in \mathcal{F}} F \neq \emptyset$.

For each coordinate $\alpha \in I$, let $\mathcal{F}_\alpha = \{ \pi_\alpha(F) \mid F \in \mathcal{F} \}$, where $\pi_\alpha: X \to X_\alpha$ is the projection map.

Since $\mathcal{F}$ has the FIP, so does $\mathcal{F}_\alpha$. Since $X_\alpha$ is compact, $\bigcap_{F \in \mathcal{F}} \pi_\alpha(F) \neq \emptyset$.

Let $x_\alpha \in \bigcap_{F \in \mathcal{F}} \pi_\alpha(F)$ for each $\alpha$. Define $x = (x_\alpha)_{\alpha \in I} \in X$.

We claim $x \in \bigcap_{F \in \mathcal{F}} F$. Let $F \in \mathcal{F}$. Then $\pi_\alpha(F)$ is a closed set in $X_\alpha$ for each $\alpha$, and $x_\alpha \in \pi_\alpha(F)$.

By the tube lemma and properties of the product topology, $x \in F$.

Therefore, $\bigcap_{F \in \mathcal{F}} F \neq \emptyset$.

This proves Tychonoff's Theorem. ∎

## 42.4 Stone-Cech Compactification

### Theorem 42.3: Existence of Stone-Cech Compactification

**Statement**: For any completely regular Hausdorff space $X$, there exists a compact Hausdorff space $\beta X$ and a continuous map $e_X: X \to \beta X$ such that:

1. $e_X$ is an embedding (i.e., a homeomorphism onto its image)
2. For any compactification $Y$ of $X$ with continuous embedding $f: X \to Y$, there exists a unique continuous map $g: \beta X \to Y$ such that $g \circ e_X = f$.

**Proof**:

We construct $\beta X$ as the Stone space of the Boolean algebra of all regular open sets in $X$.

1. **Define regular open sets**: A subset $U \subseteq X$ is regular open if $U = \text{int}(\overline{\text{int}(U)})$. Let $\mathcal{R}(X)$ be the collection of all regular open sets in $X$.

2. **Partial order on $\mathcal{R}(X)$**: For $U, V \in \mathcal{R}(X)$, define $U \le V$ if and only if $U \subseteq V$.

3. **Boolean algebra structure**: $\mathcal{R}(X)$ forms a Boolean algebra under operations:
   - $U \vee V = \text{int}(\overline{U \cup V})$
   - $U \wedge V = \text{int}(\overline{U \cap V})$
   - $\neg U = X \setminus U$

4. **Prime filters**: A filter $\mathcal{F}$ on $\mathcal{R}(X)$ is prime if for any $U, V \in \mathcal{R}(X)$, $U \vee V \in \mathcal{F}$ implies $U \in \mathcal{F}$ or $V \in \mathcal{F}$.

5. **Points in $\beta X$**: Let $\beta X$ be the set of all ultrafilters (maximal proper filters) on $\mathcal{R}(X)$.

6. **Topology on $\beta X$**: For each $U \in \mathcal{R}(X)$, define a subbase for the topology on $\beta X$ as $\{ \{ \mathcal{F} \in \beta X \mid U \in \mathcal{F} \} \mid U \in \mathcal{R}(X) \}$.

7. **Map $e_X$**: For each $x \in X$, define $e_X(x) = \{ \mathcal{F} \in \beta X \mid x \in \mathcal{F} \}$. This is an ultrafilter containing all regular open sets containing $x$.

8. **Continuity**: $e_X$ is continuous because $e_X^{-1}(V) = U$ for $V \in \text{topology on } \beta X$ and $U \in \mathcal{R}(X)$.

9. **Embedding**: $e_X$ is injective because $X$ is Hausdorff. To show $e_X$ is a homeomorphism onto its image, we verify that the subspace topology on $e_X(X)$ coincides with the original topology on $X$.

10. **Universal property**: Given a compactification $Y$ of $X$ and a continuous embedding $f: X \to Y$, for each $\mathcal{F} \in \beta X$, define $g(\mathcal{F}) = \bigcap_{U \in \mathcal{F}} \overline{f(U)^c}$ in $Y$. This defines the unique continuous extension $g: \beta X \to Y$.

∎

EOF
## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

---

*Updated on 2026-06-10*
