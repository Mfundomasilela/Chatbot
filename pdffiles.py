
#Text Extraction  from pdf

#Install the necessary libaries


import fitz

def extract_text_from_pdf(pdf_path):
    text = ""
    document = fitz.openn(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text  = text + page.get_text()
        return text 