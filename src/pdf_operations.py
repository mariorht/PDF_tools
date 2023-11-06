from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_paths, output_path):
    pdf_writer = PdfWriter()
    for pdf_path in pdf_paths:
        pdf_reader = PdfReader(pdf_path)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.write(output_path)

def split_pdf(input_pdf, output_folder):
    pdf_reader = PdfReader(input_pdf)

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output_path = f"{output_folder}/page_{page_num+1}.pdf"
        pdf_writer.write(output_path)
