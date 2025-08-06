# 📄 Resume Screening App

A **full-stack resume screening application** built with **React (Vite)** on the frontend and **FastAPI (Python)** on the backend.  
The app allows users to upload resumes (TXT, PDF, DOCX), automatically predicts the job category using a trained ML model (TF-IDF), and stores results in a database with full CRUD operations.

---

## 🚀 Features

- **Upload resumes (TXT, PDF, DOCX)** and predict job categories  
- **FastAPI backend with REST API endpoints** for prediction and CRUD  
- **SQLite database using SQLAlchemy ORM** to store predictions  
- **React (Vite) frontend with Axios** to interact with backend  
- **Bootstrap + Tailwind CSS** for responsive UI  
- **Edit/Delete predictions directly from dashboard**  
- **ML Model Integration** using a pre-trained TF-IDF model (`models/tfidf.pkl`)  

---

## 🛠 Tech Stack

### Frontend
- [React 19](https://react.dev/) with [Vite](https://vitejs.dev/)
- [Axios](https://axios-http.com/) for API calls
- [Bootstrap 5](https://getbootstrap.com/) & [Bootstrap Icons](https://icons.getbootstrap.com/)
- [TailwindCSS](https://tailwindcss.com/) for additional styling
- [React Router v7](https://reactrouter.com/) for navigation

### Backend
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) for ASGI server
- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM
- [PyPDF2](https://pypi.org/project/PyPDF2/) & [python-docx](https://pypi.org/project/python-docx/) for file parsing
- [Pickle](https://docs.python.org/3/library/pickle.html) for loading ML model
- [Starlette CORS](https://www.starlette.io/middleware/#corsmiddleware) for frontend-backend communication

---

## 📂 Project Structure
- **resume_screening_app/**
  - **backend/**
    - `main.py` – FastAPI app entry point  
    - `models.py` – SQLAlchemy models  
    - `schemas.py` – Pydantic schemas  
    - `crud.py` – Database CRUD operations  
    - `database.py` – DB connection setup  
    - `ml_model.py` – Category prediction function  
    - **models/**
      - `tfidf.pkl` – Pre-trained TF-IDF model  
  - **frontend/**
    - **src/**
      - `App.jsx` – Root React component  
      - `ResumeUpload.jsx` – Resume upload component  
      - `index.css` – Global styles  
    - `package.json` – Frontend dependencies  
  - `README.md` – Project documentation  



---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/resume_screening_app.git
cd resume_screening_app
```

### 2. Backend Setup (FastAPI)
Create virtual environment
```bash
cd backend
python -m venv venv
source venv/bin/activate      # (Linux/Mac)
venv\Scripts\activate         # (Windows)
```

Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy PyPDF2 python-docx pydantic
```

Run the backend server
```bash
uvicorn backend.main:app --reload
```
Server will start at:
http://127.0.0.1:8000

---

### 3. Frontend Setup (React + Vite)
Install dependencies
```bash
cd ../frontend
npm install
```

Start the React dev server
```bash
npm run dev
```
Frontend will run at:
http://localhost:5173 (default Vite port)
---

🎯 Usage
1. Start backend (uvicorn backend.main:app --reload)

2. Start frontend (npm run dev)

3. Open http://localhost:5173

4. Upload a resume → View predicted category → Edit/Delete records
---
🧩 Future Enhancements
-Resume parsing to extract name, email, skills, and experience

-Candidate scoring and ranking

-Job description matching

-Bulk upload support

-Analytics dashboard with charts

-Mini ATS features (status tracking, notes)
---
📜 License
This project is open-source and available under the MIT License.
---

Author: Arijit Dutta
Email: arijitdutta963952gmail.com
GitHub: (https://github.com/ArijitDutta96395)







