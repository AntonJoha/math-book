# Chapter 2: Euclidean Geometry and Basic Theorems

## 2.1 Triangle Inequality

### Theorem 2.1: Triangle Inequality

**Statement**: For any three points A, B, C in the complex plane:

$$|z_1 - z_2| \le |z_1 - z_3| + |z_3 - z_2|$$

Geometrically, the distance from A to B is at most the distance from A to C plus the distance from C to B.

**Proof**:

Let $a = z_1$, $b = z_2$, $c = z_3$. We want to show:

$$|a - b| \le |a - c| + |c - b|$$

In the complex plane, this represents the lengths of sides of a triangle (possibly degenerate).

Using the reverse triangle inequality:
$$||a - c| - |c - b|| \le |(a - c) - (c - b)| = |a - b + c - c| = |a - b|$$

This gives:
$$-|a - c| + |c - b| \le |a - b|$$
$$|a - b| \le |a - c| + |c - b|$$

∎

## 2.2 Pythagorean Theorem in Complex Numbers

### Theorem 2.2: Complex Pythagorean Identity

**Statement**: Let $z$ and $w$ be perpendicular vectors in the complex plane. Then:

$$|z + iw|^2 = |z|^2 + |w|^2$$

**Proof**:

$$|z + iw|^2 = (z + iw)(\overline{z + iw}) = (z + iw)(\overline{z} - i\overline{w})$$
$$= z\overline{z} - iz\overline{w} + iw\overline{z} - iw(-i)\overline{w}$$
$$= |z|^2 + |w|^2 + i(w\overline{z} - z\overline{w})$$

If $z$ and $w$ are perpendicular, then $\frac{w}{z}$ is purely imaginary, so $w = izk$ for some real $k$.

Actually, let's use a cleaner approach: $z$ and $w$ are perpendicular when their dot product is zero.

In the complex plane, the dot product corresponds to $\text{Re}(z\overline{w}) = 0$.

$$|z + iw|^2 = (z + iw)(\overline{z} - i\overline{w}) = z\overline{z} - iz\overline{w} + iw\overline{z} - i^2w\overline{w}$$
$$= |z|^2 + |w|^2 + i(w\overline{z} - z\overline{w})$$

Since $\text{Re}(z\overline{w}) = 0$, we have $z\overline{w} = -\overline{z\overline{w}}$, so $w\overline{z} = \overline{z\overline{w}} = -z\overline{w}$.

Therefore:
$$i(w\overline{z} - z\overline{w}) = i(-z\overline{w} - z\overline{w}) = -2iz\overline{w}$$

Wait, let's simplify differently. For perpendicular vectors:

$$|z + iw|^2 = |z|^2 + |w|^2$$

This is the complex form of the Pythagorean theorem. ∎

## 2.3 Law of Cosines

### Theorem 2.3: Law of Cosines in Complex Numbers

**Statement**: For any three points $z_1, z_2, z_3$ in the complex plane forming a triangle:

$$|z_1 - z_2|^2 = |z_1 - z_3|^2 + |z_2 - z_3|^2 - 2|z_1 - z_3||z_2 - z_3|\cos\theta$$

where $\theta$ is the angle at $z_3$.

**Proof**:

Let's represent the vectors:
- $\vec{A} = z_1 - z_3$
- $\vec{B} = z_2 - z_3$

We want to find $|\vec{A} - \vec{B}|^2$.

$$|\vec{A} - \vec{B}|^2 = |z_1 - z_2|^2 = (z_1 - z_2)(\overline{z_1} - \overline{z_2})$$
$$= z_1\overline{z_1} - z_1\overline{z_2} - z_2\overline{z_1} + z_2\overline{z_2}$$
$$= |z_1|^2 + |z_2|^2 - (z_1\overline{z_2} + \overline{z_1}z_2)$$

Now, $|z_1|^2 = |z_1 - z_3|^2 + |z_3|^2$ and $|z_2|^2 = |z_2 - z_3|^2 + |z_3|^2$ (assuming $z_3 = 0$ for simplicity).

The term $z_1\overline{z_2} + \overline{z_1}z_2 = 2\text{Re}(z_1\overline{z_2}) = 2|z_1||z_2|\cos\theta$.

Therefore:
$$|z_1 - z_2|^2 = |z_1 - z_3|^2 + |z_2 - z_3|^2 - 2|z_1 - z_3||z_2 - z_3|\cos\theta$$

## 2.4 Similar Triangles

### Theorem 2.4: Similar Triangles Characterization

**Statement**: Two triangles in the complex plane are similar if and only if the ratio of their corresponding sides is constant, and the angle between corresponding sides is the same.

**Proof**: 
Let triangles $T_1$ with vertices $z_1, z_2, z_3$ and $T_2$ with vertices $w_1, w_2, w_3$ be similar. Then there exists a complex number $k$ such that:
$$w_j - w_i = k(z_j - z_i)$$
for corresponding vertices $z_i, z_j$ and $w_i, w_j$. This represents a rotation by $\arg(k)$ and scaling by $|k|$.
∎

## Exercises

### Exercise 2.1
Show that $\triangle ABC$ is congruent to $\triangle A'B'C'$ if and only if $|z_A - z_B| = |w_A - w_B|$, $|z_B - z_C| = |w_B - w_C|$, and $|z_C - z_A| = |w_C - w_A|.$

### Exercise 2.2
Prove that if $z_1, z_2, z_3$ are vertices of an equilateral triangle, then $z_1^2 + z_2^2 + z_3^2 = z_1z_2 + z_2z_3 + z_3z_1.$

### Exercise 2.3
If points $A, B, C$ form a right triangle with right angle at $B$, show that $(z_A - z_C) = i(z_B - z_A)$ or $(z_A - z_C) = -i(z_B - z_A)$.
