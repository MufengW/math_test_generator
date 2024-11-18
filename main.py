from generator import MathTestGenerator
from latex_exporter import LatexExporter
from pdf_exporter import PDFExporter
from templates import generate_latex_document
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Generate problems
name = "Bella"
date = now.strftime("%Y-%m-%d")  # Example format: "2024-11-17"


test_generator = MathTestGenerator()
test_generator.generate_addition_subtraction_100(num_problems=10) # 100以内加减法
test_generator.generate_addition_subtraction_1000(num_problems=50) # 1000以内加减法
# test_generator.generate_multiplication_10(num_problems=5) # 10以内乘法
# test_generator.generate_multiplication_two_digit_by_one(num_problems=15) # 一位数*两位数
# test_generator.generate_gcd(num_problems=10) # 求最大公因数(Greatest Common Divisor)
# test_generator.generate_lcm(num_problems=10) # 求最小公倍数(Least Common Multiple)
# test_generator.generate_fraction_reduction(num_problems=10) # 分数约分
# test_generator.generate_fraction_operations(num_problems=5) # 分数加减

# Export to LaTeX
latex_exporter = LatexExporter()
latex_problems, latex_solutions = LatexExporter.generate_latex(test_generator, shuffle=False) # shuffle:打乱顺序

# Combine LaTeX content into a full document
latex_document = generate_latex_document(latex_problems, latex_solutions)

# Export to PDF
pdf_exporter = PDFExporter(output_dir=f"{name}_{date}/")
pdf_exporter.export_to_pdf(latex_document, "math_test")
