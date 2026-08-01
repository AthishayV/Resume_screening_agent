import fitz                     # PyMuPDF, reads PDF files
from docx import Document       # reads DOCX files
import os                       

def read_pdf(file_path):        # Read text from a PDF file
    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

def read_docx(file_path):       # Read text from a DOCX file

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text

def read_txt(file_path):        # Read text from a TXT file

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def parse_resume(file_path):    # Determine the file type and read the resume content accordingly

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf(file_path)

    elif extension == ".docx":
        return read_docx(file_path)

    elif extension == ".txt":
        return read_txt(file_path)

    else:
        raise ValueError("Unsupported file format")