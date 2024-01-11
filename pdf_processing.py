```python
from PyPDF2 import PdfFileReader, PdfFileWriter

def extract_text_from_pdf(file_path):
    pdf = PdfFileReader(file_path)
    text = ""
    for page in range(pdf.getNumPages()):
        text += pdf.getPage(page).extractText()
    return text

def split_pdf(file_path, start_page, end_page, output_path):
    pdf = PdfFileReader(file_path)
    pdf_writer = PdfFileWriter()
    for page in range(start_page, end_page):
        pdf_writer.addPage(pdf.getPage(page))
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfFileWriter()
    for file_path in file_paths:
        pdf = PdfFileReader(file_path)
        for page in range(pdf.getNumPages()):
            pdf_writer.addPage(pdf.getPage(page))
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
```