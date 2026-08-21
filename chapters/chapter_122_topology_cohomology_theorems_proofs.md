# Chapter 122: Topology - Cohomology Theorems and Proofs

## 122.1 Introduction

This chapter explores the deep structures of topological spaces through the lens of cohomology theory, connecting algebraic invariants with geometric properties. We examine:
- Singular cohomology and its fundamental theorems
- Poincaré Duality
- The Poincaré Conjecture
- Steenrod operations
- Spectral sequences

## 122.2 Singular Cohomology Fundamentals

**Theorem 122.1 (Definition of Singular Cohomology)**  
For a topological space $X$ and coefficient group $G$, the singular cohomology groups $H^n(X; G)$ are defined as the derived functors of the functor $C_*(X; G) \mapsto \prod C_n(X; G)$, where $C_*(X; G)$ is the complex of singular chains.

*Proof:*  
The definition follows from the Eilenberg-Steenrod axioms for cohomology theories, which characterize cohomology uniquely up to isomorphism. The cohomology groups are computed via the universal coefficient theorem from homology.

**Theorem 122.2 (Universal Coefficient Theorem)**  
For any topological space $X$ and abelian group $G$:
$$0 \to \text{Ext}^1(H_{n-1}(X; \mathbb{Z}), G) \to H^n(X; G) \to \text{Hom}(H_n(X; \mathbb{Z}), G) \to 0$$

The sequence splits, but not naturally.

*Proof:*  
This is a fundamental result in homological algebra, proved using the short exact sequence of chain complexes:
$$0 \to \mathbb{Z} \to \mathbb{Q} \to \mathbb{Q}/\mathbb{Z} \to 0$$

Applying the derived functors $\text{Hom}(-, G)$ and $\text{Ext}^1(-, G)$ gives the result.

## 122.3 Poincaré Duality

**Theorem 122.3 (Poincaré Duality for Manifolds)**  
Let $M$ be a compact, connected, oriented $n$-dimensional manifold without boundary. Then there is a natural isomorphism:
$$H^k(M; \mathbb{Q}) \cong H_{n-k}(M; \mathbb{Q})$$

*Proof:*  
The duality arises from the intersection pairing on homology:
$$H_k(M; \mathbb{Q}) \times H_{n-k}(M; \mathbb{Q}) \to H_n(M; \mathbb{Q}) \cong \mathbb{Q}$$

By the universal coefficient theorem and the fact that the intersection pairing is non-degenerate, this induces the isomorphism.

**Corollary (Poincaré Polynomial):**  
For a compact orientable manifold $M$, the Poincaré polynomial satisfies:
$$P_M(t) = \sum_{k=0}^n b_k t^k = \sum_{k=0}^n b_{n-k} t^{n-k}$$

*Proof:*  
The Poincaré polynomial $P_M(t) = \sum b_k t^k$ encodes the Betti numbers $b_k = \text{rank}(H_k(M; \mathbb{Q}))$. By Poincaré duality, $b_k = b_{n-k}$, giving the symmetry.

## 122.4 The Poincaré Conjecture

**Theorem 122.4 (Poincaré Conjecture - Proved)**  
Every compact, connected, smooth manifold $M$ that is homotopy equivalent to a sphere $S^n$ is homeomorphic to $S^n$.

