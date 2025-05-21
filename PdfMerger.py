from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

# Function to merge PDFs
def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

# Hide the root tkinter window
root = Tk()
root.withdraw()

# Select input PDF files
pdf_files = filedialog.askopenfilenames(
    title="Select PDF files to merge",
    filetypes=[("PDF files", "*.pdf")]
)

# Select where to save the output PDF
output_pdf = filedialog.asksaveasfilename(
    title="Save Merged PDF As",
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")]
)

# Merge at an output location
if pdf_files and output_pdf:
    merge_pdfs(pdf_files, output_pdf)
    print(f"PDFs merged successfully into {output_pdf}")
else:
    print("No files selected.")
