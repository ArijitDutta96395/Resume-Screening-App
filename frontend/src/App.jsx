import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import NavBar from './components/NavBar';
import Home from './pages/Home';
import RecentPredictions from './pages/RecentPredictions';
import CourseRecommendations from './pages/CourseRecommendations';

function App() {
  console.log('App component rendered');
  return (
    <Router>
      <div className="min-vh-100 bg-light">
        <NavBar />
        <div className="container py-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/home" element={<Home />} />
            <Route path="/predictions" element={<RecentPredictions />} />
            <Route path="/RecentPredictions" element={<RecentPredictions />} />
            <Route path="/courses" element={<CourseRecommendations />} />
            <Route path="/CourseRecommendations" element={<CourseRecommendations />} />
            <Route path="*" element={<div className="text-center mt-5"><h2>Page not found</h2></div>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
