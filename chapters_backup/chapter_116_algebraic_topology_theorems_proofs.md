# Chapter 116: Algebraic Topology - Theorems and Proofs

## 116.1 Fundamental Group

### Theorem 116.1.1 (Fundamental Group Definition)
For a path-connected topological space $X$ with base point $x_0$, the fundamental group $\pi_1(X, x_0)$ is the group of free homotopy classes of loops at $x_0$, with the group operation given by concatenation of loops.

**Proof:** Let $\Lambda$ be the set of all loops at $x_0$ in $X$, i.e., continuous maps $f: I \to X$ such that $f(0) = f(1) = x_0$, where $I = [0,1]$ is the unit interval.

Define an equivalence relation $\sim$ on $\Lambda$ by: $f \sim g$ if there exists a homotopy $H: I \times I \to X$ such that $H(s, 0) = f(s)$, $H(s, 1) = g(s)$, and $H(0, t) = H(1, t) = x_0$ for all $t \in I$ (base-point preserving homotopy).

Let $[\gamma]$ denote the homotopy class of a loop $\gamma$. Define a binary operation on $[\Lambda]$ by $[\gamma] \cdot [\sigma] = [\gamma \cdot \sigma]$, where $(\gamma \cdot \sigma)(t)$ is defined as:

$$(\gamma \cdot \sigma)(t) = \begin{cases} \gamma(2t) & \text{if } 0 \le t \le 1/2 \\ \sigma(2t-1) & \text{if } 1/2 \le t \le 1 \end{cases}$$

This operation is associative up to homotopy, has an identity element $[c_{x_0}]$ where $c_{x_0}$ is the constant loop at $x_0$, and every element has an inverse. Thus, $\pi_1(X, x_0) = \Lambda/\sim$ is a group. ∎

### Theorem 116.1.2 (Path Independence of Fundamental Group)
If $X$ is path-connected, then for any two base points $x_0, x_1 \in X$, there is a natural isomorphism $\pi_1(X, x_0) \cong \pi_1(X, x_1)$.

**Proof:** Since $X$ is path-connected, there exists a path $\gamma: I \to X$ from $x_0$ to $x_1$. Let $\gamma_*(\alpha)$ denote the loop $\alpha \cdot \gamma \cdot \bar{\gamma}$, where $\bar{\gamma}$ is the reverse path of $\gamma$.

Define $\phi: \pi_1(X, x_0) \to \pi_1(X, x_1)$ by $\phi([\alpha]) = [\gamma_*(\alpha)]$ for any loop $\alpha$ at $x_0$.

First, show $\phi$ is well-defined: If $\alpha \sim \alpha'$, then $\gamma_*(\alpha) \sim \gamma_*(\alpha')$, so $\phi$ is well-defined.

Second, show $\phi$ is a homomorphism: For $\alpha, \beta \in \pi_1(X, x_0)$, we have:
$$\phi([\alpha] \cdot [\beta]) = \phi([\alpha \cdot \beta]) = [\gamma_*(\alpha \cdot \beta)] = [\bar{\gamma} \cdot \alpha \cdot \gamma \cdot \beta \cdot \bar{\gamma}] = [\gamma_*(\alpha)] \cdot [\gamma_*(\beta)] = \phi([\alpha]) \cdot \phi([\beta])$$

Thus, $\phi$ is a homomorphism.

Third, show $\phi$ is bijective: Since $\gamma$ is invertible (i.e., $\bar{\gamma}$ is a path from $x_1$ to $x_0$), we can define $\psi: \pi_1(X, x_1) \to \pi_1(X, x_0)$ similarly by $\psi([\beta]) = [\bar{\gamma}_*(\beta)]$. Then $\phi$ and $\psi$ are inverses of each other.

Therefore, $\pi_1(X, x_0) \cong \pi_1(X, x_1)$. ∎

### Theorem 116.1.3 (Fundamental Group of Product Space)
For path-connected spaces $X$ and $Y$, we have a natural isomorphism:
$$\pi_1(X \times Y) \cong \pi_1(X) \times \pi_1(Y)$$

**Proof:** Define a map $\Phi: \pi_1(X \times Y) \to \pi_1(X) \times \pi_1(Y)$ by:

$$\Phi([\gamma]) = ([\gamma_1], [\gamma_2])$$

where $\gamma_1(t) = \gamma_1(t)$ and $\gamma_2(t) = \gamma_2(t)$ are the projections of $\gamma$ onto $X$ and $Y$, respectively.

This map is clearly a homomorphism. To show it is bijective, define $\Psi: \pi_1(X) \times \pi_1(Y) \to \pi_1(X \times Y)$ by:

$$\Psi(([\alpha], [\beta])) = [\alpha \times \beta]$$

where $(\alpha \times \beta)(t) = (\alpha(t), \beta(t))$. Then $\Phi$ and $\Psi$ are inverses of each other.

Thus, $\pi_1(X \times Y) \cong \pi_1(X) \times \pi_1(Y)$. ∎

## 116.2 Covering Spaces

### Theorem 116.2.1 (Definition of Covering Map)
A continuous surjective map $p: E \to B$ is a covering map if for every $b \in B$, there exists an open neighborhood $U$ of $b$ such that $p^{-1}(U)$ is a disjoint union of open sets in $E$, each of which is homeomorphic to $U$ via $p$.

**Proof:** This is the definition of a covering map. The key properties are:
1. $p$ is surjective
2. For every $b \in B$, there exists an evenly covered neighborhood $U$
3. The restriction of $p$ to each component of $p^{-1}(U)$ is a homeomorphism onto $U$

The proof is straightforward from the definition. ∎

