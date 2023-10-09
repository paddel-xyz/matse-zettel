---
title: Perzeptron
type: definition
---

Das *Perzeptron* ist ein vereinfachtes künstliches neuronales Netz, das  in der Grundversion (einfaches Perzeptron) aus einem einzelnen künstlichen Neuron mit anpassbaren Gewichtungen $w_1, \ldots, w_d$ und einem Schwellenwert (Bias) besteht.

Sei $\mathbf{w} = \pmatrix{w_1 & \ldots & w_d}^T$ ein Gewichtsvektor und $\mathbf{x} = \pmatrix{x_1 & \ldots & x_d}^T$ ein [[merkmalsvektor|Merkmalsvektor]].

Ziel des Perzeptrons ist es dann, einem [[merkmalsvektor|Merkmalsvektor]] $\mathbf{x}$ einen binären Output $h(\mathbf{x})$ zuzuweisen.

Es gilt die *[[perzeptron-gleichung-herleitung|Perzeptron-Gleichung]]*:
$$
	h(\mathbf{x}) = \operatorname{sgn}(\mathbf{w}^T\mathbf{x}), \ \text{mit} \ w_0 = b, \, x_0 = 1
$$

```tikz
\begin{document}
\usetikzlibrary{chains,shapes.geometric}
\usetikzlibrary{arrows.meta,arrows}
\begin{tikzpicture}[
            init/.style={
                    draw,
                    circle,
                    inner sep=2pt,
                    font=\Huge,
                    join = by -latex
                },
            squa/.style={
                    draw,
                    inner sep=2pt,
                    font=\Large,
                    join = by -latex
                },
            start chain=2,node distance=13mm
        ]
        \node[on chain=2]
        (x2) {$x_2$};
        \node[on chain=2,join=by {Circle[open]}-latex]
        {$w_2$};
        \node[on chain=2,init] (sigma)
        {$\displaystyle\Sigma$};
        \node[on chain=2,squa,label=below:{\parbox{2cm}{\centering \tiny Aktivierungs- \\ funktion}}]
        {$h$};
        \node[on chain=2,label=below:{\tiny Output},join=by -latex]
        {$y$};
        \begin{scope}[start chain=1]
            \node[on chain=1] at (0,1.5cm)
            (x1) {$x_1$};
            \node[on chain=1,join=by {Circle[open]}-latex]
            (w1) {$w_1$};
        \end{scope}
        \begin{scope}[start chain=3]
            \node[on chain=3,label=below:{\tiny Inputs}] at (0,-1.5cm)
            (x3) {$x_3$};
            \node[on chain=3,label=below:{\tiny Gewichte},join=by {Circle[open]}-latex]
            (w3) {$w_3$};
        \end{scope}
        \node[label=above:\parbox{2cm}{\centering {\tiny Bias} \\ $b$}] at (sigma|-w1) (b) {};

        \draw[-latex] (w1) -- (sigma);
        \draw[-latex] (w3) -- (sigma);
        \draw[{Circle[open]}-latex] (b) -- (sigma);

        %\draw[decorate,decoration={brace,mirror}] (x1.north west) -- node[left=10pt] {Inputs} (x3.south west);
    \end{tikzpicture}
\end{document}
```