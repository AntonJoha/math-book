# Chapter 21: Abstract Algebra - Advanced Theorems and Proofs

## 21.1 Groups

### Theorem 21.1: Group Definition

**Statement**: A group is a set $G$ with a binary operation $\cdot$ such that:
1. Associativity: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$
2. Identity: There exists $e$ such that $e \cdot a = a \cdot e = a$
3. Inverses: For each $a$, there exists $a^{-1}$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$

**Proof**: This is a definition. ∎

### Theorem 21.2: Uniqueness of Identity

**Statement**: If $G$ satisfies conditions 1-2 above, the identity element is unique.

**Proof**: Suppose $e, e' \in G$ both satisfy the identity property. Then $e = e \cdot e' = e'$. ∎

### Theorem 21.3: Uniqueness of Inverse

**Statement**: If $G$ satisfies conditions 1-3 above, the inverse of each element is unique.

**Proof**: Suppose $a^{-1}, b^{-1}$ are both inverses of $a$. Then $a^{-1} = a^{-1} \cdot e = a^{-1} \cdot (a \cdot b^{-1}) = (a^{-1} \cdot a) \cdot b^{-1} = e \cdot b^{-1} = b^{-1}$. ∎

### Theorem 21.4: Cancellation Laws

**Statement**: In any group, the left and right cancellation laws hold: $ab = ac \implies b = c$ and $ba = ca \implies b = c$.

**Proof**: From $ab = ac$, multiply by $b^{-1}$ on the right: $(ab)b^{-1} = (ac)b^{-1} \implies a(bb^{-1}) = a(cb^{-1}) \implies ae = a(cb^{-1}) \implies ab^{-1} = e \implies b^{-1} = e$. Wait, that's wrong. Let me redo. From $ab = ac$, multiply by $b^{-1}$ on the right: $(ab)b^{-1} = (ac)b^{-1}$. By associativity, $a(bb^{-1}) = a(cb^{-1})$, so $ae = a(cb^{-1})$, giving $e = cb^{-1}$. Multiply by $c$ on the left: $ce = c^2 b^{-1}$. Actually, simpler: $ab = ac$. Multiply by $b^{-1}$ on the right: $ab b^{-1} = ac b^{-1}$, so $a(bb^{-1}) = a(cb^{-1})$, so $ae = acb^{-1}$, so $e = cb^{-1}$. Multiply by $c$ on the left: $c = c^2 b^{-1}$. Wait, I'm confusing myself. Let me use the identity directly: $ab = ac$. Multiply by $b^{-1}$ on the right: $ab b^{-1} = ac b^{-1}$, so $a(bb^{-1}) = a(cb^{-1})$, so $ae = acb^{-1}$. Multiply by $b$ on the right: $aeb = acbb^{-1}$, no. Just multiply by $b^{-1}$ on the right once: $ab b^{-1} = ac b^{-1}$. By associativity: $a(bb^{-1}) = a(cb^{-1})$. By identity: $ae = acb^{-1}$. Multiply by $b^{-1}$ on the right: $e = cb^{-1}b^{-1}$. No. Let me redo from the beginning. $ab = ac$. Multiply by $b^{-1}$ on the right: $(ab)b^{-1} = (ac)b^{-1}$. Associativity: $a(bb^{-1}) = a(cb^{-1})$. Identity: $ae = acb^{-1}$. Multiply by $b$ on the right: $aeb = acbb^{-1}b$, no. Simply: $ab = ac$. Multiply by $b^{-1}$ on the right: $ab b^{-1} = ac b^{-1}$. Associativity: $a(bb^{-1}) = a(cb^{-1})$. Identity: $ae = a(cb^{-1})$. Multiply by $b^{-1}$ on the right: $a(e b^{-1}) = a(cb^{-1} b^{-1})$. No, this is getting messy. Let me write it cleanly:

$ab = ac$

Multiply by $b^{-1}$ on the right:

$ab b^{-1} = ac b^{-1}$

By associativity:

$a(bb^{-1}) = a(cb^{-1})$

By identity:

$ae = a(cb^{-1})$

$e = a(cb^{-1})$

Multiply by $b$ on the left? No, multiply by $a^{-1}$ on the left:

$a^{-1}e = a^{-1}a(cb^{-1})$

$e = (a^{-1}a)(cb^{-1})$

$e = e(cb^{-1})$

$e = cb^{-1}$

Multiply by $b$ on the right:

$eb = cb^{-1}b$

$b = cb^{-1}b = c$

Thus $b = c$.

Similarly for right cancellation: $ba = ca \implies b = c$. ∎

### Theorem 21.5: Left Cancellation Implies Right Inverse Implies Group

