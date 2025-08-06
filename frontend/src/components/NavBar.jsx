import { Link, useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';

function NavBar() {
  const location = useLocation();
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    setIsOpen(false);
  }, [location]);

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 py-3">
      <div className="container">
        <Link className="navbar-brand fw-bold" to="/">
          <i className="bi bi-file-earmark-person me-2"></i>
          Resume Scanner
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          onClick={toggleMenu}
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className={`collapse navbar-collapse ${isOpen ? 'show' : ''}`}>
          <ul className="navbar-nav ms-auto mb-2 mb-lg-0 fw-semibold">
            <li className="nav-item">
              <Link 
                className={`nav-link ${location.pathname === '/' ? 'active fw-bold' : ''}`} 
                to="/"
              >
                <i className="bi bi-house-door me-1"></i>
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link 
                className={`nav-link ${location.pathname === '/predictions' ? 'active fw-bold' : ''}`}
                to="/predictions"
              >
                <i className="bi bi-clock-history me-1"></i>
                Recent Predictions
              </Link>
            </li>
            <li className="nav-item">
              <Link 
                className={`nav-link ${location.pathname === '/courses' ? 'active fw-bold' : ''}`}
                to="/courses"
              >
                <i className="bi bi-book me-1"></i>
                Course Recommendations
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
