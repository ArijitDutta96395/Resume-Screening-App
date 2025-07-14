import { useState } from 'react';
import axios from 'axios';
import './index.css';

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:8000/upload_resume/', formData);
      setResult(response.data.predicted_category);
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('Error uploading file');
    }
  };

  return (
    <div className="bg-primary text-white p-4 rounded-4 shadow-lg" style={{ width: '100%', maxWidth: '380px' }}>
      <h1 className="text-center mb-3">
        <i className="bi bi-cpu me-2"></i>
        Resume Screening App
      </h1>
      <p className="text-center mb-4 small">
        Upload your resume and get job category prediction
      </p>

      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Select Resume (Text File):</label>
          <input
            type="file"
            className="form-control"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </div>

        <button type="submit" className="btn btn-light w-100 fw-bold">
          <i className="bi bi-file-earmark-arrow-up me-2"></i>
          Upload & Predict
        </button>
      </form>

      {result && (
        <div className="mt-4 bg-white text-dark p-3 rounded shadow-sm">
          <h6 className="fw-bold">Prediction Result:</h6>
          <p className="mb-0">{result}</p>
        </div>
      )}

      <footer className="mt-4 text-center small">
        © 2025 Resume Screening Tool
      </footer>
    </div>
  );
}

export default ResumeUpload;
