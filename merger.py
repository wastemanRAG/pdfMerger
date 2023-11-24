import PyPDF2
import os

def merge_pdfs_in_directory(directory="."):
    merged = PyPDF2.PdfFileMerger()

    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            merged.append(file)

    merged.write(os.path.join(directory, "combined.pdf"))

merge_pdfs_in_directory()
