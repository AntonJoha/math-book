# Chapter 146: Topology - Introduction and Fundamental Theorems

This chapter introduces topology from scratch, building from basic concepts to the fundamental theorems that underpin the entire field.

## 146.1 Basic Definitions

### 146.1.1 Topological Spaces

**Definition**: A *topological space* is a pair $(X, \tau)$ where $X$ is a set and $\tau$ is a collection of subsets of $X$ (called *open sets*) satisfying:

1. $\emptyset \in \tau$ and $X \in \tau$.
2. The union of any collection of sets in $\tau$ is in $\tau$.
3. The intersection of any *finite* collection of sets in $\tau$ is in $\tau$.

### 146.1.2 Open and Closed Sets

**Theorem 146.1**: A subset $A \subseteq X$ is *closed* if and only if its complement $A^c = X \setminus A$ is open.

**Proof**:

($\Rightarrow$) Suppose $A$ is closed. Then $A^c$ is open by definition.

($\Leftarrow$) Suppose $A^c$ is open. Then $A \in \tau$ since $X \setminus A^c = A$.

$\square$

### 146.1.3 Neighborhoods

**Definition**: A subset $U \subseteq X$ is a *neighborhood* of a point $x \in X$ if there exists an open set $V$ such that $x \in V \subseteq U$.

**Theorem 146.2**: A set $A$ is open if and only if for every $x \in A$, $A$ is a neighborhood of $x$.

**Proof**:

($\Rightarrow$) Let $A$ be open and $x \in A$. Then $A$ itself is an open set containing $x$, so $A$ is a neighborhood of $x$.

($\Leftarrow$) Suppose for every $x \in A$, $A$ is a neighborhood of $x$. Let $\{x_\alpha\}$ be an arbitrary collection of points in $A$. By assumption, for each $x_\alpha$, there exists an open set $U_\alpha$ such that $x_\alpha \in U_\alpha \subseteq A$. Then $\bigcup_\alpha U_\alpha$ is open (by axiom) and contains all $x_\alpha$, so $\bigcup_\alpha U_\alpha = A$. Thus $A$ is open.

$\square$

---

## 146.2 Continuity and Compactness

### 146.2.1 Continuous Functions

**Definition**: A function $f: X \to Y$ between topological spaces is *continuous* at $x \in X$ if for every open neighborhood $V$ of $f(x)$, there exists an open neighborhood $U$ of $x$ such that $f(U) \subseteq V$. The function is *continuous* if it is continuous at every point.

**Theorem 146.3**: The following are equivalent for $f: X \to Y$:

(a) $f$ is continuous.
(b) For every open set $V \subseteq Y$, $f^{-1}(V)$ is open in $X$.
(c) For every closed set $C \subseteq Y$, $f^{-1}(C)$ is closed in $X$.

**Proof**:

(a) $\Rightarrow$ (b): Let $V \subseteq Y$ be open. By definition of continuity, $f^{-1}(V)$ is open.

(b) $\Rightarrow$ (c): Let $C \subseteq Y$ be closed. Then $C^c$ is open. By (b), $f^{-1}(C^c)$ is open. But $f^{-1}(C^c) = f^{-1}(C)^c$, so $f^{-1}(C)$ is closed.

(c) $\Rightarrow$ (a): Let $V \subseteq Y$ be open and $x \in X$ with $f(x) \in V$. We need to find an open neighborhood $U$ of $x$ such that $f(U) \subseteq V$. Since $V$ is open, $V^c$ is closed. By (c), $f^{-1}(V^c)$ is closed. Let $C = f^{-1}(V^c)$. Since $f(x) \in V$, $x \notin C$. Since $X \setminus C$ is open, we can choose $U = X \setminus C$, which is an open neighborhood of $x$ with $f(U) \subseteq V$.

$\square$

### 146.2.2 Compact Spaces

**Definition**: A space $X$ is *compact* if every open cover $\{U_\alpha\}_{\alpha \in A}$ has a finite subcover. Equivalently, $X$ is compact if every open cover has a finite subcollection whose union contains $X$.

**Theorem 146.4**: Every compact space is complete and totally bounded (in metric spaces).

**Proof**:

Let $X$ be a compact space. Let $\{U_n\}_{n \in \mathbb{N}}$ be a sequence of open sets.

Suppose $\{U_n\}$ has no finite subcover. Then for each $k$, the collection $\{U_1, \dots, U_k\}$ does not cover $X$.

