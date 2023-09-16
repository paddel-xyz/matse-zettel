---
title: Kombination
type: definition
---

Eine *Kombination* oder ungeordnete [[stichprobe|Stichprobe]] ist in der Kombinatorik eine Auswahl von Objekten aus einer gegebenen Grundmenge, die (im Gegensatz zur [[permutation|Permutation]]) nicht alle Objekte der Grundmenge enthalten muss und bei der (im Gegensatz zur Permutation und [[variation|Variation]]) die Reihenfolge unberücksichtigt bleibt.

Darf jedes Objekt nur einmal auftreten, spricht man von einer *Kombination ohne Wiederholung*.

Um alle *Kombinationen $k$-ter Ordnung ohne Wiederholung* zu erhalten, müssen alle [[permutation|Permutationen]] der $n$ Kugeln betrachtet werden, wobei ein Vertauschen der Kugeln auf Plätzen mit demselben Merkmal (wird gezogen ($k$) bzw. wird nicht gezogen ($n-k$)) keine neue Kombination ergibt:
$$
    C(n;k) = P(n;k;n-k) = \frac{n!}{k! \cdot (n-k)!} = \binom{n}{k}
$$

Können Objekte mehrfach ausgewählt werden, so spricht man von einer *Kombination mit Wiederholung*.

Um alle *Kombinationen $k$-ter Ordnung mit Wiederholung* zu erhalten, gilt:
$$
    C_W(n;k) = P(n+k-1;k;n-1) = \frac{(n+k-1)!}{k! \cdot (n-1)!} = \binom{n+k-1}{k}
$$
