---
title: Bedingte Wahrscheinlichkeit
tags: 
  - definition
---

In vielen Anwendungen ist das Eintreten eines [[ereignis|Ereignisses]] $A$ nicht unabhängig davon, ob vorher ein anderes Ereignis $B$ eingetreten ist oder nicht.

Man spricht dann von einer *bedingten Wahrscheinlichkeit* und schreibt $P(A \mid B)$.
Es gilt:
$$
	P(A \mid B) = \frac{P(A \cap B)}{P(B)}
$$

Generell gilt $P(A \mid B) \neq P(B \mid A)$, aber:
$$
	P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B \cap A)}{P(B)} = \frac{P(B \cap A)}{P(A)} \cdot \frac{P(A)}{P(B)}
$$
$$
	\implies P(A \mid B) = P(B \mid A) \cdot \frac{P(A)}{P(B)}
$$

Alle Axiome für eine Wahrscheinlichkeit werden von der bedingten Wahrscheinlichkeit erfüllt.

Damit gilt auch:
- $E_1 \subseteq E_2 \implies P(E_1 \mid B) \leq P(E_2 \mid B)$
- $P(\overline{A} \mid B) = 1 - P(A \mid B)$