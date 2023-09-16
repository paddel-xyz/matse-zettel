---
title: Variation
type: definition
tags: 
  - bachelor
  - definition
  - stochastik
author:
  - Blaneck, Patrick Gustav
---

Eine *Variation* oder geordnete Stichprobe ist eine Auswahl von $k$ Objekten aus einer Menge von $n$ Objekten, wobei die Reihenfolge der Auswahl eine Rolle spielt.

Bei einer *Variation ohne Wiederholung* sollen $k$ Objekten (mit $k \leq n$) auf $k$ verfügbare Plätze platziert werden, wobei jedes Objekt nur höchstens einen Platz einnehmen darf.
Es gibt für den ersten Platz $n$ mögliche Objekte, für den zweiten Platz $n - 1$ Objekte usw. bis zum $k$-ten Platz, für den es noch $n - k + 1$ mögliche Objekte gibt.
Insgesamt gilt also:
$$
    V(n;k) = k! \cdot C(n;k) = \frac{n!}{(n-k)!}
$$

Bei einer *Variation mit Wiederholung* werden aus $n$ Objekten $k$ Objekte unter Beachtung der Reihenfolge ausgewählt, wobei Objekte auch mehrfach ausgewählt werden können.
Nachdem jedes der $n$ Objekte auf jedem der $k$ Plätze der Auswahl erscheinen kann, gilt demzufolge:
$$
    V_W(n;k) = n^k
$$
