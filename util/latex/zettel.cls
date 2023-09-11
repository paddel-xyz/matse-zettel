\ProvidesClass{zettel}

\LoadClass[a4paper]{article}
\usepackage[ngerman]{babel}

\usepackage{xcolor}
\definecolor{matse}{RGB}{11,102,168}

\usepackage[
    colorlinks,
    linkcolor = matse,
    urlcolor = matse
]{hyperref}

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