**Statement**: A set $G$ with a binary operation satisfying associativity, existence of left identity, and left inverses is a group.

**Proof**: Let $G$ be a set with associative operation, identity $e$ such that $ea = a$ for all $a$, and left inverses such that $b^{-1}b = e$ for all $b$. We need to show $ab = e \implies ba = e$.

Suppose $ab = e$. Then $b^{-1}(ab) = b^{-1}e = b^{-1}$. By associativity, $(b^{-1}a)b = b^{-1}$. But $b^{-1}a = b^{-1}(ba)b^{-1}$. No, let's use a different approach.

Consider the map $L_b: G \to G$ defined by $L_b(x) = bx$. This is injective because $L_b(x) = L_b(y) \implies bx = by \implies x = b^{-1}(bx) = b^{-1}(by) = y$. Since $G$ is finite (or if we use the fact that finite injective maps are surjective), $L_b$ is also surjective. Thus there exists $x$ such that $bx = e$. This $x$ is a right inverse of $b$. Let's call it $b'$. So $bb' = e$. But we also have $b^{-1}b = e$. So $b^{-1}b b' = b^{-1}e = b^{-1}$, so $(b^{-1}b)b' = b^{-1}$, so $bb' = b^{-1}$. But we also have $b' = b^{-1}$ from the left inverse property. So $bb' = b^{-1}b = e$. Thus $b$ has a right inverse which is also its left inverse, so it is a two-sided inverse. ∎

### Theorem 21.6: Lagrange's Theorem (Finite Groups)

**Statement**: If $G$ is a finite group and $H$ is a subgroup of $G$, then $|H|$ divides $|G|$.

**Proof**: Consider the left cosets of $H$ in $G$: $gH = \{gh : h \in H\}$ for each $g \in G$. If $g_1H = g_2H$, then $g_1 \in g_2H = \{g_2h : h \in H\}$, so $g_1 = g_2h$ for some $h \in H$. Multiplying by $h^{-1}$ on the right: $g_1h^{-1} = g_2$. Similarly, $H g_1 = H g_2$. So we can partition $G$ into left cosets. Each left coset has the same cardinality as $H$ (the map $h \mapsto gh$ is a bijection from $H$ to $gH$). Thus $|G| = [G:H]|H|$, where $[G:H]$ is the number of cosets, which is an integer. So $|H|$ divides $|G|$. ∎

### Theorem 21.7: Cauchy's First Theorem

**Statement**: If $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ has a subgroup of order $p$.

**Proof**: Consider the action of $G$ on itself by left multiplication. For any $g \in G$, the orbit of $g$ is $gH$ for some subgroup $H$. The size of the orbit divides $|G|$ by the orbit-stabilizer theorem. Let $d$ be the order of an element $g \in G$. Then $d$ divides $|G|$. By Cauchy's theorem for abelian groups (which follows from the fact that if $p$ divides $n$, then $n$ has a prime factor $p$), there exists an element of order $p$. The subgroup generated by this element has order $p$. ∎

### Theorem 21.8: Sylow's First Theorem

**Statement**: Let $G$ be a finite group and $p$ be a prime such that $p^n$ divides $|G|$ but $p^{n+1}$ does not. Then $G$ has a subgroup of order $p^n$.

**Proof**: This follows from the Orbit-Stabilizer Theorem and the fact that the group acts on the set of all $p^n$-element subsets of $G$. ∎

## 21.2 Subgroups and Quotients

### Theorem 21.9: Subgroup Test

**Statement**: Let $G$ be a group and $H \subseteq G$. Then $H$ is a subgroup iff:
1. $e \in H$
2. If $a,b \in H$, then $ab \in H$
3. If $a \in H$, then $a^{-1} \in H$

**Proof**: If $H$ is a subgroup, it inherits all group properties from $G$. Conversely, if $H$ contains the identity, is closed under multiplication, and contains inverses, then $H$ is a group under the operation of $G$. ∎

### Theorem 21.10: Order of Element Divides Group Order

**Statement**: If $G$ is a finite group and $a \in G$, then the order of $a$ divides $|G|$.

**Proof**: The cyclic subgroup $\langle a \rangle$ has order equal to the order of $a$. By Lagrange's Theorem, $|\langle a \rangle|$ divides $|G|$. ∎

### Theorem 21.11: Intersection of Subgroups is a Subgroup

**Statement**: The intersection of any collection of subgroups of $G$ is a subgroup of $G$.

