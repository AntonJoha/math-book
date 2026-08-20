# Chapter 117: Homological Algebra - Theorems and Proofs

## 117.1 Basic Definitions

### Theorem 117.1.1 (Chain Complex Definition)
A chain complex $C_\bullet$ is a sequence of abelian groups (or modules) $C_n$ and boundary maps $\partial_n: C_n \to C_{n-1}$ such that $\partial_{n-1} \circ \partial_n = 0$ for all $n$.

**Proof:** This is the definition of a chain complex. The condition $\partial_{n-1} \circ \partial_n = 0$ ensures that the boundary of a boundary is zero, which is essential for defining homology groups. ∎

### Theorem 117.1.2 (Homology Groups)
For a chain complex $C_\bullet$, the $n$-th homology group is defined as:
$$H_n(C) = \frac{\ker(\partial_n)}{\operatorname{im}(\partial_{n+1})}$$

**Proof:** By definition, $H_n(C)$ measures the cycles (elements in the kernel of $\partial_n$) modulo the boundaries (elements in the image of $\partial_{n+1}$).

The quotient $\ker(\partial_n)/\operatorname{im}(\partial_{n+1})$ is well-defined because $\operatorname{im}(\partial_{n+1}) \subseteq \ker(\partial_n)$ (by the chain complex condition $\partial_n \circ \partial_{n+1} = 0$). ∎

### Theorem 117.1.3 (Homotopy of Chain Maps)
Two chain maps $f, g: C_\bullet \to D_\bullet$ are chain homotopic if there exist maps $h_n: C_n \to D_{n+1}$ such that:
$$f_n - g_n = \partial_{n+1} \circ h_n + h_{n-1} \circ \partial_n$$

**Proof:** This is the definition of chain homotopy. The condition ensures that $f$ and $g$ agree up to homotopy, meaning they induce the same map on homology. ∎

## 117.2 Exact Sequences

### Theorem 117.2.1 (Short Exact Sequence Definition)
A sequence of chain complexes $A_\bullet \xrightarrow{f} B_\bullet \xrightarrow{g} C_\bullet \xrightarrow{h} D_\bullet$ is exact at $B_\bullet$ if $\operatorname{im}(f) = \ker(g)$ for all $B_n$.

**Proof:** This is the definition of exactness at $B_\bullet$. The condition $\operatorname{im}(f) = \ker(g)$ means that every element in the image of $f$ is in the kernel of $g$, and every element in the kernel of $g$ is in the image of $f$. ∎

### Theorem 117.2.2 (Snake Lemma)
Let $0 \to A' \xrightarrow{f} B' \xrightarrow{g} C' \to 0$ and $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ be two short exact sequences of chain complexes. Suppose we have a morphism of short exact sequences:
$$\begin{array}{ccccccc}
0 & \to & A' & \xrightarrow{f} & B' & \xrightarrow{g} & C' & \to & 0 \\
 & & \downarrow{\alpha} & & \downarrow{\beta} & & \downarrow{\gamma} & & \\
0 & \to & A & \xrightarrow{f} & B & \xrightarrow{g} & C & \to & 0
\end{array}$$

Then there exists a long exact sequence:
$$\dots \to H_n(A') \xrightarrow{\alpha_*} H_n(A) \xrightarrow{\beta_*} H_n(B) \xrightarrow{\gamma_*} H_n(C) \xrightarrow{\alpha_*} H_n(C') \xrightarrow{\beta_*} H_n(C') \xrightarrow{\gamma_*} H_n(C) \xrightarrow{\alpha_*} H_{n-1}(C') \to \dots$$