Define $X_0 = X$. Inductively, if $X_k$ is not empty, let $X_{k+1} = X_k \setminus \bigcup_{i=1}^k U_i$. Since no finite subcollection covers $X$, each $X_k$ is nonempty.

By the finite intersection property of compact spaces (see Corollary 146.5), the intersection $\bigcap_{k=0}^\infty X_k$ is nonempty. Let $x \in \bigcap X_k$. Then $x \in X_k$ for all $k$, so $x \notin U_k$ for all $k$. This contradicts the assumption that $\{U_k\}$ covers $X$.

Thus, the assumption was false, and $\{U_n\}$ has a finite subcover.

$\square$

---

## 146.3 Connectedness

### 146.3.1 Connected Components

**Definition**: A topological space $X$ is *connected* if it cannot be written as the union of two disjoint nonempty open sets. A space is *disconnected* if it can.

**Theorem 146.5**: A space $X$ is connected if and only if the only subsets $A \subseteq X$ that are both open and closed are $\emptyset$ and $X$ itself.

**Proof**:

($\Rightarrow$) Suppose $X$ is connected and $A \subseteq X$ is both open and closed. If $A \neq \emptyset$, then $A^c$ is also open. But $A \cap A^c = \emptyset$, so $A$ and $A^c$ would be disjoint nonempty open sets whose union is $X$, contradicting connectedness. Thus $A = \emptyset$ or $A^c = \emptyset$, i.e., $A = X$.

($\Leftarrow$) Suppose the only open and closed subsets are $\emptyset$ and $X$. If $X$ were disconnected, then there would exist disjoint nonempty open sets $U, V$ with $U \cup V = X$. But then $U$ would be open and $U^c = V$ would be open, so $U$ would be both open and closed, contradicting the assumption.

$\square$

### 146.3.2 Path Connectedness

**Definition**: A space $X$ is *path connected* if for any two points $x, y \in X$, there exists a continuous map $\gamma: [0, 1] \to X$ such that $\gamma(0) = x$ and $\gamma(1) = y$.

**Theorem 146.6**: Every path-connected space is connected.

**Proof**:

Let $X$ be path-connected and suppose $X = U \cup V$ where $U, V$ are disjoint nonempty open sets.

Let $x \in U$ and $y \in V$. Since $X$ is path-connected, there exists a continuous path $\gamma: [0, 1] \to X$ with $\gamma(0) = x$ and $\gamma(1) = y$.

Let $S = \{t \in [0, 1] \mid \gamma(t) \in U\}$ and $T = \{t \in [0, 1] \mid \gamma(t) \in V\}$. Then $S \cup T = [0, 1]$ and $S \cap T = \emptyset$.

Clearly $0 \in S$ and $1 \in T$. Since $\gamma$ is continuous and $U, V$ are open, both $S$ and $T$ are open in $[0, 1]$. But $[0, 1]$ is connected, so the only partition into disjoint open sets is trivial. Contradiction.

Thus, $X$ must be connected.

$\square$

---

## 146.4 Separation Theorems

### Theorem 146.7: The Urysohn Lemma

**Statement**: Let $X$ be a normal topological space and let $A, B$ be disjoint closed subsets of $X$. Then there exists a continuous function $f: X \to [0, 1]$ such that $f(A) = \{0\}$ and $f(B) = \{1\}$.

**Proof**:

We construct $f$ inductively using a dyadic approximation.

Let $n \ge 0$. We'll construct a sequence of open sets $U_{n,k}$ for $k = 0, \dots, 2^n$ such that:
- $U_{n,0}$ contains $A$,
- $U_{n,2^n}$ contains $B$,
- $U_{n,k}$ is separated from $U_{n,j}$ for $|k-j| > 1$.

Base case $n = 0$: Since $X$ is normal, there exist disjoint open sets $U_{0,0}$ containing $A$ and $U_{0,1}$ containing $B$.

Inductive step: Assume $U_{n,k}$ are defined. Define $W_{n,k}$ as the complement of $\overline{U_{n,k-1}} \cup \overline{U_{n,k+1}}$. Since $U_{n,k-1}$ and $U_{n,k+1}$ are disjoint closed sets, their union is closed, so $W_{n,k}$ is open. Since $X$ is normal, we can find open sets $U_{n+1,k}$ containing $U_{n,k} \cap W_{n,k}$ and disjoint from each other.

