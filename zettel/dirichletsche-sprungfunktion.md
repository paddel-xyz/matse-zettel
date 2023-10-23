---
title: Dirichletsche Sprungfunktion
type: definition
---

Die *Dirichletsche Sprungfunktion* $D : [0, 1] \to \{ 0, 1 \}$ ist definiert als:

$$
	D(x) = \begin{cases}
		1 & x \in [0, 1] \cap \mathbb{Q} \\
		0 & \text{sonst}
	\end{cases}
$$

```tikz
\begin{document}
\begin{tikzpicture}[domain=0:5]

  %\draw[very thin,color=gray] (0,-1) grid (5,2);

  \draw[->] (0,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,2) node[above] {$D(x)$};

  \draw[color=red] (0,1) -- (4,1);
  \draw[color=blue] (0,0) -- (4,0);
  
  \draw (0,1) node[left] {$1$};
  \draw (0,0) node[below left] {$0$};
  \draw (1,0) node[below] {$\frac{1}{4}$};
  \draw (2,0) node[below] {$\frac{1}{2}$};
  \draw (3,0) node[below] {$\frac{3}{4}$};
  \draw (4,0) node[below] {$1$};

  \fill (1,1) circle (.1) node[above] {$D(\frac{1}{4}) = 1$};
  \fill (pi,0) circle (.1) node[above] {$D(\frac{\pi}{4}) = 0$};
  
\end{tikzpicture}
\end{document}
```

Um zu versuchen das Integral $\int_{i = 0}^1 f(x)$ über die Funktion $f$ zu berechnen, verwenden wir das [[dirac-mass|Dirac Maß]] $I$.

Sei $(a_n)_{n \in \mathbb{N}} = [0, 1] \cap \mathbb{Q}$ eine Aufzählung aller rationalen Zahlen des Einheitsintervalls.
Die Aufzählung $f_n(x) := I_{\{ a_1, \cdots, a_n \}}(x)$ konvergiert offensichtlich punktweise gegen $f$.
Alle $f_n$ sind Riemann-integrierbar und es gilt für alle $n \in N$:

$$
	\int_0^1 f_n(x) \mathrm{d}x = 0
$$

$f_n$ nimmt nur in $n$ Stellen einen von $0$ verschiedenen Wert an, so dass für eine gegebene Zerlegung $p_m$ auch nur $o_{j(i, m)} \ne 0$ für $i = 1, \cdots, n$ mit $j(i. m)$ als Indizes der Mengen in der Zerlegung $p_m$, in denen die $i$-te "Eins-Stelle" von $f$ liegt.
Es folgt:

$$
	0 \le O(p_m, f_n) \le \sum_{i=1}^m o_{j(i, m)} h(p_n) = m \cdot h(p_n)
$$

und deswegen $\lim_{h \to 0} O(p_m, f_n) = 0$.

Der Grenzwert der Funktionenfolge $f_n$, also die Dirichletsche Sprungfunktion $D$ bzw. $f$, ist nicht Rieman-integrierbar, da jedes $p_m$ rationale sowie irrationale Zahlen enthält und somit:
1. Die Obersumme $O(p_n, f) = 1$
2. Die Untersumme $U(p_n, f) = 0$