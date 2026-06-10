# Algebraic Topology

Algebraic topology uses algebraic structures to classify topological spaces and investigate their properties. It bridges the gap between algebra and topology by assigning algebraic invariants to topological spaces.

## 6.1 Homotopy Groups

### Definition

A homotopy between two continuous maps $f, g: X \to Y$ is a continuous map $H: X \times [0,1] \to Y$ such that $H(x,0) = f(x)$ and $H(x,1) = g(x)$ for all $x \in X$.

We write $f \simeq g$ if there exists a homotopy between them.

### Fundamental Group

**Definition (Fundamental Group)**: For a path-connected topological space $X$ with basepoint $x_0$, the fundamental group $\pi_1(X, x_0)$ is the group of homotopy classes of loops based at $x_0$, with group operation given by path concatenation.

**Theorem 6.1 (Fundamental Group Properties)**:

1. **Homotopy Invariance**: If $f: X \to Y$ and $g: Z \to W$ are continuous maps and $h: X \to Z$ is a homotopy equivalence, then $f \circ h \simeq g \circ h$ implies $f_*$ and $g_*$ are isomorphisms.

2. **Homotopy Invariance**: If $f, g: X \to Y$ are homotopic, then $f_*$ and $g_*$: $\pi_n(X, x_0) \to \pi_n(Y, f(x_0))$ are equal.

**Proof**: Let $H: X \times [0,1] \to Y$ be a homotopy between $f$ and $g$. For any loop $\alpha: S^1 \to X$ representing an element $[\alpha] \in \pi_1(X, x_0)$, we have:
- $f \circ \alpha$ represents $f_*([\alpha])$
- $g \circ \alpha$ represents $g_*([\alpha])$
Since $f \simeq g$, there is $H$ such that $(f \circ \alpha)_t = f(\alpha(t), 0)$ and $(g \circ \alpha)_t = g(\alpha(t), 1)$ are homotopic in $Y$. Thus $f_*([\alpha]) = g_*([\alpha])$. ∎

### Higher Homotopy Groups

**Definition**: For $n \geq 1$, $\pi_n(X, x_0)$ consists of homotopy classes of maps $f: S^n \to X$ sending the basepoint $1 \in S^n$ to $x_0$. The group operation for $n \geq 2$ is induced by the pinch map.

**Theorem 6.2 (Van Kampen Theorem)**: 

Let $X = U \cup V$ where $U, V$ are open, path-connected subsets with $U \cap V$ path-connected. Then:
$$\pi_1(X) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V)$$

**Proof**: We use the pushout property of fundamental groups under pushouts of spaces. The inclusion maps $i_U: U \cap V \to U$ and $i_V: U \cap V \to V$ induce homomorphisms $i_{U*}, i_{V*}$. The universal property of pushouts in groups gives the isomorphism. ∎

## 6.2 Homology Groups

### Singular Homology

**Definition**: For a continuous map $f: X \to Y$, the induced map $f_*: H_n(X) \to H_n(Y)$ is well-defined on singular homology groups.

**Theorem 6.3 (Homotopy Invariance of Homology)**:

If $f, g: X \to Y$ are homotopic, then $f_* = g_*$.

**Proof**: Let $H: X \times [0,1] \to Y$ be a homotopy. By excision and the fact that $H$ is homotopic to constant maps, the induced maps on homology are equal. ∎

### Homology of Spaces

**Theorem 6.4 (Homology of a Point)**:

For a point space $X = \{p\}$, $H_n(X) = 0$ for $n > 0$ and $H_0(X) = \mathbb{Z}$.

**Proof**: The only 0-chain is $c(p)$. The boundary map $\partial_1$ is the zero map since there's only one vertex. Thus $H_0(X) = \ker(\partial_0)/\operatorname{im}(\partial_1) = \mathbb{Z}/0 = \mathbb{Z}$. For $n > 0$, all chains are boundaries. ∎

**Theorem 6.5 (Homology of Circle)**:

For $X = S^1$, $H_0(S^1) = \mathbb{Z}$ and $H_1(S^1) = \mathbb{Z}$.

**Proof**: Using simplicial approximation, $S^1$ can be triangulated with 2 vertices and 2 edges forming a cycle. The chain complex is:
$$C_n(S^1) = \begin{cases} \mathbb{Z} & n = 0, 1 \\ 0 & n \geq 2 \end{cases}$$
With boundary maps $\partial_1 = 0$ (since both edges go from v_0 to v_1), we get $H_0(S^1) = \mathbb{Z}$ and $H_1(S^1) = \ker(\partial_1)/\operatorname{im}(\partial_2) = \mathbb{Z}/0 = \mathbb{Z}$. ∎

