---
title: Dynkin-System
type: definition
---

Sei $\Omega$ eine beliebige Menge und $\mathcal{P}$  die [[potenzmenge|Potenzmenge]] dieser Menge.
Ein nichtleeres [[mengensystem|Mengensystem]] $\mathcal{D} \subseteq \mathcal{P}(\Omega)$ heißt *Dynkin-System über $\Omega$*, wenn folgende Eigenschaften gelten:
1. $\mathcal{D}$ enthält die Grundmenge: 
   
   $$
   \Omega \in \mathcal{D}
   $$
   
2. *Komplementstabilität*:
   
   $$
   A \in \mathcal{D} \implies A^C \in \mathcal{D}
  $$
  
3. *Vereinigungsstabilität* bezüglich *abzählbarer Vereinigungen* *paarweise [[disjunktion|disjunkter]] Mengen* ($\forall i, j \in \mathbb{N}: A_i \cap A_j = \emptyset$):
   
   $$
   A_1, A_2, \dots \in \mathcal{D} \implies \bigcup_{n \in \mathbb{N}} A_n \in \mathcal{D} \iff \sum_{n \in \mathbb{N}} A_n \in \mathcal{D}
   $$

Es gilt weiterhin:
- Jede [[sigma-algebra|$\sigma$-Algebra]] ist immer auch ein Dynkin-System. 
- Umgekehrt ist jedes durchschnittsstabile Dynkin-System auch eine σ-Algebra.