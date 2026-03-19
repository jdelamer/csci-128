\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cslab}[2026/01/01 CSCI 128 Lab Handout Class]

% =============================================================
% Base class
% =============================================================
\LoadClass[11pt,letterpaper]{article}

% =============================================================
% Required packages
% =============================================================
\RequirePackage[margin=1in]{geometry}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\RequirePackage{hyperref}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage[most]{tcolorbox}
\RequirePackage{microtype}
\RequirePackage{parskip}

% =============================================================
% Colour palette  (matching csbeamer.cls)
% =============================================================
\definecolor{stfxblue}{HTML}{001b40}
\definecolor{skyblue}{HTML}{425f8e}
\definecolor{skylight}{HTML}{5e739e}
\definecolor{marigold}{HTML}{d5a845}

% Tinted backgrounds for boxes
\definecolor{objblue}{HTML}{dce8f5}
\definecolor{gradgreen}{HTML}{d6f0e0}
\definecolor{setuporange}{HTML}{fde8cc}
\definecolor{noteyellow}{HTML}{fdf6cc}
\definecolor{hintpurple}{HTML}{ede0f5}
\definecolor{warningred}{HTML}{fde0d6}

% =============================================================
% Metadata commands
% =============================================================
\newcommand{\setlabnumber}{}
\newcommand{\labnumber}[1]{\renewcommand{\setlabnumber}{#1}}

\newcommand{\setlabtitle}{}
\newcommand{\labtitle}[1]{\renewcommand{\setlabtitle}{#1}}

\newcommand{\setcourse}{}
\newcommand{\course}[1]{\renewcommand{\setcourse}{#1}}

\newcommand{\setcourseshort}{}
\newcommand{\courseshort}[1]{\renewcommand{\setcourseshort}{#1}}

\newcommand{\setsemester}{}
\newcommand{\semester}[1]{\renewcommand{\setsemester}{#1}}

\newcommand{\settimelimit}{}
\newcommand{\timelimit}[1]{\renewcommand{\settimelimit}{#1}}

\newcommand{\setlogoimage}{}
\newcommand{\logoimage}[1]{\renewcommand{\setlogoimage}{#1}}

% =============================================================
% Header / footer
% =============================================================
\pagestyle{fancy}
\fancyhf{}

% Left header: course short name
\lhead{\small\color{stfxblue}\textbf{\setcourseshort}}
% Right header: Lab XX — Title
\rhead{\small\color{stfxblue}Lab \setlabnumber{} --- \setlabtitle}
% Centre footer: page number
\cfoot{\small\thepage}
% Decorative rule colours
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.2pt}

% Plain pages (first page after \maketitle) also get the footer
\fancypagestyle{plain}{%
    \fancyhf{}%
    \cfoot{\small\thepage}%
    \renewcommand{\headrulewidth}{0pt}%
    \renewcommand{\footrulewidth}{0.2pt}%
}

% =============================================================
% Custom \maketitle
% =============================================================
\renewcommand{\maketitle}{%
    \thispagestyle{plain}%
    \begin{center}
        % Logo
        \ifx\setlogoimage\empty\else
            \includegraphics[width=3.5cm]{\setlogoimage}\\[0.6em]
        \fi
        % Horizontal rule in stfxblue
        {\color{stfxblue}\rule{\linewidth}{2pt}}\\[0.4em]
        % Lab number badge
        {\large\color{skylight}\textbf{Lab \setlabnumber}}\\[0.2em]
        % Title
        {\LARGE\color{stfxblue}\textbf{\setlabtitle}}\\[0.4em]
        % Course
        {\large\color{skyblue}\setcourse}\\[0.2em]
        % Semester and time limit on the same line
        {\normalsize\color{stfxblue}%
            \setsemester
            \ifx\settimelimit\empty\else
                \quad\textbullet\quad Time limit: \settimelimit
            \fi
        }\\[0.4em]
        {\color{stfxblue}\rule{\linewidth}{1pt}}
    \end{center}
    \vspace{0.5em}
}

% =============================================================
% Section / subsection styling
% =============================================================
\titleformat{\section}
    {\large\bfseries\color{stfxblue}}
    {\thesection.}{0.6em}{}
    [\vspace{-0.3em}{\color{marigold}\rule{\linewidth}{1pt}}]

\titleformat{\subsection}
    {\normalsize\bfseries\color{skyblue}}
    {\thesubsection.}{0.5em}{}

% =============================================================
% Task counter and \task command
% =============================================================
\newcounter{taskcounter}

\newcommand{\task}[1]{%
    \stepcounter{taskcounter}%
    \subsection*{%
        \colorbox{stfxblue}{\color{white}\bfseries\small~Task \thetaskcounter~}%
        \quad\normalfont\bfseries\color{stfxblue}#1%
    }%
    \vspace{-0.3em}%
    {\color{marigold}\rule{\linewidth}{0.6pt}}%
    \vspace{0.3em}%
}

% =============================================================
% Coloured box environments  (tcolorbox)
% =============================================================

% --- Learning Objectives (blue) ------------------------------
\newtcolorbox{objectives}{
    enhanced,
    breakable,
    colback=objblue,
    colframe=stfxblue,
    coltitle=white,
    fonttitle=\bfseries,
    title={Learning Objectives},
    leftrule=4pt,
    arc=2pt,
    before upper={\begin{itemize}[leftmargin=1.2em,itemsep=0.2em]},
    after upper={\end{itemize}}
}

% --- Grading (green) -----------------------------------------
\newtcolorbox{grading}{
    enhanced,
    breakable,
    colback=gradgreen,
    colframe=green!50!black,
    coltitle=white,
    fonttitle=\bfseries,
    title={Grading},
    leftrule=4pt,
    arc=2pt
}

% --- Setup (orange) ------------------------------------------
\newtcolorbox{setup}{
    enhanced,
    breakable,
    colback=setuporange,
    colframe=orange!75!black,
    coltitle=white,
    fonttitle=\bfseries,
    title={Setup},
    leftrule=4pt,
    arc=2pt
}

% --- Note (yellow) -------------------------------------------
\newtcolorbox{note}{
    enhanced,
    breakable,
    colback=noteyellow,
    colframe=yellow!60!black,
    coltitle=black,
    fonttitle=\bfseries,
    title={Note},
    leftrule=4pt,
    arc=2pt
}

% --- Hint (purple) -------------------------------------------
\newtcolorbox{hint}{
    enhanced,
    breakable,
    colback=hintpurple,
    colframe=purple!60!black,
    coltitle=white,
    fonttitle=\bfseries,
    title={Hint},
    leftrule=4pt,
    arc=2pt
}

% --- Warning (red) -------------------------------------------
\newtcolorbox{warning}{
    enhanced,
    breakable,
    colback=warningred,
    colframe=red!65!black,
    coltitle=white,
    fonttitle=\bfseries,
    title={Warning},
    leftrule=4pt,
    arc=2pt
}

% =============================================================
% Hyperref colours
% =============================================================
\hypersetup{
    colorlinks=true,
    linkcolor=stfxblue,
    urlcolor=skyblue,
    citecolor=stfxblue
}

% =============================================================
% List spacing (tighter than LaTeX defaults)
% =============================================================
\setlist[itemize]{itemsep=0.15em, parsep=0pt, topsep=0.3em}
\setlist[enumerate]{itemsep=0.15em, parsep=0pt, topsep=0.3em}

\endinput