## 6.3 Covering Spaces

### Uniqueness of Lifts

**Theorem 6.6 (Lifting Property)**: 

Let $p: \tilde{X} \to X$ be a covering map, $B$ a path-connected space, $f: B \to X$ continuous, and $\tilde{x}_0 \in \tilde{X}$ with $p(\tilde{x}_0) = f(x_0)$. There exists a unique continuous map $\tilde{f}: B \to \tilde{X}$ such that $p \circ \tilde{f} = f$ and $\tilde{f}(x_0) = \tilde{x}_0$.

**Proof**: This is a standard result in covering space theory. By path-lifting, any path in $B$ can be lifted to a unique path in $\tilde{X}$ starting at $\tilde{x}_0$. The continuous extension to all of $B$ follows from compactness arguments or the fact that continuous functions are locally constant on connected components. ∎

**Theorem 6.7 (Fundamental Group of Covering Space)**:

Let $p: \tilde{X} \to X$ be a covering map with $X$ path-connected. Then $p_*$ is injective and $\pi_1(X)/\operatorname{Im}(p_*) \cong \pi_0(\tilde{X})$.

**Proof**: The injectivity follows from the path-lifting property. If $\tilde{X}$ is connected, then $\pi_1(X)$ acts on the fiber $p^{-1}(x_0)$, and the quotient is isomorphic to the action group. ∎

## 6.4 Exact Sequences

### Long Exact Sequence

**Theorem 6.8 (Long Exact Sequence of Pair)**: 

For the pair $(X, A)$, there exists a long exact sequence:
$$\dots \to H_n(A) \xrightarrow{i_*} H_n(X) \xrightarrow{j_*} H_n(X,A) \xrightarrow{\partial} H_{n-1}(A) \to \dots$$

**Proof**: This follows from the excision axiom and the naturality of the boundary map. The exactness at each term is proved by constructing explicit maps and showing $\operatorname{im} = \ker$. ∎

**Corollary 6.9 (Exact Sequence for Fibration)**: 

For a fibration $F \to E \to B$, there exists a long exact sequence:
$$\dots \to \pi_n(F) \to \pi_n(E) \to \pi_n(B) \xrightarrow{\partial} \pi_{n-1}(F) \to \dots$$

**Proof**: Follows from the homotopy exact sequence of a fibration. ∎

## 6.5 Euler Characteristic

### Definition and Formula

**Theorem 6.10 (Euler Characteristic for Polyhedra)**:

For a polyhedron $P$, $\chi(P) = V - E + F$ where $V, E, F$ are the number of vertices, edges, and faces.

**Theorem 6.11 (Euler Characteristic is Homotopy Invariant)**:

For path-connected spaces $X, Y$ with the same homotopy type, $\chi(X) = \chi(Y)$.

**Proof**: The Euler characteristic is defined as $\sum (-1)^n \operatorname{rank}(H_n(X))$. For homotopy equivalent spaces, their homology groups are isomorphic, so their Euler characteristics are equal. ∎

### Application to Torus

**Corollary 6.12 (Torus Euler Characteristic)**:

For $T^2 = S^1 \times S^1$, $\chi(T^2) = 0$.

**Proof**: $H_0(T^2) = \mathbb{Z}$, $H_1(T^2) = \mathbb{Z}^2$, $H_2(T^2) = \mathbb{Z}$. So $\chi(T^2) = 1 - 2 + 1 = 0$. ∎

## 6.6 Whitehead's Theorem

### Equivalence Conditions

**Theorem 6.13 (Whitehead's Theorem)**:

A continuous map $f: X \to Y$ is a homotopy equivalence if and only if $f_*: \pi_n(X) \to \pi_n(Y)$ is an isomorphism for all $n \geq 0$.

**Proof**: This is a deep result using spectral sequences and cellular approximation. The forward direction is clear from homotopy invariance. The backward direction requires the fact that if $f_*$ is an isomorphism on all homotopy groups, then $f$ induces isomorphisms on all homology groups, making it a weak homotopy equivalence, and by the Whitehead theorem, this is a homotopy equivalence. ∎

## Exercises

- Prove that $\pi_1(S^2) = 0$.
- Show that the covering space map for $p: \mathbb{R} \to S^1$ given by $t \mapsto e^{2\pi i t}$ has degree 1.
- Compute $H_*(\mathbb{C}P^n)$ using the long exact sequence.
- Prove the Hurewicz theorem: If $\pi_n(X) = 0$ for $n < k$, then $\pi_k(X) \cong H_k(X)$.


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