*Proof (Perelman's proof of the Smale conjecture):*  
This was proven by Grigori Perelman using his three papers on geometric flows: Ricci flow, Hamilton's Ricci flow with surgery, and the geometrization conjecture.

The key steps:
1. Ricci flow develops singularities
2. Ricci flow with surgery removes singularities
3. The resulting manifold has finite-dimensional topology
4. By the Geometrization Theorem, $M$ admits a Riemannian metric with constant curvature
5. Such manifolds are classified and homeomorphic to spheres

**Theorem 122.5 (Generalized Poincaré)**  
Every compact, connected, spin manifold $M$ that is homotopy equivalent to $S^n$ is homeomorphic to $S^n$ for $n$ odd, and diffeomorphic for $n$ even (except $n=4$).

*Proof:*  
This follows from Freedman's theorem for topological manifolds (all dimensions) and Perelman's work for smooth manifolds in dimensions other than 4.

## 122.5 Steenrod Operations

**Theorem 122.6 (Steenrod Square Definition)**  
For any odd prime $p$ and cohomology class $x \in H^n(X; \mathbb{F}_p)$, there exists a stable homomorphism:
$$Sq^k: H^n(X; \mathbb{F}_p) \to H^{n+2k}(X; \mathbb{F}_p)$$

*Proof:*  
Steenrod squares arise from the suspension isomorphism and the J-homomorphism in stable homotopy theory. They satisfy the Cartan formula:
$$Sq^k(xy) = \sum_{i+j=k} Sq^i(x)Sq^j(y)$$

**Theorem 122.7 (Milnor-Stasheff Characteristic Classes)**  
For a smooth oriented vector bundle $E \to X$ of rank $n$, the total Stiefel-Whitney class $w(E)$ has coefficients determined by the total Steenrod power operation:
$$w(E) = \sum_{i=0}^n w_i(E) \in H^*(X; \mathbb{F}_2)$$

*Proof:*  
The Steenrod squares provide a cohomological characterization of characteristic classes. Milnor and Stasheff proved that $Sq^1 = w_1$, $Sq^1 Sq^1 = w_2$, etc.

**Corollary (Hopf Invariant One Theorem)**  
If a sphere $S^{2n-1}$ admits a map of Hopf invariant 1 to $S^n$, then $n = 1, 2, 4, 8$.

*Proof:*  
Adams proved this using Steenrod operations. The Hopf invariant one problem characterizes the existence of parallelizable spheres.

## 122.6 Spectral Sequences

**Theorem 122.8 (Serre Spectral Sequence)**  
For a fibration $F \to E \to B$ with fiber $F$, base $B$, and total space $E$, there exists a first-quadrant spectral sequence with $E_2$ term:
$$E_2^{p,q} = H^p(B; \mathcal{H}^q(F)) \implies H^{p+q}(E)$$

*Proof:*  
The spectral sequence arises from a filtration of the cochain complex $C^*(E)$. The $E_1$ page is $E_1^{p,q} = \bigoplus^q H^p(B; H^q(E_p))$, where $E_p$ are the pages of the filtration.

**Theorem 122.9 (Atiyah-Hirzebruch Spectral Sequence)**  
For a complex-oriented cohomology theory $MU^*$, there exists a spectral sequence:
$$E_2^{p,q} = MU^{-p-q}(pt) \otimes H^p(B; \mathcal{H}^q(F)) \implies MU^{-n}(E)$$

*Proof:*  
This spectral sequence computes generalized cohomology theories using the Eilenberg-Steenrod axioms and the properties of oriented theories.

## 122.7 Whitehead Products

**Theorem 122.10 (Definition of Whitehead Product)**  
For spaces $X, Y$ and elements $\alpha \in \pi_i(X), \beta \in \pi_j(Y)$, there exists a Whitehead product:
$$[\alpha, \beta] \in \pi_{i+j-1}(X \vee Y)$$

*Proof:*  
Whitehead products arise from the obstruction theory of lifting maps. They are defined via the group operation in homotopy groups of wedged spaces.

**Theorem 122.11 (Vanishing Theorem)**  
If $X$ is a co-H-space, then all Whitehead products $[\alpha, \beta]$ vanish for $\alpha, \beta \in \pi_*(X)$.

*Proof:*  
In a co-H-space, the comultiplication $\Delta: X \to X \vee X \vee X$ satisfies $\Delta \circ \text{coeval} = \text{id}$. This forces the Whitehead products to be null-homotopic.

---

*End of Chapter 122*
