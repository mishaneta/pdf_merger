from PyPDF2 import PdfMerger
import glob

pdfs = glob.glob('docs/*.pdf')

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("docs/update.pdf")
merger.close()
