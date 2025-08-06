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

