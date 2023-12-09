
import PyPDF2
from docx import Document

def convert_file_to_text(file_path):
    try:
        # Identify file type based on extension
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'pdf':
            return convert_pdf_to_text(file_path)
        elif file_extension == 'docx':
            return convert_docx_to_text(file_path)
        elif file_extension == 'txt':
            return read_text_file(file_path)
        else:
            print(f"Unsupported file type: {file_extension}")
            return None

    except Exception as e:
        print(f"Error converting file: {e}")
        return None

def convert_pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error converting PDF to text: {e}")
        return None

def convert_docx_to_text(docx_path):
    try:
        doc = Document(docx_path)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
        return text
    except Exception as e:
        print(f"Error converting DOCX to text: {e}")
        return None

def read_text_file(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        return text_content
    except Exception as e:
        print(f"Error reading text file: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    file_path = 'E:/ResumeParser/tests/python_developer.pdf'
    text_content = convert_file_to_text(file_path)

    if text_content is not None:
        print(text_content)