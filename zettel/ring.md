---
title: Ring
type: definition
resources:
  - title: Ring (Mengensystem)
    url: https://de.wikipedia.org/wiki/Ring_(Mengensystem)
    type: wikipedia
---

# Mengensysteme

Sei $\Omega$ eine beliebige Menge und $\mathcal{P}$  die [[potenzmenge|Potenzmenge]] dieser Menge.
Ein nichtleeres [[mengensystem|Mengensystem]] $\mathcal{R} \subseteq \mathcal{P}(\Omega)$ heißt *Ring über $\Omega$*, wenn folgende Eigenschaften gelten:
1. *Vereinigungsstabilität*:

   $$
   A, B \in \mathcal{R} \implies A \cup B \in \mathcal{R}
  $$

2. *Differenzstabilität*:
   
   $$
   A, B \in \mathcal{R} \implies A \cap B^C \in \mathcal{R} \iff A \setminus B \in \mathcal{R}
  $$
  
3. Aus der Differenzstabilität folgt direkt die *Existenz des Nullelements*:

   $$
   A \in \mathcal{R} \implies A \setminus A = \emptyset \in \mathcal{R}
  $$

# Algebra