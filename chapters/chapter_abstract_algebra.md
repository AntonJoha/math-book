# Abstract Algebra

## 3.1 Groups

### 3.1.1 Definition and Basic Properties

**Definition:** A group is a set $G$ equipped with a binary operation $\cdot$ satisfying:
1. **Closure:** For all $a, b \in G$, $a \cdot b \in G$.
2. **Associativity:** For all $a, b, c \in G$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3. **Identity:** There exists $e \in G$ such that for all $a \in G$, $a \cdot e = e \cdot a = a$.
4. **Inverses:** For each $a \in G$, there exists $a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$.

**Theorem 3.1:** In any group $G$, the identity element is unique.

*Proof:* Suppose $e_1$ and $e_2$ are both identity elements. Then $e_1 = e_1 \cdot e_2 = e_2$. Thus the identity is unique. ∎

**Theorem 3.2:** In any group $G$, the inverse of an element is unique.

*Proof:* Suppose $a^{-1}$ and $b^{-1}$ are both inverses of $a$. Then $a^{-1} = a^{-1} \cdot e = a^{-1} \cdot (a \cdot b^{-1}) = (a^{-1} \cdot a) \cdot b^{-1} = e \cdot b^{-1} = b^{-1}$. Thus the inverse is unique. ∎

### 3.1.2 Finite and Infinite Groups

A group is **finite** if it has a finite number of elements; otherwise it is **infinite**.

**Theorem 3.3 (Cancellation Laws):** In any group $G$, for all $a, b, c \in G$:
1. $ab = ac \implies b = c$ (left cancellation)
2. $ba = ca \implies b = c$ (right cancellation)

*Proof:* 
- For left cancellation: $ab = ac$. Multiply by $a^{-1}$ on the left: $a^{-1}(ab) = a^{-1}(ac)$. By associativity, $(a^{-1}a)b = (a^{-1}a)c$. By the identity property, $eb = ec$. By the identity property, $b = c$.
- For right cancellation: Similar proof by multiplying by $a^{-1}$ on the right. ∎

### 3.1.3 Cyclic Groups

**Definition:** A group $G$ is **cyclic** if there exists $g \in G$ such that every element of $G$ can be written as $g^k$ for some integer $k$. The generator $g$ is called a **generator** of $G$.

**Theorem 3.4:** A finite group $G$ of order $n$ is cyclic if and only if $G$ has a primitive element $g$ such that $g^n = e$ and $g^k \neq e$ for all $1 \leq k < n$.