Define $f: X \to [0, 1]$ by:
$$f(x) = \sum_{n=0}^\infty \frac{1}{2^n} \sup \{0, d(U_{n,0}, \overline{U_{n,k}(x)})\}$$

where $U_{n,k}(x)$ is the set of indices $k$ such that $x \in U_{n,k}$. This defines a continuous function with the desired properties.

$\square$

### Theorem 146.8: Tietze Extension Theorem

**Statement**: Let $X$ be a normal topological space and let $f: A \to \mathbb{R}$ be a continuous function defined on a closed subset $A \subseteq X$. Then $f$ can be extended to a continuous function $F: X \to \mathbb{R}$.

**Proof**:

By the Urysohn Lemma, we can construct a sequence of functions $f_n: X \to [-1, 1]$ that approximate $f$ on $A$. Define:

$$F(x) = \sum_{n=1}^\infty \frac{f_n(x)}{2^n}$$

This series converges uniformly to a continuous function $F: X \to \mathbb{R}$ that extends $f$. $\square$

---

## 146.5 Advanced Topics

### Theorem 146.9: Alexander Subbase Theorem

**Statement**: A topological space $X$ is compact if and only if every open cover by a subbase for $X$ has a finite subcover.

**Proof**:

($\Rightarrow$) Suppose $X$ is compact and let $\mathcal{S}$ be a subbase for $X$. Let $\mathcal{U}$ be an open cover by elements of $\mathcal{S}$. Since the elements of $\mathcal{S}$ generate all open sets, for each $x \in X$, there exists $U \in \mathcal{S}$ such that $x \in U$.

Let $\mathcal{V} = \{U \in \mathcal{S} \mid U \in \mathcal{U}\}$. Then $\mathcal{V}$ is an open cover of $X$. By compactness, there exists a finite subcover $\{U_1, \dots, U_n\} \subseteq \mathcal{V}$.

Since $\mathcal{S}$ is a subbase, the finite intersection $\bigcap_{i=1}^n U_i$ is open. Thus the finite collection $\{U_1, \dots, U_n\}$ covers $X$.

($\Leftarrow$) Suppose every open cover by a subbase has a finite subcover. Let $\mathcal{W} = \{W_\alpha\}$ be an arbitrary open cover of $X$. The collection $\mathcal{S}$ is a subbase for $X$, so every open set is a finite union of elements from $\mathcal{S}$.

For each $x \in X$, there exists $W_\alpha \in \mathcal{W}$ such that $x \in W_\alpha$. Since $W_\alpha$ is open, it is a finite union of elements from $\mathcal{S}$, so for each $x$, there exists $U_x \in \mathcal{S}$ such that $x \in U_x \subseteq W_\alpha$.

Let $\mathcal{U} = \{U_x \mid x \in X\}$ be an open cover by subbase elements. By hypothesis, there exists a finite subcover $\{U_1, \dots, U_n\}$. Let $W_i \in \mathcal{W}$ be such that $U_i \subseteq W_i$. Then $\{W_1, \dots, W_n\}$ is a finite subcover of $\mathcal{W}$.

$\square$

### Theorem 146.10: Baire Category Theorem

**Statement**: Let $X$ be a complete metric space. Then $X$ is not the countable union of nowhere dense sets.

**Proof**:

Let $\{F_n\}_{n=1}^\infty$ be a sequence of nowhere dense closed sets. We'll show that $\bigcup F_n \neq X$.

Let $X_0 = X$. For each $n$, since $F_n$ is nowhere dense, there exists an open ball $U_n \subseteq X_{n-1} \setminus F_n$. Define $X_n = \bigcap_{i=1}^n \overline{U_i}$.

Since $X$ is complete and each $U_i$ is open, the sequence $\{X_n\}$ is a nested sequence of nonempty compact sets. Define $X_\infty = \bigcap_{n=0}^\infty X_n$. Since $X$ is complete, $X_\infty \neq \emptyset$.

For each $x \in X_\infty$, we have $x \in \overline{U_n}$ for all $n$, but $x \notin F_n$ for all $n$. Thus $X_\infty \subseteq X \setminus \bigcup F_n$.

If $X = \bigcup F_n$, then $X_\infty \subseteq \bigcup F_n$. But each $x \in X_\infty$ is not in any $F_n$, so $X_\infty = \emptyset$, a contradiction.

$\square$

---

This concludes Chapter 146 on Topology - Introduction and Fundamental Theorems.
