import { useEffect, useState } from "react";
import axios from "axios";

function RecentPredictions() {
  console.log('RecentPredictions component rendered');
  const [predictions, setPredictions] = useState([]);
  const [selectedPrediction, setSelectedPrediction] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState(null);

  // Fetch predictions
  useEffect(() => {
    console.log('Fetching predictions...');
    fetchPredictions();
  }, []);

  const fetchPredictions = async () => {
    try {
      console.log('Making API request...');
      const response = await axios.get("http://127.0.0.1:8000/recent_predictions/");
      console.log('API Response:', response.data);
      setPredictions(response.data);
      setError(null);
    } catch (error) {
      console.error("Error fetching predictions:", error);
      setError(error.message);
      setPredictions([]);
    }
  };

  // Delete prediction
  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this prediction?")) {
      try {
        await axios.delete(`http://127.0.0.1:8000/prediction/${id}`);
        setPredictions(predictions.filter(pred => pred.id !== id));
      } catch (error) {
        console.error("Error deleting prediction:", error);
      }
    }
  };

  // Update prediction
  const handleUpdate = async (id, updatedData) => {
    try {
      await axios.put(`http://127.0.0.1:8000/prediction/${id}`, updatedData);
      fetchPredictions(); // Refresh the list
      setIsEditing(false);
    } catch (error) {
      console.error("Error updating prediction:", error);
    }
  };

  return (
    <div className="container">
      <h2 className="mb-4">Recent Predictions</h2>
      <div className="bg-white rounded-4 shadow p-4">
        {error && (
          <div className="alert alert-danger" role="alert">
            Error: {error}
          </div>
        )}
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Filename</th>
                <th>Category</th>
                <th>Date</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {predictions.length === 0 ? (
                <tr>
                  <td colSpan="4" className="text-center">
                    No predictions found
                  </td>
                </tr>
              ) : predictions.map((prediction) => (
                <tr key={prediction.id}>
                  <td>{prediction.filename}</td>
                  <td>{prediction.predicted_category}</td>
                  <td>{new Date(prediction.prediction_date).toLocaleString()}</td>
                  <td>
                    <button 
                      className="btn btn-sm btn-danger me-2"
                      onClick={() => handleDelete(prediction.id)}
                    >
                      <i className="bi bi-trash"></i>
                    </button>
                    <button 
                      className="btn btn-sm btn-primary"
                      onClick={() => {
                        setSelectedPrediction(prediction);
                        setIsEditing(true);
                      }}
                    >
                      <i className="bi bi-pencil"></i>
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Edit Modal */}
        {isEditing && selectedPrediction && (
          <div className="modal show d-block" tabIndex="-1">
            <div className="modal-dialog">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title">Edit Prediction</h5>
                  <button type="button" className="btn-close" onClick={() => setIsEditing(false)}></button>
                </div>
                <div className="modal-body">
                  <form onSubmit={(e) => {
                    e.preventDefault();
                    handleUpdate(selectedPrediction.id, {
                      filename: e.target.filename.value,
                      predicted_category: e.target.category.value
                    });
                  }}>
                    <div className="mb-3">
                      <label className="form-label">Filename</label>
                      <input 
                        type="text" 
                        className="form-control" 
                        name="filename"
                        defaultValue={selectedPrediction.filename}
                      />
                    </div>
                    <div className="mb-3">
                      <label className="form-label">Category</label>
                      <input 
                        type="text" 
                        className="form-control" 
                        name="category"
                        defaultValue={selectedPrediction.predicted_category}
                      />
                    </div>
                    <button type="submit" className="btn btn-primary">Save Changes</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default RecentPredictions;
