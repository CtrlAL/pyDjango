import pdfplumber
def cut_on_page(file):
    page_list = []
    with pdfplumber.open(file) as pdf:
       for page in pdf.pages:
           page_list.append(page.extract_text())
    return page_list

