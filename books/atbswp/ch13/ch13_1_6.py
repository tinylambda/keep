import PyPDF3

if __name__ == "__main__":
    pdf_file = open("/home/felix/Downloads/abc.pdf", "rb")
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    pdf_reader.decrypt("123")

    watermark_pdf_file = open("/home/felix/Downloads/wartermark.pdf", "rb")
    watermark_pdf_reader = PyPDF3.PdfFileReader(watermark_pdf_file)

    firstPage = pdf_reader.getPage(0)
    watermark_page = watermark_pdf_reader.getPage(0)
    watermark_page.rotateClockwise(180)
    firstPage.mergePage(watermark_pdf_reader.getPage(0))

    pdf_writer = PyPDF3.PdfFileWriter()
    pdf_writer.encrypt("abc")  # encryption PDF file
    pdf_writer.addPage(firstPage)

    for page_num in range(1, pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

    output_pdf_file = open("/home/felix/Downloads/abc_cover.pdf", "wb")
    pdf_writer.write(output_pdf_file)

    pdf_file.close()
    watermark_pdf_file.close()
    output_pdf_file.close()
