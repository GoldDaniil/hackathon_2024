import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import axios from 'axios';
import BookingSystem from './components/BookingSystem';
import MonitoringPage from './components/MonitoringPage';
import BookingPage from './components/BookingPage';
import SettingsPage from './components/SettingsPage';
import './App.css'; // Импортируйте ваш CSS файл

function App() {
  const [servers, setServers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/servers')
      .then(response => {
        setServers(response.data.servers);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the servers!', error);
        setLoading(false);
      });
  }, []);

  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li><Link to="/">Booking System</Link></li>
            <li><Link to="/monitoring">Monitoring</Link></li>
            <li><Link to="/booking">Booking</Link></li>
            <li><Link to="/settings">Settings</Link></li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<BookingSystem />} />
          <Route path="/monitoring" element={<MonitoringPage servers={servers} loading={loading} />} />
          <Route path="/booking" element={<BookingPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
