from PyPDF2 import PdfMerger

pdfs = [
    # 'your-pdf-name.pdf', 
]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("docs/update.pdf")
merger.close()
