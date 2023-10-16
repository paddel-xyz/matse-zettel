---
title: Konvergenz von Folgen auf Mengen
type: definition
---

Seien $A_n, n \in \mathbb{N}$ Teilmengen von $\Omega$.

Die Folge $(A_n)_{n \in \mathbb{N}}$ heißt *isoton konvergent* gegen $A \subseteq \Omega$, falls $A_n \subseteq A_{n+1}, \forall n \in \mathbb{N}$ und $A = \bigcup_{n \in \mathbb{N}} A_n$.
Man schreibt $A_n \uparrow A$.

Die Folge $(A_n)_{n \in \mathbb{N}}$ heißt *isoton konvergent* gegen $A \subseteq \Omega$, falls $A_{n+1} \subseteq A_n, \forall n \in \mathbb{N}$ und $A = \bigcup_{n \in \mathbb{N}} A_n$.
Man schreibt $A_n \downarrow A$.

Sei $\mathcal{R}$ ein [[ring|Ring]] auf $\Omega$ und $\mu : \mathcal{R} \to \overline{\mathbb{R}}_+$.
Wir betrachten folgende Aussagen:
1. $\mu$ ist $\sigma$-additiv
2. Für $A_n \in \mathcal{R}, n \in \mathbb{N}$ mit $A_n \uparrow A \in \mathcal{R}$ gilt:
   
   $$
    \lim_{n \to \infty} \mu(A_n) = \mu(A)
   $$
   
3.

Es gilt $1. \iff 2. \implies 3. \implies 4.$