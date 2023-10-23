---
title: Obersumme
type: definition
---

Für eine gegebene [[zerlegung|Zerlegung]] $p_n$ mit den Werten $x_1, \cdots, x_n \in p_n$ einer Funktion $f$ sei die Obersumme $O(p_n, f), n \in \mathbb{N}$ definiert als

$$
	O(p_n, f) := \sum_{i=1}^n u_i(f) \cdot (x_i - x_{i-1})
$$

mit

$$
	u_i(f) := \sup_{x_{i-1} \le t \le x_i} f(t)
$$