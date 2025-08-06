from sqlalchemy.orm import Session
from models import ResumePrediction
from schemas import ResumePredictionCreate

def create_resume_prediction(db: Session, prediction: ResumePredictionCreate):
    db_prediction = ResumePrediction(**prediction.model_dump())
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

def get_recent_predictions(db: Session, limit: int = 10):
    return db.query(ResumePrediction).order_by(ResumePrediction.prediction_date.desc()).limit(limit).all()

def get_course_recommendations(category: str):
    recommendations = {
        "Engineering": {
            "courses": ["ML Fundamentals", "Cloud Computing"],
            "videos": [
                {
                    "title": "Introduction to Machine Learning",
                    "url": "https://www.youtube.com/watch?v=aircAruvnKk",
                    "thumbnail": "https://img.youtube.com/vi/aircAruvnKk/mqdefault.jpg"
                },
                {
                    "title": "Cloud Computing Basics",
                    "url": "https://www.youtube.com/watch?v=M988_fsOSWo",
                    "thumbnail": "https://img.youtube.com/vi/M988_fsOSWo/mqdefault.jpg"
                }
            ]
        },
        "Health and fitness": {
            "courses": ["Medical Ethics", "Anatomy"],
            "videos": [
                {
                    "title": "Medical Ethics",
                    "url": "https://www.youtube.com/watch?v=knGwTLYwCf0",
                    "thumbnail": "https://img.youtube.com/vi/knGwTLYwCf0/hqdefault.jpg"
                }
            ]
        },
        "Finance": {
            "courses": ["Investment 101", "Accounting"],
            "videos": [
                {
                    "title": "Finance Basics",
                    "url": "https://www.youtube.com/watch?v=Omi9LdMpRPI",
                    "thumbnail": "https://img.youtube.com/vi/Omi9LdMpRPI/mqdefault.jpg"
                }
            ]
        },
        "HR": {
            "courses": ["Talent Management", "Recruitment Strategies"],
            "videos": [
                {
                    "title": "HR Management",
                    "url": "https://www.youtube.com/watch?v=c8_avX9miag",
                    "thumbnail": "https://img.youtube.com/vi/c8_avX9miag/mqdefault.jpg"
                }
            ]
        }
    }
    
    default_recommendation = {
        "courses": ["Professional Skills"],
        "videos": [
            {
                "title": "Professional Skills Development",
                "url": "https://www.youtube.com/watch?v=8eXbDQyXdDo",
                "thumbnail": "https://img.youtube.com/vi/8eXbDQyXdDo/mqdefault.jpg"
            }
        ]
    }
    
    return recommendations.get(category, default_recommendation)