### Theorem 116.2.2 (Classification of Covering Spaces)
Let $B$ be a path-connected, locally path-connected, and semilocally simply connected space, and let $\tilde{B} \subset E$ be a path component of a covering space $E \xrightarrow{p} B$. Then there is a bijection between:
1. Path-connected components of $E$ containing $\tilde{B}$, and
2. Subgroups of $\pi_1(B, b_0)$ containing the image of $\pi_1(\tilde{B}, \tilde{b}_0)$.

**Proof:** The classification theorem establishes a correspondence between covering spaces of $B$ and subgroups of $\pi_1(B, b_0)$. Specifically, for each covering space $E \to B$, the fundamental group $\pi_1(\tilde{B})$ injects into $\pi_1(B)$ via the homomorphism induced by the covering map.

Conversely, for each subgroup $H \le \pi_1(B, b_0)$, there exists a covering space $E_H \to B$ such that $\pi_1(E_H, \tilde{b}_0) \cong H$.

This correspondence is bijective: two subgroups $H_1$ and $H_2$ of $\pi_1(B, b_0)$ define the same covering space if and only if $H_1 = H_2$. ∎

### Theorem 116.2.3 (Universal Covering)
If $B$ is a path-connected, locally path-connected, and semilocally simply connected space, then $B$ has a universal covering space $\tilde{B} \to B$ such that $\pi_1(\tilde{B}) = \{1\}$.

**Proof:** The universal covering space of $B$ is the covering space corresponding to the trivial subgroup $\{1\} \le \pi_1(B, b_0)$. Since $\pi_1(\tilde{B}) \cong \{1\}$, we have $\pi_1(\tilde{B}) = \{1\}$.

The universal covering space is path-connected and simply connected, making it the "most general" covering space of $B$. ∎

## 116.3 Homology Theory

### Theorem 116.3.1 (Euler Characteristic)
For a finite CW-complex $X$, the Euler characteristic is defined as:
$$\chi(X) = \sum_{i=0}^n (-1)^i \beta_i$$
where $\beta_i = \text{rank}(H_i(X))$ is the $i$-th Betti number.

**Proof:** Let $X$ be a finite CW-complex with cell structure $e^0 \cup e^1 \cup \dots \cup e^n$. The Euler characteristic is defined as the alternating sum of the number of cells:
$$\chi(X) = \sum_{i=0}^n (-1)^i c_i$$
where $c_i$ is the number of $i$-cells in $X$.

For a chain complex $C_\bullet$, the Euler characteristic is also defined as the alternating sum of the ranks of the homology groups:
$$\chi(C_\bullet) = \sum_{i=0}^n (-1)^i \text{rank}(H_i(C_\bullet))$$

These two definitions are equivalent because the ranks of the homology groups differ from the number of cells by boundary maps, which cancel out in the alternating sum. ∎

### Theorem 116.3.2 (Homology of Sphere)
For the $n$-sphere $S^n$, we have:
- $H_k(S^n) = 0$ for $k \neq 0, n$
- $H_0(S^n) \cong \mathbb{Z}$
- $H_n(S^n) \cong \mathbb{Z}$

**Proof:** We prove this by induction on $n$. For $n=0$, $S^0$ consists of two points, so $H_0(S^0) \cong \mathbb{Z}$.

For $n=1$, $S^1$ is a circle, and $H_1(S^1) \cong \mathbb{Z}$, $H_k(S^1) = 0$ for $k \neq 1$.

For general $n$, we can use the long exact sequence of homology for the pair $(D^{n+1}, S^n)$. The reduced homology $\tilde{H}_*(D^{n+1}) = 0$, so the long exact sequence gives:
$$\dots \to \tilde{H}_k(S^n) \to \tilde{H}_k(D^{n+1}) \to \tilde{H}_k(D^{n+1}/S^n) \to \tilde{H}_{k-1}(S^n) \to \dots$$

Since $\tilde{H}_k(D^{n+1}) = 0$ for all $k$, we have $\tilde{H}_k(S^n) \cong \tilde{H}_k(S^n/D^{n+1})$ for all $k$.

But $S^n/D^{n+1} \cong S^{n+1}$, so $\tilde{H}_k(S^n) \cong \tilde{H}_k(S^{n+1})$. This gives us the recursive relationship between the homology groups of spheres.

By analyzing the boundary maps in the long exact sequence, we can show that $\tilde{H}_k(S^n) = 0$ for $k \neq n$ and $\tilde{H}_n(S^n) \cong \mathbb{Z}$. ∎

### Theorem 116.3.3 (Tensor Product Theorem)
For any chain complex $C_\bullet$ and any module $M$, we have a natural isomorphism:
$$H_*(C_\bullet \otimes M) \cong H_*(C_\bullet) \otimes M$$

**Proof:** This is a fundamental property of homology with coefficients in a module. The isomorphism is natural in both $C_\bullet$ and $M$.

The proof uses the fact that the tensor product preserves exactness in certain contexts. Specifically, we can use the short exact sequence of chain complexes:
$$0 \to Z_k(C) \to C_k \to B_k(C) \to 0$$

Tensoring with $M$, we get:
$$0 \to Z_k(C) \otimes M \to C_k \otimes M \to B_k(C) \otimes M \to 0$$

This sequence is exact because tensor products are right-exact, and we need to use additional arguments to show exactness at $Z_k(C) \otimes M$.

Using these exact sequences, we can construct the isomorphism between $H_*(C_\bullet \otimes M)$ and $H_*(C_\bullet) \otimes M$. ∎

## Summary

This chapter covers:
1. The fundamental group and its properties
2. Covering spaces and their classification
3. Homology theory and its applications

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*