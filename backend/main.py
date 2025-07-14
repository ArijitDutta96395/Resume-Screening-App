from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ml_model import predict_category  # Import your ML function

app = FastAPI()

# Allow CORS (For frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust later for security
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "Server is running"}

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    try:
        file_content = await file.read()
        text = file_content.decode("utf-8")

        category = predict_category(text)

        return {
            "predicted_category": category,
            "message": "Prediction successful"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
