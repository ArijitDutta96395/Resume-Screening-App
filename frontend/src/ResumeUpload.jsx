import { useState } from "react";
import axios from "axios";
import "./index.css";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload_resume/",
        formData
      );
      setResult(response.data.predicted_category);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Error uploading file");
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-start min-vh-100 pt-5">
      <div
        className="bg-primary text-white p-4 rounded-4 shadow-lg mt-4"
        style={{ width: "100%", maxWidth: "400px" }}
      >
      <h1 className="text-center mb-3">
        <i className="bi bi-cpu me-2"></i>
        Resume Screening App
      </h1>

      <p className="text-center mb-4 small">
        Upload your resume and get job category prediction
      </p>

      <form onSubmit={handleSubmit}>
        <div className="mb-3 text-center">
          <label className="form-label d-flex align-items-center justify-content-center gap-2 mb-2">
            <i className="bi bi-upload fs-5"></i>
            <span className="fw-semibold">Select Resume (txt, pdf, docx):</span>
          </label>
          <input
            type="file"
            className="form-control"
            onChange={(e) => setFile(e.target.files[0])}
            accept=".txt,.pdf,.doc,.docx"
            style={{ textAlign: "center" }}
          />
        </div>

        <button type="submit" className="btn btn-light w-100 fw-bold">
          <i className="bi bi-file-earmark-arrow-up me-2"></i>
          Upload & Predict
        </button>
      </form>

      {result && (
        <div className="mt-4 bg-white text-dark p-3 rounded shadow-sm">
          <h6 className="fw-bold">
            <i className="bi bi-lightbulb me-2 text-warning"></i>
            Prediction Result:
          </h6>
          <p className="mb-0">{result}</p>
        </div>
      )}

      <footer className="mt-5 pt-4 border-top border-light">
        <div className="row text-center">
          <div className="col-12 mb-3">
            <h6 className="fw-bold mb-2">
              <i className="bi bi-code-slash me-2"></i>
              Developed by
            </h6>
            <p className="mb-1">Arijit Dutta</p>
            <p className="small mb-0">Full Stack Developer</p>
          </div>
          <div className="col-12 mb-3">
            <div className="d-flex justify-content-center gap-3">
              <a href="https://github.com/ArijitDutta96395" className="text-white" target="_blank" rel="noopener noreferrer">
                <i className="bi bi-github fs-5"></i>
              </a>
              <a href="https://www.linkedin.com/in/arijitduttaa1" className="text-white" target="_blank" rel="noopener noreferrer">
                <i className="bi bi-linkedin fs-5"></i>
              </a>
              <a href="mailto:arijitdutta96395@gmail.com" className="text-white">
                <i className="bi bi-envelope fs-5"></i>
              </a>
            </div>
          </div>
          <div className="col-12">
            <p className="small mb-1">
              <i className="bi bi-tools me-2"></i>
              Built with React, FastAPI, and ML
            </p>
            <p className="small mb-0">
              © 2025 Resume Screening Tool | All Rights Reserved
            </p>
          </div>
        </div>
      </footer>
      </div>
    </div>
  );
}

export default ResumeUpload;
