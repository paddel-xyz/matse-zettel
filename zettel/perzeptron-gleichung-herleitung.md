---
title: Herleitung der Perzeptron-Gleichung
type: bonus
---

Sei $b := -\text{Schwellwert}$, so soll gelten:
$$
h(\mathbf{x}) =
\begin{cases}
1, \quad & \text{wenn} \ \displaystyle \sum_{i=1}^d w_i x_i > -b \\
-1, \quad & \text{wenn} \ \displaystyle \sum_{i=1}^d w_i x_i < -b
\end{cases}
$$

Wir formen um und erhalten:
$$
\sum_{i=1}^d w_i x_i > -b
$$

$$
\sum_{i=1}^d w_i x_i + 1 \cdot b > 0
$$

Vereinfachen wir die Notation, indem wir $b$ in $w$ einbauen.
$$
w = \pmatrix{b & w_1 & \dots & w_N}^T
$$

$$
x = \pmatrix{1 & x_1 & \dots & x_N}^T
$$

So gilt:
$$
\sum_{i=1}^d w_i x_i + x_0 \cdot w_0 > 0
$$

$$
\sum_{i=0}^d w_i x_i > 0
$$

$$
\mathbf{w}^T \mathbf{x} > 0
$$

$$
h(\mathbf{x}) = \operatorname{sgn}(\mathbf{w}^T\mathbf{x})
$$