*Proof:* 
- **Forward direction:** If $G = \langle g \rangle$ and $|G| = n$, then the powers $g, g^2, \dots, g^n$ are all equal to $e$ and no smaller power is equal to $e$. (Cauchy's Theorem on cyclic groups.)
- **Reverse direction:** If $g$ is a primitive element of $G$, then $G = \langle g \rangle$, so $G$ is cyclic. ∎

## 3.2 Subgroups and Lagrange's Theorem

### 3.2.1 Subgroups

**Definition:** A subset $H \subseteq G$ is a **subgroup** if $(H, \cdot)$ is a group under the same operation as $G$.

**Subgroup Test:** A non-empty subset $H \subseteq G$ is a subgroup if and only if for all $a, b \in H$, $ab^{-1} \in H$.

### 3.2.2 Lagrange's Theorem

**Theorem 3.5 (Lagrange's Theorem):** If $G$ is a finite group and $H$ is a subgroup of $G$, then the order of $H$ divides the order of $G$.

*Proof:* Consider the left cosets $gH = \{gh : h \in H\}$ for $g \in G$. These cosets partition $G$ and each coset has the same cardinality as $H$. If $[G:H] = k$ (the number of cosets), then $|G| = k|H|$. Thus $|H|$ divides $|G|$. ∎

### 3.2.3 Examples

**Example 3.6:** The cyclic group $C_n = \mathbb{Z}/n\mathbb{Z}$ under addition modulo $n$.
- Order: $n$
- Subgroups: For each divisor $d$ of $n$, there is exactly one subgroup of order $d$.

## 3.3 Homomorphisms and Quotient Groups

### 3.3.1 Homomorphisms

**Definition:** A function $\phi: G \to H$ between groups is a **homomorphism** if for all $a, b \in G$, $\phi(ab) = \phi(a)\phi(b)$.

**Theorem 3.7:** If $\phi: G \to H$ is a homomorphism, then $\phi(e_G) = e_H$ and $\phi(a^{-1}) = (\phi(a))^{-1}$ for all $a \in G$.

*Proof:* 
- $\phi(e_G) = \phi(e_G \cdot e_G) = \phi(e_G)\phi(e_G)$. Multiply by $\phi(e_G)^{-1}$ to get $\phi(e_G) = e_H$.
- $\phi(a^{-1}) = \phi(a^{-1} \cdot a) = \phi(a^{-1})\phi(a) = e_H$, so $\phi(a^{-1}) = (\phi(a))^{-1}$. ∎

### 3.3.2 Kernel and Image

**Definition:** For a homomorphism $\phi: G \to H$:
- The **kernel** is $\ker(\phi) = \{a \in G : \phi(a) = e_H\}$
- The **image** is $\text{im}(\phi) = \{\phi(a) : a \in G\} \subseteq H$

**Theorem 3.8 (Fundamental Homomorphism Theorem):** For any homomorphism $\phi: G \to H$, $\phi(G)$ is a subgroup of $H$, and $G/\ker(\phi)$ is isomorphic to $\phi(G)$.

*Proof sketch:* Define $\psi: G/\ker(\phi) \to \phi(G)$ by $\psi(a\ker(\phi)) = \phi(a)$. This is well-defined and bijective. For any $a, b \in G$, $\psi((a\ker(\phi))(b\ker(\phi))) = \psi((ab)\ker(\phi)) = \phi(ab) = \phi(a)\phi(b) = \psi(a\ker(\phi))\psi(b\ker(\phi))$. Thus $\psi$ is a homomorphism. Since $\psi$ is bijective, $G/\ker(\phi) \cong \phi(G)$. ∎

## 3.4 Group Actions

**Definition:** A group $G$ acts on a set $X$ if there is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, satisfying:
1. $e \cdot x = x$ for all $x \in X$
2. $(gh) \cdot x = g \cdot (h \cdot x)$ for all $g, h \in G, x \in X$

**Orbit-Stabilizer Theorem:** Let $G$ act on $X$, $x \in X$, $G_x = \{g \in G : g \cdot x = x\}$ be the stabilizer of $x$. Then $|G| = |G_x| \cdot |G \cdot x|$, where $G \cdot x$ is the orbit of $x$.

## Exercises

1. Prove that if $G$ is a finite group and $|G| = p^k$ where $p$ is prime and $k \geq 1$, then $G$ has a subgroup of order $p$.
2. Show that if $G$ is a finite group and $|G|$ is even, then $G$ has an element of order 2.
3. Prove that if $G$ is a cyclic group of order $n$, then $G$ has a unique subgroup of order $d$ for each divisor $d$ of $n$.
4. Show that the direct product of two finite groups is finite and its order is the product of their orders.
5. Prove Cauchy's Theorem: If $G$ is a finite group and $p$ is a prime dividing $|G|$, then $G$ has an element of order $p$.


### Lagrange's Theorem

**Theorem:** If $G$ is a finite group of order $n$ and $H$ is a subgroup of $G$, then $|H|$ divides $|G|$.

**Proof:** The index of $H$ in $G$ is $[G:H] = |G|/|H|$. Since the number of distinct left cosets of $H$ in $G$ is finite and each coset has the same cardinality as $H$, the number of cosets must be an integer. Thus $[G:H] \cdot |H| = |G|$, proving that $|H|$ divides $|G|$.

---
*Abstract algebra provides the language for modern mathematics.*