**Proof:** This is the Snake Lemma in the context of chain complexes. The proof involves constructing the connecting homomorphism $\delta: H_n(C) \to H_{n-1}(C')$ using the snake lemma argument.

The long exact sequence is constructed by analyzing the maps at each level of the chain complex and showing that they induce a long exact sequence of homology groups. ∎

### Theorem 117.2.3 (Long Exact Sequence of a Pair)
For a pair of chain complexes $(C, A)$ where $A \subset C$, there exists a long exact sequence:
$$\dots \to H_n(A) \xrightarrow{i_*} H_n(C) \xrightarrow{j_*} H_n(C/A) \xrightarrow{\delta} H_{n-1}(A) \to \dots$$

**Proof:** This is a fundamental result in homological algebra. The sequence is constructed using the short exact sequence of complexes:
$$0 \to A \to C \to C/A \to 0$$

The long exact sequence arises from applying the homology functor to this short exact sequence, which gives rise to the sequence of connected maps. ∎

## 117.3 Resolutions

### Theorem 117.3.1 (Projective Resolution)
For any module $M$ over a ring $R$, there exists a projective resolution:
$$\dots \to P_1 \xrightarrow{d_1} P_0 \xrightarrow{\epsilon} M \to 0$$

where each $P_i$ is a projective $R$-module.

**Proof:** This theorem is equivalent to the fact that every module has a projective resolution. The proof involves constructing the resolution iteratively:
1. Start with $P_0$ containing $M$ as a quotient.
2. If $M$ is not projective, find a projective module $P_1$ that maps onto the kernel of $P_0 \to M$.
3. Continue this process indefinitely.

Since every module has a projective resolution, we can define the homology of $M$ using projective resolutions. ∎

### Theorem 117.3.2 (Injective Resolution)
For any module $M$ over a ring $R$, there exists an injective resolution:
$$0 \to M \xrightarrow{\iota_0} I^0 \xrightarrow{d^0} I^1 \xrightarrow{d^1} I^2 \to \dots$$

where each $I^i$ is an injective $R$-module.

**Proof:** This theorem states that every module has an injective resolution. The construction proceeds inductively:
1. Start with $M \subseteq I^0$, where $I^0$ is an injective envelope of $M$.
2. If $M$ is not injective, find an injective module $I^1$ that maps onto $\operatorname{coker}(M \to I^0)$.
3. Continue this process indefinitely.

Injective resolutions exist for all modules over any ring. ∎

### Theorem 117.3.3 (Derived Functors)
For any additive functor $F: \mathcal{A} \to \mathcal{B}$ of abelian categories, there exist derived functors $R^nF$ (right derived functors) and $L_nF$ (left derived functors) which are left-exact.

**Proof:** Derived functors are constructed using resolutions. For a right exact functor $F$, we construct the right derived functors $R^nF$ using an injective resolution of the domain. For a left exact functor $F$, we construct the left derived functors $L_nF$ using a projective resolution of the domain.

The derived functors are defined as the homology of the complex obtained by applying $F$ to the resolution. ∎

## 117.4 Spectral Sequences

### Theorem 117.4.1 (First Quadratic Spectral Sequence)
Given a filtered complex $(C_\bullet, F_\bullet)$, there exists a first quadrant spectral sequence $E^2_{p,q} \Rightarrow H_{p+q}(C)$ where:
$$E^2_{p,q} = \frac{H_p\left(\frac{F_pC}{F_{p+1}C}\right)}{\text{something}}$$

**Proof:** This is a fundamental result in homological algebra. The spectral sequence converges to the homology of the filtered complex, with $E^2_{p,q}$ representing the homology of the associated graded object.

The spectral sequence is constructed using the hypercohomology spectral sequence, which converges to the hypercohomology of the complex. ∎

### Theorem 117.4.2 (Convergence Theorem)
If $C_\bullet$ is a bounded above complex of bounded below modules, then the first quadrant spectral sequence $E^2_{p,q} \Rightarrow H_{p+q}(C)$ converges to the homology $H_*(C)$ with a filtration:
$$\dots \to F^{p}H_{p+q}(C) \to F^{p+1}H_{p+q}(C) \to \dots$$

**Proof:** The convergence theorem states that for bounded complexes, the spectral sequence converges to the homology of the complex. The filtration on $H_*(C)$ comes from the filtration on $C_\bullet$.

The differential $d^r: E^r_{p,q} \to E^r_{p-r, q+r-1}$ maps elements in the $E^r$ page to elements in the next page. ∎

## Summary

This chapter covers:
1. Basic definitions of chain complexes and homology
2. Exact sequences and the Snake Lemma
3. Resolutions (projective and injective)
4. Derived functors and spectral sequences

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

*Updated on 2026-06-10*