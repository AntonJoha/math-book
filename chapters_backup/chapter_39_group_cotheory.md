# Chapter 39: Group Cohomology and Representation Theory

## 39.1 Introduction to Group Cohomology

**Definition 39.1.** Let $G$ be a group and $A$ a $G$-module (abelian group with $G$-action). The **group cohomology** $H^n(G,A)$ measures the extent to which $A$ fails to have "good" properties with respect to $G$.

**Definition 39.2.** A **$G$-module** is an abelian group $A$ equipped with an action $\cdot: G \times A \to A$ satisfying:
- $(gh) \cdot a = g \cdot (h \cdot a)$ for all $g,h \in G, a \in A$,
- $e \cdot a = a$ for all $a \in A$, where $e$ is the identity of $G$.

**Definition 39.3.** A **$G$-module** is **trivial** if $g \cdot a = a$ for all $g \in G, a \in A$.

**Theorem 39.4 (Cobar Construction).** For any group $G$, $H^n(G,\mathbb{Z}) \cong H^n(G; \mathbb{Z})$ via the cobar construction from the simplicial group $BG$.

**Theorem 39.5 (Group Extension).** There is a short exact sequence
$$1 \to A \to E \to G \to 1$$
called a group extension. Equivalence classes of extensions with kernel $A$ are in bijection with $H^2(G,A)$.

**Theorem 39.6 (Universal Coefficient Theorem).** For any group $G$ and $G$-module $A$:
$$H^n(G; A) \cong \text{Ext}_{\mathbb{Z}[G]}^n(\mathbb{Z}, A) \cong \begin{cases} H^n(G; A)/\text{Tor}(H^{n+1}(G;\mathbb{Z})) & \text{if } n \text{ is odd}, \\ H^n(G; A)/\text{Ext}(H^{n-1}(G; \mathbb{Z}), A) & \text{if } n \text{ is even}. \end{cases}$$

