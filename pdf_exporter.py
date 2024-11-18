import os
import subprocess
import shutil

class PDFExporter:
    """
    Exports LaTeX content as a PDF in US Letter format.
    """
    def __init__(self, output_dir="output/"):
        self.output_dir = output_dir
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)  # Remove the folder and its contents
        os.makedirs(output_dir, exist_ok=False)

    def export_to_pdf(self, latex_content, filename):
        tex_file = os.path.join(self.output_dir, f"{filename}.tex")
        pdf_file = os.path.join(self.output_dir, f"{filename}.pdf")
        with open(tex_file, "w") as f:
            f.write(latex_content)
        try:
            subprocess.run(
                ["pdflatex", "-output-directory", self.output_dir, tex_file],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            print(f"PDF generated successfully: {pdf_file}")
        except subprocess.CalledProcessError as e:
            print("Error generating PDF:", e.stderr.decode())