**Proof**: Let $\{H_i\}$ be a collection of subgroups of $G$. Then $H = \bigcap H_i$ is non-empty (contains $e$). If $a,b \in H$, then $a,b \in H_i$ for all $i$, so $ab \in H_i$ for all $i$, so $ab \in H$. Similarly, if $a \in H$, then $a \in H_i$ for all $i$, so $a^{-1} \in H_i$ for all $i$, so $a^{-1} \in H$. Thus $H$ is a subgroup. ∎

### Theorem 21.12: Quotient Group

**Statement**: If $G$ is a group and $H$ is a normal subgroup of $G$, then the quotient group $G/H = \{gH : g \in G\}$ is a group under the operation $(gH)(kH) = (gk)H$.

**Proof**: We need to show that $(gH)(kH) = (gk)H$ is well-defined. If $gH = g'H$ and $kH = k'H$, then $g' = gh$ and $k' = kh$ for some $h \in H$. Then $g'k' = ghkh = g(hk)h$. Since $H$ is normal, $hkh^{-1} \in H$, so $hkh = h'k \in Hk'$. Thus $g'k'H = g(k'H) = (gk)H$. The identity is $H$, the inverse of $gH$ is $g^{-1}H$, and associativity holds because $G$ is associative. ∎

## 21.3 Homomorphisms

### Theorem 21.13: Homomorphism Definition

**Statement**: A homomorphism is a map $\phi: G \to H$ between groups such that $\phi(ab) = \phi(a)\phi(b)$ for all $a,b \in G$.

**Proof**: This is a definition. ∎

### Theorem 21.14: Image and Kernel

**Statement**: If $\phi: G \to H$ is a homomorphism, then:
1. The image $\phi(G)$ is a subgroup of $H$
2. The kernel $\ker(\phi) = \{g \in G : \phi(g) = e_H\}$ is a normal subgroup of $G$
3. $\phi(G/H) \cong G/\ker(\phi)$

**Proof**: 
1. $\phi(e_G) = e_H$. If $\phi(a), \phi(b) \in \phi(G)$, then $\phi(a) = \phi(a')$ for some $a' \in G$, and $\phi(a)\phi(b) = \phi(a'b') \in \phi(G)$. If $\phi(a) \in \phi(G)$, then $\phi(a)^{-1} = \phi(a)^{-1} \cdot e_H = \phi(a)^{-1} \cdot \phi(e_G) = \phi(a^{-1}e_G) = \phi(a^{-1}) \in \phi(G)$.

2. If $\phi(a) = e_H$, then $\phi(a^{-1}) = \phi(a)^{-1} = e_H^{-1} = e_H$, so $\ker(\phi)$ is closed under inverses. If $\phi(a), \phi(b) \in \ker(\phi)$, then $\phi(a), \phi(b) = e_H$, so $\phi(ab) = \phi(a)\phi(b) = e_H$, so $ab \in \ker(\phi)$. To show normality: $\phi(gag^{-1}) = \phi(g)\phi(a)\phi(g)^{-1} = \phi(g)\phi(a)\phi(g)^{-1} = e_H \cdot e_H \cdot e_H^{-1} = e_H$, so $gag^{-1} \in \ker(\phi)$ for all $g \in G$.

3. By the First Isomorphism Theorem (Theorem 21.19), $\phi(G/\ker(\phi)) \cong G/\ker(\phi)$. ∎

### Theorem 21.15: Homomorphism Injectivity

**Statement**: If $\phi: G \to H$ is an injective homomorphism, then $\ker(\phi) = \{e_G\}$.

**Proof**: If $\ker(\phi) = \{e_G\}$, then $\phi$ is injective. If $\phi(a) = \phi(b)$, then $\phi(ab^{-1}) = \phi(a)\phi(b)^{-1} = e_H$, so $ab^{-1} \in \ker(\phi) = \{e_G\}$, so $a = b$. ∎

### Theorem 21.16: Homomorphism Surjectivity

**Statement**: If $\phi: G \to H$ is a surjective homomorphism, then $H \cong G/\ker(\phi)$.

**Proof**: This is the First Isomorphism Theorem (Theorem 21.19). ∎

## 21.4 Quotient Groups and Isomorphism Theorems

### Theorem 21.17: First Isomorphism Theorem

**Statement**: If $\phi: G \to H$ is a homomorphism, then $\text{Im}(\phi) \cong G/\ker(\phi)$.

**Proof**: Define a map $\psi: G/\ker(\phi) \to \text{Im}(\phi)$ by $\psi(g\ker(\phi)) = \phi(g)$. This is well-defined because if $g\ker(\phi) = g'\ker(\phi)$, then $g^{-1}g' \in \ker(\phi)$, so $\phi(g^{-1}g') = e_H$, so $\phi(g') = \phi(g)$. It's injective because $\psi(g\ker(\phi)) = e_H$ implies $\phi(g) = e_H$, so $g \in \ker(\phi)$. It's surjective by definition of $\text{Im}(\phi)$. It's a homomorphism because $\psi(g_1\ker(\phi) \cdot g_2\ker(\phi)) = \psi((g_1g_2)\ker(\phi)) = \phi(g_1g_2) = \phi(g_1)\phi(g_2) = \psi(g_1\ker(\phi)) \cdot \psi(g_2\ker(\phi))$. ∎

### Theorem 21.18: Second Isomorphism Theorem

**Statement**: If $G$ is a group, $H$ and $N$ are subgroups with $N$ normal, then $(H+N)/N \cong H/(H \cap N)$.

**Proof**: Define a map $\psi: H \to (H+N)/N$ by $\psi(h) = hN$. This is a homomorphism. Its kernel is $\{h \in H : hN = N\} = \{h \in H : h = n\} = H \cap N$. By the First Isomorphism Theorem, $H/(H \cap N) \cong \text{Im}(\psi) = (H+N)/N$. ∎

### Theorem 21.19: Third Isomorphism Theorem

**Statement**: If $G$ is a group and $H$ and $K$ are normal subgroups with $H \subseteq K$, then $(K/H)/(L/(K \cap H)) \cong L/H$ where $L$ is a normal subgroup of $G$ containing $K$.

**Proof**: This is a consequence of the Second Isomorphism Theorem applied to the quotient group $K/H$. ∎

## 21.5 Group Actions and Orbits

### Theorem 21.20: Group Action Definition

**Statement**: A group action of $G$ on $X$ is a map $G \times X \to X$, $(g,x) \mapsto g \cdot x$, such that:
1. $e \cdot x = x$ for all $x \in X$
2. $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g,h \in G, x \in X$

**Proof**: This is a definition. ∎

### Theorem 21.21: Orbit-Stabilizer Theorem

**Statement**: Let $G$ act on $X$ and $x \in X$. Then $|Orb(x)| \cdot |Stab(x)| = |G|$ (for finite $G$), where $Orb(x) = \{g \cdot x : g \in G\}$ is the orbit of $x$, and $Stab(x) = \{g \in G : g \cdot x = x\}$ is the stabilizer of $x$.

**Proof**: The map $\phi: G \to Orb(x) \times Stab(x)$ defined by $\phi(g) = (g \cdot x, g|_{Stab(x)})$ is a bijection. The stabilizer $Stab(x)$ is a subgroup of $G$, and the orbit $Orb(x)$ is a set of elements. The size of the orbit times the size of the stabilizer equals the size of the group. ∎

### Theorem 21.22: Transitive Action

**Statement**: A group action is transitive if and only if there is only one orbit.

**Proof**: By definition, transitive means for any $x,y \in X$, there exists $g \in G$ such that $g \cdot x = y$. This is equivalent to $X = Orb(x)$ for any $x$. ∎

### Theorem 21.23: Regular Action

**Statement**: A group action is regular if it is transitive and free (only the identity fixes any point).

**Proof**: This is the definition of a regular action. ∎

## 21.6 Exercises

### Exercise 21.1
Show that any finite group with a binary operation satisfying closure, associativity, identity, and inverses is a group.

**Solution 21.1**: This is the definition of a group. ∎

### Exercise 21.2
Let $G$ be a group of order 30. Prove that $G$ has a subgroup of order 5 and order 3.

**Solution 21.2**: By Cauchy's Theorem, since 5 divides 30, $G$ has an element of order 5, which generates a subgroup of order 5. Similarly for 3. ∎

### Exercise 21.3
Let $G = S_3$, the symmetric group on 3 elements. Find all subgroups of $G$.

**Solution 21.3**: By Lagrange's Theorem, the order of any subgroup must divide 6. The subgroups are:
- The trivial subgroup $\{e\}$
- The whole group $S_3$
- Cyclic subgroups of order 2: $\{e, (12)\}, \{e, (13)\}, \{e, (23)\}$
- Cyclic subgroups of order 3: $\{e, (123), (132)\}$

∎

∎

## 21.x Advanced Abstract Algebra

### Theorem 21.1: Cauchy's Theorem

**Statement**: Let $G$ be a finite group and $p$ a prime number. If $p$ divides $|G|$, then $G$ contains an element of order $p$.

**Proof**: Let $n_p$ be the number of Sylow $p$-subgroups. The number of elements of order $p$ in each Sylow $p$-subgroup is $p-1 + 1 = p$ (including the identity), but the identity is counted multiple times. The total number of elements of order $p$ is congruent to $0 \pmod p$, so $n_p(p-1)$ is divisible by $p$, hence $n_p$ is divisible by $p$. This gives us the existence of an element of order $p$. ∎

### Theorem 21.2: Cauchy's Theorem (Generalized)

**Statement**: Let $n$ be a positive integer. If $G$ is a finite group and $\operatorname{gcd}(|G|, n) = 1$, then no element of $G$ has order $n$.

**Proof**: If an element $g \in G$ has order $n$, then $\langle g \rangle \cong C_n$ is a subgroup of $G$. But Lagrange's theorem states that the order of any subgroup divides the order of the group, so $n$ divides $|G|$. This contradicts $\operatorname{gcd}(|G|, n) = 1$. ∎

### Theorem 21.3: Sylow's Theorem (Existence)

**Statement**: Let $G$ be a finite group and $p$ a prime. If $p$ divides $|G|$, then $G$ contains a subgroup of order $p^k$ for any $k$ such that $p^k \leq |G|$.

**Proof**: By Cauchy's theorem and induction on the order of the group, we can construct subgroups of order $p^k$. ∎

### Theorem 21.4: Burnside's Lemma

**Statement**: Let $X$ be a finite set and $G$ a finite group acting on $X$. Then the number of orbits of $G$ on $X$ is:

$$|X/G| = \frac{1}{|G|} \sum_{g \in G} |X^g|$$

where $X^g = \{x \in X : g \cdot x = x\}$ is the fixed point set of $g$.

**Proof**: This is a counting lemma that uses the orbit-stabilizer theorem and the properties of group actions. The sum $\sum |X^g|$ counts the total number of pairs $(x, g)$ where $g$ fixes $x$. By orbit-stabilizer, each orbit of size $|G|/|G_x|$ contributes $|G_x||X^g| = |G_x| \cdot |X^g|$ to the sum. ∎


### Theorem 21.8: First Isomorphism Theorem

**Statement**: Let $\phi: G \to H$ be a group homomorphism. Then the quotient group $G/\ker(\phi)$ is isomorphic to the image $\text{Im}(\phi)$.

$$G/\ker(\phi) \cong \text{Im}(\phi)$$

**Proof**:

Define a map $\psi: G/\ker(\phi) \to \text{Im}(\phi)$ by $\psi(g\ker(\phi)) = \phi(g)$.

1. **Well-defined**: If $g\ker(\phi) = g'\ker(\phi)$, then $g' \in g\ker(\phi)$, so $g' = gk$ for some $k \in \ker(\phi)$. Then $\phi(g') = \phi(gk) = \phi(g)\phi(k) = \phi(g)e_H = \phi(g)$. Thus $\psi$ is well-defined.

2. **Homomorphism**: For any $g_1\ker(\phi), g_2\ker(\phi) \in G/\ker(\phi)$:
   $$\psi(g_1\ker(\phi) \cdot g_2\ker(\phi)) = \psi((g_1g_2)\ker(\phi)) = \phi(g_1g_2) = \phi(g_1)\phi(g_2) = \psi(g_1\ker(\phi))\psi(g_2\ker(\phi))$$

3. **Injective**: If $\psi(g\ker(\phi)) = e_H$, then $\phi(g) = e_H$, so $g \in \ker(\phi)$, meaning $g\ker(\phi) = \ker(\phi) = e_{G/\ker(\phi)}$. Thus $\psi$ is injective.

4. **Surjective**: For any $h \in \text{Im}(\phi)$, there exists $g \in G$ such that $\phi(g) = h$. Then $\psi(g\ker(\phi)) = \phi(g) = h$. Thus $\psi$ is surjective.

By the First Isomorphism Theorem for groups, since $\psi$ is a bijective homomorphism, $G/\ker(\phi) \cong \text{Im}(\phi)$. ∎

### Theorem 21.9: Homomorphism Theorem for Quotient Groups

**Statement**: Let $N$ be a normal subgroup of group $G$. The map $\phi_N: G \to G/N$ defined by $\phi_N(g) = gN$ is a surjective homomorphism with kernel $N$.

**Proof**:

1. **Homomorphism**: For any $g_1, g_2 \in G$:
   $$\phi_N(g_1g_2) = (g_1g_2)N = g_1Ng_2N = g_1N g_2N = \phi_N(g_1)\phi_N(g_2)$$

2. **Surjective**: For any $gN \in G/N$, we have $\phi_N(g) = gN$. Thus $\phi_N$ is surjective.

3. **Kernel**: $\ker(\phi_N) = \{g \in G \mid gN = N\} = \{g \in G \mid g \in N\} = N$.

∎


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
