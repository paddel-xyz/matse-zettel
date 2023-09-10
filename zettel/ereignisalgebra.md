---
title: Ereignisalgebra
tags: 
  - definition
---

Es sei $\Omega$ eine nicht-leere Menge.
Eine *Ereignisalgebra* über $\Omega$ ist eine nicht-leere Menge $S$ von Teilmengen von $\Omega$, für die gilt:
- Für jedes $E \in S$ ist $\overline{E} \in S$.
- Für jede Folge $E_1, E_2, \ldots \in S$ ist $\bigcup_{E_i \in \Omega} E_i \in S$.

Folgerungen:
- Für jede Folge $E_1, E_2, \ldots \in S$ ist $\bigcap_{E_i \in \Omega} E_i \in S$.
- $\emptyset \in S$ und $\Omega \in S$.
- Für jede nicht-leere Menge $\Omega$ ist die [[potenzmenge|Potenzmenge]] $\mathcal{P}(\Omega)$ eine Ereignisalgebra über $\Omega$.

Ist $\Omega$ endlich oder abzählbar unendlich, wählt man als Ereignisalgebra stets die Potenzmenge.