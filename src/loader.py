import os
import PyPDF2

def load_pdfs(pdf_folder: str):
    docs = []

    if not os.path.exists(pdf_folder):
        raise ValueError(f"Folder {pdf_folder} does not exist!")

    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_folder, file)

            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)

                text = ""
                for page in reader.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"

                if text.strip():
                    docs.append({
                        "filename": file,
                        "text": text
                    })

    if not docs:
        raise ValueError("No valid PDFs found!")

    return docs