**Theorem 39.7 (Shapiro's Lemma).** Let $H \subseteq G$ be a subgroup and $A$ an $H$-module. Then
$$H^*(G, \text{Ind}_H^G(A)) \cong H^*(H, A).$$

**Theorem 39.8 (Transfer/Multiplication by G).** For any finite-index subgroup $H \subseteq G$, there is a transfer map
$$\text{Tr}: H^*(G,A) \to H^*(H, A).$$

**Theorem 39.9 (Norm Map).** For any $A$ with trivial $G$-action, there is a norm map
$$N: H^n(G,A) \to H^n(G,A)$$
given by $N(\alpha) = \sum_{g \in G} g \cdot \alpha$.

**Theorem 39.10 (Inflation-Restriction-Transfer).** Let $1 \to H \to G \to Q \to 1$ be a short exact sequence of groups. Then for any $Q$-module $A$:
- $\text{Inf}: H^n(Q,A) \to H^n(G,A)$,
- $\text{Res}: H^n(G,A)^H \to H^n(H,A)$,
- $\text{Tr}: H^n(G,A) \to H^n(H,A)$.
These satisfy a Mayer-Vietoris type exact sequence:
$$\dots \to H^n(Q,A) \xrightarrow{\text{Inf}} H^n(G,A) \xrightarrow{\text{Tr}} H^n(H,A) \xrightarrow{\delta} H^{n+1}(Q,A) \to \dots$$

**Theorem 39.11 (Group Cohomology with Trivial Action).** For $A$ a trivial $G$-module, $H^n(G,A)$ classifies $n$-dimensional classifying spaces with coefficients in $A$.

**Theorem 39.12 (Tate Cohomology).** For a finite group $G$ and a $G$-module $A$, the Tate cohomology groups $\hat{H}^n(G,A)$ are defined for all $n \in \mathbb{Z}$.

**Theorem 39.13 (Periodicity of Tate Cohomology).** If $G$ is finite of order $m$, then $H^n(G,A) \cong H^{n+m}(G,A)$ for any $G$-module $A$.

**Theorem 39.14 (Vanishing Theorem).** Let $H \subseteq G$ be a subgroup of finite index. Then $H^n(G,\mathbb{Z}) \cong H^n(G/\mathbb{Z}, \mathbb{Z}) \cong 0$ for $n > 0$.

**Theorem 39.15 (Euler Characteristic Relation).** For a finite group $G$ and $G$-module $A$,
$$\sum_{n \geq 0} (-1)^n \dim H^n(G,A) = \chi(G) \dim A,$$
where $\chi(G) = 1$ if $G$ is trivial and $0$ otherwise.

## 39.2 Cohomology of Specific Groups

**Theorem 39.16 (Cohomology of Free Group).** $H^n(F_m, \mathbb{Z}) = 0$ for $n > 1$ and any free group $F_m$ on $m$ generators.

**Theorem 39.17 (Cohomology of Finite Groups).** For a finite group $G$ and $G$-module $A$, $H^n(G,A)$ can be computed using the bar resolution.

**Theorem 39.18 (Schur Z-cohomology).** For a finite $p$-group $P$ and $P$-module $M$, $H^n(P,M) = 0$ for $n \geq 2$ if $M$ has a $P$-invariant basis.

**Theorem 39.19 (Brouwer's Fixed Point Theorem - Cohomological).** For any action of a finite $p$-group $P$ on a contractible space $X$, there exists a fixed point.

**Theorem 39.20 (Hypothesis).** For any action of a finite $p$-group $P$ on a finite set $X$, the cardinality $|X|$ is divisible by $p$ or has a fixed point.

## 39.3 Representation Theory

**Definition 39.21.** A **representation** of a group $G$ on a vector space $V$ is a homomorphism $\rho: G \to GL(V)$.

**Theorem 39.22 (Peter-Weyl Theorem).** For any finite group $G$, the regular representation decomposes as:
$$\mathbb{C}[G] \cong \bigoplus_{i} \bigoplus_{j=1}^{\dim V_i} V_i \otimes V_i^*,$$
where $V_i$ range over irreducible representations.

**Theorem 39.23 (Mackey's Irreducibility Criterion).** A representation $\rho: G \to GL(V)$ is irreducible if and only if it has no non-trivial invariant subspaces.

**Theorem 39.24 (Schur's Lemma).** Let $G$ be a finite group and $V$ an irreducible representation over $\mathbb{C}$. Then:
- $\text{End}_G(V) \cong \mathbb{C}$,
- Any $G$-linear endomorphism of an irreducible representation is a scalar multiple of the identity.

**Theorem 39.25 (Maschke's Theorem).** A finite group $G$ has all representations completely reducible if and only if characteristic of the field does not divide $|G|$.

**Theorem 39.26 (Complete Reductivity).** Over a field $k$ of characteristic not dividing $|G|$, every representation of $G$ is completely reducible.

**Theorem 39.27 (Clifford Theory).** Let $G$ be a finite group and $H \subseteq G$ a normal subgroup. Let $\chi$ be a character of $H$. The restriction $\chi \downarrow_H$ to an irreducible representation $\theta$ is:
$$\text{Ind}_H^G(\theta)|_H \cong \sum_{i} m_i \chi_i,$$
where $\chi_i$ are irreducible characters of $H$.

**Theorem 39.28 (Burnside's Theorem on Groups).** A finite group $G$ whose order is a prime power $p^n$ has a unique minimal normal subgroup which is the Frattini subgroup.

**Theorem 39.29 (Burnside's $p^a q^b$ Theorem).** A finite group of order $p^a q^b$ (where $p,q$ are primes) is solvable.

**Theorem 39.30 (Complete Reductivity of Group Representations).** Every finite-dimensional representation of a finite group over an algebraically closed field of characteristic zero is completely reducible.

**Theorem 39.31 (Weyl's Theorem on Complete Reductivity).** Every representation of a compact Lie group over $\mathbb{C}$ is completely reducible.

**Theorem 39.32 (Weyl's Character Formula).** For a compact Lie group $G$, irreducible characters $\chi_\lambda$ are given by:
$$\chi_\lambda(g) = \frac{\det(\exp(i\lambda(\alpha_j)))}{\det(\exp(i(\alpha_i - \rho)(g)))} \prod_{\alpha \in \Delta^+} (1 - e^{i\alpha(g)}),$$
where $\lambda$ is a highest weight, $\alpha$ runs over positive roots, and $\rho$ is the half-sum of positive roots.

**Theorem 39.33 (Littlewood-Richardson Rule).** For Lie algebras $\mathfrak{g}$,
$$V_\mu \otimes V_\nu \cong \bigoplus_{\lambda} c_{\mu,\nu}^\lambda V_\lambda,$$
where $c_{\mu,\nu}^\lambda$ are the Littlewood-Richardson coefficients.

**Theorem 39.34 (Cartan's Theorem on Lie Algebra Cohomology).** For a Lie algebra $\mathfrak{g}$ over $\mathbb{R}$, $H^n(\mathfrak{g}, \mathbb{R}) = 0$ for $n \geq 1$ (by Cartan's theorem on Lie algebra cohomology).

**Theorem 39.35 (Borel-Weil Theorem).** Irreducible representations of a compact Lie group $G$ correspond to holomorphic line bundles $L_\lambda$ on flag manifolds $G/B$.


## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*