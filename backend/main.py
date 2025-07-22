from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from docx import Document
from PyPDF2 import PdfReader
from ml_model import predict_category


app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    filename = file.filename.lower()

    if filename.endswith('.txt'):
        text = contents.decode('utf-8')

    elif filename.endswith('.pdf'):
        with open("temp.pdf", "wb") as f:
            f.write(contents)
        reader = PdfReader("temp.pdf")
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    elif filename.endswith('.docx') or filename.endswith('.doc'):
        with open("temp.docx", "wb") as f:
            f.write(contents)
        doc = Document("temp.docx")
        text = "\n".join([para.text for para in doc.paragraphs])

    else:
        return {"error": "Unsupported file format"}

    predicted_category = predict_category(text)
    return {"predicted_category": predicted_category}
