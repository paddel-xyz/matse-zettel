---
title: Permutation
type: definition
---

Eine Anordnung von $n$ verschiedenen Elementen in einer bestimmten Reihenfolge heißt eine *Permutation* der $n$ Elemente.

Für eine $n$-elementige Menge gilt für die Anzahl $P$ der Permutationen:
$$
    P(n) = n \cdot (n-1) \cdot (n-1) \cdot \ldots \cdot 1 = n!
$$

Befinden sich unter den $n$ Elementen jeweils $n_1, n_2, \ldots, n_k$ gleiche, dann gilt:
$$
    P(n ; n_1 ; n_2 ; \ldots, n_k) = \frac{n!}{n_1! \cdot n_2! \cdot \ldots \cdot n_k} \quad \text{mit} \quad \sum_{i=1}^{k} n_i = n \quad (k \leq n)
$$