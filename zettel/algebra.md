---
title: Algebra
type: definition
resources:
  - title: Algebra (Mengensystem)
    url: https://de.wikipedia.org/wiki/Algebra_(Mengensystem)
    type: wikipedia
---

Sei $\Omega$ eine beliebige Menge und $\mathcal{P}$  die [[potenzmenge|Potenzmenge]] dieser Menge.
Ein nichtleeres [[mengensystem|Mengensystem]] $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ heißt *Algebra über $\Omega$*, wenn folgende Eigenschaften gelten:

1. *Vereinigungsstabilität*:

   $$
   A, B \in \mathcal{A} \implies A \cup B \in \mathcal{A}
  $$

2. *Komplementstabilität*:
   
   $$
   A \in \mathcal{A} \implies A^C \in \mathcal{A}
  $$
  
3. Aus der Vereinigungs- und Komplementstabilität folgt direkt:
  
   $$
   \Omega \in \mathcal{A} \iff \emptyset \in \mathcal{A}
  $$

Es gilt weiterhin:
- Für jede beliebige Grundmenge $\Omega$ ist $\{\emptyset, \Omega\}$ die kleinste und die [[potenzmenge|Potenzmenge]] $\mathcal{P}(\Omega)$ die größte mögliche Mengenalgebra.
- Jede [[sigma-algebra|$\sigma$-Algebra]] ist eine Mengenalgebra.