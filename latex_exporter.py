import random
class LatexExporter:
    """
    Exports problems and solutions into LaTeX format.
    """
    latex_problem_template = "\\begin{{enumerate}}[label=\\arabic*.]\n{items}\n\\end{{enumerate}}"
    latex_solution_template = "\\begin{{enumerate}}[label=\\arabic*.]\n{items}\n\\end{{enumerate}}"

    @staticmethod
    def generate_latex(test_generator, shuffle=False):
        """
        Generates LaTeX-formatted problems and solutions.

        Args:
            test_generator (MathTestGenerator): The test generator containing problems and solutions.
            shuffle (bool): Whether to shuffle the problems (and map corresponding solutions).

        Returns:
            tuple: (problems_latex, solutions_latex)
        """
        problems = test_generator.problems
        solutions = test_generator.solutions

        if shuffle:
            # Shuffle problems and map corresponding solutions
            combined = list(zip(problems, solutions))
            random.shuffle(combined)
            problems, solutions = zip(*combined)

        # Create numbered LaTeX items for problems and solutions
        problem_items = "\n".join([f"  \\item[{i+1}.] {problem}" for i, problem in enumerate(problems)])
        solution_items = "\n".join([f"  \\item[{i+1}.] {solution}" for i, solution in enumerate(solutions)])

        # Format the templates
        problems_latex = LatexExporter.latex_problem_template.format(items=problem_items)
        solutions_latex = LatexExporter.latex_solution_template.format(items=solution_items)

        return problems_latex, solutions_latex
