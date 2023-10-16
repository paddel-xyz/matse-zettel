---
title: Limes
type: definition
---

Ist die Indexmenge $I$ gleich der Menge der natürlichen Zahlen $\mathbb{N}$, dann stellt die indizierbare [[menge|Menge]] $(A_n)_{n \in \mathbb{N}}$ eine [[mengenfolge|Mengenfolge]] dar.
Folgende Größen lassen sich definieren:
1. *limes inferior*:
   
   $$
   \liminf_{n \to \infty} := \bigcup_{m \in \mathbb{N}} \bigcap_{n \ge m} A_n
   $$
   
2. *limes superior*:
   
   $$
   \limsup_{n \to \infty} := \bigcap_{m \in \mathbb{N}} \bigcup_{n \ge m} A_n
   $$

Sind limes inferior und limes superior einer Mengenfolge identisch, dann sagt man, die Mengenfolge habe einen Grenzwert:

$$
	\lim_{n \to \infty} A_n = A \iff \liminf_{n \to \infty} A_n = A = \limsup_{n \to \infty} A_n
$$

Ferner lassen sich auf Mengenfolgen die von reellen Zahlenfolgen bekannten Monotoniebegriffe entsprechend übertragen:

$$
	A_n \uparrow A \iff A_1 \subseteq A_2 \subseteq \cdots \land \bigcup_{n \in \mathbb{N}} A_n = \lim_{n \to \infty} A_n = A
$$

$$
	A_n \downarrow A \iff \cdots \subseteq A_2 \subseteq A_1 \land \bigcap_{n \in \mathbb{N}} A_n = \lim_{n \to \infty} A_n = A
$$