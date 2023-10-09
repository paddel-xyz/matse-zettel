---
title: Lernproblem
type: definition
---

```tikz
\begin{document}
	\begin{tikzpicture}
	[myBox/.style={rectangle,
	            draw,
	            align=center,
	            inner sep=2.5mm}]
	
	\node[myBox, fill=blue!20] (unknownTargetFunction) at (-4, 4) {Unbekannte Target Function\\$f: \mathcal{X} \rightarrow \mathcal{Y}$};
	\node[myBox, fill=blue!20] (trainingExamples) at (-4, 2) {Trainingsdaten\\$\mathcal{D} = (\mathbf{x}_1,y_1),...,(\mathbf{x}_n,y_n)$};
	\node[myBox, fill=blue!20] (learningAlgorithm) at ( 0, 0) {Lernalgorithmus\\$\mathcal{A}$};
	\node[myBox, fill=blue!20] (finalHypothesis) at ( 5, 0) {Finale Hypothese\\$g \approx f$};
	\node[myBox, fill=blue!20] (hypothesisSet) at (-4,-2) {Hypothesenset\\$\mathcal{H}$};
	
	\node[myBox, fill=red!20] (probabilityDistribution) at (5,4) {Unbekannte\\Wahrscheinlichkeitsverteilung\\$P(\mathbf{x})$};
	
	\node[red] (x) at (2, 2) {$\mathbf{x}_1, \ldots, \mathbf{x}_N$};
	
	\draw [->] (unknownTargetFunction) to (trainingExamples);
	\draw [->] (trainingExamples) to [bend right] (learningAlgorithm.170);
	\draw [->] (hypothesisSet) to [bend left] (learningAlgorithm.190);
	\draw [->] (learningAlgorithm) to (finalHypothesis);
	
	\draw [->, red] (probabilityDistribution) to [bend left] (x.east);
	\draw [->, red] (x) to (trainingExamples);
	\draw [->, red] (probabilityDistribution) to node [midway, right] {$\mathbf{x}$} (finalHypothesis) ;
	
	%\node[draw,dashed,red,inner sep=2mm,label={[text=red]below:Lernmodell},fit=(learningAlgorithm) (hypothesisSet)] {};
	\end{tikzpicture}
\end{document}
```