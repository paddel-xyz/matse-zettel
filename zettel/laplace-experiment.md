---
title: Laplace-Experiment
type: definition
---

Es gibt eine Reihe von [[zufallsexperiment|Zufallsexperimenten]], bei denen keines der [[ereignis|Elementarereignisse]] gegenüber einem anderen bevorzugt ist, d.h. bei ausreichend häufiger Wiederholung des Experimentes tritt jedes Elementarereignis mit nahezu gleicher Häufigkeit auf.
Ein derartiges Experiment bezeichnen wir als *Laplace-Experiment*.

Einem Elementarereignis $\omega_i$ aus einer [[ergebnismenge|Ergebnismenge]] $\Omega$ mit $m$ möglichen Elementarereignissen wird definitionsgemäß die positive Zahl
$$
	P(\{ \omega_i \}) = p(\omega_i) = \frac{1}{m} = \frac{1}{|\Omega|}
$$
als Wahrscheinlichkeit zugeordnet. 

Damit gilt für ein Ereignis $A$ direkt:
$$
	P(A) = \sum_{\omega_i \in A} P(\{ \omega_i \}) = p(\omega_i) = \frac{|A|}{m} = \frac{|A|}{|\Omega|}
$$

Das gilt allerdings nur, wenn:
- Die Ergebnismenge $\Omega$ endlich ist.
- Alle Elementarereignisse gleichwahrscheinlich sind.