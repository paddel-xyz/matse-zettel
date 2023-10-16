---
title: Ringe und endlich additive Maße
type: definition
---

Sei $\mathcal{R}$ ein [[ring|Ring]] auf $\Omega$ und $\mu : \mathcal{R} \to \overline{\mathbb{R}}_+$ ein endlich additives [[mass|Maß]].

Dann gelten folgende Eigenschaften:
1. *Isotonie*: $A, B \in \mathcal{R}, A \subseteq B \implies \mu(A) \le p(B)$
2. *Subtraktivität*: $A, B \in \mathcal{R}, A \subseteq B, \mu(A) \lt \infty \implies \mu(B \cap A^C) = \mu(B) - \mu(A)$
3. *Siebformel*: Für $A_1, \dots, A_n \in \mathcal{R}$ mit $\mu(\bigcup_{k=1}^n A_k) \lt \infty$ gilt:
   
   $$
   \mu\left(\bigcup_{k=1}^n A_k\right) = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \le i_1 \lt \cdots \lt i_k \le n} \mu(A_{i_1} \cap \cdots \cap A_{i_k})
   $$
   
4. *Subadditivität*: Für $A_1, \dots, A_n \in \mathcal{R}$ gilt:
   
   $$
   \mu\left(\bigcup_{j=1}^n A_j\right) \le \sum_{j=1}^n \mu(A_j)
   $$
   
5. *Sub-$\sigma$-Additivität*: Ist $\mu$ $\sigma$-additiv, $A_n \in \mathcal{R}$ für $n \in \mathbb{N}$ mit $\bigcup_{n=1}^\infty A_n \in \mathcal{R}$, so gilt:
   
   $$
   \mu\left(\bigcup_{j=1}^\infty A_j\right) \le \sum_{j=1}^\infty \mu(A_j)
   $$
   
6. Sind $A_n \subseteq \mathcal{R}, n \in \mathbb{N}$ paarweise disjunkt, so gilt:
   
   $$
   \sum_{n=1}^\infty A_n \in \mathcal{R} \implies \mu\left(\sum_{n=1}^\infty A_n\right) \ge \sum_{n=1}^\infty \mu(A_n)
   $$