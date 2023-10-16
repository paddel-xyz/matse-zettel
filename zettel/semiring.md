---
title: Semiring
type: definition
aliases:
  - Halbring
  - Sesamring
resources:
  - title: Halbring (Mengensystem)
    url: https://de.wikipedia.org/wiki/Halbring_(Mengensystem)
    type: wikipedia
---

# Mengensysteme

Sei $\Omega$ eine beliebige Menge und $\mathcal{P}$  die [[potenzmenge|Potenzmenge]] dieser Menge.
Ein nichtleeres [[mengensystem|Mengensystem]] $\mathcal{H} \subseteq \mathcal{P}(\Omega)$ heißt *Semiring über $\Omega$*, wenn folgende Eigenschaften gelten:
1. *Existenz des Nullelements*:

   $$
   \emptyset \in \mathcal{H}
   $$
   
2. *Durchschnittsstabilität*:

   $$
   A, B \in \mathcal{H} \implies A \cap B \in \mathcal{H}
  $$
  
3. Die *Differenz* zweier Mengen $A, B \in \mathcal{H}$ lässt sich als *endliche Vereinigung von paarweise disjunkten Mengen* aus $\mathcal{H}$ darstellen:
   $$
   \exists C_1, C_2, \dots, C_n \in \mathcal{H}: A \setminus B = \bigcup_{i=1}^{n} C_j = \sum_{i=1}^{n} C_j
  $$