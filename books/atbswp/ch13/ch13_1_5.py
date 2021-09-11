import PyPDF3

if __name__ == '__main__':
    pdf_file = open('/home/felix/Downloads/abc.pdf', 'rb')
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    pdf_reader.decrypt('123')
    page_obj = pdf_reader.getPage(0)
    page_obj.rotateClockwise(90)

    pdf_writer = PyPDF3.PdfFileWriter()
    pdf_writer.addPage(page_obj)

    output_file = open('/home/felix/Downloads/abc_rotate.pdf', 'wb')
    pdf_writer.write(output_file)
    pdf_file.close()
    output_file.close()
    