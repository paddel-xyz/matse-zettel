---
title: Definition verschiedener Mengensysteme auf Teilmengen
type: bonus
---

Sei $\mathcal{C} \subseteq \mathcal{P}(\Omega)$ eine beliebige Teilmenge, dann ist
- der von $\mathcal{C}$ erzeugte [[ring|Ring]] $R(\mathcal{C})$ definiert als:
   $$
	R(\mathcal{C}) := \bigcap_{\substack{\mathcal{R} \ \text{Ring auf} \ \Omega \\ \mathcal{C} \subseteq \mathcal{R}}} \mathcal{R}
   $$
- die von $\mathcal{C}$ erzeugte [[algebra|Algebra]] $A(\mathcal{C})$ auf $\Omega$ definiert als:
   $$
	A(\mathcal{C}) := \bigcap_{\substack{\mathcal{A} \ \text{Algebra auf} \ \Omega \\ \mathcal{C} \subseteq \mathcal{A}}} \mathcal{A}
   $$
- die von $\mathcal{C}$ erzeugte [[sigma-algebra|$\sigma$-Algebra]] $\sigma(\mathcal{C})$ $\Omega$ definiert als:
   $$
	\sigma(\mathcal{C}) := \bigcap_{\substack{\mathcal{A} \ \sigma\text{-Algebra auf} \ \Omega \\ \mathcal{C} \subseteq \mathcal{A}}} \mathcal{A} 
   $$
- das von $\mathcal{C}$ erzeugte [[dynkin-system|Dynkin-System]] $D(\mathcal{C})$ auf $\Omega$ definiert als:
   $$
	D(\mathcal{C}) := \bigcap_{\substack{\mathcal{D} \ \text{Dynkin-System auf} \ \Omega \\ \mathcal{C} \in \mathcal{A}}} \mathcal{A}
   $$