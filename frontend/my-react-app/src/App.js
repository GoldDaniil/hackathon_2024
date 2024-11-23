import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import BookingSystem from './components/BookingSystem';
import MonitoringPage from './components/MonitoringPage';
import BookingPage from './components/BookingPage';
import SettingsPage from './components/SettingsPage'
import './App.css'; // Импортируйте ваш CSS файл, если он есть

function App() {
  return (
    <Router>
        <div className="App">
          <Routes>
          <Route path="/monitoring" element={<MonitoringPage />} />
          <Route path="/booking" element={<BookingPage />} />
          <Route path="/settings" element={<SettingsPage />} />
          <Route path="/" element={<BookingSystem />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
