from io import BytesIO
from docx import Document
from pypdf import PdfReader
def _read_pdf(data:bytes) -> str:
    reader = PdfReader(BytesIO(data))
    return "\n".join((page.extract_text() or "") for page in reader.pages)
def _read_docx(data:bytes) ->str:
    doc = Document(BytesIO(data))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)
def _read_text(data:bytes) ->str:
    try:
         return data.decode("utf-8")
    except:
        return data.decode("latin-1", errors="ignore")
def load_text(filename: str, data: bytes) -> str:
    name = filename.lower()
    if name.endswith("txt"):
        text = _read_text(data)
    elif name.endswith("pdf"):
        text = _read_pdf(data)
    elif name.endswith("docx"):
        text = _read_docx(data)
    else:
        raise ValueError(f"Unsupported file type:{filename}")
    if not text.strip():
        raise ValueError(f"No readable text found in {filename}"
        "if it is scanned pdf,it has no selectable text to extract")
    return text
   

if __name__ == "__main__":
    with open("UPLOADED_DOCS.pdf", "rb") as f:
        data = f.read()

    text = load_text("UPLOADED_DOCS.pdf", data)
    print(text)