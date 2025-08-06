from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class ResumePrediction(Base):
    __tablename__ = "resume_predictions"  # Fixed typo from previous version
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content = Column(String)
    predicted_category = Column(String)
    prediction_date = Column(DateTime, default=datetime.utcnow)