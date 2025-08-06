from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from docx import Document
from PyPDF2 import PdfReader
from datetime import datetime
from sqlalchemy.orm import Session
import os

# Local imports
from crud import create_resume_prediction, get_recent_predictions as crud_get_recent, get_course_recommendations as crud_get_courses
from schemas import ResumePrediction, ResumePredictionCreate, PredictionUpdate
from database import SessionLocal
from models import ResumePrediction as ResumePredictionModel
from ml_model import predict_category

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_text_from_file(file: UploadFile) -> str:
    if file.filename is None:
        raise ValueError("No filename provided")
    
    contents = file.file.read()
    filename = file.filename.lower()
    
    if filename.endswith('.txt'):
        return contents.decode('utf-8')
    elif filename.endswith('.pdf'):
        with open("temp.pdf", "wb") as f:
            f.write(contents)
        try:
            reader = PdfReader("temp.pdf")
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
            return text
        finally:
            os.remove("temp.pdf")
    elif filename.endswith(('.docx', '.doc')):
        with open("temp.docx", "wb") as f:
            f.write(contents)
        try:
            doc = Document("temp.docx")
            text = "\n".join(para.text for para in doc.paragraphs)
            return text
        finally:
            os.remove("temp.docx")
    else:
        raise ValueError("Unsupported file format")

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        text = extract_text_from_file(file)
        predicted_category = predict_category(text)
        
        db = SessionLocal()
        try:
            if file.filename is None:
                raise ValueError("No filename provided")
                
            prediction_data = ResumePredictionCreate(
                filename=file.filename,
                content=text[:1000],  # Store first 1000 chars
                predicted_category=predicted_category
            )
            create_resume_prediction(db, prediction_data)
            return {"predicted_category": predicted_category}
        finally:
            db.close()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")

@app.get("/recent_predictions/", response_model=List[ResumePrediction])
def get_recent_predictions(limit: int = 10):
    db = SessionLocal()
    try:
        predictions = crud_get_recent(db, limit)
        return predictions
    finally:
        db.close()

@app.get("/course_recommendations/{category}")
def get_course_recommendations(category: str):
    recommendations = crud_get_courses(category)
    return recommendations

@app.delete("/prediction/{prediction_id}")
def delete_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = db.query(ResumePredictionModel).filter(ResumePredictionModel.id == prediction_id).first()
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    db.delete(prediction)
    db.commit()
    return {"message": "Prediction deleted"}

@app.put("/prediction/{prediction_id}")
def update_prediction(prediction_id: int, prediction: PredictionUpdate, db: Session = Depends(get_db)):
    db_prediction = db.query(ResumePredictionModel).filter(ResumePredictionModel.id == prediction_id).first()
    if db_prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    for key, value in prediction.dict(exclude_unset=True).items():
        setattr(db_prediction, key, value)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

@app.get("/prediction/{prediction_id}")
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = db.query(ResumePredictionModel).filter(ResumePredictionModel.id == prediction_id).first()
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return prediction