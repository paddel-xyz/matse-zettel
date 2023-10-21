---
title: Mengenerweiterung
type: definition
---

Die reellen Zahlen bilden mit ihrer üblichen Topologie einen lokalkompakten Raum.
Durch geeignetes Erweitern um die Ausdrücke $\infty$ und $-\infty$ entsteht hieraus ein kompakter Raum.
Wir schreiben beispielsweise:

$$
	\overline{\mathbb{R}}_+ := \mathbb{R}_+ \cup \{ \infty \}
$$

$$
	\overline{\mathbb{R}} := \mathbb{R} \cup \{ \infty, -\infty \}
$$

Durch diese Erweiterung müssen neben den üblichen Rechenregeln noch folgende Regeln hinzugefügt werden.
Sei $x \in \mathbb{R}$:

1. *Anordnung*:
   
   $$
   -\infty \lt x \lt \infty
   $$
   
2. *Kommunativgesetz der Addition*:
   
   $$
   x \pm \infty = \pm\infty + x = \pm\infty
   $$
   
3. *erstes Monotoniegesetz der Multiplikation*:
   
   $$
   x \cdot \pm\infty = \pm\infty \cdot x = \begin{cases}
	   \pm\infty & \text{für } x \gt 0 \\
	   0 & \text{für } x = 0 \\
	   \mp\infty & \text{für } x \lt 0
   \end{cases}
   $$
   
4. *zweites Monotoniegesetz der Multiplikationen*:
   
   $$
   (\pm\infty) \cdot (\pm\infty) = \infty
   $$
   
   $$
   (\pm\infty) \cdot (\mp\infty) = -\infty
   $$
   
5. *Division durch $\pm\infty$*:
   
   $$
   \frac{x}{\pm\infty} = 0
   $$

Nicht erlaubt bzw. undefiniert ($n. d.$) sind die Ausdrücke:

$$
	\frac{\pm\infty}{\pm\infty}, \quad \frac{\pm\infty}{\mp\infty}, \quad \infty - \infty
$$