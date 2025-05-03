from PyPDF2 import PdfMerger

# Function to merge PDFs
def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

# Specify the input PDFs and output file
pdf_files = [
    r"C:\Users\willi\My Drive\Engineering\Obsidian Vault\All Else\CURLFC\Sports Grant Form - Will Hewes.pdf",
    r"C:\Users\willi\My Drive\Engineering\Obsidian Vault\All Else\CURLFC\CURLFC Subs 23_24 - Basic Invoice-2.pdf"
]

output_pdf = r"C:\Users\willi\My Drive\Engineering\Obsidian Vault\All Else\CURLFC\Sports Expense Form - Will Hewes.pdf"

# Merge the PDFs
merge_pdfs(pdf_files, output_pdf)
print(f"PDFs merged successfully into {output_pdf}")
