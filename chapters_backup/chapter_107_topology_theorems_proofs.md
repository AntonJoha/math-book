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