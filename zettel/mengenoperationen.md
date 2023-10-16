---
title: Mengenoperationen
type: bonus
---

Seien $A, B \in \mathcal{P}(X)$ beliebige Teilmengen einer Menge $X$ und $(A_i)_{i \in \mathcal{I}}$ ein indiziertes Mengensystem.
Folgende Operationen sind definiert:
1. *Disjunktion* (Vereinigung)
   
   $$
   A \cup B:= \{ x \in X \mid x \in A \lor x \in B \}
   $$
   
   $$
   \bigcup_{i \in I} A_i := \{ x \in X \mid \exists i \in I : x \in A_i \}
   $$
   
2. *Konjunktion* (Schnitt)
   
   $$
   A \cap B := \{ x \in X \mid x \in A \land x \in B \}
   $$
   
   $$
   \bigcap_{i \in I} A_i := \{ x \in X \mid \forall i \in I : x \in A_i \}
   $$
   
4. *Differenz*
   
   $$
   A \setminus B := \{ x \in A \mid x \notin B \}
   $$
   
1. *Kartesisches Produkt*
   
   $$
   A \times B := \{ (a, b) \mid a \in A, b \in B \}
   $$
   
3. *Komplement*
   
   $$
   A^C = \{ x \in X \mid x \notin A \}
   $$