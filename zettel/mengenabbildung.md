---
title: Mengenabbildung
type: definition
aliases:
  - Mengenfunktion
---

Eine *Mengenabbildung* $\mu : \mathcal{C} \to \overline{\mathbb{R}}_+$ ordnet bestimmten Mengen Werte zu.
Dies sind in der Regel nicht-negative reele Zahlen oder der Wert $\infty$.

Eine Abbildung $\mu : \mathcal{C} \to \overline{\mathbb{R}}_+$ heißt *endlich additiv*, falls:
1. $\mu(\emptyset) = 0$
2. für paarweise disjunkte $A_1, \dots, A_n \in \mathcal{C}$ mit $\sum_{i=1}^n A_i \in \mathcal{C}$ gilt:
   
   $$
	\mu\left(\sum_{i=1}^n A_i\right) = \sum_{i=1}^n \mu(A_i)
   $$

Eine Abbildung $\mu : \mathcal{C} \to \overline{\mathbb{R}}_+$ heißt *$\sigma$-Additiv*, falls:
1. $\mu(\emptyset) = 0$
2. für paarweise disjunkte $A_i \in \mathcal{C}, i \in \mathbb{N}$
   
   $$
	\mu\left(\sum_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i)
   $$