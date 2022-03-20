import pdfplumber
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
import uuid



def cut_on_page(file):
    page_list = []
    with pdfplumber.open(file) as pdf:
       for page in pdf.pages:
           page_list.append(page.extract_text())
    return page_list


def cut_on_page_pyPDF2(file):
    fr = file.open()
    inputpdf = PdfFileReader(fr)
    listp_pdf_names = []
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        unique_filename = str(uuid.uuid4())
        with open(f"pages/{unique_filename}.pdf", "wb") as outputStream:
            listp_pdf_names.append(f"pages/{unique_filename}.pdf")
            output.write(outputStream)

    return listp_pdf_names