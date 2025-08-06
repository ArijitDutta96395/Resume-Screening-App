import { useState } from "react";
import axios from "axios";

function CourseRecommendations() {
  const [category, setCategory] = useState("");
  const [courses, setCourses] = useState([]);
  const [videos, setVideos] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!category) return;

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/course_recommendations/${category}`
      );
      console.log('API Response:', response.data); // Debug log
      
      if (response.data && response.data.courses) {
        setCourses(response.data.courses);
        setVideos(response.data.videos || []);
      } else {
        console.error('Invalid response format:', response.data);
        setCourses([]);
        setVideos([]);
      }
    } catch (error) {
      console.error("Error fetching recommendations:", error);
      setCourses([]);
      setVideos([]);
    }
  };

  return (
    <div className="container">
      <h2 className="mb-4">Course Recommendations</h2>
      <div className="bg-white rounded-4 shadow p-4">
        <form onSubmit={handleSubmit} className="mb-4">
          <div className="input-group">
            <input
              type="text"
              className="form-control"
              placeholder="Enter job category (e.g., Engineering)"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
            />
            <button className="btn btn-primary" type="submit">
              Get Recommendations
            </button>
          </div>
        </form>

        {courses.length > 0 && (
          <div className="mb-4">
            <h5>Recommended courses for {category}:</h5>
            <ul className="list-group">
              {courses.map((course, index) => (
                <li key={index} className="list-group-item">
                  <i className="bi bi-check-circle-fill text-success me-2"></i>
                  {course}
                </li>
              ))}
            </ul>
          </div>
        )}

        {videos.length > 0 && (
          <div>
            <h5>Recommended videos:</h5>
            <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
              {videos.map((video, index) => (
                <div key={index} className="col">
                  <div className="card h-100">
                    <img
                      src={video.thumbnail}
                      className="card-img-top"
                      alt={video.title}
                    />
                    <div className="card-body">
                      <h6 className="card-title">{video.title}</h6>
                      <a
                        href={video.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="btn btn-primary btn-sm"
                      >
                        Watch Video
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default CourseRecommendations;
