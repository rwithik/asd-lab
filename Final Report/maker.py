from pprint import pprint

aims = [
    # "Install POSTGRESQL on my system, and do the inital configuration like creating the postgres user, setting up the database, etc",
    # "Familiarize oneself with SQL. Learn about its history and how it works.",
    "To study some basic SQL queries like, SELECT, INSERT, UPDATE, DELETE, and the WHERE clause.",
    "To study some more basic SQL queries like, SELECT DISTINCT, IN, ALTER TABLE, etc.",
    "To study aggregate function: SUM, COUNT, AVG, MAX, MIN.",
    "To study about various data constraints and views in SQL.",
    "To study string functions like, UPPER, LOWER, REVERSE, LPAD, LTRIM, RPAD, RTRIM, and the LIKE keyword.",
    "To study joins, set operations, nested queries, and grouping using the GROUP BY keyword.",
    "To study the basic PLpg/SQL and SEQUENCE queries.",
    "To study the use of CURSOR in PLpg/SQL",
    "To study PLpg/SQL triggers and exception handling.",
    "To study the implementation of functions, procedures and packages in PLpg/SQL"
]

titles = [
    # "Installation of POSTGRESQL",
    # "Instroduction to SQL",
    "Basic SQL Queries I",
    "Basic SQL Queries II",
    "Aggregate Functions",
    "Data Constraints and Views",
    "String Functions and Pattern Matching",
    "Join Statements, Set Operations, Nested Queries and Grouping",
    "PL/SQL and Sequence",
    "Cursors",
    "Triggers and Exception Handling",
    "Procedure, Functions and Packages"
]

files = [
    # "../Reports/53_Rwithik_Manoj_Installation.tex",
    # "../Reports/53_Rwithik_Manoj_Introduction_To_Sql.tex",
    "../Reports/53_Rwithik_Manoj_Basic_Sql_Queries_I.tex",
    "../Reports/53_Rwithik_Manoj_Basic_Sql_Queries_II.tex",
    "../Reports/53_Rwithik_Manoj_Aggregate_Functions.tex",
    "../Reports/53_Rwithik_Manoj_Constraints_And_Views.tex",
    "../Reports/53_Rwithik_Manoj_Strings.tex",
    "../Reports/53_Rwithik_Manoj_Joins_and_Set_Ops.tex",
    "../Reports/53_Rwithik_Manoj_PLSQL.tex",
    "../Reports/53_Rwithik_Manoj_Cursors.tex",
    "../Reports/53_Rwithik_Manoj_Triggers.tex",
    "../Reports/53_Rwithik_Manoj_Functions.tex"
]

preamble = r'''
\documentclass[10pt,a4paper,titlepage]{report}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{minted}
\usepackage[hidelinks]{hyperref}

\newcommand{\HRule}[1]{\rule{\linewidth}{#1}}
\renewcommand{\chaptername}{Experiment}

\nonstopmode


\begin{document}
{\fontfamily{cmr}\selectfont
\title{ \normalsize \textsc{}
\\ [2.0cm]
\HRule{0.5pt} \\
\LARGE \textbf{\uppercase{Application Software Development Lab Report}
\HRule{2pt} \\ [0.5cm]
\normalsize \today \vspace*{5\baselineskip}}
}

\date{}
\author{
    Rwithik Manoj \\
    College of Engineering, Trivandrum \\
    Department of Computer Science and Engineering }

\maketitle
\tableofcontents
\newpage

\sectionfont{\scshape}
\chapterfont{\scshape}
'''

end_content = '''
    
}
\end{document}
'''

output_file = open("Final_Report.tex", "w")

output_file.write(preamble)

i = 0

for file in files:
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]
        lineno = lines.index("\\sectionfont{\\scshape}")
        if (lineno == -1):
            lineno = lines.index("\\chapterfont{\\scshape}")
        lines = lines[lineno+1:-2]
        print(file)

    # with open(file[11:], "w") as f:
    #     f.write("\\section{{Aim}}\n {0}\n\n".format(aims[i]))
    #     f.write("\\section{{Theory}}\n\n\n\n")
    #     f.write("\\section{{Code and Output}}\n")
    #     # f.write('\n'.join(lines))
    #     for line in lines:
    #         if "includegraphics" in line:
    #             f.write("\\begin{minted}{sql}\n\n\nkjsbbx\n\\end{minted}\n\\newline\n")
    #         f.write(line+"\n")
    #     f.write("\\section{{Result}}\nImplemented the program for {0} using Postgresql 11.5 on Manjaro Linux and the output was obtained.".format(titles[i]))

    output_file.write("\\chapter{{{0}}}\n".format(titles[i]))
    output_file.write('\\input{0}\n'.format("{./" + file[11:] + "}"))
    output_file.write('\\newpage\n\n')

    i += 1

output_file.write(end_content)