\ProvidesClass{zettel}

\LoadClass[a4paper]{article}
\usepackage[ngerman]{babel}

% tables

\usepackage{longtable}
\usepackage{booktabs}

\usepackage{xcolor}
\definecolor{matse}{RGB}{11,102,168}
\definecolor{fhmint}{RGB}{0, 177, 172}

\usepackage[
    colorlinks,
    linkcolor = matse,
    urlcolor = matse
]{hyperref}

% titlepage

\renewcommand{\maketitle}{
    \begin{center}
        {
            \Large\bfseries
            \href{https://matse.paddel.xyz/spicker}{https://matse.paddel.xyz/spicker}
            \vspace*{1.5em}
        }

        {
            \Large
            Fachhochschule Aachen
            \vspace*{1.5em}
        }

        {
            \large
            Angewandte Mathematik und Informatik, M. Sc.
            \vspace*{1em}
        }

        {
            \Huge\bfseries
            \@title
        }

        {
            Sommersemester 2017
            \vspace*{1em}
        }

        {
            \large
            \@author
            \vspace*{1em}
        }

        {
            Letzte Änderung: \today
        }
    \end{center}
}

% pandoc

\def\tightlist{}

% environments

\usepackage{tcolorbox}

\newenvironment{definition}[1]{
    \index{#1}
    \label{defi:#1}
    \begin{tcolorbox}[colback=fhmint!5!white, colframe=fhmint!75!black, title={\sffamily Definition: #1}, label=defi:#1]
        }{
    \end{tcolorbox}
}

\newenvironment{exercise}[1]{
    \index{#1}
    \label{defi:#1}
    \begin{tcolorbox}[colback=fhmint!5!white, colframe=fhmint!75!black, title={\sffamily Aufgabe: #1}, label=defi:#1]
        }{
    \end{tcolorbox}
}

\newenvironment{bonus}[1]{
    \index{#1}
    \label{defi:#1}
    \begin{tcolorbox}[colback=fhmint!5!white, colframe=fhmint!75!black, title={\sffamily Bonus: #1}, label=defi:#1]
        }{
    \end{tcolorbox}
}