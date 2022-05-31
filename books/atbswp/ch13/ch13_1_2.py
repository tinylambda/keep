import PyPDF3
from PyPDF3.utils import PdfReadError

if __name__ == "__main__":
    pdf_file = "/home/felix/Downloads/abc.pdf"
    pdf_reader = PyPDF3.PdfFileReader(open(pdf_file, "rb"))
    print(pdf_reader.isEncrypted)

    try:
        print(pdf_reader.getPage(0))
    except PdfReadError:
        print("PdfReadError")

    pdf_reader = PyPDF3.PdfFileReader(open(pdf_file, "rb"))
    print(pdf_reader.isEncrypted)
    pdf_reader.decrypt("123")
    page_obj = pdf_reader.getPage(0)
    print(page_obj.extractText())
