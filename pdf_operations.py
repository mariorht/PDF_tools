from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(pdf_paths, output_path):
    pdf_writer = PdfFileWriter()

    for pdf_path in pdf_paths:
        pdf_reader = PdfFileReader(open(pdf_path, 'rb'))
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def split_pdf(input_pdf, output_folder):
    pdf_reader = PdfFileReader(open(input_pdf, 'rb'))

    for page_num in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page_num))

        output_path = f"{output_folder}/page_{page_num+1}.pdf"
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
