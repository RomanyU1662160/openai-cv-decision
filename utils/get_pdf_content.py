import PyPDF2


def get_pdf_content(pdf_file_path):
    content = ""
    with open(pdf_file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content += page.extract_text() + "\n"
    return content
