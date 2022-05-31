import PyPDF3

if __name__ == "__main__":
    pdf_file = "/home/felix/Downloads/The Definitive Guide to Masonite.pdf"
    pdf_file_obj = open(pdf_file, "rb")
    pdf_reader = PyPDF3.PdfFileReader(pdf_file_obj)
    print(pdf_reader.getNumPages())

    page_obj = pdf_reader.getPage(0)
    print(page_obj.extractText())
