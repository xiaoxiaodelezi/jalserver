import pdfplumber

pdf = pdfplumber.open('hawb.pdf')

for page in pdf.pages:
    print(page.extract_text())
    print("-----")