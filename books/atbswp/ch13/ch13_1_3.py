import PyPDF3

if __name__ == '__main__':
    pdf_file = '/home/felix/Downloads/abc.pdf'
    pdf_reader = PyPDF3.PdfFileReader(open(pdf_file, 'rb'))
    pdf_reader.decrypt('123')

    pdf_writer = PyPDF3.PdfFileWriter()
    for page_num in range(pdf_reader.getNumPages()):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

    pdf_output_file = open('/home/felix/Downloads/abc_copy.pdf', 'wb')
    pdf_writer.write(pdf_output_file)
    pdf_output_file.close()
