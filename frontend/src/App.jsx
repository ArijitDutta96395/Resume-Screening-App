import 'bootstrap-icons/font/bootstrap-icons.css';
import ResumeUpload from "./ResumeUpload";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";

function App() {
  return (
    <div
      className="d-flex justify-content-center align-items-start vh-100"
      style={{ backgroundColor: "#e6f0ff", paddingTop: "60px" }}
    >
      <ResumeUpload />
    </div>
  );
}

export default App;
