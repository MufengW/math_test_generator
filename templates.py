def generate_latex_document(problems_latex, solutions_latex):
    """
    Combines LaTeX problems and solutions into a two-column LaTeX document.

    Args:
        problems_latex (str): LaTeX-formatted problems.
        solutions_latex (str): LaTeX-formatted solutions.

    Returns:
        str: Full LaTeX document as a string.
    """
    return f"""
\\documentclass[12pt]{{article}}
\\usepackage[margin=1in]{{geometry}}
\\usepackage{{amsmath}}
\\usepackage{{enumitem}}  % For custom enumerate labels
\\usepackage{{multicol}}  % For two-column layout
\\setlength{{\\parindent}}{{0pt}}

\\begin{{document}}

\\section*{{Math Test}}

Solve the following problems:

\\begin{{multicols}}{{2}}
{problems_latex}
\\end{{multicols}}

\\newpage

\\section*{{Solutions}}

Here are the answers:

\\begin{{multicols}}{{2}}
{solutions_latex}
\\end{{multicols}}

\\end{{document}}
"""
