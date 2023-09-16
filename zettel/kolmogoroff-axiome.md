---
title: Kolmogoroff-Axiome
type: definition
---

Es sei $\Omega$ eine [[ergebnismenge|Ergebnismenge]] und $S$ eine [[ereignisalgebra|Ereignisalgebra]] über $\Omega$.

Eine Zuordnungsvorschrift $P: S \to \mathbb{R}$ heißt [[wahrscheinlichkeitsmass|Wahrscheinlichkeitsmaß]], wenn gilt:
- $\forall E \in S: 0 \leq P(E) \leq 1$.
- $P(\Omega) = 1$
- Falls $E_1, E_2, \ldots$ disjunkte Ereignisse sind, gilt
$$
	P \left( \bigcup_{i} E_i \right) = \sum_{i} P(E_i) \quad \text{($\sigma$-Additivität)}
$$

Das Tripel $(\Omega, S, P)$ mit $\Omega$ als Ergebnismenge, $S$ als Ereignisalgebra und $P$ als Wahrscheinlichkeitsmaß bezeichnet man als [[wahrscheinlichkeitsraum|Wahrscheinlichkeitsraum]].