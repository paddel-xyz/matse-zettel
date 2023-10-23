---
title: Rieman-Integral
type: definition
---

Ein *Rieman-Integral* ist für eine beschränkte Funktion $f : [a, b] \to \mathbb{R}$ definiert als Grenzwert der entsprechenden [[untersumme|Unter-]] bzw. [[obersumme|Obersumme]], falls beide existieren und identisch sind.

Der Grenzwert von den Unter- $U(p_n, f)$ bzw. Obersummen $O(p_n, f)$ ist dann definiert, falls für eine [[zerlegung|Zerlegung]] $p_n$ die [[feinheit|Feinheit]] $h$ sich dem Wert $0$ annähert..
Man schreibt:

$$
	\int_a^b f(x) \mathrm{d}x := \lim_{h(p_n) \to 0} U(p_n, f) = \lim_{h(p_n) \to 0} O(p_n, f)
$$