import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './MonitoringPage.css'; // Импортируйте файл стилей, если его еще нет

const MonitoringPage = () => {
  const [servers, setServers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/servers')
      .then(response => {
        setServers(response.data.servers);  // Предполагаем, что данные о серверах возвращаются в поле servers
        setLoading(false);  // Устанавливаем состояние loading в false после загрузки
      })
      .catch(error => {
        console.error('Error fetching servers:', error);
        setLoading(false);  // Устанавливаем loading в false, даже если произошла ошибка
      });
  }, []);

  if (loading) {
    return <div className="loading">Загрузка...</div>;
  }

  return (
    <div className="monitoring-page">
      <h1>Страница Мониторинга</h1>
      <img 
        src="https://i.pinimg.com/564x/7c/88/fc/7c88fceb91e92455ef1709dded48033a.jpg" 
        alt="Monitoring" 
        className="monitoring-image"
      />
      
      <h2>Список серверов</h2>
      <ul className="servers-list">
        {servers.length > 0 ? (
          servers.map(server => (
            <li key={server.id} className="server-item">
              <strong>{server.name}</strong> - Статус: {server.status} - 
              IP: {server.ip_address} - Создан: {new Date(server.created_at).toLocaleString()}
            </li>
          ))
        ) : (
          <li>Серверы не найдены</li>
        )}
      </ul>
    </div>
  );
};

export default MonitoringPage;
