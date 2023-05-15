import PyPDF2
pdf = open("shirin.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[0]  # page number you want to extract text from
print(page.extract_text())
