from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ResumePredictionBase(BaseModel):
    filename: str
    content: str
    predicted_category: str

class PredictionUpdate(BaseModel):
    filename: Optional[str]
    predicted_category: Optional[str]

class ResumePredictionCreate(ResumePredictionBase):
    pass

class ResumePrediction(ResumePredictionBase):
    id: int
    prediction_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True  # Updated from orm_mode

class VideoRecommendation(BaseModel):
    title: str
    url: str
    thumbnail: str

class CourseRecommendation(BaseModel):
    category: str
    courses: list[str]
    videos: list[VideoRecommendation]