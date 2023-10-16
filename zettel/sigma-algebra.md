---
title: $\sigma$-Algebra
type: definition
resources:
  - title: $\sigma$-Algebra
    url: https://de.wikipedia.org/wiki/%CE%A3-Algebra
    type: wikipedia
---

Sei $\Omega$ eine beliebige Menge und $\mathcal{P}$  die [[potenzmenge|Potenzmenge]] dieser Menge.
Ein nichtleeres [[mengensystem|Mengensystem]] $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ heißt *$\sigma$-Algebra über $\Omega$*, wenn folgende Eigenschaften gelten:
1. $\mathcal{A}$ enthält die Grundmenge: 
   
   $$
   \Omega \in \mathcal{A}
   $$
   
2. *Komplementstabilität*:
   
   $$
   A \in \mathcal{A} \implies A^C \in \mathcal{A}
  $$
  
3. *Vereinigungsstabilität* bezüglich *abzählbarer Vereinigungen*:
   
   $$
   A_1, A_2, \dots \in \mathcal{A} \implies \bigcup_{n \in \mathbb{N}} A_n \in \mathcal{A}
   $$

Es gilt weiterhin:
- Für jede beliebige Menge $\Omega$ ist $\mathcal{A} = \{\emptyset, \Omega\}$ die kleinstmögliche (triviale) $\sigma$-Algebra.
- Die Potenzmenge $\mathcal{A} = \mathcal{P}(\Omega)$ ist die größtmögliche $\sigma$-Algebra mit $\Omega$ als Grundmenge.
- Für jede beliebige Menge $\Omega$ und eine Teilmenge $A \subseteq \Omega$ ist $\mathcal{A} = \{ \emptyset, A, A^C, \Omega \}$ die kleinste $\sigma$-Algebra, die $A$ enthält.