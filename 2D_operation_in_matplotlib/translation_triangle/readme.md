

**Theory of Translating a Triangle in Computer Graphics**

**1. What is Translation?**
Translation is a type of geometric transformation that moves every point of a shape or object by the same distance in a given direction. In computer graphics, this is commonly used to reposition objects on the screen.

**2. Translation in 2D Space**
For a 2D object like a triangle, translation involves shifting its vertices in the X and Y directions.

If a point **P(x, y)** is translated by a translation vector **T(tx, ty)**, the new point **P′(x′, y′)** is calculated as:

$$
x' = x + tx  
$$

$$
y' = y + ty
$$

**3. Translating a Triangle**
A triangle has three vertices:
Let the original coordinates be:

* A(x₁, y₁)
* B(x₂, y₂)
* C(x₃, y₃)

After translation by **(tx, ty)**, the new vertices become:

* A′(x₁ + tx, y₁ + ty)
* B′(x₂ + tx, y₂ + ty)
* C′(x₃ + tx, y₃ + ty)

This shifts the entire triangle without altering its shape, size, or orientation.

**4. Homogeneous Coordinates (Optional Advanced Concept)**
In matrix form, translation can be represented using homogeneous coordinates. A 2D point (x, y) becomes (x, y, 1), and the translation is performed using a transformation matrix:

$$
\begin{bmatrix}
1 & 0 & tx \\
0 & 1 & ty \\
0 & 0 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
=
\begin{bmatrix}
x + tx \\
y + ty \\
1
\end{bmatrix}
$$

**5. Applications**
Translation is used in:

* Moving objects in games or simulations
* Creating animations
* Aligning UI elements
* Implementing collision detection and response

