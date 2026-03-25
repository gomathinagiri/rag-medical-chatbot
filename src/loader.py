import os
import PyPDF2

def load_pdfs(pdf_folder: str):
    all_texts = []
    if not os.path.exists(pdf_folder):
        raise ValueError(f"Folder {pdf_folder} does not exist!")
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_folder, filename)
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                if text.strip():  # only add non-empty PDFs
                    all_texts.append({"filename": filename, "text": text})
    if not all_texts:
        raise ValueError(f"No valid PDFs found in {pdf_folder}!")
    return all_texts